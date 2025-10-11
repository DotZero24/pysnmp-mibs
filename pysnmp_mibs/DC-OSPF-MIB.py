# SNMP MIB module (DC-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-OSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:09:26 2025
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

(AuthUserDataString,
 IfOperStatus,
 IgpShortcutMetricType,
 NpgOperStatus,
 NumericIndex) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AuthUserDataString",
    "IfOperStatus",
    "IgpShortcutMetricType",
    "NpgOperStatus",
    "NumericIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

ospfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3)
)
if mibBuilder.loadTexts:
    ospfMib.setRevisions(
        ("2014-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OspfPmAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusUp", 1),
          ("adminStatusDown", 2))
    )



class OspfPmOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("operStatusUp", 1),
          ("operStatusDown", 2),
          ("operStatusGoingUp", 3),
          ("operStatusGoingDown", 4),
          ("operStatusActFailed", 5))
    )



class OspfPmIndex(TextualConvention, Unsigned32):
    status = "current"


class OspfPmMjStatus(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("mjNotJoined", 1),
          ("mjSentAddJoin", 2),
          ("mjSentRegister", 3),
          ("mjJoinActive", 4),
          ("mjSentDelJoin", 5),
          ("mjSentUnregister", 6),
          ("mjJoinGone", 7),
          ("mjFailedToRegister", 8),
          ("mjFailingOver", 9),
          ("mjFailed", 10))
    )



class OspfPmSjStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("sjNotJoined", 1),
          ("sjJoined", 2),
          ("sjJoinActive", 3),
          ("sjJoinUnreg", 4),
          ("sjJoinGone", 5),
          ("sjFailingOver", 6),
          ("sjFailed", 7))
    )



class OspfPmInterfaceId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ifIpSockets", 1),
          ("ifIfInfo", 2),
          ("ifRteProtInput", 3))
    )



class OspfPmSlaveInterfaceId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ifCspfInterface", 1),
          ("ifNmInterface", 2),
          ("ifPdiInterface", 3))
    )



class AreaID(TextualConvention, IpAddress):
    status = "current"


class RouterID(TextualConvention, IpAddress):
    status = "current"


class OspfVersionNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )



class OspfAuthTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authNone", 0),
          ("authSimplePassword", 1),
          ("authMd5", 2),
          ("authHmacSha1", 3),
          ("authHmacSha256", 4),
          ("authHmacSha384", 5),
          ("authHmacSha512", 6))
    )



class OspfImportTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )



class OspfSummaryTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("summNoAreaSummary", 1),
          ("summSendAreaSummary", 2))
    )



class OspfTransRoles(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roleAlways", 1),
          ("roleCandidate", 2))
    )



class OspfTransStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateEnabled", 1),
          ("stateElected", 2),
          ("stateDisabled", 3))
    )



class OspfMetricTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("metricStandard", 1),
          ("metricComparableCost", 2),
          ("metricNonComparable", 3))
    )



class OspfExtLsTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("lsExternalLink", 5),
          ("lsExternalOpaqueLink", 11))
    )



class OspfAreaLsTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("lsRouterLink", 1),
          ("lsNetworkLink", 2),
          ("lsSummaryLink", 3),
          ("lsAsSummaryLink", 4),
          ("lsMulticastLink", 6),
          ("lsNssaExternalLink", 7),
          ("lsAreaOpaqueLink", 10))
    )



class OspfLinkLsTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("lsLinkOpaqueLink", 9)
    )



class OspfAggLsTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("lsSummaryLink", 3),
          ("lsNssaExternalLink", 7))
    )



class OspfNetworkTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("networkUndefined", 0),
          ("networkBroadcast", 1),
          ("networkNbma", 2),
          ("networkPointToPoint", 3),
          ("networkPointToMultipoint", 5),
          ("networkLoopback", 10))
    )



class OspfInterfaceStates(TextualConvention, Integer32):
    status = "current"
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
        *(("ifDown", 1),
          ("ifLoopback", 2),
          ("ifWaiting", 3),
          ("ifPointToPoint", 4),
          ("ifDesignatedRouter", 5),
          ("ifBackupDesignatedRouter", 6),
          ("ifOtherDesignatedRouter", 7),
          ("ifStandby", 8))
    )



class OspfMulticastFwardTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicastBlocked", 1),
          ("multicast", 2),
          ("multicastUnicast", 3))
    )



class OspfNeighborStates(TextualConvention, Integer32):
    status = "current"
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
        *(("nbrDown", 1),
          ("nbrAttempt", 2),
          ("nbrInit", 3),
          ("nbrTwoWay", 4),
          ("nbrExchangeStart", 5),
          ("nbrExchange", 6),
          ("nbrLoading", 7),
          ("nbrFull", 8))
    )



class OspfNbrPermanence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permDynamic", 1),
          ("permPermanent", 2))
    )



class OspfAggregateEffects(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("effectAdvertiseMatching", 1),
          ("effectDoNotAdvertiseMatching", 2))
    )



class OspfHitlessRestartReasons(TextualConvention, Integer32):
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
        *(("reasonUnknown", 0),
          ("reasonSoftwareRestart", 1),
          ("reasonSoftwareReload", 2),
          ("reasonSwitchToBackup", 3))
    )



class Metric(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class PositiveInteger(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class FastHelloMultiplierRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )



class UpToMaxAge(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class UpToRefreshInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )



class DesignatedRouterPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TOSType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



class OspfPmIfLinkProtValue(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("linkUnused0", 0),
          ("linkUnused1", 1),
          ("linkUnused2", 2),
          ("linkUnused3", 3),
          ("linkUnused4", 4),
          ("linkUnused5", 5),
          ("linkUnused6", 6),
          ("linkUnused7", 7),
          ("linkUnused8", 8),
          ("linkUnused9", 9),
          ("linkUnused10", 10),
          ("linkUnused11", 11),
          ("linkUnused12", 12),
          ("linkUnused13", 13),
          ("linkUnused14", 14),
          ("linkUnused15", 15),
          ("linkUnused16", 16),
          ("linkUnused17", 17),
          ("linkUnused18", 18),
          ("linkUnused19", 19),
          ("linkUnused20", 20),
          ("linkUnused21", 21),
          ("linkUnused22", 22),
          ("linkUnused23", 23),
          ("linkExtraTraffic", 24),
          ("linkUnprotected", 25),
          ("linkShared", 26),
          ("linkDedicated1To1", 27),
          ("linkDedicated1Plus1", 28),
          ("linkEnhanced", 29))
    )


class OspfPmIfSwitchCapValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51,
              100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("ifPacketSwitchCapable1", 1),
          ("ifPacketSwitchCapable2", 2),
          ("ifPacketSwitchCapable3", 3),
          ("ifPacketSwitchCapable4", 4),
          ("ifLayer2SwitchCapable", 51),
          ("ifTDMCapable", 100),
          ("ifLambdaSwitchCapable", 150),
          ("ifFiberSwitchCapable", 200))
    )



class OspfPmIfSwitchEncodingValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ifPacketCapable", 1),
          ("ifEthernetCapable", 2),
          ("ifAnsiEtsiPdhCapable", 3),
          ("ifSdhSonetCapable", 5),
          ("ifDigWrapperCapable", 7),
          ("ifLambdaCapable", 8),
          ("ifFiberCapable", 9),
          ("ifFiberChannelCapable", 11))
    )



class OspfPmIfSwitchSonetSdhValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ifSonetSdhStandard", 0),
          ("ifSonetSdhArbitrary", 1))
    )



class OspfPmEntPrivateDataType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class OspfHelperModePolicy(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("helpPolicyUnknown", 0),
          ("helpPolicySoftware", 1),
          ("helpPolicyReload", 2),
          ("helpPolicySwitch", 3))
    )


class OspfRestartHelperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )



class OspfRestartExitReason(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )



class OspfShamConflictFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("shamConflictIf", 0),
          ("shamConflictHost", 1),
          ("shamConflictRtm", 2),
          ("shamConflictStable", 3))
    )


class OspfPathType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pathTypeNone", 0),
          ("pathTypeIntraArea", 1),
          ("pathTypeInterArea", 2),
          ("pathTypeType1Ext", 3),
          ("pathTypeType2Ext", 4))
    )



class OspfDesignatedRtrState(TextualConvention, Integer32):
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
        *(("designatedOther", 0),
          ("designatedRouter", 1),
          ("backupDesignatedRouter", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_OspfObjects_ObjectIdentity = ObjectIdentity
ospfObjects = _OspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1)
)
_OspfPmEntTable_Object = MibTable
ospfPmEntTable = _OspfPmEntTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ospfPmEntTable.setStatus("current")
_OspfPmEntEntry_Object = MibTableRow
ospfPmEntEntry = _OspfPmEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1)
)
ospfPmEntEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmEntIndex"),
)
if mibBuilder.loadTexts:
    ospfPmEntEntry.setStatus("current")


class _OspfPmEntRouterId_Type(RouterID):
    """Custom type ospfPmEntRouterId based on RouterID"""
    defaultHexValue = "00000000"


_OspfPmEntRouterId_Type.__name__ = "RouterID"
_OspfPmEntRouterId_Object = MibTableColumn
ospfPmEntRouterId = _OspfPmEntRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 1),
    _OspfPmEntRouterId_Type()
)
ospfPmEntRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntRouterId.setStatus("current")


class _OspfPmEntAdminStat_Type(OspfPmAdminStatus):
    """Custom type ospfPmEntAdminStat based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmEntAdminStat_Type.__name__ = "OspfPmAdminStatus"
_OspfPmEntAdminStat_Object = MibTableColumn
ospfPmEntAdminStat = _OspfPmEntAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 2),
    _OspfPmEntAdminStat_Type()
)
ospfPmEntAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntAdminStat.setStatus("current")
_OspfPmEntVersionNumber_Type = OspfVersionNumber
_OspfPmEntVersionNumber_Object = MibTableColumn
ospfPmEntVersionNumber = _OspfPmEntVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 3),
    _OspfPmEntVersionNumber_Type()
)
ospfPmEntVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntVersionNumber.setStatus("current")
_OspfPmEntAreaBdrRtrStatus_Type = TruthValue
_OspfPmEntAreaBdrRtrStatus_Object = MibTableColumn
ospfPmEntAreaBdrRtrStatus = _OspfPmEntAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 4),
    _OspfPmEntAreaBdrRtrStatus_Type()
)
ospfPmEntAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntAreaBdrRtrStatus.setStatus("current")


class _OspfPmEntASBdrRtrStatus_Type(TruthValue):
    """Custom type ospfPmEntASBdrRtrStatus based on TruthValue"""
    defaultValue = 1


_OspfPmEntASBdrRtrStatus_Type.__name__ = "TruthValue"
_OspfPmEntASBdrRtrStatus_Object = MibTableColumn
ospfPmEntASBdrRtrStatus = _OspfPmEntASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 5),
    _OspfPmEntASBdrRtrStatus_Type()
)
ospfPmEntASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntASBdrRtrStatus.setStatus("current")
_OspfPmEntExternLsaCount_Type = Gauge32
_OspfPmEntExternLsaCount_Object = MibTableColumn
ospfPmEntExternLsaCount = _OspfPmEntExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 6),
    _OspfPmEntExternLsaCount_Type()
)
ospfPmEntExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntExternLsaCount.setStatus("current")
_OspfPmEntExternLsaCksumSum_Type = Integer32
_OspfPmEntExternLsaCksumSum_Object = MibTableColumn
ospfPmEntExternLsaCksumSum = _OspfPmEntExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 7),
    _OspfPmEntExternLsaCksumSum_Type()
)
ospfPmEntExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntExternLsaCksumSum.setStatus("current")


class _OspfPmEntTOSSupport_Type(TruthValue):
    """Custom type ospfPmEntTOSSupport based on TruthValue"""
    defaultValue = 2


_OspfPmEntTOSSupport_Type.__name__ = "TruthValue"
_OspfPmEntTOSSupport_Object = MibTableColumn
ospfPmEntTOSSupport = _OspfPmEntTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 8),
    _OspfPmEntTOSSupport_Type()
)
ospfPmEntTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntTOSSupport.setStatus("current")
_OspfPmEntOriginateNewLsas_Type = Counter32
_OspfPmEntOriginateNewLsas_Object = MibTableColumn
ospfPmEntOriginateNewLsas = _OspfPmEntOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 9),
    _OspfPmEntOriginateNewLsas_Type()
)
ospfPmEntOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntOriginateNewLsas.setStatus("current")
_OspfPmEntRxNewLsas_Type = Counter32
_OspfPmEntRxNewLsas_Object = MibTableColumn
ospfPmEntRxNewLsas = _OspfPmEntRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 10),
    _OspfPmEntRxNewLsas_Type()
)
ospfPmEntRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntRxNewLsas.setStatus("current")


class _OspfPmEntExtLsdbLimit_Type(Integer32):
    """Custom type ospfPmEntExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_OspfPmEntExtLsdbLimit_Type.__name__ = "Integer32"
_OspfPmEntExtLsdbLimit_Object = MibTableColumn
ospfPmEntExtLsdbLimit = _OspfPmEntExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 11),
    _OspfPmEntExtLsdbLimit_Type()
)
ospfPmEntExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntExtLsdbLimit.setStatus("current")


class _OspfPmEntMulticastExtns_Type(Integer32):
    """Custom type ospfPmEntMulticastExtns based on Integer32"""
    defaultValue = 0


_OspfPmEntMulticastExtns_Type.__name__ = "Integer32"
_OspfPmEntMulticastExtns_Object = MibTableColumn
ospfPmEntMulticastExtns = _OspfPmEntMulticastExtns_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 12),
    _OspfPmEntMulticastExtns_Type()
)
ospfPmEntMulticastExtns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntMulticastExtns.setStatus("current")


class _OspfPmEntExitOverflowIntvl_Type(PositiveInteger):
    """Custom type ospfPmEntExitOverflowIntvl based on PositiveInteger"""
    defaultValue = 0


_OspfPmEntExitOverflowIntvl_Type.__name__ = "PositiveInteger"
_OspfPmEntExitOverflowIntvl_Object = MibTableColumn
ospfPmEntExitOverflowIntvl = _OspfPmEntExitOverflowIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 13),
    _OspfPmEntExitOverflowIntvl_Type()
)
ospfPmEntExitOverflowIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntExitOverflowIntvl.setStatus("current")


class _OspfPmEntDemandExtensions_Type(TruthValue):
    """Custom type ospfPmEntDemandExtensions based on TruthValue"""
    defaultValue = 2


_OspfPmEntDemandExtensions_Type.__name__ = "TruthValue"
_OspfPmEntDemandExtensions_Object = MibTableColumn
ospfPmEntDemandExtensions = _OspfPmEntDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 14),
    _OspfPmEntDemandExtensions_Type()
)
ospfPmEntDemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntDemandExtensions.setStatus("current")


class _OspfPmEntRFC1583Comp_Type(TruthValue):
    """Custom type ospfPmEntRFC1583Comp based on TruthValue"""
    defaultValue = 2


_OspfPmEntRFC1583Comp_Type.__name__ = "TruthValue"
_OspfPmEntRFC1583Comp_Object = MibTableColumn
ospfPmEntRFC1583Comp = _OspfPmEntRFC1583Comp_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 15),
    _OspfPmEntRFC1583Comp_Type()
)
ospfPmEntRFC1583Comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntRFC1583Comp.setStatus("current")


class _OspfPmEntOpaqueLsaSupport_Type(TruthValue):
    """Custom type ospfPmEntOpaqueLsaSupport based on TruthValue"""
    defaultValue = 1


_OspfPmEntOpaqueLsaSupport_Type.__name__ = "TruthValue"
_OspfPmEntOpaqueLsaSupport_Object = MibTableColumn
ospfPmEntOpaqueLsaSupport = _OspfPmEntOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 16),
    _OspfPmEntOpaqueLsaSupport_Type()
)
ospfPmEntOpaqueLsaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntOpaqueLsaSupport.setStatus("current")


class _OspfPmEntTrafficEngSupport_Type(TruthValue):
    """Custom type ospfPmEntTrafficEngSupport based on TruthValue"""
    defaultValue = 1


_OspfPmEntTrafficEngSupport_Type.__name__ = "TruthValue"
_OspfPmEntTrafficEngSupport_Object = MibTableColumn
ospfPmEntTrafficEngSupport = _OspfPmEntTrafficEngSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 17),
    _OspfPmEntTrafficEngSupport_Type()
)
ospfPmEntTrafficEngSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntTrafficEngSupport.setStatus("current")
_OspfPmEntIndex_Type = OspfPmIndex
_OspfPmEntIndex_Object = MibTableColumn
ospfPmEntIndex = _OspfPmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 18),
    _OspfPmEntIndex_Type()
)
ospfPmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmEntIndex.setStatus("current")
_OspfPmEntOperStatus_Type = OspfPmOperStatus
_OspfPmEntOperStatus_Object = MibTableColumn
ospfPmEntOperStatus = _OspfPmEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 19),
    _OspfPmEntOperStatus_Type()
)
ospfPmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntOperStatus.setStatus("current")
_OspfPmEntRowStatus_Type = RowStatus
_OspfPmEntRowStatus_Object = MibTableColumn
ospfPmEntRowStatus = _OspfPmEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 20),
    _OspfPmEntRowStatus_Type()
)
ospfPmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntRowStatus.setStatus("current")


class _OspfPmEntCalcMaxDelay_Type(Unsigned32):
    """Custom type ospfPmEntCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000


_OspfPmEntCalcMaxDelay_Type.__name__ = "Unsigned32"
_OspfPmEntCalcMaxDelay_Object = MibTableColumn
ospfPmEntCalcMaxDelay = _OspfPmEntCalcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 21),
    _OspfPmEntCalcMaxDelay_Type()
)
ospfPmEntCalcMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCalcMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmEntCalcMaxDelay.setUnits("milliseconds")


class _OspfPmEntCalcThrshUpdStart_Type(Unsigned32):
    """Custom type ospfPmEntCalcThrshUpdStart based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmEntCalcThrshUpdStart_Type.__name__ = "Unsigned32"
_OspfPmEntCalcThrshUpdStart_Object = MibTableColumn
ospfPmEntCalcThrshUpdStart = _OspfPmEntCalcThrshUpdStart_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 22),
    _OspfPmEntCalcThrshUpdStart_Type()
)
ospfPmEntCalcThrshUpdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCalcThrshUpdStart.setStatus("current")


class _OspfPmEntCalcThrshUpdRestart_Type(Unsigned32):
    """Custom type ospfPmEntCalcThrshUpdRestart based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmEntCalcThrshUpdRestart_Type.__name__ = "Unsigned32"
_OspfPmEntCalcThrshUpdRestart_Object = MibTableColumn
ospfPmEntCalcThrshUpdRestart = _OspfPmEntCalcThrshUpdRestart_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 23),
    _OspfPmEntCalcThrshUpdRestart_Type()
)
ospfPmEntCalcThrshUpdRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCalcThrshUpdRestart.setStatus("current")


class _OspfPmEntCalcThrshIncUpdates_Type(Unsigned32):
    """Custom type ospfPmEntCalcThrshIncUpdates based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmEntCalcThrshIncUpdates_Type.__name__ = "Unsigned32"
_OspfPmEntCalcThrshIncUpdates_Object = MibTableColumn
ospfPmEntCalcThrshIncUpdates = _OspfPmEntCalcThrshIncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 24),
    _OspfPmEntCalcThrshIncUpdates_Type()
)
ospfPmEntCalcThrshIncUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCalcThrshIncUpdates.setStatus("current")


class _OspfPmEntCalcThrshIncSpfUpd_Type(Unsigned32):
    """Custom type ospfPmEntCalcThrshIncSpfUpd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmEntCalcThrshIncSpfUpd_Type.__name__ = "Unsigned32"
_OspfPmEntCalcThrshIncSpfUpd_Object = MibTableColumn
ospfPmEntCalcThrshIncSpfUpd = _OspfPmEntCalcThrshIncSpfUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 25),
    _OspfPmEntCalcThrshIncSpfUpd_Type()
)
ospfPmEntCalcThrshIncSpfUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCalcThrshIncSpfUpd.setStatus("current")


class _OspfPmEntCalcPauseFreq_Type(Unsigned32):
    """Custom type ospfPmEntCalcPauseFreq based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmEntCalcPauseFreq_Type.__name__ = "Unsigned32"
_OspfPmEntCalcPauseFreq_Object = MibTableColumn
ospfPmEntCalcPauseFreq = _OspfPmEntCalcPauseFreq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 26),
    _OspfPmEntCalcPauseFreq_Type()
)
ospfPmEntCalcPauseFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCalcPauseFreq.setStatus("current")


class _OspfPmEntRteMaxEqCostPaths_Type(Unsigned32):
    """Custom type ospfPmEntRteMaxEqCostPaths based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfPmEntRteMaxEqCostPaths_Type.__name__ = "Unsigned32"
_OspfPmEntRteMaxEqCostPaths_Object = MibTableColumn
ospfPmEntRteMaxEqCostPaths = _OspfPmEntRteMaxEqCostPaths_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 27),
    _OspfPmEntRteMaxEqCostPaths_Type()
)
ospfPmEntRteMaxEqCostPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntRteMaxEqCostPaths.setStatus("current")


class _OspfPmEntCheckAge_Type(Unsigned32):
    """Custom type ospfPmEntCheckAge based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmEntCheckAge_Type.__name__ = "Unsigned32"
_OspfPmEntCheckAge_Object = MibTableColumn
ospfPmEntCheckAge = _OspfPmEntCheckAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 28),
    _OspfPmEntCheckAge_Type()
)
ospfPmEntCheckAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntCheckAge.setStatus("current")


class _OspfPmEntExtLsaRfshIntvl_Type(Integer32):
    """Custom type ospfPmEntExtLsaRfshIntvl based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_OspfPmEntExtLsaRfshIntvl_Type.__name__ = "Integer32"
_OspfPmEntExtLsaRfshIntvl_Object = MibTableColumn
ospfPmEntExtLsaRfshIntvl = _OspfPmEntExtLsaRfshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 29),
    _OspfPmEntExtLsaRfshIntvl_Type()
)
ospfPmEntExtLsaRfshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntExtLsaRfshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmEntExtLsaRfshIntvl.setUnits("seconds")
_OspfPmEntExtOpLsaCount_Type = Gauge32
_OspfPmEntExtOpLsaCount_Object = MibTableColumn
ospfPmEntExtOpLsaCount = _OspfPmEntExtOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 30),
    _OspfPmEntExtOpLsaCount_Type()
)
ospfPmEntExtOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntExtOpLsaCount.setStatus("current")
_OspfPmEntExtOpLsaCksumSum_Type = Integer32
_OspfPmEntExtOpLsaCksumSum_Object = MibTableColumn
ospfPmEntExtOpLsaCksumSum = _OspfPmEntExtOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 31),
    _OspfPmEntExtOpLsaCksumSum_Type()
)
ospfPmEntExtOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntExtOpLsaCksumSum.setStatus("current")
_OspfPmEntNumUpdPending_Type = Unsigned32
_OspfPmEntNumUpdPending_Object = MibTableColumn
ospfPmEntNumUpdPending = _OspfPmEntNumUpdPending_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 32),
    _OspfPmEntNumUpdPending_Type()
)
ospfPmEntNumUpdPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntNumUpdPending.setStatus("current")
_OspfPmEntNumUpdMerged_Type = Unsigned32
_OspfPmEntNumUpdMerged_Object = MibTableColumn
ospfPmEntNumUpdMerged = _OspfPmEntNumUpdMerged_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 33),
    _OspfPmEntNumUpdMerged_Type()
)
ospfPmEntNumUpdMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntNumUpdMerged.setStatus("current")
_OspfPmEntNumCksumsPending_Type = Unsigned32
_OspfPmEntNumCksumsPending_Object = MibTableColumn
ospfPmEntNumCksumsPending = _OspfPmEntNumCksumsPending_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 34),
    _OspfPmEntNumCksumsPending_Type()
)
ospfPmEntNumCksumsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntNumCksumsPending.setStatus("current")


class _OspfPmEntDoGraceHitless_Type(TruthValue):
    """Custom type ospfPmEntDoGraceHitless based on TruthValue"""
    defaultValue = 2


_OspfPmEntDoGraceHitless_Type.__name__ = "TruthValue"
_OspfPmEntDoGraceHitless_Object = MibTableColumn
ospfPmEntDoGraceHitless = _OspfPmEntDoGraceHitless_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 35),
    _OspfPmEntDoGraceHitless_Type()
)
ospfPmEntDoGraceHitless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntDoGraceHitless.setStatus("current")


class _OspfPmEntDoGraceUnplannedHitless_Type(TruthValue):
    """Custom type ospfPmEntDoGraceUnplannedHitless based on TruthValue"""
    defaultValue = 2


_OspfPmEntDoGraceUnplannedHitless_Type.__name__ = "TruthValue"
_OspfPmEntDoGraceUnplannedHitless_Object = MibTableColumn
ospfPmEntDoGraceUnplannedHitless = _OspfPmEntDoGraceUnplannedHitless_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 36),
    _OspfPmEntDoGraceUnplannedHitless_Type()
)
ospfPmEntDoGraceUnplannedHitless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntDoGraceUnplannedHitless.setStatus("current")


class _OspfPmEntHitlessGracePeriod_Type(UpToRefreshInterval):
    """Custom type ospfPmEntHitlessGracePeriod based on UpToRefreshInterval"""
    defaultValue = 120


_OspfPmEntHitlessGracePeriod_Type.__name__ = "UpToRefreshInterval"
_OspfPmEntHitlessGracePeriod_Object = MibTableColumn
ospfPmEntHitlessGracePeriod = _OspfPmEntHitlessGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 37),
    _OspfPmEntHitlessGracePeriod_Type()
)
ospfPmEntHitlessGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntHitlessGracePeriod.setStatus("current")


class _OspfPmEntHitlessRestartReason_Type(OspfHitlessRestartReasons):
    """Custom type ospfPmEntHitlessRestartReason based on OspfHitlessRestartReasons"""
    defaultValue = 0


_OspfPmEntHitlessRestartReason_Type.__name__ = "OspfHitlessRestartReasons"
_OspfPmEntHitlessRestartReason_Object = MibTableColumn
ospfPmEntHitlessRestartReason = _OspfPmEntHitlessRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 38),
    _OspfPmEntHitlessRestartReason_Type()
)
ospfPmEntHitlessRestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntHitlessRestartReason.setStatus("current")


class _OspfPmEntTERouterId_Type(RouterID):
    """Custom type ospfPmEntTERouterId based on RouterID"""
    defaultHexValue = "00000000"


_OspfPmEntTERouterId_Type.__name__ = "RouterID"
_OspfPmEntTERouterId_Object = MibTableColumn
ospfPmEntTERouterId = _OspfPmEntTERouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 39),
    _OspfPmEntTERouterId_Type()
)
ospfPmEntTERouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmEntTERouterId.setStatus("current")
_OspfPmEntPrivateData_Type = OspfPmEntPrivateDataType
_OspfPmEntPrivateData_Object = MibTableColumn
ospfPmEntPrivateData = _OspfPmEntPrivateData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 40),
    _OspfPmEntPrivateData_Type()
)
ospfPmEntPrivateData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntPrivateData.setStatus("current")


class _OspfPmEntSupportEnniRouting_Type(TruthValue):
    """Custom type ospfPmEntSupportEnniRouting based on TruthValue"""
    defaultValue = 2


_OspfPmEntSupportEnniRouting_Type.__name__ = "TruthValue"
_OspfPmEntSupportEnniRouting_Object = MibTableColumn
ospfPmEntSupportEnniRouting = _OspfPmEntSupportEnniRouting_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 41),
    _OspfPmEntSupportEnniRouting_Type()
)
ospfPmEntSupportEnniRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntSupportEnniRouting.setStatus("current")


class _OspfPmEntRestartStatus_Type(Integer32):
    """Custom type ospfPmEntRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_OspfPmEntRestartStatus_Type.__name__ = "Integer32"
_OspfPmEntRestartStatus_Object = MibTableColumn
ospfPmEntRestartStatus = _OspfPmEntRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 42),
    _OspfPmEntRestartStatus_Type()
)
ospfPmEntRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntRestartStatus.setStatus("current")
_OspfPmEntRestartAge_Type = UpToRefreshInterval
_OspfPmEntRestartAge_Object = MibTableColumn
ospfPmEntRestartAge = _OspfPmEntRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 43),
    _OspfPmEntRestartAge_Type()
)
ospfPmEntRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmEntRestartAge.setUnits("seconds")
_OspfPmEntRestartExitReason_Type = OspfRestartExitReason
_OspfPmEntRestartExitReason_Object = MibTableColumn
ospfPmEntRestartExitReason = _OspfPmEntRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 44),
    _OspfPmEntRestartExitReason_Type()
)
ospfPmEntRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntRestartExitReason.setStatus("current")
_OspfPmEntCurrentRouterId_Type = RouterID
_OspfPmEntCurrentRouterId_Object = MibTableColumn
ospfPmEntCurrentRouterId = _OspfPmEntCurrentRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 45),
    _OspfPmEntCurrentRouterId_Type()
)
ospfPmEntCurrentRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntCurrentRouterId.setStatus("current")
_OspfPmEntCurrentTERouterId_Type = RouterID
_OspfPmEntCurrentTERouterId_Object = MibTableColumn
ospfPmEntCurrentTERouterId = _OspfPmEntCurrentTERouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 46),
    _OspfPmEntCurrentTERouterId_Type()
)
ospfPmEntCurrentTERouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntCurrentTERouterId.setStatus("current")


class _OspfPmEntCalcSoonAfterIfChng_Type(TruthValue):
    """Custom type ospfPmEntCalcSoonAfterIfChng based on TruthValue"""
    defaultValue = 2


_OspfPmEntCalcSoonAfterIfChng_Type.__name__ = "TruthValue"
_OspfPmEntCalcSoonAfterIfChng_Object = MibTableColumn
ospfPmEntCalcSoonAfterIfChng = _OspfPmEntCalcSoonAfterIfChng_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 47),
    _OspfPmEntCalcSoonAfterIfChng_Type()
)
ospfPmEntCalcSoonAfterIfChng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntCalcSoonAfterIfChng.setStatus("current")


class _OspfPmEntI3EntIndex_Type(NumericIndex):
    """Custom type ospfPmEntI3EntIndex based on NumericIndex"""
    defaultValue = 1


_OspfPmEntI3EntIndex_Type.__name__ = "NumericIndex"
_OspfPmEntI3EntIndex_Object = MibTableColumn
ospfPmEntI3EntIndex = _OspfPmEntI3EntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 48),
    _OspfPmEntI3EntIndex_Type()
)
ospfPmEntI3EntIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntI3EntIndex.setStatus("current")


class _OspfPmEntEnableIgpShortcut_Type(TruthValue):
    """Custom type ospfPmEntEnableIgpShortcut based on TruthValue"""
    defaultValue = 1


_OspfPmEntEnableIgpShortcut_Type.__name__ = "TruthValue"
_OspfPmEntEnableIgpShortcut_Object = MibTableColumn
ospfPmEntEnableIgpShortcut = _OspfPmEntEnableIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 49),
    _OspfPmEntEnableIgpShortcut_Type()
)
ospfPmEntEnableIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntEnableIgpShortcut.setStatus("current")


class _OspfPmEntVpnPeCeSupport_Type(TruthValue):
    """Custom type ospfPmEntVpnPeCeSupport based on TruthValue"""
    defaultValue = 2


_OspfPmEntVpnPeCeSupport_Type.__name__ = "TruthValue"
_OspfPmEntVpnPeCeSupport_Object = MibTableColumn
ospfPmEntVpnPeCeSupport = _OspfPmEntVpnPeCeSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 50),
    _OspfPmEntVpnPeCeSupport_Type()
)
ospfPmEntVpnPeCeSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntVpnPeCeSupport.setStatus("current")


class _OspfPmEntVpnRouteTag_Type(Unsigned32):
    """Custom type ospfPmEntVpnRouteTag based on Unsigned32"""
    defaultValue = 0


_OspfPmEntVpnRouteTag_Type.__name__ = "Unsigned32"
_OspfPmEntVpnRouteTag_Object = MibTableColumn
ospfPmEntVpnRouteTag = _OspfPmEntVpnRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 51),
    _OspfPmEntVpnRouteTag_Type()
)
ospfPmEntVpnRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntVpnRouteTag.setStatus("current")


class _OspfPmEntVpnRouterIdAttr_Type(TruthValue):
    """Custom type ospfPmEntVpnRouterIdAttr based on TruthValue"""
    defaultValue = 2


_OspfPmEntVpnRouterIdAttr_Type.__name__ = "TruthValue"
_OspfPmEntVpnRouterIdAttr_Object = MibTableColumn
ospfPmEntVpnRouterIdAttr = _OspfPmEntVpnRouterIdAttr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 52),
    _OspfPmEntVpnRouterIdAttr_Type()
)
ospfPmEntVpnRouterIdAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntVpnRouterIdAttr.setStatus("current")


class _OspfPmEntDfltExtType1Metric_Type(Integer32):
    """Custom type ospfPmEntDfltExtType1Metric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfPmEntDfltExtType1Metric_Type.__name__ = "Integer32"
_OspfPmEntDfltExtType1Metric_Object = MibTableColumn
ospfPmEntDfltExtType1Metric = _OspfPmEntDfltExtType1Metric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 53),
    _OspfPmEntDfltExtType1Metric_Type()
)
ospfPmEntDfltExtType1Metric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntDfltExtType1Metric.setStatus("current")


class _OspfPmEntDfltExtType2Metric_Type(Integer32):
    """Custom type ospfPmEntDfltExtType2Metric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfPmEntDfltExtType2Metric_Type.__name__ = "Integer32"
_OspfPmEntDfltExtType2Metric_Object = MibTableColumn
ospfPmEntDfltExtType2Metric = _OspfPmEntDfltExtType2Metric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 54),
    _OspfPmEntDfltExtType2Metric_Type()
)
ospfPmEntDfltExtType2Metric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntDfltExtType2Metric.setStatus("current")


class _OspfPmEntRtmPurgeTime_Type(Integer32):
    """Custom type ospfPmEntRtmPurgeTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmEntRtmPurgeTime_Type.__name__ = "Integer32"
_OspfPmEntRtmPurgeTime_Object = MibTableColumn
ospfPmEntRtmPurgeTime = _OspfPmEntRtmPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 55),
    _OspfPmEntRtmPurgeTime_Type()
)
ospfPmEntRtmPurgeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntRtmPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmEntRtmPurgeTime.setUnits("seconds")


class _OspfPmEntMinLsInterval_Type(Integer32):
    """Custom type ospfPmEntMinLsInterval based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_OspfPmEntMinLsInterval_Type.__name__ = "Integer32"
_OspfPmEntMinLsInterval_Object = MibTableColumn
ospfPmEntMinLsInterval = _OspfPmEntMinLsInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 56),
    _OspfPmEntMinLsInterval_Type()
)
ospfPmEntMinLsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntMinLsInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmEntMinLsInterval.setUnits("milliseconds")


class _OspfPmEntMinLsArrival_Type(Integer32):
    """Custom type ospfPmEntMinLsArrival based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_OspfPmEntMinLsArrival_Type.__name__ = "Integer32"
_OspfPmEntMinLsArrival_Object = MibTableColumn
ospfPmEntMinLsArrival = _OspfPmEntMinLsArrival_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 57),
    _OspfPmEntMinLsArrival_Type()
)
ospfPmEntMinLsArrival.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntMinLsArrival.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmEntMinLsArrival.setUnits("milliseconds")


class _OspfPmEntVpnDfltShamLinkMetric_Type(Integer32):
    """Custom type ospfPmEntVpnDfltShamLinkMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfPmEntVpnDfltShamLinkMetric_Type.__name__ = "Integer32"
_OspfPmEntVpnDfltShamLinkMetric_Object = MibTableColumn
ospfPmEntVpnDfltShamLinkMetric = _OspfPmEntVpnDfltShamLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 58),
    _OspfPmEntVpnDfltShamLinkMetric_Type()
)
ospfPmEntVpnDfltShamLinkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntVpnDfltShamLinkMetric.setStatus("current")


class _OspfPmEntInstanceId_Type(Integer32):
    """Custom type ospfPmEntInstanceId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfPmEntInstanceId_Type.__name__ = "Integer32"
_OspfPmEntInstanceId_Object = MibTableColumn
ospfPmEntInstanceId = _OspfPmEntInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 59),
    _OspfPmEntInstanceId_Type()
)
ospfPmEntInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntInstanceId.setStatus("current")


class _OspfPmEntStatsReset_Type(TruthValue):
    """Custom type ospfPmEntStatsReset based on TruthValue"""
    defaultValue = 2


_OspfPmEntStatsReset_Type.__name__ = "TruthValue"
_OspfPmEntStatsReset_Object = MibTableColumn
ospfPmEntStatsReset = _OspfPmEntStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 60),
    _OspfPmEntStatsReset_Type()
)
ospfPmEntStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntStatsReset.setStatus("current")


class _OspfPmEntEnableTrapSupport_Type(TruthValue):
    """Custom type ospfPmEntEnableTrapSupport based on TruthValue"""
    defaultValue = 2


_OspfPmEntEnableTrapSupport_Type.__name__ = "TruthValue"
_OspfPmEntEnableTrapSupport_Object = MibTableColumn
ospfPmEntEnableTrapSupport = _OspfPmEntEnableTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 1, 1, 61),
    _OspfPmEntEnableTrapSupport_Type()
)
ospfPmEntEnableTrapSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmEntEnableTrapSupport.setStatus("current")
_OspfPmAreaTable_Object = MibTable
ospfPmAreaTable = _OspfPmAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ospfPmAreaTable.setStatus("current")
_OspfPmAreaEntry_Object = MibTableRow
ospfPmAreaEntry = _OspfPmAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1)
)
ospfPmAreaEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmAreaApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmAreaId"),
)
if mibBuilder.loadTexts:
    ospfPmAreaEntry.setStatus("current")
_OspfPmAreaId_Type = AreaID
_OspfPmAreaId_Object = MibTableColumn
ospfPmAreaId = _OspfPmAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 1),
    _OspfPmAreaId_Type()
)
ospfPmAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaId.setStatus("current")


class _OspfPmAuthType_Type(OspfAuthTypes):
    """Custom type ospfPmAuthType based on OspfAuthTypes"""
    defaultValue = 0


_OspfPmAuthType_Type.__name__ = "OspfAuthTypes"
_OspfPmAuthType_Object = MibTableColumn
ospfPmAuthType = _OspfPmAuthType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 2),
    _OspfPmAuthType_Type()
)
ospfPmAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAuthType.setStatus("obsolete")


class _OspfPmImportAsExtern_Type(OspfImportTypes):
    """Custom type ospfPmImportAsExtern based on OspfImportTypes"""
    defaultValue = 1


_OspfPmImportAsExtern_Type.__name__ = "OspfImportTypes"
_OspfPmImportAsExtern_Object = MibTableColumn
ospfPmImportAsExtern = _OspfPmImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 3),
    _OspfPmImportAsExtern_Type()
)
ospfPmImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmImportAsExtern.setStatus("current")
_OspfPmSpfRuns_Type = Counter32
_OspfPmSpfRuns_Object = MibTableColumn
ospfPmSpfRuns = _OspfPmSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 4),
    _OspfPmSpfRuns_Type()
)
ospfPmSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfRuns.setStatus("current")
_OspfPmAreaBdrRtrCount_Type = Gauge32
_OspfPmAreaBdrRtrCount_Object = MibTableColumn
ospfPmAreaBdrRtrCount = _OspfPmAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 5),
    _OspfPmAreaBdrRtrCount_Type()
)
ospfPmAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaBdrRtrCount.setStatus("current")
_OspfPmASBdrRtrCount_Type = Gauge32
_OspfPmASBdrRtrCount_Object = MibTableColumn
ospfPmASBdrRtrCount = _OspfPmASBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 6),
    _OspfPmASBdrRtrCount_Type()
)
ospfPmASBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmASBdrRtrCount.setStatus("current")
_OspfPmAreaLsaCount_Type = Gauge32
_OspfPmAreaLsaCount_Object = MibTableColumn
ospfPmAreaLsaCount = _OspfPmAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 7),
    _OspfPmAreaLsaCount_Type()
)
ospfPmAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaLsaCount.setStatus("current")


class _OspfPmAreaLsaCksumSum_Type(Integer32):
    """Custom type ospfPmAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_OspfPmAreaLsaCksumSum_Type.__name__ = "Integer32"
_OspfPmAreaLsaCksumSum_Object = MibTableColumn
ospfPmAreaLsaCksumSum = _OspfPmAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 8),
    _OspfPmAreaLsaCksumSum_Type()
)
ospfPmAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaLsaCksumSum.setStatus("current")


class _OspfPmAreaSummary_Type(OspfSummaryTypes):
    """Custom type ospfPmAreaSummary based on OspfSummaryTypes"""
    defaultValue = 2


_OspfPmAreaSummary_Type.__name__ = "OspfSummaryTypes"
_OspfPmAreaSummary_Object = MibTableColumn
ospfPmAreaSummary = _OspfPmAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 9),
    _OspfPmAreaSummary_Type()
)
ospfPmAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaSummary.setStatus("current")
_OspfPmAreaStatus_Type = RowStatus
_OspfPmAreaStatus_Object = MibTableColumn
ospfPmAreaStatus = _OspfPmAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 10),
    _OspfPmAreaStatus_Type()
)
ospfPmAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaStatus.setStatus("current")


class _OspfPmAreaNssaTranslatorRole_Type(OspfTransRoles):
    """Custom type ospfPmAreaNssaTranslatorRole based on OspfTransRoles"""
    defaultValue = 2


_OspfPmAreaNssaTranslatorRole_Type.__name__ = "OspfTransRoles"
_OspfPmAreaNssaTranslatorRole_Object = MibTableColumn
ospfPmAreaNssaTranslatorRole = _OspfPmAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 11),
    _OspfPmAreaNssaTranslatorRole_Type()
)
ospfPmAreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaNssaTranslatorRole.setStatus("current")
_OspfPmAreaNssaTranslatorState_Type = OspfTransStates
_OspfPmAreaNssaTranslatorState_Object = MibTableColumn
ospfPmAreaNssaTranslatorState = _OspfPmAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 12),
    _OspfPmAreaNssaTranslatorState_Type()
)
ospfPmAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaNssaTranslatorState.setStatus("current")


class _OspfPmAreaNssaTranStabIntvl_Type(PositiveInteger):
    """Custom type ospfPmAreaNssaTranStabIntvl based on PositiveInteger"""
    defaultValue = 40


_OspfPmAreaNssaTranStabIntvl_Type.__name__ = "PositiveInteger"
_OspfPmAreaNssaTranStabIntvl_Object = MibTableColumn
ospfPmAreaNssaTranStabIntvl = _OspfPmAreaNssaTranStabIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 13),
    _OspfPmAreaNssaTranStabIntvl_Type()
)
ospfPmAreaNssaTranStabIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaNssaTranStabIntvl.setStatus("current")
_OspfPmAreaNssaTranslatorEvents_Type = Counter32
_OspfPmAreaNssaTranslatorEvents_Object = MibTableColumn
ospfPmAreaNssaTranslatorEvents = _OspfPmAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 14),
    _OspfPmAreaNssaTranslatorEvents_Type()
)
ospfPmAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaNssaTranslatorEvents.setStatus("current")
_OspfPmAreaApplIndex_Type = OspfPmIndex
_OspfPmAreaApplIndex_Object = MibTableColumn
ospfPmAreaApplIndex = _OspfPmAreaApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 15),
    _OspfPmAreaApplIndex_Type()
)
ospfPmAreaApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaApplIndex.setStatus("current")


class _OspfPmAreaAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfPmAreaAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmAreaAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfPmAreaAdminStatus_Object = MibTableColumn
ospfPmAreaAdminStatus = _OspfPmAreaAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 16),
    _OspfPmAreaAdminStatus_Type()
)
ospfPmAreaAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaAdminStatus.setStatus("current")
_OspfPmAreaOperStatus_Type = OspfPmOperStatus
_OspfPmAreaOperStatus_Object = MibTableColumn
ospfPmAreaOperStatus = _OspfPmAreaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 17),
    _OspfPmAreaOperStatus_Type()
)
ospfPmAreaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaOperStatus.setStatus("current")


class _OspfPmAreaTransitCapability_Type(TruthValue):
    """Custom type ospfPmAreaTransitCapability based on TruthValue"""
    defaultValue = 2


_OspfPmAreaTransitCapability_Type.__name__ = "TruthValue"
_OspfPmAreaTransitCapability_Object = MibTableColumn
ospfPmAreaTransitCapability = _OspfPmAreaTransitCapability_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 18),
    _OspfPmAreaTransitCapability_Type()
)
ospfPmAreaTransitCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaTransitCapability.setStatus("current")


class _OspfPmAreaLsaRfshIntvl_Type(Integer32):
    """Custom type ospfPmAreaLsaRfshIntvl based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_OspfPmAreaLsaRfshIntvl_Type.__name__ = "Integer32"
_OspfPmAreaLsaRfshIntvl_Object = MibTableColumn
ospfPmAreaLsaRfshIntvl = _OspfPmAreaLsaRfshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 19),
    _OspfPmAreaLsaRfshIntvl_Type()
)
ospfPmAreaLsaRfshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmAreaLsaRfshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmAreaLsaRfshIntvl.setUnits("seconds")
_OspfPmAreaRtrLsaCount_Type = Gauge32
_OspfPmAreaRtrLsaCount_Object = MibTableColumn
ospfPmAreaRtrLsaCount = _OspfPmAreaRtrLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 20),
    _OspfPmAreaRtrLsaCount_Type()
)
ospfPmAreaRtrLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaRtrLsaCount.setStatus("current")
_OspfPmAreaRtrLsaCksumSum_Type = Integer32
_OspfPmAreaRtrLsaCksumSum_Object = MibTableColumn
ospfPmAreaRtrLsaCksumSum = _OspfPmAreaRtrLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 21),
    _OspfPmAreaRtrLsaCksumSum_Type()
)
ospfPmAreaRtrLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaRtrLsaCksumSum.setStatus("current")
_OspfPmAreaNetLsaCount_Type = Gauge32
_OspfPmAreaNetLsaCount_Object = MibTableColumn
ospfPmAreaNetLsaCount = _OspfPmAreaNetLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 22),
    _OspfPmAreaNetLsaCount_Type()
)
ospfPmAreaNetLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaNetLsaCount.setStatus("current")
_OspfPmAreaNetLsaCksumSum_Type = Integer32
_OspfPmAreaNetLsaCksumSum_Object = MibTableColumn
ospfPmAreaNetLsaCksumSum = _OspfPmAreaNetLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 23),
    _OspfPmAreaNetLsaCksumSum_Type()
)
ospfPmAreaNetLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaNetLsaCksumSum.setStatus("current")
_OspfPmAreaSummLsaCount_Type = Gauge32
_OspfPmAreaSummLsaCount_Object = MibTableColumn
ospfPmAreaSummLsaCount = _OspfPmAreaSummLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 24),
    _OspfPmAreaSummLsaCount_Type()
)
ospfPmAreaSummLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaSummLsaCount.setStatus("current")
_OspfPmAreaSummLsaCksumSum_Type = Integer32
_OspfPmAreaSummLsaCksumSum_Object = MibTableColumn
ospfPmAreaSummLsaCksumSum = _OspfPmAreaSummLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 25),
    _OspfPmAreaSummLsaCksumSum_Type()
)
ospfPmAreaSummLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaSummLsaCksumSum.setStatus("current")
_OspfPmAreaSummAsLsaCount_Type = Gauge32
_OspfPmAreaSummAsLsaCount_Object = MibTableColumn
ospfPmAreaSummAsLsaCount = _OspfPmAreaSummAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 26),
    _OspfPmAreaSummAsLsaCount_Type()
)
ospfPmAreaSummAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaSummAsLsaCount.setStatus("current")
_OspfPmAreaSummAsLsaCksumSum_Type = Integer32
_OspfPmAreaSummAsLsaCksumSum_Object = MibTableColumn
ospfPmAreaSummAsLsaCksumSum = _OspfPmAreaSummAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 27),
    _OspfPmAreaSummAsLsaCksumSum_Type()
)
ospfPmAreaSummAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaSummAsLsaCksumSum.setStatus("current")
_OspfPmAreaNssaLsaCount_Type = Gauge32
_OspfPmAreaNssaLsaCount_Object = MibTableColumn
ospfPmAreaNssaLsaCount = _OspfPmAreaNssaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 28),
    _OspfPmAreaNssaLsaCount_Type()
)
ospfPmAreaNssaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaNssaLsaCount.setStatus("current")
_OspfPmAreaNssaLsaCksumSum_Type = Integer32
_OspfPmAreaNssaLsaCksumSum_Object = MibTableColumn
ospfPmAreaNssaLsaCksumSum = _OspfPmAreaNssaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 29),
    _OspfPmAreaNssaLsaCksumSum_Type()
)
ospfPmAreaNssaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaNssaLsaCksumSum.setStatus("current")
_OspfPmAreaOpLsaCount_Type = Gauge32
_OspfPmAreaOpLsaCount_Object = MibTableColumn
ospfPmAreaOpLsaCount = _OspfPmAreaOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 30),
    _OspfPmAreaOpLsaCount_Type()
)
ospfPmAreaOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaOpLsaCount.setStatus("current")
_OspfPmAreaOpLsaCksumSum_Type = Integer32
_OspfPmAreaOpLsaCksumSum_Object = MibTableColumn
ospfPmAreaOpLsaCksumSum = _OspfPmAreaOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 31),
    _OspfPmAreaOpLsaCksumSum_Type()
)
ospfPmAreaOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmAreaOpLsaCksumSum.setStatus("current")


class _OspfPmAreaNssaNoExtRedist_Type(TruthValue):
    """Custom type ospfPmAreaNssaNoExtRedist based on TruthValue"""
    defaultValue = 2


_OspfPmAreaNssaNoExtRedist_Type.__name__ = "TruthValue"
_OspfPmAreaNssaNoExtRedist_Object = MibTableColumn
ospfPmAreaNssaNoExtRedist = _OspfPmAreaNssaNoExtRedist_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 2, 1, 32),
    _OspfPmAreaNssaNoExtRedist_Type()
)
ospfPmAreaNssaNoExtRedist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaNssaNoExtRedist.setStatus("current")
_OspfPmStubAreaTable_Object = MibTable
ospfPmStubAreaTable = _OspfPmStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ospfPmStubAreaTable.setStatus("current")
_OspfPmStubAreaEntry_Object = MibTableRow
ospfPmStubAreaEntry = _OspfPmStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1)
)
ospfPmStubAreaEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmStubApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmStubAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmStubTOS"),
)
if mibBuilder.loadTexts:
    ospfPmStubAreaEntry.setStatus("current")
_OspfPmStubAreaId_Type = AreaID
_OspfPmStubAreaId_Object = MibTableColumn
ospfPmStubAreaId = _OspfPmStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1, 1),
    _OspfPmStubAreaId_Type()
)
ospfPmStubAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmStubAreaId.setStatus("current")
_OspfPmStubTOS_Type = TOSType
_OspfPmStubTOS_Object = MibTableColumn
ospfPmStubTOS = _OspfPmStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1, 2),
    _OspfPmStubTOS_Type()
)
ospfPmStubTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmStubTOS.setStatus("current")


class _OspfPmStubMetric_Type(BigMetric):
    """Custom type ospfPmStubMetric based on BigMetric"""
    defaultValue = 1


_OspfPmStubMetric_Type.__name__ = "BigMetric"
_OspfPmStubMetric_Object = MibTableColumn
ospfPmStubMetric = _OspfPmStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1, 3),
    _OspfPmStubMetric_Type()
)
ospfPmStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmStubMetric.setStatus("current")
_OspfPmStubStatus_Type = RowStatus
_OspfPmStubStatus_Object = MibTableColumn
ospfPmStubStatus = _OspfPmStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1, 4),
    _OspfPmStubStatus_Type()
)
ospfPmStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmStubStatus.setStatus("current")


class _OspfPmStubMetricType_Type(OspfMetricTypes):
    """Custom type ospfPmStubMetricType based on OspfMetricTypes"""
    defaultValue = 1


_OspfPmStubMetricType_Type.__name__ = "OspfMetricTypes"
_OspfPmStubMetricType_Object = MibTableColumn
ospfPmStubMetricType = _OspfPmStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1, 5),
    _OspfPmStubMetricType_Type()
)
ospfPmStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmStubMetricType.setStatus("current")
_OspfPmStubApplIndex_Type = OspfPmIndex
_OspfPmStubApplIndex_Object = MibTableColumn
ospfPmStubApplIndex = _OspfPmStubApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 3, 1, 6),
    _OspfPmStubApplIndex_Type()
)
ospfPmStubApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmStubApplIndex.setStatus("current")
_OspfPmLsdbTable_Object = MibTable
ospfPmLsdbTable = _OspfPmLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ospfPmLsdbTable.setStatus("current")
_OspfPmLsdbEntry_Object = MibTableRow
ospfPmLsdbEntry = _OspfPmLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1)
)
ospfPmLsdbEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmLsdbApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmLsdbAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmLsdbLsid"),
    (0, "DC-OSPF-MIB", "ospfPmLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfPmLsdbEntry.setStatus("current")
_OspfPmLsdbAreaId_Type = AreaID
_OspfPmLsdbAreaId_Object = MibTableColumn
ospfPmLsdbAreaId = _OspfPmLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 1),
    _OspfPmLsdbAreaId_Type()
)
ospfPmLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLsdbAreaId.setStatus("current")
_OspfPmLsdbType_Type = OspfAreaLsTypes
_OspfPmLsdbType_Object = MibTableColumn
ospfPmLsdbType = _OspfPmLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 2),
    _OspfPmLsdbType_Type()
)
ospfPmLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLsdbType.setStatus("current")
_OspfPmLsdbLsid_Type = IpAddress
_OspfPmLsdbLsid_Object = MibTableColumn
ospfPmLsdbLsid = _OspfPmLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 3),
    _OspfPmLsdbLsid_Type()
)
ospfPmLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLsdbLsid.setStatus("current")
_OspfPmLsdbRouterId_Type = RouterID
_OspfPmLsdbRouterId_Object = MibTableColumn
ospfPmLsdbRouterId = _OspfPmLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 4),
    _OspfPmLsdbRouterId_Type()
)
ospfPmLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLsdbRouterId.setStatus("current")
_OspfPmLsdbSequence_Type = Integer32
_OspfPmLsdbSequence_Object = MibTableColumn
ospfPmLsdbSequence = _OspfPmLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 5),
    _OspfPmLsdbSequence_Type()
)
ospfPmLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLsdbSequence.setStatus("current")
_OspfPmLsdbAge_Type = Integer32
_OspfPmLsdbAge_Object = MibTableColumn
ospfPmLsdbAge = _OspfPmLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 6),
    _OspfPmLsdbAge_Type()
)
ospfPmLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLsdbAge.setStatus("current")
_OspfPmLsdbChecksum_Type = Integer32
_OspfPmLsdbChecksum_Object = MibTableColumn
ospfPmLsdbChecksum = _OspfPmLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 7),
    _OspfPmLsdbChecksum_Type()
)
ospfPmLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLsdbChecksum.setStatus("current")


class _OspfPmLsdbAdvertisement_Type(OctetString):
    """Custom type ospfPmLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfPmLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfPmLsdbAdvertisement_Object = MibTableColumn
ospfPmLsdbAdvertisement = _OspfPmLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 8),
    _OspfPmLsdbAdvertisement_Type()
)
ospfPmLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLsdbAdvertisement.setStatus("current")
_OspfPmLsdbApplIndex_Type = OspfPmIndex
_OspfPmLsdbApplIndex_Object = MibTableColumn
ospfPmLsdbApplIndex = _OspfPmLsdbApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 4, 1, 9),
    _OspfPmLsdbApplIndex_Type()
)
ospfPmLsdbApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLsdbApplIndex.setStatus("current")
_OspfPmHostTable_Object = MibTable
ospfPmHostTable = _OspfPmHostTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ospfPmHostTable.setStatus("current")
_OspfPmHostEntry_Object = MibTableRow
ospfPmHostEntry = _OspfPmHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1)
)
ospfPmHostEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmHostApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmHostIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmHostTOS"),
)
if mibBuilder.loadTexts:
    ospfPmHostEntry.setStatus("current")
_OspfPmHostIpAddress_Type = IpAddress
_OspfPmHostIpAddress_Object = MibTableColumn
ospfPmHostIpAddress = _OspfPmHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 1),
    _OspfPmHostIpAddress_Type()
)
ospfPmHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmHostIpAddress.setStatus("current")
_OspfPmHostTOS_Type = TOSType
_OspfPmHostTOS_Object = MibTableColumn
ospfPmHostTOS = _OspfPmHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 2),
    _OspfPmHostTOS_Type()
)
ospfPmHostTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmHostTOS.setStatus("current")


class _OspfPmHostMetric_Type(Metric):
    """Custom type ospfPmHostMetric based on Metric"""
    defaultValue = 1


_OspfPmHostMetric_Type.__name__ = "Metric"
_OspfPmHostMetric_Object = MibTableColumn
ospfPmHostMetric = _OspfPmHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 3),
    _OspfPmHostMetric_Type()
)
ospfPmHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmHostMetric.setStatus("current")
_OspfPmHostStatus_Type = RowStatus
_OspfPmHostStatus_Object = MibTableColumn
ospfPmHostStatus = _OspfPmHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 4),
    _OspfPmHostStatus_Type()
)
ospfPmHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmHostStatus.setStatus("current")


class _OspfPmHostAreaID_Type(AreaID):
    """Custom type ospfPmHostAreaID based on AreaID"""
    defaultHexValue = "00000000"


_OspfPmHostAreaID_Type.__name__ = "AreaID"
_OspfPmHostAreaID_Object = MibTableColumn
ospfPmHostAreaID = _OspfPmHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 5),
    _OspfPmHostAreaID_Type()
)
ospfPmHostAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmHostAreaID.setStatus("current")
_OspfPmHostApplIndex_Type = OspfPmIndex
_OspfPmHostApplIndex_Object = MibTableColumn
ospfPmHostApplIndex = _OspfPmHostApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 6),
    _OspfPmHostApplIndex_Type()
)
ospfPmHostApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmHostApplIndex.setStatus("current")


class _OspfPmHostAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfPmHostAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmHostAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfPmHostAdminStatus_Object = MibTableColumn
ospfPmHostAdminStatus = _OspfPmHostAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 7),
    _OspfPmHostAdminStatus_Type()
)
ospfPmHostAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmHostAdminStatus.setStatus("current")
_OspfPmHostOperStatus_Type = OspfPmOperStatus
_OspfPmHostOperStatus_Object = MibTableColumn
ospfPmHostOperStatus = _OspfPmHostOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 6, 1, 8),
    _OspfPmHostOperStatus_Type()
)
ospfPmHostOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmHostOperStatus.setStatus("current")
_OspfPmIfTable_Object = MibTable
ospfPmIfTable = _OspfPmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ospfPmIfTable.setStatus("current")
_OspfPmIfEntry_Object = MibTableRow
ospfPmIfEntry = _OspfPmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1)
)
ospfPmIfEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmIfApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmIfIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfPmIfEntry.setStatus("current")
_OspfPmIfIpAddress_Type = IpAddress
_OspfPmIfIpAddress_Object = MibTableColumn
ospfPmIfIpAddress = _OspfPmIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 1),
    _OspfPmIfIpAddress_Type()
)
ospfPmIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfIpAddress.setStatus("current")
_OspfPmAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmAddressLessIf_Object = MibTableColumn
ospfPmAddressLessIf = _OspfPmAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 2),
    _OspfPmAddressLessIf_Type()
)
ospfPmAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAddressLessIf.setStatus("current")


class _OspfPmIfAreaId_Type(AreaID):
    """Custom type ospfPmIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_OspfPmIfAreaId_Type.__name__ = "AreaID"
_OspfPmIfAreaId_Object = MibTableColumn
ospfPmIfAreaId = _OspfPmIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 3),
    _OspfPmIfAreaId_Type()
)
ospfPmIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfAreaId.setStatus("current")
_OspfPmIfType_Type = OspfNetworkTypes
_OspfPmIfType_Object = MibTableColumn
ospfPmIfType = _OspfPmIfType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 4),
    _OspfPmIfType_Type()
)
ospfPmIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfType.setStatus("current")


class _OspfPmIfAdminStat_Type(OspfPmAdminStatus):
    """Custom type ospfPmIfAdminStat based on OspfPmAdminStatus"""
    defaultValue = 2


_OspfPmIfAdminStat_Type.__name__ = "OspfPmAdminStatus"
_OspfPmIfAdminStat_Object = MibTableColumn
ospfPmIfAdminStat = _OspfPmIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 5),
    _OspfPmIfAdminStat_Type()
)
ospfPmIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfAdminStat.setStatus("current")


class _OspfPmIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfPmIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfPmIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_OspfPmIfRtrPriority_Object = MibTableColumn
ospfPmIfRtrPriority = _OspfPmIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 6),
    _OspfPmIfRtrPriority_Type()
)
ospfPmIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfRtrPriority.setStatus("current")


class _OspfPmIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfPmIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfPmIfTransitDelay_Type.__name__ = "UpToMaxAge"
_OspfPmIfTransitDelay_Object = MibTableColumn
ospfPmIfTransitDelay = _OspfPmIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 7),
    _OspfPmIfTransitDelay_Type()
)
ospfPmIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfTransitDelay.setStatus("current")


class _OspfPmIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfPmIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfPmIfRetransInterval_Type.__name__ = "UpToMaxAge"
_OspfPmIfRetransInterval_Object = MibTableColumn
ospfPmIfRetransInterval = _OspfPmIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 8),
    _OspfPmIfRetransInterval_Type()
)
ospfPmIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfRetransInterval.setStatus("current")


class _OspfPmIfHelloInterval_Type(HelloRange):
    """Custom type ospfPmIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfPmIfHelloInterval_Type.__name__ = "HelloRange"
_OspfPmIfHelloInterval_Object = MibTableColumn
ospfPmIfHelloInterval = _OspfPmIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 9),
    _OspfPmIfHelloInterval_Type()
)
ospfPmIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfHelloInterval.setStatus("current")


class _OspfPmIfRtrDeadInterval_Type(Integer32):
    """Custom type ospfPmIfRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmIfRtrDeadInterval_Type.__name__ = "Integer32"
_OspfPmIfRtrDeadInterval_Object = MibTableColumn
ospfPmIfRtrDeadInterval = _OspfPmIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 10),
    _OspfPmIfRtrDeadInterval_Type()
)
ospfPmIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfRtrDeadInterval.setStatus("current")


class _OspfPmIfPollInterval_Type(PositiveInteger):
    """Custom type ospfPmIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_OspfPmIfPollInterval_Type.__name__ = "PositiveInteger"
_OspfPmIfPollInterval_Object = MibTableColumn
ospfPmIfPollInterval = _OspfPmIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 11),
    _OspfPmIfPollInterval_Type()
)
ospfPmIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfPollInterval.setStatus("current")


class _OspfPmIfState_Type(OspfInterfaceStates):
    """Custom type ospfPmIfState based on OspfInterfaceStates"""
    defaultValue = 1


_OspfPmIfState_Type.__name__ = "OspfInterfaceStates"
_OspfPmIfState_Object = MibTableColumn
ospfPmIfState = _OspfPmIfState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 12),
    _OspfPmIfState_Type()
)
ospfPmIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfState.setStatus("current")


class _OspfPmIfDesignatedRouter_Type(IpAddress):
    """Custom type ospfPmIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfPmIfDesignatedRouter_Type.__name__ = "IpAddress"
_OspfPmIfDesignatedRouter_Object = MibTableColumn
ospfPmIfDesignatedRouter = _OspfPmIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 13),
    _OspfPmIfDesignatedRouter_Type()
)
ospfPmIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfDesignatedRouter.setStatus("current")


class _OspfPmIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type ospfPmIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfPmIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_OspfPmIfBackupDesignatedRouter_Object = MibTableColumn
ospfPmIfBackupDesignatedRouter = _OspfPmIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 14),
    _OspfPmIfBackupDesignatedRouter_Type()
)
ospfPmIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBackupDesignatedRouter.setStatus("current")
_OspfPmIfEvents_Type = Counter32
_OspfPmIfEvents_Object = MibTableColumn
ospfPmIfEvents = _OspfPmIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 15),
    _OspfPmIfEvents_Type()
)
ospfPmIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfEvents.setStatus("current")


class _OspfPmIfAuthKey_Type(OctetString):
    """Custom type ospfPmIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfPmIfAuthKey_Type.__name__ = "OctetString"
_OspfPmIfAuthKey_Object = MibTableColumn
ospfPmIfAuthKey = _OspfPmIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 16),
    _OspfPmIfAuthKey_Type()
)
ospfPmIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfAuthKey.setStatus("current")
_OspfPmIfStatus_Type = RowStatus
_OspfPmIfStatus_Object = MibTableColumn
ospfPmIfStatus = _OspfPmIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 17),
    _OspfPmIfStatus_Type()
)
ospfPmIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfStatus.setStatus("current")


class _OspfPmIfMulticastForwarding_Type(OspfMulticastFwardTypes):
    """Custom type ospfPmIfMulticastForwarding based on OspfMulticastFwardTypes"""
    defaultValue = 1


_OspfPmIfMulticastForwarding_Type.__name__ = "OspfMulticastFwardTypes"
_OspfPmIfMulticastForwarding_Object = MibTableColumn
ospfPmIfMulticastForwarding = _OspfPmIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 18),
    _OspfPmIfMulticastForwarding_Type()
)
ospfPmIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfMulticastForwarding.setStatus("current")


class _OspfPmIfDemand_Type(TruthValue):
    """Custom type ospfPmIfDemand based on TruthValue"""
    defaultValue = 2


_OspfPmIfDemand_Type.__name__ = "TruthValue"
_OspfPmIfDemand_Object = MibTableColumn
ospfPmIfDemand = _OspfPmIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 19),
    _OspfPmIfDemand_Type()
)
ospfPmIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfDemand.setStatus("current")


class _OspfPmIfAuthType_Type(OspfAuthTypes):
    """Custom type ospfPmIfAuthType based on OspfAuthTypes"""
    defaultValue = 0


_OspfPmIfAuthType_Type.__name__ = "OspfAuthTypes"
_OspfPmIfAuthType_Object = MibTableColumn
ospfPmIfAuthType = _OspfPmIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 20),
    _OspfPmIfAuthType_Type()
)
ospfPmIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfAuthType.setStatus("current")
_OspfPmIfLsaCount_Type = Gauge32
_OspfPmIfLsaCount_Object = MibTableColumn
ospfPmIfLsaCount = _OspfPmIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 21),
    _OspfPmIfLsaCount_Type()
)
ospfPmIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLsaCount.setStatus("current")
_OspfPmIfLsaCksumSum_Type = Integer32
_OspfPmIfLsaCksumSum_Object = MibTableColumn
ospfPmIfLsaCksumSum = _OspfPmIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 22),
    _OspfPmIfLsaCksumSum_Type()
)
ospfPmIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLsaCksumSum.setStatus("current")
_OspfPmIfApplIndex_Type = OspfPmIndex
_OspfPmIfApplIndex_Object = MibTableColumn
ospfPmIfApplIndex = _OspfPmIfApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 23),
    _OspfPmIfApplIndex_Type()
)
ospfPmIfApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfApplIndex.setStatus("current")
_OspfPmIfOperStatus_Type = OspfPmOperStatus
_OspfPmIfOperStatus_Object = MibTableColumn
ospfPmIfOperStatus = _OspfPmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 24),
    _OspfPmIfOperStatus_Type()
)
ospfPmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfOperStatus.setStatus("current")
_OspfPmIfNetMask_Type = IpAddress
_OspfPmIfNetMask_Object = MibTableColumn
ospfPmIfNetMask = _OspfPmIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 25),
    _OspfPmIfNetMask_Type()
)
ospfPmIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfNetMask.setStatus("current")
_OspfPmIfResourceClass_Type = Unsigned32
_OspfPmIfResourceClass_Object = MibTableColumn
ospfPmIfResourceClass = _OspfPmIfResourceClass_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 26),
    _OspfPmIfResourceClass_Type()
)
ospfPmIfResourceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfResourceClass.setStatus("current")


class _OspfPmIfTransmitTimerDelay_Type(Integer32):
    """Custom type ospfPmIfTransmitTimerDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OspfPmIfTransmitTimerDelay_Type.__name__ = "Integer32"
_OspfPmIfTransmitTimerDelay_Object = MibTableColumn
ospfPmIfTransmitTimerDelay = _OspfPmIfTransmitTimerDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 27),
    _OspfPmIfTransmitTimerDelay_Type()
)
ospfPmIfTransmitTimerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfTransmitTimerDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmIfTransmitTimerDelay.setUnits("milliseconds")


class _OspfPmIfIPMaxPacketSize_Type(Integer32):
    """Custom type ospfPmIfIPMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmIfIPMaxPacketSize_Type.__name__ = "Integer32"
_OspfPmIfIPMaxPacketSize_Object = MibTableColumn
ospfPmIfIPMaxPacketSize = _OspfPmIfIPMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 28),
    _OspfPmIfIPMaxPacketSize_Type()
)
ospfPmIfIPMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfIPMaxPacketSize.setStatus("current")


class _OspfPmIfPassive_Type(TruthValue):
    """Custom type ospfPmIfPassive based on TruthValue"""
    defaultValue = 2


_OspfPmIfPassive_Type.__name__ = "TruthValue"
_OspfPmIfPassive_Object = MibTableColumn
ospfPmIfPassive = _OspfPmIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 29),
    _OspfPmIfPassive_Type()
)
ospfPmIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfPassive.setStatus("current")
_OspfPmIfInterfaceName_Type = DisplayString
_OspfPmIfInterfaceName_Object = MibTableColumn
ospfPmIfInterfaceName = _OspfPmIfInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 30),
    _OspfPmIfInterfaceName_Type()
)
ospfPmIfInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfInterfaceName.setStatus("current")


class _OspfPmIfLsaRefreshIntvl_Type(Integer32):
    """Custom type ospfPmIfLsaRefreshIntvl based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_OspfPmIfLsaRefreshIntvl_Type.__name__ = "Integer32"
_OspfPmIfLsaRefreshIntvl_Object = MibTableColumn
ospfPmIfLsaRefreshIntvl = _OspfPmIfLsaRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 31),
    _OspfPmIfLsaRefreshIntvl_Type()
)
ospfPmIfLsaRefreshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfLsaRefreshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmIfLsaRefreshIntvl.setUnits("seconds")


class _OspfPmIfQOSSupport_Type(TruthValue):
    """Custom type ospfPmIfQOSSupport based on TruthValue"""
    defaultValue = 1


_OspfPmIfQOSSupport_Type.__name__ = "TruthValue"
_OspfPmIfQOSSupport_Object = MibTableColumn
ospfPmIfQOSSupport = _OspfPmIfQOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 32),
    _OspfPmIfQOSSupport_Type()
)
ospfPmIfQOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfQOSSupport.setStatus("current")


class _OspfPmIfTEMetricPcntge_Type(Integer32):
    """Custom type ospfPmIfTEMetricPcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfTEMetricPcntge_Type.__name__ = "Integer32"
_OspfPmIfTEMetricPcntge_Object = MibTableColumn
ospfPmIfTEMetricPcntge = _OspfPmIfTEMetricPcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 33),
    _OspfPmIfTEMetricPcntge_Type()
)
ospfPmIfTEMetricPcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfTEMetricPcntge.setStatus("current")
_OspfPmIfTEMetric_Type = Integer32
_OspfPmIfTEMetric_Object = MibTableColumn
ospfPmIfTEMetric = _OspfPmIfTEMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 34),
    _OspfPmIfTEMetric_Type()
)
ospfPmIfTEMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfTEMetric.setStatus("current")
_OspfPmIfLastTEMetric_Type = Integer32
_OspfPmIfLastTEMetric_Object = MibTableColumn
ospfPmIfLastTEMetric = _OspfPmIfLastTEMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 35),
    _OspfPmIfLastTEMetric_Type()
)
ospfPmIfLastTEMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastTEMetric.setStatus("current")


class _OspfPmIfMaxBwidthPcntge_Type(Integer32):
    """Custom type ospfPmIfMaxBwidthPcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfMaxBwidthPcntge_Type.__name__ = "Integer32"
_OspfPmIfMaxBwidthPcntge_Object = MibTableColumn
ospfPmIfMaxBwidthPcntge = _OspfPmIfMaxBwidthPcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 36),
    _OspfPmIfMaxBwidthPcntge_Type()
)
ospfPmIfMaxBwidthPcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMaxBwidthPcntge.setStatus("current")
_OspfPmIfMaxBandwidth_Type = Integer32
_OspfPmIfMaxBandwidth_Object = MibTableColumn
ospfPmIfMaxBandwidth = _OspfPmIfMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 37),
    _OspfPmIfMaxBandwidth_Type()
)
ospfPmIfMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfMaxBandwidth.setStatus("current")
_OspfPmIfLastMaxBwidth_Type = Integer32
_OspfPmIfLastMaxBwidth_Object = MibTableColumn
ospfPmIfLastMaxBwidth = _OspfPmIfLastMaxBwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 38),
    _OspfPmIfLastMaxBwidth_Type()
)
ospfPmIfLastMaxBwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastMaxBwidth.setStatus("current")


class _OspfPmIfMaxResBwidthPcntge_Type(Integer32):
    """Custom type ospfPmIfMaxResBwidthPcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfMaxResBwidthPcntge_Type.__name__ = "Integer32"
_OspfPmIfMaxResBwidthPcntge_Object = MibTableColumn
ospfPmIfMaxResBwidthPcntge = _OspfPmIfMaxResBwidthPcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 39),
    _OspfPmIfMaxResBwidthPcntge_Type()
)
ospfPmIfMaxResBwidthPcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMaxResBwidthPcntge.setStatus("current")
_OspfPmIfMaxResBwidth_Type = Integer32
_OspfPmIfMaxResBwidth_Object = MibTableColumn
ospfPmIfMaxResBwidth = _OspfPmIfMaxResBwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 40),
    _OspfPmIfMaxResBwidth_Type()
)
ospfPmIfMaxResBwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfMaxResBwidth.setStatus("current")
_OspfPmIfLastMaxResBwidth_Type = Integer32
_OspfPmIfLastMaxResBwidth_Object = MibTableColumn
ospfPmIfLastMaxResBwidth = _OspfPmIfLastMaxResBwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 41),
    _OspfPmIfLastMaxResBwidth_Type()
)
ospfPmIfLastMaxResBwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastMaxResBwidth.setStatus("current")


class _OspfPmIfUnresBwidthPcntge_Type(Integer32):
    """Custom type ospfPmIfUnresBwidthPcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfUnresBwidthPcntge_Type.__name__ = "Integer32"
_OspfPmIfUnresBwidthPcntge_Object = MibTableColumn
ospfPmIfUnresBwidthPcntge = _OspfPmIfUnresBwidthPcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 42),
    _OspfPmIfUnresBwidthPcntge_Type()
)
ospfPmIfUnresBwidthPcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidthPcntge.setStatus("current")
_OspfPmIfUnresBwidth0_Type = Integer32
_OspfPmIfUnresBwidth0_Object = MibTableColumn
ospfPmIfUnresBwidth0 = _OspfPmIfUnresBwidth0_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 43),
    _OspfPmIfUnresBwidth0_Type()
)
ospfPmIfUnresBwidth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth0.setStatus("current")
_OspfPmIfLastUnresBwidth0_Type = Integer32
_OspfPmIfLastUnresBwidth0_Object = MibTableColumn
ospfPmIfLastUnresBwidth0 = _OspfPmIfLastUnresBwidth0_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 44),
    _OspfPmIfLastUnresBwidth0_Type()
)
ospfPmIfLastUnresBwidth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth0.setStatus("current")
_OspfPmIfUnresBwidth1_Type = Integer32
_OspfPmIfUnresBwidth1_Object = MibTableColumn
ospfPmIfUnresBwidth1 = _OspfPmIfUnresBwidth1_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 45),
    _OspfPmIfUnresBwidth1_Type()
)
ospfPmIfUnresBwidth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth1.setStatus("current")
_OspfPmIfLastUnresBwidth1_Type = Integer32
_OspfPmIfLastUnresBwidth1_Object = MibTableColumn
ospfPmIfLastUnresBwidth1 = _OspfPmIfLastUnresBwidth1_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 46),
    _OspfPmIfLastUnresBwidth1_Type()
)
ospfPmIfLastUnresBwidth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth1.setStatus("current")
_OspfPmIfUnresBwidth2_Type = Integer32
_OspfPmIfUnresBwidth2_Object = MibTableColumn
ospfPmIfUnresBwidth2 = _OspfPmIfUnresBwidth2_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 47),
    _OspfPmIfUnresBwidth2_Type()
)
ospfPmIfUnresBwidth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth2.setStatus("current")
_OspfPmIfLastUnresBwidth2_Type = Integer32
_OspfPmIfLastUnresBwidth2_Object = MibTableColumn
ospfPmIfLastUnresBwidth2 = _OspfPmIfLastUnresBwidth2_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 48),
    _OspfPmIfLastUnresBwidth2_Type()
)
ospfPmIfLastUnresBwidth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth2.setStatus("current")
_OspfPmIfUnresBwidth3_Type = Integer32
_OspfPmIfUnresBwidth3_Object = MibTableColumn
ospfPmIfUnresBwidth3 = _OspfPmIfUnresBwidth3_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 49),
    _OspfPmIfUnresBwidth3_Type()
)
ospfPmIfUnresBwidth3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth3.setStatus("current")
_OspfPmIfLastUnresBwidth3_Type = Integer32
_OspfPmIfLastUnresBwidth3_Object = MibTableColumn
ospfPmIfLastUnresBwidth3 = _OspfPmIfLastUnresBwidth3_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 50),
    _OspfPmIfLastUnresBwidth3_Type()
)
ospfPmIfLastUnresBwidth3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth3.setStatus("current")
_OspfPmIfUnresBwidth4_Type = Integer32
_OspfPmIfUnresBwidth4_Object = MibTableColumn
ospfPmIfUnresBwidth4 = _OspfPmIfUnresBwidth4_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 51),
    _OspfPmIfUnresBwidth4_Type()
)
ospfPmIfUnresBwidth4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth4.setStatus("current")
_OspfPmIfLastUnresBwidth4_Type = Integer32
_OspfPmIfLastUnresBwidth4_Object = MibTableColumn
ospfPmIfLastUnresBwidth4 = _OspfPmIfLastUnresBwidth4_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 52),
    _OspfPmIfLastUnresBwidth4_Type()
)
ospfPmIfLastUnresBwidth4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth4.setStatus("current")
_OspfPmIfUnresBwidth5_Type = Integer32
_OspfPmIfUnresBwidth5_Object = MibTableColumn
ospfPmIfUnresBwidth5 = _OspfPmIfUnresBwidth5_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 53),
    _OspfPmIfUnresBwidth5_Type()
)
ospfPmIfUnresBwidth5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth5.setStatus("current")
_OspfPmIfLastUnresBwidth5_Type = Integer32
_OspfPmIfLastUnresBwidth5_Object = MibTableColumn
ospfPmIfLastUnresBwidth5 = _OspfPmIfLastUnresBwidth5_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 54),
    _OspfPmIfLastUnresBwidth5_Type()
)
ospfPmIfLastUnresBwidth5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth5.setStatus("current")
_OspfPmIfUnresBwidth6_Type = Integer32
_OspfPmIfUnresBwidth6_Object = MibTableColumn
ospfPmIfUnresBwidth6 = _OspfPmIfUnresBwidth6_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 55),
    _OspfPmIfUnresBwidth6_Type()
)
ospfPmIfUnresBwidth6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth6.setStatus("current")
_OspfPmIfLastUnresBwidth6_Type = Integer32
_OspfPmIfLastUnresBwidth6_Object = MibTableColumn
ospfPmIfLastUnresBwidth6 = _OspfPmIfLastUnresBwidth6_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 56),
    _OspfPmIfLastUnresBwidth6_Type()
)
ospfPmIfLastUnresBwidth6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth6.setStatus("current")
_OspfPmIfUnresBwidth7_Type = Integer32
_OspfPmIfUnresBwidth7_Object = MibTableColumn
ospfPmIfUnresBwidth7 = _OspfPmIfUnresBwidth7_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 57),
    _OspfPmIfUnresBwidth7_Type()
)
ospfPmIfUnresBwidth7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfUnresBwidth7.setStatus("current")
_OspfPmIfLastUnresBwidth7_Type = Integer32
_OspfPmIfLastUnresBwidth7_Object = MibTableColumn
ospfPmIfLastUnresBwidth7 = _OspfPmIfLastUnresBwidth7_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 58),
    _OspfPmIfLastUnresBwidth7_Type()
)
ospfPmIfLastUnresBwidth7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLastUnresBwidth7.setStatus("current")
_OspfPmIfIfIndex_Type = Integer32
_OspfPmIfIfIndex_Object = MibTableColumn
ospfPmIfIfIndex = _OspfPmIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 59),
    _OspfPmIfIfIndex_Type()
)
ospfPmIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfIfIndex.setStatus("current")
_OspfPmIfRemoteIfIndex_Type = Integer32
_OspfPmIfRemoteIfIndex_Object = MibTableColumn
ospfPmIfRemoteIfIndex = _OspfPmIfRemoteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 60),
    _OspfPmIfRemoteIfIndex_Type()
)
ospfPmIfRemoteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfRemoteIfIndex.setStatus("current")


class _OspfPmIfLinkProtectionType_Type(OspfPmIfLinkProtValue):
    """Custom type ospfPmIfLinkProtectionType based on OspfPmIfLinkProtValue"""
    defaultBinValue = "00000000000000000000000001"


_OspfPmIfLinkProtectionType_Type.__name__ = "OspfPmIfLinkProtValue"
_OspfPmIfLinkProtectionType_Object = MibTableColumn
ospfPmIfLinkProtectionType = _OspfPmIfLinkProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 61),
    _OspfPmIfLinkProtectionType_Type()
)
ospfPmIfLinkProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfLinkProtectionType.setStatus("current")


class _OspfPmIfSRLG_Type(OctetString):
    """Custom type ospfPmIfSRLG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfPmIfSRLG_Type.__name__ = "OctetString"
_OspfPmIfSRLG_Object = MibTableColumn
ospfPmIfSRLG = _OspfPmIfSRLG_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 62),
    _OspfPmIfSRLG_Type()
)
ospfPmIfSRLG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSRLG.setStatus("current")


class _OspfPmIfMaxLSPBwidthPcntge_Type(Integer32):
    """Custom type ospfPmIfMaxLSPBwidthPcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfMaxLSPBwidthPcntge_Type.__name__ = "Integer32"
_OspfPmIfMaxLSPBwidthPcntge_Object = MibTableColumn
ospfPmIfMaxLSPBwidthPcntge = _OspfPmIfMaxLSPBwidthPcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 63),
    _OspfPmIfMaxLSPBwidthPcntge_Type()
)
ospfPmIfMaxLSPBwidthPcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMaxLSPBwidthPcntge.setStatus("current")


class _OspfPmIfMinLSPBwidthPcntge_Type(Integer32):
    """Custom type ospfPmIfMinLSPBwidthPcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfMinLSPBwidthPcntge_Type.__name__ = "Integer32"
_OspfPmIfMinLSPBwidthPcntge_Object = MibTableColumn
ospfPmIfMinLSPBwidthPcntge = _OspfPmIfMinLSPBwidthPcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 64),
    _OspfPmIfMinLSPBwidthPcntge_Type()
)
ospfPmIfMinLSPBwidthPcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMinLSPBwidthPcntge.setStatus("current")


class _OspfPmIfMTUSizePcntge_Type(Integer32):
    """Custom type ospfPmIfMTUSizePcntge based on Integer32"""
    defaultValue = 0


_OspfPmIfMTUSizePcntge_Type.__name__ = "Integer32"
_OspfPmIfMTUSizePcntge_Object = MibTableColumn
ospfPmIfMTUSizePcntge = _OspfPmIfMTUSizePcntge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 65),
    _OspfPmIfMTUSizePcntge_Type()
)
ospfPmIfMTUSizePcntge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMTUSizePcntge.setStatus("current")


class _OspfPmIfHelperModePolicy_Type(OspfHelperModePolicy):
    """Custom type ospfPmIfHelperModePolicy based on OspfHelperModePolicy"""
    defaultBinValue = "0"


_OspfPmIfHelperModePolicy_Type.__name__ = "OspfHelperModePolicy"
_OspfPmIfHelperModePolicy_Object = MibTableColumn
ospfPmIfHelperModePolicy = _OspfPmIfHelperModePolicy_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 66),
    _OspfPmIfHelperModePolicy_Type()
)
ospfPmIfHelperModePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfHelperModePolicy.setStatus("current")


class _OspfPmIfMaxHitlessGracePeriod_Type(UpToRefreshInterval):
    """Custom type ospfPmIfMaxHitlessGracePeriod based on UpToRefreshInterval"""
    defaultValue = 140


_OspfPmIfMaxHitlessGracePeriod_Type.__name__ = "UpToRefreshInterval"
_OspfPmIfMaxHitlessGracePeriod_Object = MibTableColumn
ospfPmIfMaxHitlessGracePeriod = _OspfPmIfMaxHitlessGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 67),
    _OspfPmIfMaxHitlessGracePeriod_Type()
)
ospfPmIfMaxHitlessGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMaxHitlessGracePeriod.setStatus("current")


class _OspfPmIfEnableTeFlooding_Type(TruthValue):
    """Custom type ospfPmIfEnableTeFlooding based on TruthValue"""
    defaultValue = 1


_OspfPmIfEnableTeFlooding_Type.__name__ = "TruthValue"
_OspfPmIfEnableTeFlooding_Object = MibTableColumn
ospfPmIfEnableTeFlooding = _OspfPmIfEnableTeFlooding_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 68),
    _OspfPmIfEnableTeFlooding_Type()
)
ospfPmIfEnableTeFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfEnableTeFlooding.setStatus("current")


class _OspfPmIfAuthUserData_Type(AuthUserDataString):
    """Custom type ospfPmIfAuthUserData based on AuthUserDataString"""
    defaultHexValue = ""


_OspfPmIfAuthUserData_Type.__name__ = "AuthUserDataString"
_OspfPmIfAuthUserData_Object = MibTableColumn
ospfPmIfAuthUserData = _OspfPmIfAuthUserData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 69),
    _OspfPmIfAuthUserData_Type()
)
ospfPmIfAuthUserData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfAuthUserData.setStatus("current")


class _OspfPmIfFastHelloMultiplier_Type(FastHelloMultiplierRange):
    """Custom type ospfPmIfFastHelloMultiplier based on FastHelloMultiplierRange"""
    defaultValue = 5


_OspfPmIfFastHelloMultiplier_Type.__name__ = "FastHelloMultiplierRange"
_OspfPmIfFastHelloMultiplier_Object = MibTableColumn
ospfPmIfFastHelloMultiplier = _OspfPmIfFastHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 70),
    _OspfPmIfFastHelloMultiplier_Type()
)
ospfPmIfFastHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfFastHelloMultiplier.setStatus("current")


class _OspfPmIfAutoDeleteNbr_Type(TruthValue):
    """Custom type ospfPmIfAutoDeleteNbr based on TruthValue"""
    defaultValue = 1


_OspfPmIfAutoDeleteNbr_Type.__name__ = "TruthValue"
_OspfPmIfAutoDeleteNbr_Object = MibTableColumn
ospfPmIfAutoDeleteNbr = _OspfPmIfAutoDeleteNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 71),
    _OspfPmIfAutoDeleteNbr_Type()
)
ospfPmIfAutoDeleteNbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfAutoDeleteNbr.setStatus("current")


class _OspfPmIfNumBwidthCnstrnts_Type(Integer32):
    """Custom type ospfPmIfNumBwidthCnstrnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OspfPmIfNumBwidthCnstrnts_Type.__name__ = "Integer32"
_OspfPmIfNumBwidthCnstrnts_Object = MibTableColumn
ospfPmIfNumBwidthCnstrnts = _OspfPmIfNumBwidthCnstrnts_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 72),
    _OspfPmIfNumBwidthCnstrnts_Type()
)
ospfPmIfNumBwidthCnstrnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfNumBwidthCnstrnts.setStatus("current")
_OspfPmIfBwidthCnstrntModel_Type = Integer32
_OspfPmIfBwidthCnstrntModel_Object = MibTableColumn
ospfPmIfBwidthCnstrntModel = _OspfPmIfBwidthCnstrntModel_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 73),
    _OspfPmIfBwidthCnstrntModel_Type()
)
ospfPmIfBwidthCnstrntModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrntModel.setStatus("current")
_OspfPmIfBwidthCnstrnt0_Type = Integer32
_OspfPmIfBwidthCnstrnt0_Object = MibTableColumn
ospfPmIfBwidthCnstrnt0 = _OspfPmIfBwidthCnstrnt0_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 74),
    _OspfPmIfBwidthCnstrnt0_Type()
)
ospfPmIfBwidthCnstrnt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt0.setStatus("current")
_OspfPmIfBwidthCnstrnt1_Type = Integer32
_OspfPmIfBwidthCnstrnt1_Object = MibTableColumn
ospfPmIfBwidthCnstrnt1 = _OspfPmIfBwidthCnstrnt1_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 75),
    _OspfPmIfBwidthCnstrnt1_Type()
)
ospfPmIfBwidthCnstrnt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt1.setStatus("current")
_OspfPmIfBwidthCnstrnt2_Type = Integer32
_OspfPmIfBwidthCnstrnt2_Object = MibTableColumn
ospfPmIfBwidthCnstrnt2 = _OspfPmIfBwidthCnstrnt2_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 76),
    _OspfPmIfBwidthCnstrnt2_Type()
)
ospfPmIfBwidthCnstrnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt2.setStatus("current")
_OspfPmIfBwidthCnstrnt3_Type = Integer32
_OspfPmIfBwidthCnstrnt3_Object = MibTableColumn
ospfPmIfBwidthCnstrnt3 = _OspfPmIfBwidthCnstrnt3_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 77),
    _OspfPmIfBwidthCnstrnt3_Type()
)
ospfPmIfBwidthCnstrnt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt3.setStatus("current")
_OspfPmIfBwidthCnstrnt4_Type = Integer32
_OspfPmIfBwidthCnstrnt4_Object = MibTableColumn
ospfPmIfBwidthCnstrnt4 = _OspfPmIfBwidthCnstrnt4_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 78),
    _OspfPmIfBwidthCnstrnt4_Type()
)
ospfPmIfBwidthCnstrnt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt4.setStatus("current")
_OspfPmIfBwidthCnstrnt5_Type = Integer32
_OspfPmIfBwidthCnstrnt5_Object = MibTableColumn
ospfPmIfBwidthCnstrnt5 = _OspfPmIfBwidthCnstrnt5_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 79),
    _OspfPmIfBwidthCnstrnt5_Type()
)
ospfPmIfBwidthCnstrnt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt5.setStatus("current")
_OspfPmIfBwidthCnstrnt6_Type = Integer32
_OspfPmIfBwidthCnstrnt6_Object = MibTableColumn
ospfPmIfBwidthCnstrnt6 = _OspfPmIfBwidthCnstrnt6_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 80),
    _OspfPmIfBwidthCnstrnt6_Type()
)
ospfPmIfBwidthCnstrnt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt6.setStatus("current")
_OspfPmIfBwidthCnstrnt7_Type = Integer32
_OspfPmIfBwidthCnstrnt7_Object = MibTableColumn
ospfPmIfBwidthCnstrnt7 = _OspfPmIfBwidthCnstrnt7_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 81),
    _OspfPmIfBwidthCnstrnt7_Type()
)
ospfPmIfBwidthCnstrnt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfBwidthCnstrnt7.setStatus("current")


class _OspfPmIfMtuIgnore_Type(TruthValue):
    """Custom type ospfPmIfMtuIgnore based on TruthValue"""
    defaultValue = 2


_OspfPmIfMtuIgnore_Type.__name__ = "TruthValue"
_OspfPmIfMtuIgnore_Object = MibTableColumn
ospfPmIfMtuIgnore = _OspfPmIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 82),
    _OspfPmIfMtuIgnore_Type()
)
ospfPmIfMtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmIfMtuIgnore.setStatus("current")


class _OspfPmIfNmEntity_Type(Integer32):
    """Custom type ospfPmIfNmEntity based on Integer32"""
    defaultValue = 1


_OspfPmIfNmEntity_Type.__name__ = "Integer32"
_OspfPmIfNmEntity_Object = MibTableColumn
ospfPmIfNmEntity = _OspfPmIfNmEntity_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 83),
    _OspfPmIfNmEntity_Type()
)
ospfPmIfNmEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfNmEntity.setStatus("current")


class _OspfPmIfBfdDesired_Type(TruthValue):
    """Custom type ospfPmIfBfdDesired based on TruthValue"""
    defaultValue = 1


_OspfPmIfBfdDesired_Type.__name__ = "TruthValue"
_OspfPmIfBfdDesired_Object = MibTableColumn
ospfPmIfBfdDesired = _OspfPmIfBfdDesired_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 84),
    _OspfPmIfBfdDesired_Type()
)
ospfPmIfBfdDesired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfBfdDesired.setStatus("current")


class _OspfPmIfRstHlprStrictLsaChk_Type(TruthValue):
    """Custom type ospfPmIfRstHlprStrictLsaChk based on TruthValue"""
    defaultValue = 1


_OspfPmIfRstHlprStrictLsaChk_Type.__name__ = "TruthValue"
_OspfPmIfRstHlprStrictLsaChk_Object = MibTableColumn
ospfPmIfRstHlprStrictLsaChk = _OspfPmIfRstHlprStrictLsaChk_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 85),
    _OspfPmIfRstHlprStrictLsaChk_Type()
)
ospfPmIfRstHlprStrictLsaChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfRstHlprStrictLsaChk.setStatus("current")


class _OspfPmIfStatsReset_Type(TruthValue):
    """Custom type ospfPmIfStatsReset based on TruthValue"""
    defaultValue = 2


_OspfPmIfStatsReset_Type.__name__ = "TruthValue"
_OspfPmIfStatsReset_Object = MibTableColumn
ospfPmIfStatsReset = _OspfPmIfStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 86),
    _OspfPmIfStatsReset_Type()
)
ospfPmIfStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfStatsReset.setStatus("current")


class _OspfPmIfGraceLsaResendTimer_Type(Integer32):
    """Custom type ospfPmIfGraceLsaResendTimer based on Integer32"""
    defaultValue = 0


_OspfPmIfGraceLsaResendTimer_Type.__name__ = "Integer32"
_OspfPmIfGraceLsaResendTimer_Object = MibTableColumn
ospfPmIfGraceLsaResendTimer = _OspfPmIfGraceLsaResendTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 87),
    _OspfPmIfGraceLsaResendTimer_Type()
)
ospfPmIfGraceLsaResendTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfGraceLsaResendTimer.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmIfGraceLsaResendTimer.setUnits("seconds")


class _OspfPmIfGRDelayTimer_Type(Integer32):
    """Custom type ospfPmIfGRDelayTimer based on Integer32"""
    defaultValue = 10


_OspfPmIfGRDelayTimer_Type.__name__ = "Integer32"
_OspfPmIfGRDelayTimer_Object = MibTableColumn
ospfPmIfGRDelayTimer = _OspfPmIfGRDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 7, 1, 88),
    _OspfPmIfGRDelayTimer_Type()
)
ospfPmIfGRDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfGRDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmIfGRDelayTimer.setUnits("seconds")
_OspfPmIfMetricTable_Object = MibTable
ospfPmIfMetricTable = _OspfPmIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ospfPmIfMetricTable.setStatus("current")
_OspfPmIfMetricEntry_Object = MibTableRow
ospfPmIfMetricEntry = _OspfPmIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1)
)
ospfPmIfMetricEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmIfMetricApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmIfMetricIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmIfMetricAddressLessIf"),
    (0, "DC-OSPF-MIB", "ospfPmIfMetricTOS"),
)
if mibBuilder.loadTexts:
    ospfPmIfMetricEntry.setStatus("current")
_OspfPmIfMetricIpAddress_Type = IpAddress
_OspfPmIfMetricIpAddress_Object = MibTableColumn
ospfPmIfMetricIpAddress = _OspfPmIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1, 1),
    _OspfPmIfMetricIpAddress_Type()
)
ospfPmIfMetricIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfMetricIpAddress.setStatus("current")
_OspfPmIfMetricAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmIfMetricAddressLessIf_Object = MibTableColumn
ospfPmIfMetricAddressLessIf = _OspfPmIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1, 2),
    _OspfPmIfMetricAddressLessIf_Type()
)
ospfPmIfMetricAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfMetricAddressLessIf.setStatus("current")
_OspfPmIfMetricTOS_Type = TOSType
_OspfPmIfMetricTOS_Object = MibTableColumn
ospfPmIfMetricTOS = _OspfPmIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1, 3),
    _OspfPmIfMetricTOS_Type()
)
ospfPmIfMetricTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfMetricTOS.setStatus("current")
_OspfPmIfMetricValue_Type = Metric
_OspfPmIfMetricValue_Object = MibTableColumn
ospfPmIfMetricValue = _OspfPmIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1, 4),
    _OspfPmIfMetricValue_Type()
)
ospfPmIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfMetricValue.setStatus("current")
_OspfPmIfMetricStatus_Type = RowStatus
_OspfPmIfMetricStatus_Object = MibTableColumn
ospfPmIfMetricStatus = _OspfPmIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1, 5),
    _OspfPmIfMetricStatus_Type()
)
ospfPmIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmIfMetricStatus.setStatus("current")
_OspfPmIfMetricApplIndex_Type = OspfPmIndex
_OspfPmIfMetricApplIndex_Object = MibTableColumn
ospfPmIfMetricApplIndex = _OspfPmIfMetricApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 8, 1, 6),
    _OspfPmIfMetricApplIndex_Type()
)
ospfPmIfMetricApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfMetricApplIndex.setStatus("current")
_OspfPmVirtIfTable_Object = MibTable
ospfPmVirtIfTable = _OspfPmVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9)
)
if mibBuilder.loadTexts:
    ospfPmVirtIfTable.setStatus("current")
_OspfPmVirtIfEntry_Object = MibTableRow
ospfPmVirtIfEntry = _OspfPmVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1)
)
ospfPmVirtIfEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmVirtIfApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmVirtIfAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    ospfPmVirtIfEntry.setStatus("current")
_OspfPmVirtIfAreaId_Type = AreaID
_OspfPmVirtIfAreaId_Object = MibTableColumn
ospfPmVirtIfAreaId = _OspfPmVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 1),
    _OspfPmVirtIfAreaId_Type()
)
ospfPmVirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtIfAreaId.setStatus("current")
_OspfPmVirtIfNeighbor_Type = RouterID
_OspfPmVirtIfNeighbor_Object = MibTableColumn
ospfPmVirtIfNeighbor = _OspfPmVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 2),
    _OspfPmVirtIfNeighbor_Type()
)
ospfPmVirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtIfNeighbor.setStatus("current")


class _OspfPmVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfPmVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfPmVirtIfTransitDelay_Type.__name__ = "UpToMaxAge"
_OspfPmVirtIfTransitDelay_Object = MibTableColumn
ospfPmVirtIfTransitDelay = _OspfPmVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 3),
    _OspfPmVirtIfTransitDelay_Type()
)
ospfPmVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfTransitDelay.setStatus("current")


class _OspfPmVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfPmVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfPmVirtIfRetransInterval_Type.__name__ = "UpToMaxAge"
_OspfPmVirtIfRetransInterval_Object = MibTableColumn
ospfPmVirtIfRetransInterval = _OspfPmVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 4),
    _OspfPmVirtIfRetransInterval_Type()
)
ospfPmVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfRetransInterval.setStatus("current")


class _OspfPmVirtIfHelloInterval_Type(HelloRange):
    """Custom type ospfPmVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfPmVirtIfHelloInterval_Type.__name__ = "HelloRange"
_OspfPmVirtIfHelloInterval_Object = MibTableColumn
ospfPmVirtIfHelloInterval = _OspfPmVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 5),
    _OspfPmVirtIfHelloInterval_Type()
)
ospfPmVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfHelloInterval.setStatus("current")


class _OspfPmVirtIfRtrDeadInterval_Type(Integer32):
    """Custom type ospfPmVirtIfRtrDeadInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmVirtIfRtrDeadInterval_Type.__name__ = "Integer32"
_OspfPmVirtIfRtrDeadInterval_Object = MibTableColumn
ospfPmVirtIfRtrDeadInterval = _OspfPmVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 6),
    _OspfPmVirtIfRtrDeadInterval_Type()
)
ospfPmVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfRtrDeadInterval.setStatus("current")


class _OspfPmVirtIfState_Type(OspfInterfaceStates):
    """Custom type ospfPmVirtIfState based on OspfInterfaceStates"""
    defaultValue = 1


_OspfPmVirtIfState_Type.__name__ = "OspfInterfaceStates"
_OspfPmVirtIfState_Object = MibTableColumn
ospfPmVirtIfState = _OspfPmVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 7),
    _OspfPmVirtIfState_Type()
)
ospfPmVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfState.setStatus("current")
_OspfPmVirtIfEvents_Type = Counter32
_OspfPmVirtIfEvents_Object = MibTableColumn
ospfPmVirtIfEvents = _OspfPmVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 8),
    _OspfPmVirtIfEvents_Type()
)
ospfPmVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfEvents.setStatus("current")


class _OspfPmVirtIfAuthKey_Type(OctetString):
    """Custom type ospfPmVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfPmVirtIfAuthKey_Type.__name__ = "OctetString"
_OspfPmVirtIfAuthKey_Object = MibTableColumn
ospfPmVirtIfAuthKey = _OspfPmVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 9),
    _OspfPmVirtIfAuthKey_Type()
)
ospfPmVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfAuthKey.setStatus("current")
_OspfPmVirtIfStatus_Type = RowStatus
_OspfPmVirtIfStatus_Object = MibTableColumn
ospfPmVirtIfStatus = _OspfPmVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 10),
    _OspfPmVirtIfStatus_Type()
)
ospfPmVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatus.setStatus("current")


class _OspfPmVirtIfAuthType_Type(OspfAuthTypes):
    """Custom type ospfPmVirtIfAuthType based on OspfAuthTypes"""
    defaultValue = 0


_OspfPmVirtIfAuthType_Type.__name__ = "OspfAuthTypes"
_OspfPmVirtIfAuthType_Object = MibTableColumn
ospfPmVirtIfAuthType = _OspfPmVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 11),
    _OspfPmVirtIfAuthType_Type()
)
ospfPmVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfAuthType.setStatus("current")
_OspfPmVirtIfLsaCount_Type = Gauge32
_OspfPmVirtIfLsaCount_Object = MibTableColumn
ospfPmVirtIfLsaCount = _OspfPmVirtIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 12),
    _OspfPmVirtIfLsaCount_Type()
)
ospfPmVirtIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfLsaCount.setStatus("current")
_OspfPmVirtIfLsaCksumSum_Type = Integer32
_OspfPmVirtIfLsaCksumSum_Object = MibTableColumn
ospfPmVirtIfLsaCksumSum = _OspfPmVirtIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 13),
    _OspfPmVirtIfLsaCksumSum_Type()
)
ospfPmVirtIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfLsaCksumSum.setStatus("current")
_OspfPmVirtIfApplIndex_Type = OspfPmIndex
_OspfPmVirtIfApplIndex_Object = MibTableColumn
ospfPmVirtIfApplIndex = _OspfPmVirtIfApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 14),
    _OspfPmVirtIfApplIndex_Type()
)
ospfPmVirtIfApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtIfApplIndex.setStatus("current")


class _OspfPmVirtIfAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfPmVirtIfAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmVirtIfAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfPmVirtIfAdminStatus_Object = MibTableColumn
ospfPmVirtIfAdminStatus = _OspfPmVirtIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 15),
    _OspfPmVirtIfAdminStatus_Type()
)
ospfPmVirtIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfAdminStatus.setStatus("current")
_OspfPmVirtIfOperStatus_Type = OspfPmOperStatus
_OspfPmVirtIfOperStatus_Object = MibTableColumn
ospfPmVirtIfOperStatus = _OspfPmVirtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 16),
    _OspfPmVirtIfOperStatus_Type()
)
ospfPmVirtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfOperStatus.setStatus("current")
_OspfPmVirtIfResourceClass_Type = Integer32
_OspfPmVirtIfResourceClass_Object = MibTableColumn
ospfPmVirtIfResourceClass = _OspfPmVirtIfResourceClass_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 17),
    _OspfPmVirtIfResourceClass_Type()
)
ospfPmVirtIfResourceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfResourceClass.setStatus("current")


class _OspfPmVirtIfTransmitTimerDelay_Type(Integer32):
    """Custom type ospfPmVirtIfTransmitTimerDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OspfPmVirtIfTransmitTimerDelay_Type.__name__ = "Integer32"
_OspfPmVirtIfTransmitTimerDelay_Object = MibTableColumn
ospfPmVirtIfTransmitTimerDelay = _OspfPmVirtIfTransmitTimerDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 18),
    _OspfPmVirtIfTransmitTimerDelay_Type()
)
ospfPmVirtIfTransmitTimerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfTransmitTimerDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmVirtIfTransmitTimerDelay.setUnits("milliseconds")


class _OspfPmVirtIfIPMaxPacketSize_Type(Integer32):
    """Custom type ospfPmVirtIfIPMaxPacketSize based on Integer32"""
    defaultValue = 576

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmVirtIfIPMaxPacketSize_Type.__name__ = "Integer32"
_OspfPmVirtIfIPMaxPacketSize_Object = MibTableColumn
ospfPmVirtIfIPMaxPacketSize = _OspfPmVirtIfIPMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 19),
    _OspfPmVirtIfIPMaxPacketSize_Type()
)
ospfPmVirtIfIPMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfIPMaxPacketSize.setStatus("current")


class _OspfPmVirtIfPassive_Type(TruthValue):
    """Custom type ospfPmVirtIfPassive based on TruthValue"""
    defaultValue = 2


_OspfPmVirtIfPassive_Type.__name__ = "TruthValue"
_OspfPmVirtIfPassive_Object = MibTableColumn
ospfPmVirtIfPassive = _OspfPmVirtIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 20),
    _OspfPmVirtIfPassive_Type()
)
ospfPmVirtIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfPassive.setStatus("current")
_OspfPmVirtIfInterfaceName_Type = DisplayString
_OspfPmVirtIfInterfaceName_Object = MibTableColumn
ospfPmVirtIfInterfaceName = _OspfPmVirtIfInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 21),
    _OspfPmVirtIfInterfaceName_Type()
)
ospfPmVirtIfInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfInterfaceName.setStatus("current")


class _OspfPmVirtIfLsaRefreshIntvl_Type(Integer32):
    """Custom type ospfPmVirtIfLsaRefreshIntvl based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_OspfPmVirtIfLsaRefreshIntvl_Type.__name__ = "Integer32"
_OspfPmVirtIfLsaRefreshIntvl_Object = MibTableColumn
ospfPmVirtIfLsaRefreshIntvl = _OspfPmVirtIfLsaRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 22),
    _OspfPmVirtIfLsaRefreshIntvl_Type()
)
ospfPmVirtIfLsaRefreshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfLsaRefreshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmVirtIfLsaRefreshIntvl.setUnits("seconds")


class _OspfPmVirtIfHelperModePolicy_Type(OspfHelperModePolicy):
    """Custom type ospfPmVirtIfHelperModePolicy based on OspfHelperModePolicy"""
    defaultBinValue = "0"


_OspfPmVirtIfHelperModePolicy_Type.__name__ = "OspfHelperModePolicy"
_OspfPmVirtIfHelperModePolicy_Object = MibTableColumn
ospfPmVirtIfHelperModePolicy = _OspfPmVirtIfHelperModePolicy_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 23),
    _OspfPmVirtIfHelperModePolicy_Type()
)
ospfPmVirtIfHelperModePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfHelperModePolicy.setStatus("current")


class _OspfPmVirtIfMaxHtlssGracePeriod_Type(UpToRefreshInterval):
    """Custom type ospfPmVirtIfMaxHtlssGracePeriod based on UpToRefreshInterval"""
    defaultValue = 140


_OspfPmVirtIfMaxHtlssGracePeriod_Type.__name__ = "UpToRefreshInterval"
_OspfPmVirtIfMaxHtlssGracePeriod_Object = MibTableColumn
ospfPmVirtIfMaxHtlssGracePeriod = _OspfPmVirtIfMaxHtlssGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 24),
    _OspfPmVirtIfMaxHtlssGracePeriod_Type()
)
ospfPmVirtIfMaxHtlssGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfMaxHtlssGracePeriod.setStatus("current")


class _OspfPmVirtIfEnableTeFlooding_Type(TruthValue):
    """Custom type ospfPmVirtIfEnableTeFlooding based on TruthValue"""
    defaultValue = 1


_OspfPmVirtIfEnableTeFlooding_Type.__name__ = "TruthValue"
_OspfPmVirtIfEnableTeFlooding_Object = MibTableColumn
ospfPmVirtIfEnableTeFlooding = _OspfPmVirtIfEnableTeFlooding_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 25),
    _OspfPmVirtIfEnableTeFlooding_Type()
)
ospfPmVirtIfEnableTeFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfEnableTeFlooding.setStatus("current")


class _OspfPmVirtIfAuthUserData_Type(AuthUserDataString):
    """Custom type ospfPmVirtIfAuthUserData based on AuthUserDataString"""
    defaultHexValue = ""


_OspfPmVirtIfAuthUserData_Type.__name__ = "AuthUserDataString"
_OspfPmVirtIfAuthUserData_Object = MibTableColumn
ospfPmVirtIfAuthUserData = _OspfPmVirtIfAuthUserData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 26),
    _OspfPmVirtIfAuthUserData_Type()
)
ospfPmVirtIfAuthUserData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfAuthUserData.setStatus("current")


class _OspfPmVirtIfFastHelloMultiplier_Type(FastHelloMultiplierRange):
    """Custom type ospfPmVirtIfFastHelloMultiplier based on FastHelloMultiplierRange"""
    defaultValue = 5


_OspfPmVirtIfFastHelloMultiplier_Type.__name__ = "FastHelloMultiplierRange"
_OspfPmVirtIfFastHelloMultiplier_Object = MibTableColumn
ospfPmVirtIfFastHelloMultiplier = _OspfPmVirtIfFastHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 27),
    _OspfPmVirtIfFastHelloMultiplier_Type()
)
ospfPmVirtIfFastHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfFastHelloMultiplier.setStatus("current")


class _OspfPmVirtIfMtuIgnore_Type(TruthValue):
    """Custom type ospfPmVirtIfMtuIgnore based on TruthValue"""
    defaultValue = 2


_OspfPmVirtIfMtuIgnore_Type.__name__ = "TruthValue"
_OspfPmVirtIfMtuIgnore_Object = MibTableColumn
ospfPmVirtIfMtuIgnore = _OspfPmVirtIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 28),
    _OspfPmVirtIfMtuIgnore_Type()
)
ospfPmVirtIfMtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmVirtIfMtuIgnore.setStatus("current")
_OspfPmVirtIfNmEntity_Type = Integer32
_OspfPmVirtIfNmEntity_Object = MibTableColumn
ospfPmVirtIfNmEntity = _OspfPmVirtIfNmEntity_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 29),
    _OspfPmVirtIfNmEntity_Type()
)
ospfPmVirtIfNmEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfNmEntity.setStatus("current")


class _OspfPmVirtIfBfdDesired_Type(TruthValue):
    """Custom type ospfPmVirtIfBfdDesired based on TruthValue"""
    defaultValue = 1


_OspfPmVirtIfBfdDesired_Type.__name__ = "TruthValue"
_OspfPmVirtIfBfdDesired_Object = MibTableColumn
ospfPmVirtIfBfdDesired = _OspfPmVirtIfBfdDesired_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 30),
    _OspfPmVirtIfBfdDesired_Type()
)
ospfPmVirtIfBfdDesired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfBfdDesired.setStatus("current")


class _OspfPmVirtIfRstHlprStrictLsaChk_Type(TruthValue):
    """Custom type ospfPmVirtIfRstHlprStrictLsaChk based on TruthValue"""
    defaultValue = 1


_OspfPmVirtIfRstHlprStrictLsaChk_Type.__name__ = "TruthValue"
_OspfPmVirtIfRstHlprStrictLsaChk_Object = MibTableColumn
ospfPmVirtIfRstHlprStrictLsaChk = _OspfPmVirtIfRstHlprStrictLsaChk_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 31),
    _OspfPmVirtIfRstHlprStrictLsaChk_Type()
)
ospfPmVirtIfRstHlprStrictLsaChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfRstHlprStrictLsaChk.setStatus("current")


class _OspfPmVirtIfStatsReset_Type(TruthValue):
    """Custom type ospfPmVirtIfStatsReset based on TruthValue"""
    defaultValue = 2


_OspfPmVirtIfStatsReset_Type.__name__ = "TruthValue"
_OspfPmVirtIfStatsReset_Object = MibTableColumn
ospfPmVirtIfStatsReset = _OspfPmVirtIfStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 32),
    _OspfPmVirtIfStatsReset_Type()
)
ospfPmVirtIfStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsReset.setStatus("current")


class _OspfPmVirtIfGRDelayTimer_Type(Integer32):
    """Custom type ospfPmVirtIfGRDelayTimer based on Integer32"""
    defaultValue = 10


_OspfPmVirtIfGRDelayTimer_Type.__name__ = "Integer32"
_OspfPmVirtIfGRDelayTimer_Object = MibTableColumn
ospfPmVirtIfGRDelayTimer = _OspfPmVirtIfGRDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 9, 1, 33),
    _OspfPmVirtIfGRDelayTimer_Type()
)
ospfPmVirtIfGRDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmVirtIfGRDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmVirtIfGRDelayTimer.setUnits("seconds")
_OspfPmNbrTable_Object = MibTable
ospfPmNbrTable = _OspfPmNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ospfPmNbrTable.setStatus("current")
_OspfPmNbrEntry_Object = MibTableRow
ospfPmNbrEntry = _OspfPmNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1)
)
ospfPmNbrEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmNbrApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmNbrIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    ospfPmNbrEntry.setStatus("current")
_OspfPmNbrIpAddr_Type = IpAddress
_OspfPmNbrIpAddr_Object = MibTableColumn
ospfPmNbrIpAddr = _OspfPmNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 1),
    _OspfPmNbrIpAddr_Type()
)
ospfPmNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmNbrIpAddr.setStatus("current")
_OspfPmNbrAddressLessIndex_Type = InterfaceIndexOrZero
_OspfPmNbrAddressLessIndex_Object = MibTableColumn
ospfPmNbrAddressLessIndex = _OspfPmNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 2),
    _OspfPmNbrAddressLessIndex_Type()
)
ospfPmNbrAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmNbrAddressLessIndex.setStatus("current")


class _OspfPmNbrRtrId_Type(RouterID):
    """Custom type ospfPmNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_OspfPmNbrRtrId_Type.__name__ = "RouterID"
_OspfPmNbrRtrId_Object = MibTableColumn
ospfPmNbrRtrId = _OspfPmNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 3),
    _OspfPmNbrRtrId_Type()
)
ospfPmNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrRtrId.setStatus("current")


class _OspfPmNbrOptions_Type(Integer32):
    """Custom type ospfPmNbrOptions based on Integer32"""
    defaultValue = 0


_OspfPmNbrOptions_Type.__name__ = "Integer32"
_OspfPmNbrOptions_Object = MibTableColumn
ospfPmNbrOptions = _OspfPmNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 4),
    _OspfPmNbrOptions_Type()
)
ospfPmNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrOptions.setStatus("current")
_OspfPmNbrPriority_Type = DesignatedRouterPriority
_OspfPmNbrPriority_Object = MibTableColumn
ospfPmNbrPriority = _OspfPmNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 5),
    _OspfPmNbrPriority_Type()
)
ospfPmNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrPriority.setStatus("current")
_OspfPmNbrState_Type = OspfNeighborStates
_OspfPmNbrState_Object = MibTableColumn
ospfPmNbrState = _OspfPmNbrState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 6),
    _OspfPmNbrState_Type()
)
ospfPmNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrState.setStatus("current")
_OspfPmNbrEvents_Type = Counter32
_OspfPmNbrEvents_Object = MibTableColumn
ospfPmNbrEvents = _OspfPmNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 7),
    _OspfPmNbrEvents_Type()
)
ospfPmNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrEvents.setStatus("current")
_OspfPmNbrLsRetransQLen_Type = Gauge32
_OspfPmNbrLsRetransQLen_Object = MibTableColumn
ospfPmNbrLsRetransQLen = _OspfPmNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 8),
    _OspfPmNbrLsRetransQLen_Type()
)
ospfPmNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrLsRetransQLen.setStatus("current")
_OspfPmNbrStatus_Type = RowStatus
_OspfPmNbrStatus_Object = MibTableColumn
ospfPmNbrStatus = _OspfPmNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 9),
    _OspfPmNbrStatus_Type()
)
ospfPmNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmNbrStatus.setStatus("current")


class _OspfPmNbrPermanence_Type(OspfNbrPermanence):
    """Custom type ospfPmNbrPermanence based on OspfNbrPermanence"""
    defaultValue = 2


_OspfPmNbrPermanence_Type.__name__ = "OspfNbrPermanence"
_OspfPmNbrPermanence_Object = MibTableColumn
ospfPmNbrPermanence = _OspfPmNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 10),
    _OspfPmNbrPermanence_Type()
)
ospfPmNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrPermanence.setStatus("current")
_OspfPmNbrHelloSuppressed_Type = TruthValue
_OspfPmNbrHelloSuppressed_Object = MibTableColumn
ospfPmNbrHelloSuppressed = _OspfPmNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 11),
    _OspfPmNbrHelloSuppressed_Type()
)
ospfPmNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrHelloSuppressed.setStatus("current")
_OspfPmNbrApplIndex_Type = OspfPmIndex
_OspfPmNbrApplIndex_Object = MibTableColumn
ospfPmNbrApplIndex = _OspfPmNbrApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 12),
    _OspfPmNbrApplIndex_Type()
)
ospfPmNbrApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmNbrApplIndex.setStatus("current")


class _OspfPmNbrAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfPmNbrAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmNbrAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfPmNbrAdminStatus_Object = MibTableColumn
ospfPmNbrAdminStatus = _OspfPmNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 13),
    _OspfPmNbrAdminStatus_Type()
)
ospfPmNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmNbrAdminStatus.setStatus("current")
_OspfPmNbrOperStatus_Type = OspfPmOperStatus
_OspfPmNbrOperStatus_Object = MibTableColumn
ospfPmNbrOperStatus = _OspfPmNbrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 14),
    _OspfPmNbrOperStatus_Type()
)
ospfPmNbrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrOperStatus.setStatus("current")


class _OspfPmNbrNumRequests_Type(Unsigned32):
    """Custom type ospfPmNbrNumRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmNbrNumRequests_Type.__name__ = "Unsigned32"
_OspfPmNbrNumRequests_Object = MibTableColumn
ospfPmNbrNumRequests = _OspfPmNbrNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 15),
    _OspfPmNbrNumRequests_Type()
)
ospfPmNbrNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrNumRequests.setStatus("current")


class _OspfPmNbrIfIpAddr_Type(IpAddress):
    """Custom type ospfPmNbrIfIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_OspfPmNbrIfIpAddr_Type.__name__ = "IpAddress"
_OspfPmNbrIfIpAddr_Object = MibTableColumn
ospfPmNbrIfIpAddr = _OspfPmNbrIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 16),
    _OspfPmNbrIfIpAddr_Type()
)
ospfPmNbrIfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmNbrIfIpAddr.setStatus("current")
_OspfPmNbrDeadTime_Type = PositiveInteger
_OspfPmNbrDeadTime_Object = MibTableColumn
ospfPmNbrDeadTime = _OspfPmNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 17),
    _OspfPmNbrDeadTime_Type()
)
ospfPmNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrDeadTime.setStatus("current")
_OspfPmNbrAreaId_Type = AreaID
_OspfPmNbrAreaId_Object = MibTableColumn
ospfPmNbrAreaId = _OspfPmNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 18),
    _OspfPmNbrAreaId_Type()
)
ospfPmNbrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrAreaId.setStatus("current")
_OspfPmNbrRestartHelperStatus_Type = OspfRestartHelperStatus
_OspfPmNbrRestartHelperStatus_Object = MibTableColumn
ospfPmNbrRestartHelperStatus = _OspfPmNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 19),
    _OspfPmNbrRestartHelperStatus_Type()
)
ospfPmNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrRestartHelperStatus.setStatus("current")
_OspfPmNbrRestartHelperAge_Type = UpToRefreshInterval
_OspfPmNbrRestartHelperAge_Object = MibTableColumn
ospfPmNbrRestartHelperAge = _OspfPmNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 20),
    _OspfPmNbrRestartHelperAge_Type()
)
ospfPmNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmNbrRestartHelperAge.setUnits("seconds")
_OspfPmNbrRestartHelperExitReason_Type = OspfRestartExitReason
_OspfPmNbrRestartHelperExitReason_Object = MibTableColumn
ospfPmNbrRestartHelperExitReason = _OspfPmNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 21),
    _OspfPmNbrRestartHelperExitReason_Type()
)
ospfPmNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrRestartHelperExitReason.setStatus("current")


class _OspfPmNbrConfiguredPriority_Type(DesignatedRouterPriority):
    """Custom type ospfPmNbrConfiguredPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfPmNbrConfiguredPriority_Type.__name__ = "DesignatedRouterPriority"
_OspfPmNbrConfiguredPriority_Object = MibTableColumn
ospfPmNbrConfiguredPriority = _OspfPmNbrConfiguredPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 22),
    _OspfPmNbrConfiguredPriority_Type()
)
ospfPmNbrConfiguredPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmNbrConfiguredPriority.setStatus("current")
_OspfPmNbrDesignatedRtrState_Type = OspfDesignatedRtrState
_OspfPmNbrDesignatedRtrState_Object = MibTableColumn
ospfPmNbrDesignatedRtrState = _OspfPmNbrDesignatedRtrState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 10, 1, 23),
    _OspfPmNbrDesignatedRtrState_Type()
)
ospfPmNbrDesignatedRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmNbrDesignatedRtrState.setStatus("current")
_OspfPmVirtNbrTable_Object = MibTable
ospfPmVirtNbrTable = _OspfPmVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11)
)
if mibBuilder.loadTexts:
    ospfPmVirtNbrTable.setStatus("current")
_OspfPmVirtNbrEntry_Object = MibTableRow
ospfPmVirtNbrEntry = _OspfPmVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1)
)
ospfPmVirtNbrEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmVirtNbrApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmVirtNbrArea"),
    (0, "DC-OSPF-MIB", "ospfPmVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    ospfPmVirtNbrEntry.setStatus("current")
_OspfPmVirtNbrArea_Type = AreaID
_OspfPmVirtNbrArea_Object = MibTableColumn
ospfPmVirtNbrArea = _OspfPmVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 1),
    _OspfPmVirtNbrArea_Type()
)
ospfPmVirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtNbrArea.setStatus("current")
_OspfPmVirtNbrRtrId_Type = RouterID
_OspfPmVirtNbrRtrId_Object = MibTableColumn
ospfPmVirtNbrRtrId = _OspfPmVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 2),
    _OspfPmVirtNbrRtrId_Type()
)
ospfPmVirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtNbrRtrId.setStatus("current")
_OspfPmVirtNbrIpAddr_Type = IpAddress
_OspfPmVirtNbrIpAddr_Object = MibTableColumn
ospfPmVirtNbrIpAddr = _OspfPmVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 3),
    _OspfPmVirtNbrIpAddr_Type()
)
ospfPmVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrIpAddr.setStatus("current")
_OspfPmVirtNbrOptions_Type = Integer32
_OspfPmVirtNbrOptions_Object = MibTableColumn
ospfPmVirtNbrOptions = _OspfPmVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 4),
    _OspfPmVirtNbrOptions_Type()
)
ospfPmVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrOptions.setStatus("current")
_OspfPmVirtNbrState_Type = OspfNeighborStates
_OspfPmVirtNbrState_Object = MibTableColumn
ospfPmVirtNbrState = _OspfPmVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 5),
    _OspfPmVirtNbrState_Type()
)
ospfPmVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrState.setStatus("current")
_OspfPmVirtNbrEvents_Type = Counter32
_OspfPmVirtNbrEvents_Object = MibTableColumn
ospfPmVirtNbrEvents = _OspfPmVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 6),
    _OspfPmVirtNbrEvents_Type()
)
ospfPmVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrEvents.setStatus("current")
_OspfPmVirtNbrLsRetransQLen_Type = Gauge32
_OspfPmVirtNbrLsRetransQLen_Object = MibTableColumn
ospfPmVirtNbrLsRetransQLen = _OspfPmVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 7),
    _OspfPmVirtNbrLsRetransQLen_Type()
)
ospfPmVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrLsRetransQLen.setStatus("current")
_OspfPmVirtNbrHelloSuppressed_Type = TruthValue
_OspfPmVirtNbrHelloSuppressed_Object = MibTableColumn
ospfPmVirtNbrHelloSuppressed = _OspfPmVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 8),
    _OspfPmVirtNbrHelloSuppressed_Type()
)
ospfPmVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrHelloSuppressed.setStatus("current")
_OspfPmVirtNbrApplIndex_Type = OspfPmIndex
_OspfPmVirtNbrApplIndex_Object = MibTableColumn
ospfPmVirtNbrApplIndex = _OspfPmVirtNbrApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 9),
    _OspfPmVirtNbrApplIndex_Type()
)
ospfPmVirtNbrApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtNbrApplIndex.setStatus("current")


class _OspfPmVirtNbrNumRequests_Type(Unsigned32):
    """Custom type ospfPmVirtNbrNumRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmVirtNbrNumRequests_Type.__name__ = "Unsigned32"
_OspfPmVirtNbrNumRequests_Object = MibTableColumn
ospfPmVirtNbrNumRequests = _OspfPmVirtNbrNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 10),
    _OspfPmVirtNbrNumRequests_Type()
)
ospfPmVirtNbrNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrNumRequests.setStatus("current")
_OspfPmVirtNbrDeadTime_Type = PositiveInteger
_OspfPmVirtNbrDeadTime_Object = MibTableColumn
ospfPmVirtNbrDeadTime = _OspfPmVirtNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 11),
    _OspfPmVirtNbrDeadTime_Type()
)
ospfPmVirtNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrDeadTime.setStatus("current")
_OspfPmVirtNbrRestartHelperStatus_Type = OspfRestartHelperStatus
_OspfPmVirtNbrRestartHelperStatus_Object = MibTableColumn
ospfPmVirtNbrRestartHelperStatus = _OspfPmVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 12),
    _OspfPmVirtNbrRestartHelperStatus_Type()
)
ospfPmVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrRestartHelperStatus.setStatus("current")
_OspfPmVirtNbrRestartHelperAge_Type = UpToRefreshInterval
_OspfPmVirtNbrRestartHelperAge_Object = MibTableColumn
ospfPmVirtNbrRestartHelperAge = _OspfPmVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 13),
    _OspfPmVirtNbrRestartHelperAge_Type()
)
ospfPmVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmVirtNbrRestartHelperAge.setUnits("seconds")
_OspfPmVirtNbrRestartHelperExit_Type = OspfRestartExitReason
_OspfPmVirtNbrRestartHelperExit_Object = MibTableColumn
ospfPmVirtNbrRestartHelperExit = _OspfPmVirtNbrRestartHelperExit_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 11, 1, 14),
    _OspfPmVirtNbrRestartHelperExit_Type()
)
ospfPmVirtNbrRestartHelperExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtNbrRestartHelperExit.setStatus("current")
_OspfPmExtLsdbTable_Object = MibTable
ospfPmExtLsdbTable = _OspfPmExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12)
)
if mibBuilder.loadTexts:
    ospfPmExtLsdbTable.setStatus("current")
_OspfPmExtLsdbEntry_Object = MibTableRow
ospfPmExtLsdbEntry = _OspfPmExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1)
)
ospfPmExtLsdbEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmExtLsdbApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmExtLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmExtLsdbLsid"),
    (0, "DC-OSPF-MIB", "ospfPmExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfPmExtLsdbEntry.setStatus("current")
_OspfPmExtLsdbType_Type = OspfExtLsTypes
_OspfPmExtLsdbType_Object = MibTableColumn
ospfPmExtLsdbType = _OspfPmExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 1),
    _OspfPmExtLsdbType_Type()
)
ospfPmExtLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmExtLsdbType.setStatus("current")
_OspfPmExtLsdbLsid_Type = IpAddress
_OspfPmExtLsdbLsid_Object = MibTableColumn
ospfPmExtLsdbLsid = _OspfPmExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 2),
    _OspfPmExtLsdbLsid_Type()
)
ospfPmExtLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmExtLsdbLsid.setStatus("current")
_OspfPmExtLsdbRouterId_Type = RouterID
_OspfPmExtLsdbRouterId_Object = MibTableColumn
ospfPmExtLsdbRouterId = _OspfPmExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 3),
    _OspfPmExtLsdbRouterId_Type()
)
ospfPmExtLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmExtLsdbRouterId.setStatus("current")
_OspfPmExtLsdbSequence_Type = Integer32
_OspfPmExtLsdbSequence_Object = MibTableColumn
ospfPmExtLsdbSequence = _OspfPmExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 4),
    _OspfPmExtLsdbSequence_Type()
)
ospfPmExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmExtLsdbSequence.setStatus("current")
_OspfPmExtLsdbAge_Type = Integer32
_OspfPmExtLsdbAge_Object = MibTableColumn
ospfPmExtLsdbAge = _OspfPmExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 5),
    _OspfPmExtLsdbAge_Type()
)
ospfPmExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmExtLsdbAge.setStatus("current")
_OspfPmExtLsdbChecksum_Type = Integer32
_OspfPmExtLsdbChecksum_Object = MibTableColumn
ospfPmExtLsdbChecksum = _OspfPmExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 6),
    _OspfPmExtLsdbChecksum_Type()
)
ospfPmExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmExtLsdbChecksum.setStatus("current")


class _OspfPmExtLsdbAdvertisement_Type(OctetString):
    """Custom type ospfPmExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_OspfPmExtLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfPmExtLsdbAdvertisement_Object = MibTableColumn
ospfPmExtLsdbAdvertisement = _OspfPmExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 7),
    _OspfPmExtLsdbAdvertisement_Type()
)
ospfPmExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmExtLsdbAdvertisement.setStatus("current")
_OspfPmExtLsdbApplIndex_Type = OspfPmIndex
_OspfPmExtLsdbApplIndex_Object = MibTableColumn
ospfPmExtLsdbApplIndex = _OspfPmExtLsdbApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 12, 1, 8),
    _OspfPmExtLsdbApplIndex_Type()
)
ospfPmExtLsdbApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmExtLsdbApplIndex.setStatus("current")
_OspfPmRouteGroup_ObjectIdentity = ObjectIdentity
ospfPmRouteGroup = _OspfPmRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 13)
)
_OspfPmIntraArea_ObjectIdentity = ObjectIdentity
ospfPmIntraArea = _OspfPmIntraArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 13, 1)
)
_OspfPmInterArea_ObjectIdentity = ObjectIdentity
ospfPmInterArea = _OspfPmInterArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 13, 2)
)
_OspfPmExternalType1_ObjectIdentity = ObjectIdentity
ospfPmExternalType1 = _OspfPmExternalType1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 13, 3)
)
_OspfPmExternalType2_ObjectIdentity = ObjectIdentity
ospfPmExternalType2 = _OspfPmExternalType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 13, 4)
)
_OspfPmAreaAggregateTable_Object = MibTable
ospfPmAreaAggregateTable = _OspfPmAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14)
)
if mibBuilder.loadTexts:
    ospfPmAreaAggregateTable.setStatus("current")
_OspfPmAreaAggregateEntry_Object = MibTableRow
ospfPmAreaAggregateEntry = _OspfPmAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1)
)
ospfPmAreaAggregateEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmAreaAggregateApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmAreaAggregateAreaID"),
    (0, "DC-OSPF-MIB", "ospfPmAreaAggregateLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmAreaAggregateNet"),
    (0, "DC-OSPF-MIB", "ospfPmAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    ospfPmAreaAggregateEntry.setStatus("current")
_OspfPmAreaAggregateAreaID_Type = AreaID
_OspfPmAreaAggregateAreaID_Object = MibTableColumn
ospfPmAreaAggregateAreaID = _OspfPmAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 1),
    _OspfPmAreaAggregateAreaID_Type()
)
ospfPmAreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateAreaID.setStatus("current")
_OspfPmAreaAggregateLsdbType_Type = OspfAggLsTypes
_OspfPmAreaAggregateLsdbType_Object = MibTableColumn
ospfPmAreaAggregateLsdbType = _OspfPmAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 2),
    _OspfPmAreaAggregateLsdbType_Type()
)
ospfPmAreaAggregateLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateLsdbType.setStatus("current")
_OspfPmAreaAggregateNet_Type = IpAddress
_OspfPmAreaAggregateNet_Object = MibTableColumn
ospfPmAreaAggregateNet = _OspfPmAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 3),
    _OspfPmAreaAggregateNet_Type()
)
ospfPmAreaAggregateNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateNet.setStatus("current")
_OspfPmAreaAggregateMask_Type = IpAddress
_OspfPmAreaAggregateMask_Object = MibTableColumn
ospfPmAreaAggregateMask = _OspfPmAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 4),
    _OspfPmAreaAggregateMask_Type()
)
ospfPmAreaAggregateMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateMask.setStatus("current")
_OspfPmAreaAggregateStatus_Type = RowStatus
_OspfPmAreaAggregateStatus_Object = MibTableColumn
ospfPmAreaAggregateStatus = _OspfPmAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 5),
    _OspfPmAreaAggregateStatus_Type()
)
ospfPmAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateStatus.setStatus("current")


class _OspfPmAreaAggregateEffect_Type(OspfAggregateEffects):
    """Custom type ospfPmAreaAggregateEffect based on OspfAggregateEffects"""
    defaultValue = 1


_OspfPmAreaAggregateEffect_Type.__name__ = "OspfAggregateEffects"
_OspfPmAreaAggregateEffect_Object = MibTableColumn
ospfPmAreaAggregateEffect = _OspfPmAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 6),
    _OspfPmAreaAggregateEffect_Type()
)
ospfPmAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateEffect.setStatus("current")
_OspfPmAreaAggregateApplIndex_Type = OspfPmIndex
_OspfPmAreaAggregateApplIndex_Object = MibTableColumn
ospfPmAreaAggregateApplIndex = _OspfPmAreaAggregateApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 14, 1, 7),
    _OspfPmAreaAggregateApplIndex_Type()
)
ospfPmAreaAggregateApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmAreaAggregateApplIndex.setStatus("current")
_OspfPmLocalLsdbTable_Object = MibTable
ospfPmLocalLsdbTable = _OspfPmLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17)
)
if mibBuilder.loadTexts:
    ospfPmLocalLsdbTable.setStatus("current")
_OspfPmLocalLsdbEntry_Object = MibTableRow
ospfPmLocalLsdbEntry = _OspfPmLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1)
)
ospfPmLocalLsdbEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmLocalLsdbApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmLocalLsdbIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmLocalLsdbAddressLessIf"),
    (0, "DC-OSPF-MIB", "ospfPmLocalLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmLocalLsdbLsid"),
    (0, "DC-OSPF-MIB", "ospfPmLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfPmLocalLsdbEntry.setStatus("current")
_OspfPmLocalLsdbIpAddress_Type = IpAddress
_OspfPmLocalLsdbIpAddress_Object = MibTableColumn
ospfPmLocalLsdbIpAddress = _OspfPmLocalLsdbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 1),
    _OspfPmLocalLsdbIpAddress_Type()
)
ospfPmLocalLsdbIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbIpAddress.setStatus("current")
_OspfPmLocalLsdbAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmLocalLsdbAddressLessIf_Object = MibTableColumn
ospfPmLocalLsdbAddressLessIf = _OspfPmLocalLsdbAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 2),
    _OspfPmLocalLsdbAddressLessIf_Type()
)
ospfPmLocalLsdbAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbAddressLessIf.setStatus("current")
_OspfPmLocalLsdbType_Type = OspfLinkLsTypes
_OspfPmLocalLsdbType_Object = MibTableColumn
ospfPmLocalLsdbType = _OspfPmLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 3),
    _OspfPmLocalLsdbType_Type()
)
ospfPmLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbType.setStatus("current")
_OspfPmLocalLsdbLsid_Type = IpAddress
_OspfPmLocalLsdbLsid_Object = MibTableColumn
ospfPmLocalLsdbLsid = _OspfPmLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 4),
    _OspfPmLocalLsdbLsid_Type()
)
ospfPmLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbLsid.setStatus("current")
_OspfPmLocalLsdbRouterId_Type = RouterID
_OspfPmLocalLsdbRouterId_Object = MibTableColumn
ospfPmLocalLsdbRouterId = _OspfPmLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 5),
    _OspfPmLocalLsdbRouterId_Type()
)
ospfPmLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbRouterId.setStatus("current")
_OspfPmLocalLsdbSequence_Type = Integer32
_OspfPmLocalLsdbSequence_Object = MibTableColumn
ospfPmLocalLsdbSequence = _OspfPmLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 6),
    _OspfPmLocalLsdbSequence_Type()
)
ospfPmLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbSequence.setStatus("current")
_OspfPmLocalLsdbAge_Type = Integer32
_OspfPmLocalLsdbAge_Object = MibTableColumn
ospfPmLocalLsdbAge = _OspfPmLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 7),
    _OspfPmLocalLsdbAge_Type()
)
ospfPmLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbAge.setStatus("current")
_OspfPmLocalLsdbChecksum_Type = Integer32
_OspfPmLocalLsdbChecksum_Object = MibTableColumn
ospfPmLocalLsdbChecksum = _OspfPmLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 8),
    _OspfPmLocalLsdbChecksum_Type()
)
ospfPmLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbChecksum.setStatus("current")


class _OspfPmLocalLsdbAdvertisement_Type(OctetString):
    """Custom type ospfPmLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfPmLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfPmLocalLsdbAdvertisement_Object = MibTableColumn
ospfPmLocalLsdbAdvertisement = _OspfPmLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 9),
    _OspfPmLocalLsdbAdvertisement_Type()
)
ospfPmLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbAdvertisement.setStatus("current")
_OspfPmLocalLsdbApplIndex_Type = OspfPmIndex
_OspfPmLocalLsdbApplIndex_Object = MibTableColumn
ospfPmLocalLsdbApplIndex = _OspfPmLocalLsdbApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 10),
    _OspfPmLocalLsdbApplIndex_Type()
)
ospfPmLocalLsdbApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbApplIndex.setStatus("current")
_OspfPmLocalLsdbAreaId_Type = AreaID
_OspfPmLocalLsdbAreaId_Object = MibTableColumn
ospfPmLocalLsdbAreaId = _OspfPmLocalLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 17, 1, 11),
    _OspfPmLocalLsdbAreaId_Type()
)
ospfPmLocalLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmLocalLsdbAreaId.setStatus("current")
_OspfPmVirtLocalLsdbTable_Object = MibTable
ospfPmVirtLocalLsdbTable = _OspfPmVirtLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18)
)
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbTable.setStatus("current")
_OspfPmVirtLocalLsdbEntry_Object = MibTableRow
ospfPmVirtLocalLsdbEntry = _OspfPmVirtLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1)
)
ospfPmVirtLocalLsdbEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmVirtLocalLsdbApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmVirtLocalLsdbTransitArea"),
    (0, "DC-OSPF-MIB", "ospfPmVirtLocalLsdbNeighbor"),
    (0, "DC-OSPF-MIB", "ospfPmVirtLocalLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmVirtLocalLsdbLsid"),
    (0, "DC-OSPF-MIB", "ospfPmVirtLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbEntry.setStatus("current")
_OspfPmVirtLocalLsdbTransitArea_Type = AreaID
_OspfPmVirtLocalLsdbTransitArea_Object = MibTableColumn
ospfPmVirtLocalLsdbTransitArea = _OspfPmVirtLocalLsdbTransitArea_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 1),
    _OspfPmVirtLocalLsdbTransitArea_Type()
)
ospfPmVirtLocalLsdbTransitArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbTransitArea.setStatus("current")
_OspfPmVirtLocalLsdbNeighbor_Type = RouterID
_OspfPmVirtLocalLsdbNeighbor_Object = MibTableColumn
ospfPmVirtLocalLsdbNeighbor = _OspfPmVirtLocalLsdbNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 2),
    _OspfPmVirtLocalLsdbNeighbor_Type()
)
ospfPmVirtLocalLsdbNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbNeighbor.setStatus("current")
_OspfPmVirtLocalLsdbType_Type = OspfLinkLsTypes
_OspfPmVirtLocalLsdbType_Object = MibTableColumn
ospfPmVirtLocalLsdbType = _OspfPmVirtLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 3),
    _OspfPmVirtLocalLsdbType_Type()
)
ospfPmVirtLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbType.setStatus("current")
_OspfPmVirtLocalLsdbLsid_Type = IpAddress
_OspfPmVirtLocalLsdbLsid_Object = MibTableColumn
ospfPmVirtLocalLsdbLsid = _OspfPmVirtLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 4),
    _OspfPmVirtLocalLsdbLsid_Type()
)
ospfPmVirtLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbLsid.setStatus("current")
_OspfPmVirtLocalLsdbRouterId_Type = RouterID
_OspfPmVirtLocalLsdbRouterId_Object = MibTableColumn
ospfPmVirtLocalLsdbRouterId = _OspfPmVirtLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 5),
    _OspfPmVirtLocalLsdbRouterId_Type()
)
ospfPmVirtLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbRouterId.setStatus("current")
_OspfPmVirtLocalLsdbSequence_Type = Integer32
_OspfPmVirtLocalLsdbSequence_Object = MibTableColumn
ospfPmVirtLocalLsdbSequence = _OspfPmVirtLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 6),
    _OspfPmVirtLocalLsdbSequence_Type()
)
ospfPmVirtLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbSequence.setStatus("current")
_OspfPmVirtLocalLsdbAge_Type = Integer32
_OspfPmVirtLocalLsdbAge_Object = MibTableColumn
ospfPmVirtLocalLsdbAge = _OspfPmVirtLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 7),
    _OspfPmVirtLocalLsdbAge_Type()
)
ospfPmVirtLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbAge.setStatus("current")
_OspfPmVirtLocalLsdbChecksum_Type = Integer32
_OspfPmVirtLocalLsdbChecksum_Object = MibTableColumn
ospfPmVirtLocalLsdbChecksum = _OspfPmVirtLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 8),
    _OspfPmVirtLocalLsdbChecksum_Type()
)
ospfPmVirtLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbChecksum.setStatus("current")


class _OspfPmVirtLocalLsdbAdv_Type(OctetString):
    """Custom type ospfPmVirtLocalLsdbAdv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfPmVirtLocalLsdbAdv_Type.__name__ = "OctetString"
_OspfPmVirtLocalLsdbAdv_Object = MibTableColumn
ospfPmVirtLocalLsdbAdv = _OspfPmVirtLocalLsdbAdv_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 9),
    _OspfPmVirtLocalLsdbAdv_Type()
)
ospfPmVirtLocalLsdbAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbAdv.setStatus("current")
_OspfPmVirtLocalLsdbApplIndex_Type = OspfPmIndex
_OspfPmVirtLocalLsdbApplIndex_Object = MibTableColumn
ospfPmVirtLocalLsdbApplIndex = _OspfPmVirtLocalLsdbApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 18, 1, 10),
    _OspfPmVirtLocalLsdbApplIndex_Type()
)
ospfPmVirtLocalLsdbApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtLocalLsdbApplIndex.setStatus("current")
_OspfPmMjTable_Object = MibTable
ospfPmMjTable = _OspfPmMjTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19)
)
if mibBuilder.loadTexts:
    ospfPmMjTable.setStatus("current")
_OspfPmMjEntry_Object = MibTableRow
ospfPmMjEntry = _OspfPmMjEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1)
)
ospfPmMjEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmMjApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmMjInterfaceId"),
    (0, "DC-OSPF-MIB", "ospfPmMjPartnerIndex"),
)
if mibBuilder.loadTexts:
    ospfPmMjEntry.setStatus("current")
_OspfPmMjApplIndex_Type = Unsigned32
_OspfPmMjApplIndex_Object = MibTableColumn
ospfPmMjApplIndex = _OspfPmMjApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 1),
    _OspfPmMjApplIndex_Type()
)
ospfPmMjApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMjApplIndex.setStatus("current")
_OspfPmMjInterfaceId_Type = OspfPmInterfaceId
_OspfPmMjInterfaceId_Object = MibTableColumn
ospfPmMjInterfaceId = _OspfPmMjInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 2),
    _OspfPmMjInterfaceId_Type()
)
ospfPmMjInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMjInterfaceId.setStatus("current")
_OspfPmMjPartnerIndex_Type = Unsigned32
_OspfPmMjPartnerIndex_Object = MibTableColumn
ospfPmMjPartnerIndex = _OspfPmMjPartnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 3),
    _OspfPmMjPartnerIndex_Type()
)
ospfPmMjPartnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMjPartnerIndex.setStatus("current")
_OspfPmMjRowStatus_Type = RowStatus
_OspfPmMjRowStatus_Object = MibTableColumn
ospfPmMjRowStatus = _OspfPmMjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 4),
    _OspfPmMjRowStatus_Type()
)
ospfPmMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMjRowStatus.setStatus("current")


class _OspfPmMjAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfPmMjAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 2


_OspfPmMjAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfPmMjAdminStatus_Object = MibTableColumn
ospfPmMjAdminStatus = _OspfPmMjAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 5),
    _OspfPmMjAdminStatus_Type()
)
ospfPmMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMjAdminStatus.setStatus("current")
_OspfPmMjOperStatus_Type = OspfPmOperStatus
_OspfPmMjOperStatus_Object = MibTableColumn
ospfPmMjOperStatus = _OspfPmMjOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 6),
    _OspfPmMjOperStatus_Type()
)
ospfPmMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMjOperStatus.setStatus("current")
_OspfPmMjJoinStatus_Type = OspfPmMjStatus
_OspfPmMjJoinStatus_Object = MibTableColumn
ospfPmMjJoinStatus = _OspfPmMjJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 19, 1, 7),
    _OspfPmMjJoinStatus_Type()
)
ospfPmMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMjJoinStatus.setStatus("current")
_OspfPmSjTable_Object = MibTable
ospfPmSjTable = _OspfPmSjTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20)
)
if mibBuilder.loadTexts:
    ospfPmSjTable.setStatus("current")
_OspfPmSjEntry_Object = MibTableRow
ospfPmSjEntry = _OspfPmSjEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20, 1)
)
ospfPmSjEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmSjApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmSjInterfaceId"),
    (0, "DC-OSPF-MIB", "ospfPmSjMasterIndex"),
)
if mibBuilder.loadTexts:
    ospfPmSjEntry.setStatus("current")
_OspfPmSjApplIndex_Type = Unsigned32
_OspfPmSjApplIndex_Object = MibTableColumn
ospfPmSjApplIndex = _OspfPmSjApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20, 1, 1),
    _OspfPmSjApplIndex_Type()
)
ospfPmSjApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSjApplIndex.setStatus("current")
_OspfPmSjMasterIndex_Type = Unsigned32
_OspfPmSjMasterIndex_Object = MibTableColumn
ospfPmSjMasterIndex = _OspfPmSjMasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20, 1, 2),
    _OspfPmSjMasterIndex_Type()
)
ospfPmSjMasterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSjMasterIndex.setStatus("current")
_OspfPmSjJoinIndex_Type = Unsigned32
_OspfPmSjJoinIndex_Object = MibTableColumn
ospfPmSjJoinIndex = _OspfPmSjJoinIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20, 1, 3),
    _OspfPmSjJoinIndex_Type()
)
ospfPmSjJoinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSjJoinIndex.setStatus("current")
_OspfPmSjJoinStatus_Type = OspfPmSjStatus
_OspfPmSjJoinStatus_Object = MibTableColumn
ospfPmSjJoinStatus = _OspfPmSjJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20, 1, 4),
    _OspfPmSjJoinStatus_Type()
)
ospfPmSjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSjJoinStatus.setStatus("current")
_OspfPmSjInterfaceId_Type = OspfPmSlaveInterfaceId
_OspfPmSjInterfaceId_Object = MibTableColumn
ospfPmSjInterfaceId = _OspfPmSjInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 20, 1, 5),
    _OspfPmSjInterfaceId_Type()
)
ospfPmSjInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSjInterfaceId.setStatus("current")
_OspfPmIfSwitchTable_Object = MibTable
ospfPmIfSwitchTable = _OspfPmIfSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21)
)
if mibBuilder.loadTexts:
    ospfPmIfSwitchTable.setStatus("current")
_OspfPmIfSwitchEntry_Object = MibTableRow
ospfPmIfSwitchEntry = _OspfPmIfSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1)
)
ospfPmIfSwitchEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmIfSwitchApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmIfSwitchIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmIfSwitchAddressLessIf"),
    (0, "DC-OSPF-MIB", "ospfPmIfSwitchingCap"),
    (0, "DC-OSPF-MIB", "ospfPmIfSwitchEncoding"),
    (0, "DC-OSPF-MIB", "ospfPmIfSwitchISDIndex"),
)
if mibBuilder.loadTexts:
    ospfPmIfSwitchEntry.setStatus("current")
_OspfPmIfSwitchApplIndex_Type = OspfPmIndex
_OspfPmIfSwitchApplIndex_Object = MibTableColumn
ospfPmIfSwitchApplIndex = _OspfPmIfSwitchApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 1),
    _OspfPmIfSwitchApplIndex_Type()
)
ospfPmIfSwitchApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfSwitchApplIndex.setStatus("current")
_OspfPmIfSwitchIpAddress_Type = IpAddress
_OspfPmIfSwitchIpAddress_Object = MibTableColumn
ospfPmIfSwitchIpAddress = _OspfPmIfSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 2),
    _OspfPmIfSwitchIpAddress_Type()
)
ospfPmIfSwitchIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfSwitchIpAddress.setStatus("current")
_OspfPmIfSwitchAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmIfSwitchAddressLessIf_Object = MibTableColumn
ospfPmIfSwitchAddressLessIf = _OspfPmIfSwitchAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 3),
    _OspfPmIfSwitchAddressLessIf_Type()
)
ospfPmIfSwitchAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfSwitchAddressLessIf.setStatus("current")
_OspfPmIfSwitchingCap_Type = OspfPmIfSwitchCapValue
_OspfPmIfSwitchingCap_Object = MibTableColumn
ospfPmIfSwitchingCap = _OspfPmIfSwitchingCap_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 4),
    _OspfPmIfSwitchingCap_Type()
)
ospfPmIfSwitchingCap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfSwitchingCap.setStatus("current")
_OspfPmIfSwitchEncoding_Type = OspfPmIfSwitchEncodingValue
_OspfPmIfSwitchEncoding_Object = MibTableColumn
ospfPmIfSwitchEncoding = _OspfPmIfSwitchEncoding_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 5),
    _OspfPmIfSwitchEncoding_Type()
)
ospfPmIfSwitchEncoding.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfSwitchEncoding.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth0_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth0_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth0 = _OspfPmIfSwitchMaxLSPBwidth0_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 6),
    _OspfPmIfSwitchMaxLSPBwidth0_Type()
)
ospfPmIfSwitchMaxLSPBwidth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth0.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth0_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth0_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth0 = _OspfPmIfSwitchLastMaxLSPBwidth0_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 7),
    _OspfPmIfSwitchLastMaxLSPBwidth0_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth0.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth1_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth1_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth1 = _OspfPmIfSwitchMaxLSPBwidth1_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 8),
    _OspfPmIfSwitchMaxLSPBwidth1_Type()
)
ospfPmIfSwitchMaxLSPBwidth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth1.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth1_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth1_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth1 = _OspfPmIfSwitchLastMaxLSPBwidth1_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 9),
    _OspfPmIfSwitchLastMaxLSPBwidth1_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth1.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth2_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth2_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth2 = _OspfPmIfSwitchMaxLSPBwidth2_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 10),
    _OspfPmIfSwitchMaxLSPBwidth2_Type()
)
ospfPmIfSwitchMaxLSPBwidth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth2.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth2_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth2_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth2 = _OspfPmIfSwitchLastMaxLSPBwidth2_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 11),
    _OspfPmIfSwitchLastMaxLSPBwidth2_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth2.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth3_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth3_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth3 = _OspfPmIfSwitchMaxLSPBwidth3_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 12),
    _OspfPmIfSwitchMaxLSPBwidth3_Type()
)
ospfPmIfSwitchMaxLSPBwidth3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth3.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth3_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth3_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth3 = _OspfPmIfSwitchLastMaxLSPBwidth3_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 13),
    _OspfPmIfSwitchLastMaxLSPBwidth3_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth3.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth4_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth4_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth4 = _OspfPmIfSwitchMaxLSPBwidth4_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 14),
    _OspfPmIfSwitchMaxLSPBwidth4_Type()
)
ospfPmIfSwitchMaxLSPBwidth4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth4.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth4_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth4_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth4 = _OspfPmIfSwitchLastMaxLSPBwidth4_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 15),
    _OspfPmIfSwitchLastMaxLSPBwidth4_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth4.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth5_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth5_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth5 = _OspfPmIfSwitchMaxLSPBwidth5_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 16),
    _OspfPmIfSwitchMaxLSPBwidth5_Type()
)
ospfPmIfSwitchMaxLSPBwidth5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth5.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth5_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth5_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth5 = _OspfPmIfSwitchLastMaxLSPBwidth5_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 17),
    _OspfPmIfSwitchLastMaxLSPBwidth5_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth5.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth6_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth6_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth6 = _OspfPmIfSwitchMaxLSPBwidth6_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 18),
    _OspfPmIfSwitchMaxLSPBwidth6_Type()
)
ospfPmIfSwitchMaxLSPBwidth6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth6.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth6_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth6_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth6 = _OspfPmIfSwitchLastMaxLSPBwidth6_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 19),
    _OspfPmIfSwitchLastMaxLSPBwidth6_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth6.setStatus("current")
_OspfPmIfSwitchMaxLSPBwidth7_Type = Integer32
_OspfPmIfSwitchMaxLSPBwidth7_Object = MibTableColumn
ospfPmIfSwitchMaxLSPBwidth7 = _OspfPmIfSwitchMaxLSPBwidth7_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 20),
    _OspfPmIfSwitchMaxLSPBwidth7_Type()
)
ospfPmIfSwitchMaxLSPBwidth7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMaxLSPBwidth7.setStatus("current")
_OspfPmIfSwitchLastMaxLSPBwidth7_Type = Integer32
_OspfPmIfSwitchLastMaxLSPBwidth7_Object = MibTableColumn
ospfPmIfSwitchLastMaxLSPBwidth7 = _OspfPmIfSwitchLastMaxLSPBwidth7_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 21),
    _OspfPmIfSwitchLastMaxLSPBwidth7_Type()
)
ospfPmIfSwitchLastMaxLSPBwidth7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMaxLSPBwidth7.setStatus("current")
_OspfPmIfSwitchMinLSPBwidth_Type = Integer32
_OspfPmIfSwitchMinLSPBwidth_Object = MibTableColumn
ospfPmIfSwitchMinLSPBwidth = _OspfPmIfSwitchMinLSPBwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 22),
    _OspfPmIfSwitchMinLSPBwidth_Type()
)
ospfPmIfSwitchMinLSPBwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMinLSPBwidth.setStatus("current")
_OspfPmIfSwitchLastMinLSPBwidth_Type = Integer32
_OspfPmIfSwitchLastMinLSPBwidth_Object = MibTableColumn
ospfPmIfSwitchLastMinLSPBwidth = _OspfPmIfSwitchLastMinLSPBwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 23),
    _OspfPmIfSwitchLastMinLSPBwidth_Type()
)
ospfPmIfSwitchLastMinLSPBwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMinLSPBwidth.setStatus("current")
_OspfPmIfSwitchMTUSize_Type = Integer32
_OspfPmIfSwitchMTUSize_Object = MibTableColumn
ospfPmIfSwitchMTUSize = _OspfPmIfSwitchMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 24),
    _OspfPmIfSwitchMTUSize_Type()
)
ospfPmIfSwitchMTUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchMTUSize.setStatus("current")
_OspfPmIfSwitchLastMTUSize_Type = Integer32
_OspfPmIfSwitchLastMTUSize_Object = MibTableColumn
ospfPmIfSwitchLastMTUSize = _OspfPmIfSwitchLastMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 25),
    _OspfPmIfSwitchLastMTUSize_Type()
)
ospfPmIfSwitchLastMTUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchLastMTUSize.setStatus("current")


class _OspfPmIfSwitchSonetSdhSupport_Type(OspfPmIfSwitchSonetSdhValue):
    """Custom type ospfPmIfSwitchSonetSdhSupport based on OspfPmIfSwitchSonetSdhValue"""
    defaultValue = 0


_OspfPmIfSwitchSonetSdhSupport_Type.__name__ = "OspfPmIfSwitchSonetSdhValue"
_OspfPmIfSwitchSonetSdhSupport_Object = MibTableColumn
ospfPmIfSwitchSonetSdhSupport = _OspfPmIfSwitchSonetSdhSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 26),
    _OspfPmIfSwitchSonetSdhSupport_Type()
)
ospfPmIfSwitchSonetSdhSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfSwitchSonetSdhSupport.setStatus("current")
_OspfPmIfSwitchISDIndex_Type = NumericIndex
_OspfPmIfSwitchISDIndex_Object = MibTableColumn
ospfPmIfSwitchISDIndex = _OspfPmIfSwitchISDIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 21, 1, 27),
    _OspfPmIfSwitchISDIndex_Type()
)
ospfPmIfSwitchISDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfSwitchISDIndex.setStatus("current")
_OspfNmEntTable_Object = MibTable
ospfNmEntTable = _OspfNmEntTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22)
)
if mibBuilder.loadTexts:
    ospfNmEntTable.setStatus("current")
_OspfNmEntEntry_Object = MibTableRow
ospfNmEntEntry = _OspfNmEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1)
)
ospfNmEntEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfNmEntIndex"),
)
if mibBuilder.loadTexts:
    ospfNmEntEntry.setStatus("current")
_OspfNmEntIndex_Type = OspfPmIndex
_OspfNmEntIndex_Object = MibTableColumn
ospfNmEntIndex = _OspfNmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 1),
    _OspfNmEntIndex_Type()
)
ospfNmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNmEntIndex.setStatus("current")
_OspfNmEntRowStatus_Type = RowStatus
_OspfNmEntRowStatus_Object = MibTableColumn
ospfNmEntRowStatus = _OspfNmEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 2),
    _OspfNmEntRowStatus_Type()
)
ospfNmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmEntRowStatus.setStatus("current")


class _OspfNmEntAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfNmEntAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfNmEntAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfNmEntAdminStatus_Object = MibTableColumn
ospfNmEntAdminStatus = _OspfNmEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 3),
    _OspfNmEntAdminStatus_Type()
)
ospfNmEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmEntAdminStatus.setStatus("current")
_OspfNmEntOperStatus_Type = NpgOperStatus
_OspfNmEntOperStatus_Object = MibTableColumn
ospfNmEntOperStatus = _OspfNmEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 4),
    _OspfNmEntOperStatus_Type()
)
ospfNmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntOperStatus.setStatus("current")


class _OspfNmMjEntityIndex_Type(Unsigned32):
    """Custom type ospfNmMjEntityIndex based on Unsigned32"""
    defaultValue = 1


_OspfNmMjEntityIndex_Type.__name__ = "Unsigned32"
_OspfNmMjEntityIndex_Object = MibTableColumn
ospfNmMjEntityIndex = _OspfNmMjEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 5),
    _OspfNmMjEntityIndex_Type()
)
ospfNmMjEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmMjEntityIndex.setStatus("current")


class _OspfNmSckEntityIndex_Type(Unsigned32):
    """Custom type ospfNmSckEntityIndex based on Unsigned32"""
    defaultValue = 1


_OspfNmSckEntityIndex_Type.__name__ = "Unsigned32"
_OspfNmSckEntityIndex_Object = MibTableColumn
ospfNmSckEntityIndex = _OspfNmSckEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 6),
    _OspfNmSckEntityIndex_Type()
)
ospfNmSckEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmSckEntityIndex.setStatus("current")
_OspfNmEntNmiJoinOperStatus_Type = NpgOperStatus
_OspfNmEntNmiJoinOperStatus_Object = MibTableColumn
ospfNmEntNmiJoinOperStatus = _OspfNmEntNmiJoinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 7),
    _OspfNmEntNmiJoinOperStatus_Type()
)
ospfNmEntNmiJoinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntNmiJoinOperStatus.setStatus("current")
_OspfNmEntSckJoinOperStatus_Type = NpgOperStatus
_OspfNmEntSckJoinOperStatus_Object = MibTableColumn
ospfNmEntSckJoinOperStatus = _OspfNmEntSckJoinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 8),
    _OspfNmEntSckJoinOperStatus_Type()
)
ospfNmEntSckJoinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntSckJoinOperStatus.setStatus("current")


class _OspfNmEntBfdEntityIndex_Type(Unsigned32):
    """Custom type ospfNmEntBfdEntityIndex based on Unsigned32"""
    defaultValue = 0


_OspfNmEntBfdEntityIndex_Type.__name__ = "Unsigned32"
_OspfNmEntBfdEntityIndex_Object = MibTableColumn
ospfNmEntBfdEntityIndex = _OspfNmEntBfdEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 9),
    _OspfNmEntBfdEntityIndex_Type()
)
ospfNmEntBfdEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmEntBfdEntityIndex.setStatus("current")
_OspfNmEntBfdJoinOperStatus_Type = NpgOperStatus
_OspfNmEntBfdJoinOperStatus_Object = MibTableColumn
ospfNmEntBfdJoinOperStatus = _OspfNmEntBfdJoinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 10),
    _OspfNmEntBfdJoinOperStatus_Type()
)
ospfNmEntBfdJoinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntBfdJoinOperStatus.setStatus("current")


class _OspfNmEntStatsReset_Type(TruthValue):
    """Custom type ospfNmEntStatsReset based on TruthValue"""
    defaultValue = 2


_OspfNmEntStatsReset_Type.__name__ = "TruthValue"
_OspfNmEntStatsReset_Object = MibTableColumn
ospfNmEntStatsReset = _OspfNmEntStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 11),
    _OspfNmEntStatsReset_Type()
)
ospfNmEntStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmEntStatsReset.setStatus("current")


class _OspfNmEntEnableTrapSupport_Type(TruthValue):
    """Custom type ospfNmEntEnableTrapSupport based on TruthValue"""
    defaultValue = 2


_OspfNmEntEnableTrapSupport_Type.__name__ = "TruthValue"
_OspfNmEntEnableTrapSupport_Object = MibTableColumn
ospfNmEntEnableTrapSupport = _OspfNmEntEnableTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 22, 1, 12),
    _OspfNmEntEnableTrapSupport_Type()
)
ospfNmEntEnableTrapSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNmEntEnableTrapSupport.setStatus("current")
_OspfPmIgpShortcutTable_Object = MibTable
ospfPmIgpShortcutTable = _OspfPmIgpShortcutTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23)
)
if mibBuilder.loadTexts:
    ospfPmIgpShortcutTable.setStatus("current")
_OspfPmIgpShortcutEntry_Object = MibTableRow
ospfPmIgpShortcutEntry = _OspfPmIgpShortcutEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1)
)
ospfPmIgpShortcutEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmShortcutApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmShortcutIfIndex"),
)
if mibBuilder.loadTexts:
    ospfPmIgpShortcutEntry.setStatus("current")
_OspfPmShortcutApplIndex_Type = OspfPmIndex
_OspfPmShortcutApplIndex_Object = MibTableColumn
ospfPmShortcutApplIndex = _OspfPmShortcutApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1, 1),
    _OspfPmShortcutApplIndex_Type()
)
ospfPmShortcutApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShortcutApplIndex.setStatus("current")
_OspfPmShortcutIfIndex_Type = InterfaceIndex
_OspfPmShortcutIfIndex_Object = MibTableColumn
ospfPmShortcutIfIndex = _OspfPmShortcutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1, 2),
    _OspfPmShortcutIfIndex_Type()
)
ospfPmShortcutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShortcutIfIndex.setStatus("current")
_OspfPmShortcutRemoteAddress_Type = IpAddress
_OspfPmShortcutRemoteAddress_Object = MibTableColumn
ospfPmShortcutRemoteAddress = _OspfPmShortcutRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1, 3),
    _OspfPmShortcutRemoteAddress_Type()
)
ospfPmShortcutRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShortcutRemoteAddress.setStatus("current")
_OspfPmShortcutMetricType_Type = IgpShortcutMetricType
_OspfPmShortcutMetricType_Object = MibTableColumn
ospfPmShortcutMetricType = _OspfPmShortcutMetricType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1, 4),
    _OspfPmShortcutMetricType_Type()
)
ospfPmShortcutMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShortcutMetricType.setStatus("current")
_OspfPmShortcutMetricValue_Type = Integer32
_OspfPmShortcutMetricValue_Object = MibTableColumn
ospfPmShortcutMetricValue = _OspfPmShortcutMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1, 5),
    _OspfPmShortcutMetricValue_Type()
)
ospfPmShortcutMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShortcutMetricValue.setStatus("current")
_OspfPmShortcutOperStatus_Type = IfOperStatus
_OspfPmShortcutOperStatus_Object = MibTableColumn
ospfPmShortcutOperStatus = _OspfPmShortcutOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 23, 1, 6),
    _OspfPmShortcutOperStatus_Type()
)
ospfPmShortcutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShortcutOperStatus.setStatus("current")
_OspfPmDomainIdTable_Object = MibTable
ospfPmDomainIdTable = _OspfPmDomainIdTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24)
)
if mibBuilder.loadTexts:
    ospfPmDomainIdTable.setStatus("current")
_OspfPmDomainIdEntry_Object = MibTableRow
ospfPmDomainIdEntry = _OspfPmDomainIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24, 1)
)
ospfPmDomainIdEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmDomainIdApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmDomainIdValue"),
)
if mibBuilder.loadTexts:
    ospfPmDomainIdEntry.setStatus("current")
_OspfPmDomainIdApplIndex_Type = OspfPmIndex
_OspfPmDomainIdApplIndex_Object = MibTableColumn
ospfPmDomainIdApplIndex = _OspfPmDomainIdApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24, 1, 1),
    _OspfPmDomainIdApplIndex_Type()
)
ospfPmDomainIdApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmDomainIdApplIndex.setStatus("current")


class _OspfPmDomainIdValue_Type(OctetString):
    """Custom type ospfPmDomainIdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OspfPmDomainIdValue_Type.__name__ = "OctetString"
_OspfPmDomainIdValue_Object = MibTableColumn
ospfPmDomainIdValue = _OspfPmDomainIdValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24, 1, 2),
    _OspfPmDomainIdValue_Type()
)
ospfPmDomainIdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmDomainIdValue.setStatus("current")
_OspfPmDomainIdRowStatus_Type = RowStatus
_OspfPmDomainIdRowStatus_Object = MibTableColumn
ospfPmDomainIdRowStatus = _OspfPmDomainIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24, 1, 3),
    _OspfPmDomainIdRowStatus_Type()
)
ospfPmDomainIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmDomainIdRowStatus.setStatus("current")


class _OspfPmDomainIdRole_Type(Integer32):
    """Custom type ospfPmDomainIdRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domRolePrimary", 1),
          ("domRoleSecondary", 2))
    )


_OspfPmDomainIdRole_Type.__name__ = "Integer32"
_OspfPmDomainIdRole_Object = MibTableColumn
ospfPmDomainIdRole = _OspfPmDomainIdRole_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24, 1, 4),
    _OspfPmDomainIdRole_Type()
)
ospfPmDomainIdRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmDomainIdRole.setStatus("current")


class _OspfPmDomainIdStatus_Type(Integer32):
    """Custom type ospfPmDomainIdStatus based on Integer32"""
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
        *(("domStsPrimary", 1),
          ("domStsSecondary", 2),
          ("domStsInactive", 3),
          ("domStsInvalid", 4),
          ("domStsInconsistent", 5))
    )


_OspfPmDomainIdStatus_Type.__name__ = "Integer32"
_OspfPmDomainIdStatus_Object = MibTableColumn
ospfPmDomainIdStatus = _OspfPmDomainIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 24, 1, 5),
    _OspfPmDomainIdStatus_Type()
)
ospfPmDomainIdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmDomainIdStatus.setStatus("current")
_OspfPmShamLinkTable_Object = MibTable
ospfPmShamLinkTable = _OspfPmShamLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25)
)
if mibBuilder.loadTexts:
    ospfPmShamLinkTable.setStatus("current")
_OspfPmShamLinkEntry_Object = MibTableRow
ospfPmShamLinkEntry = _OspfPmShamLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1)
)
ospfPmShamLinkEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmShamLinkApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmShamLinkAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmShamLinkLocalIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmShamLinkRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    ospfPmShamLinkEntry.setStatus("current")
_OspfPmShamLinkApplIndex_Type = OspfPmIndex
_OspfPmShamLinkApplIndex_Object = MibTableColumn
ospfPmShamLinkApplIndex = _OspfPmShamLinkApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 1),
    _OspfPmShamLinkApplIndex_Type()
)
ospfPmShamLinkApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkApplIndex.setStatus("current")
_OspfPmShamLinkAreaId_Type = AreaID
_OspfPmShamLinkAreaId_Object = MibTableColumn
ospfPmShamLinkAreaId = _OspfPmShamLinkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 2),
    _OspfPmShamLinkAreaId_Type()
)
ospfPmShamLinkAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkAreaId.setStatus("current")
_OspfPmShamLinkLocalIpAddr_Type = IpAddress
_OspfPmShamLinkLocalIpAddr_Object = MibTableColumn
ospfPmShamLinkLocalIpAddr = _OspfPmShamLinkLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 3),
    _OspfPmShamLinkLocalIpAddr_Type()
)
ospfPmShamLinkLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkLocalIpAddr.setStatus("current")
_OspfPmShamLinkRemoteIpAddr_Type = IpAddress
_OspfPmShamLinkRemoteIpAddr_Object = MibTableColumn
ospfPmShamLinkRemoteIpAddr = _OspfPmShamLinkRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 4),
    _OspfPmShamLinkRemoteIpAddr_Type()
)
ospfPmShamLinkRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkRemoteIpAddr.setStatus("current")
_OspfPmShamLinkRowStatus_Type = RowStatus
_OspfPmShamLinkRowStatus_Object = MibTableColumn
ospfPmShamLinkRowStatus = _OspfPmShamLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 5),
    _OspfPmShamLinkRowStatus_Type()
)
ospfPmShamLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkRowStatus.setStatus("current")
_OspfPmShamLinkIfIndex_Type = InterfaceIndex
_OspfPmShamLinkIfIndex_Object = MibTableColumn
ospfPmShamLinkIfIndex = _OspfPmShamLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 6),
    _OspfPmShamLinkIfIndex_Type()
)
ospfPmShamLinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkIfIndex.setStatus("current")


class _OspfPmShamLinkMetric_Type(Integer32):
    """Custom type ospfPmShamLinkMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmShamLinkMetric_Type.__name__ = "Integer32"
_OspfPmShamLinkMetric_Object = MibTableColumn
ospfPmShamLinkMetric = _OspfPmShamLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 7),
    _OspfPmShamLinkMetric_Type()
)
ospfPmShamLinkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkMetric.setStatus("current")


class _OspfPmShamLinkTransitDelay_Type(UpToMaxAge):
    """Custom type ospfPmShamLinkTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfPmShamLinkTransitDelay_Type.__name__ = "UpToMaxAge"
_OspfPmShamLinkTransitDelay_Object = MibTableColumn
ospfPmShamLinkTransitDelay = _OspfPmShamLinkTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 8),
    _OspfPmShamLinkTransitDelay_Type()
)
ospfPmShamLinkTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkTransitDelay.setStatus("current")


class _OspfPmShamLinkRetransInterval_Type(UpToMaxAge):
    """Custom type ospfPmShamLinkRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfPmShamLinkRetransInterval_Type.__name__ = "UpToMaxAge"
_OspfPmShamLinkRetransInterval_Object = MibTableColumn
ospfPmShamLinkRetransInterval = _OspfPmShamLinkRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 9),
    _OspfPmShamLinkRetransInterval_Type()
)
ospfPmShamLinkRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkRetransInterval.setStatus("current")


class _OspfPmShamLinkHelloInterval_Type(HelloRange):
    """Custom type ospfPmShamLinkHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfPmShamLinkHelloInterval_Type.__name__ = "HelloRange"
_OspfPmShamLinkHelloInterval_Object = MibTableColumn
ospfPmShamLinkHelloInterval = _OspfPmShamLinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 10),
    _OspfPmShamLinkHelloInterval_Type()
)
ospfPmShamLinkHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkHelloInterval.setStatus("current")


class _OspfPmShamLinkRtrDeadInterval_Type(Integer32):
    """Custom type ospfPmShamLinkRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmShamLinkRtrDeadInterval_Type.__name__ = "Integer32"
_OspfPmShamLinkRtrDeadInterval_Object = MibTableColumn
ospfPmShamLinkRtrDeadInterval = _OspfPmShamLinkRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 11),
    _OspfPmShamLinkRtrDeadInterval_Type()
)
ospfPmShamLinkRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkRtrDeadInterval.setStatus("current")
_OspfPmShamLinkState_Type = OspfInterfaceStates
_OspfPmShamLinkState_Object = MibTableColumn
ospfPmShamLinkState = _OspfPmShamLinkState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 12),
    _OspfPmShamLinkState_Type()
)
ospfPmShamLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkState.setStatus("current")
_OspfPmShamLinkEvents_Type = Counter32
_OspfPmShamLinkEvents_Object = MibTableColumn
ospfPmShamLinkEvents = _OspfPmShamLinkEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 13),
    _OspfPmShamLinkEvents_Type()
)
ospfPmShamLinkEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkEvents.setStatus("current")


class _OspfPmShamLinkAuthType_Type(OspfAuthTypes):
    """Custom type ospfPmShamLinkAuthType based on OspfAuthTypes"""
    defaultValue = 0


_OspfPmShamLinkAuthType_Type.__name__ = "OspfAuthTypes"
_OspfPmShamLinkAuthType_Object = MibTableColumn
ospfPmShamLinkAuthType = _OspfPmShamLinkAuthType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 14),
    _OspfPmShamLinkAuthType_Type()
)
ospfPmShamLinkAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkAuthType.setStatus("current")


class _OspfPmShamLinkAuthKey_Type(OctetString):
    """Custom type ospfPmShamLinkAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfPmShamLinkAuthKey_Type.__name__ = "OctetString"
_OspfPmShamLinkAuthKey_Object = MibTableColumn
ospfPmShamLinkAuthKey = _OspfPmShamLinkAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 15),
    _OspfPmShamLinkAuthKey_Type()
)
ospfPmShamLinkAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkAuthKey.setStatus("current")
_OspfPmShamLinkLsaCount_Type = Gauge32
_OspfPmShamLinkLsaCount_Object = MibTableColumn
ospfPmShamLinkLsaCount = _OspfPmShamLinkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 16),
    _OspfPmShamLinkLsaCount_Type()
)
ospfPmShamLinkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkLsaCount.setStatus("current")
_OspfPmShamLinkLsaCksumSum_Type = Integer32
_OspfPmShamLinkLsaCksumSum_Object = MibTableColumn
ospfPmShamLinkLsaCksumSum = _OspfPmShamLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 17),
    _OspfPmShamLinkLsaCksumSum_Type()
)
ospfPmShamLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkLsaCksumSum.setStatus("current")


class _OspfPmShamLinkAdminStatus_Type(OspfPmAdminStatus):
    """Custom type ospfPmShamLinkAdminStatus based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmShamLinkAdminStatus_Type.__name__ = "OspfPmAdminStatus"
_OspfPmShamLinkAdminStatus_Object = MibTableColumn
ospfPmShamLinkAdminStatus = _OspfPmShamLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 18),
    _OspfPmShamLinkAdminStatus_Type()
)
ospfPmShamLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkAdminStatus.setStatus("current")
_OspfPmShamLinkOperStatus_Type = OspfPmOperStatus
_OspfPmShamLinkOperStatus_Object = MibTableColumn
ospfPmShamLinkOperStatus = _OspfPmShamLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 19),
    _OspfPmShamLinkOperStatus_Type()
)
ospfPmShamLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkOperStatus.setStatus("current")


class _OspfPmShamLinkTransmitDelay_Type(Integer32):
    """Custom type ospfPmShamLinkTransmitDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OspfPmShamLinkTransmitDelay_Type.__name__ = "Integer32"
_OspfPmShamLinkTransmitDelay_Object = MibTableColumn
ospfPmShamLinkTransmitDelay = _OspfPmShamLinkTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 20),
    _OspfPmShamLinkTransmitDelay_Type()
)
ospfPmShamLinkTransmitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkTransmitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmShamLinkTransmitDelay.setUnits("milliseconds")


class _OspfPmShamLinkIPMaxPacketSize_Type(Integer32):
    """Custom type ospfPmShamLinkIPMaxPacketSize based on Integer32"""
    defaultValue = 576

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfPmShamLinkIPMaxPacketSize_Type.__name__ = "Integer32"
_OspfPmShamLinkIPMaxPacketSize_Object = MibTableColumn
ospfPmShamLinkIPMaxPacketSize = _OspfPmShamLinkIPMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 21),
    _OspfPmShamLinkIPMaxPacketSize_Type()
)
ospfPmShamLinkIPMaxPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkIPMaxPacketSize.setStatus("current")
_OspfPmShamLinkInterfaceName_Type = DisplayString
_OspfPmShamLinkInterfaceName_Object = MibTableColumn
ospfPmShamLinkInterfaceName = _OspfPmShamLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 22),
    _OspfPmShamLinkInterfaceName_Type()
)
ospfPmShamLinkInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkInterfaceName.setStatus("current")


class _OspfPmShamLinkLsaRefreshIntvl_Type(Integer32):
    """Custom type ospfPmShamLinkLsaRefreshIntvl based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_OspfPmShamLinkLsaRefreshIntvl_Type.__name__ = "Integer32"
_OspfPmShamLinkLsaRefreshIntvl_Object = MibTableColumn
ospfPmShamLinkLsaRefreshIntvl = _OspfPmShamLinkLsaRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 23),
    _OspfPmShamLinkLsaRefreshIntvl_Type()
)
ospfPmShamLinkLsaRefreshIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkLsaRefreshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmShamLinkLsaRefreshIntvl.setUnits("seconds")


class _OspfPmShamLinkHelperModePolicy_Type(OspfHelperModePolicy):
    """Custom type ospfPmShamLinkHelperModePolicy based on OspfHelperModePolicy"""
    defaultBinValue = "0"


_OspfPmShamLinkHelperModePolicy_Type.__name__ = "OspfHelperModePolicy"
_OspfPmShamLinkHelperModePolicy_Object = MibTableColumn
ospfPmShamLinkHelperModePolicy = _OspfPmShamLinkHelperModePolicy_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 24),
    _OspfPmShamLinkHelperModePolicy_Type()
)
ospfPmShamLinkHelperModePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkHelperModePolicy.setStatus("current")


class _OspfPmShamLinkMaxGracePeriod_Type(UpToRefreshInterval):
    """Custom type ospfPmShamLinkMaxGracePeriod based on UpToRefreshInterval"""
    defaultValue = 140


_OspfPmShamLinkMaxGracePeriod_Type.__name__ = "UpToRefreshInterval"
_OspfPmShamLinkMaxGracePeriod_Object = MibTableColumn
ospfPmShamLinkMaxGracePeriod = _OspfPmShamLinkMaxGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 25),
    _OspfPmShamLinkMaxGracePeriod_Type()
)
ospfPmShamLinkMaxGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkMaxGracePeriod.setStatus("current")


class _OspfPmShamLinkEnableTeFlooding_Type(TruthValue):
    """Custom type ospfPmShamLinkEnableTeFlooding based on TruthValue"""
    defaultValue = 1


_OspfPmShamLinkEnableTeFlooding_Type.__name__ = "TruthValue"
_OspfPmShamLinkEnableTeFlooding_Object = MibTableColumn
ospfPmShamLinkEnableTeFlooding = _OspfPmShamLinkEnableTeFlooding_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 26),
    _OspfPmShamLinkEnableTeFlooding_Type()
)
ospfPmShamLinkEnableTeFlooding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkEnableTeFlooding.setStatus("current")


class _OspfPmShamLinkAuthUserData_Type(AuthUserDataString):
    """Custom type ospfPmShamLinkAuthUserData based on AuthUserDataString"""
    defaultHexValue = ""


_OspfPmShamLinkAuthUserData_Type.__name__ = "AuthUserDataString"
_OspfPmShamLinkAuthUserData_Object = MibTableColumn
ospfPmShamLinkAuthUserData = _OspfPmShamLinkAuthUserData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 27),
    _OspfPmShamLinkAuthUserData_Type()
)
ospfPmShamLinkAuthUserData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkAuthUserData.setStatus("current")


class _OspfPmShamLinkFastHelloMult_Type(FastHelloMultiplierRange):
    """Custom type ospfPmShamLinkFastHelloMult based on FastHelloMultiplierRange"""
    defaultValue = 5


_OspfPmShamLinkFastHelloMult_Type.__name__ = "FastHelloMultiplierRange"
_OspfPmShamLinkFastHelloMult_Object = MibTableColumn
ospfPmShamLinkFastHelloMult = _OspfPmShamLinkFastHelloMult_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 28),
    _OspfPmShamLinkFastHelloMult_Type()
)
ospfPmShamLinkFastHelloMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkFastHelloMult.setStatus("current")


class _OspfPmShamLinkMtuIgnore_Type(TruthValue):
    """Custom type ospfPmShamLinkMtuIgnore based on TruthValue"""
    defaultValue = 2


_OspfPmShamLinkMtuIgnore_Type.__name__ = "TruthValue"
_OspfPmShamLinkMtuIgnore_Object = MibTableColumn
ospfPmShamLinkMtuIgnore = _OspfPmShamLinkMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 29),
    _OspfPmShamLinkMtuIgnore_Type()
)
ospfPmShamLinkMtuIgnore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkMtuIgnore.setStatus("current")


class _OspfPmShamLinkNmEntity_Type(Integer32):
    """Custom type ospfPmShamLinkNmEntity based on Integer32"""
    defaultValue = 1


_OspfPmShamLinkNmEntity_Type.__name__ = "Integer32"
_OspfPmShamLinkNmEntity_Object = MibTableColumn
ospfPmShamLinkNmEntity = _OspfPmShamLinkNmEntity_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 30),
    _OspfPmShamLinkNmEntity_Type()
)
ospfPmShamLinkNmEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkNmEntity.setStatus("current")


class _OspfPmShamLinkRstStrictLsaChk_Type(TruthValue):
    """Custom type ospfPmShamLinkRstStrictLsaChk based on TruthValue"""
    defaultValue = 1


_OspfPmShamLinkRstStrictLsaChk_Type.__name__ = "TruthValue"
_OspfPmShamLinkRstStrictLsaChk_Object = MibTableColumn
ospfPmShamLinkRstStrictLsaChk = _OspfPmShamLinkRstStrictLsaChk_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 31),
    _OspfPmShamLinkRstStrictLsaChk_Type()
)
ospfPmShamLinkRstStrictLsaChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkRstStrictLsaChk.setStatus("current")
_OspfPmShamLinkIpAddrConflict_Type = OspfShamConflictFlags
_OspfPmShamLinkIpAddrConflict_Object = MibTableColumn
ospfPmShamLinkIpAddrConflict = _OspfPmShamLinkIpAddrConflict_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 32),
    _OspfPmShamLinkIpAddrConflict_Type()
)
ospfPmShamLinkIpAddrConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkIpAddrConflict.setStatus("current")


class _OspfPmShamLinkStatsReset_Type(TruthValue):
    """Custom type ospfPmShamLinkStatsReset based on TruthValue"""
    defaultValue = 2


_OspfPmShamLinkStatsReset_Type.__name__ = "TruthValue"
_OspfPmShamLinkStatsReset_Object = MibTableColumn
ospfPmShamLinkStatsReset = _OspfPmShamLinkStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 33),
    _OspfPmShamLinkStatsReset_Type()
)
ospfPmShamLinkStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsReset.setStatus("current")


class _OspfPmShamLinkGrcLsaRsndTmr_Type(Integer32):
    """Custom type ospfPmShamLinkGrcLsaRsndTmr based on Integer32"""
    defaultValue = 0


_OspfPmShamLinkGrcLsaRsndTmr_Type.__name__ = "Integer32"
_OspfPmShamLinkGrcLsaRsndTmr_Object = MibTableColumn
ospfPmShamLinkGrcLsaRsndTmr = _OspfPmShamLinkGrcLsaRsndTmr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 34),
    _OspfPmShamLinkGrcLsaRsndTmr_Type()
)
ospfPmShamLinkGrcLsaRsndTmr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkGrcLsaRsndTmr.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmShamLinkGrcLsaRsndTmr.setUnits("seconds")


class _OspfPmShamLinkGRDelayTimer_Type(Integer32):
    """Custom type ospfPmShamLinkGRDelayTimer based on Integer32"""
    defaultValue = 10


_OspfPmShamLinkGRDelayTimer_Type.__name__ = "Integer32"
_OspfPmShamLinkGRDelayTimer_Object = MibTableColumn
ospfPmShamLinkGRDelayTimer = _OspfPmShamLinkGRDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 25, 1, 35),
    _OspfPmShamLinkGRDelayTimer_Type()
)
ospfPmShamLinkGRDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmShamLinkGRDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmShamLinkGRDelayTimer.setUnits("seconds")
_OspfPmShamNbrTable_Object = MibTable
ospfPmShamNbrTable = _OspfPmShamNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26)
)
if mibBuilder.loadTexts:
    ospfPmShamNbrTable.setStatus("current")
_OspfPmShamNbrEntry_Object = MibTableRow
ospfPmShamNbrEntry = _OspfPmShamNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1)
)
ospfPmShamNbrEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmShamNbrApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmShamNbrAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmShamNbrLocalIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmShamNbrRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    ospfPmShamNbrEntry.setStatus("current")
_OspfPmShamNbrApplIndex_Type = OspfPmIndex
_OspfPmShamNbrApplIndex_Object = MibTableColumn
ospfPmShamNbrApplIndex = _OspfPmShamNbrApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 1),
    _OspfPmShamNbrApplIndex_Type()
)
ospfPmShamNbrApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamNbrApplIndex.setStatus("current")
_OspfPmShamNbrAreaId_Type = AreaID
_OspfPmShamNbrAreaId_Object = MibTableColumn
ospfPmShamNbrAreaId = _OspfPmShamNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 2),
    _OspfPmShamNbrAreaId_Type()
)
ospfPmShamNbrAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamNbrAreaId.setStatus("current")
_OspfPmShamNbrLocalIpAddr_Type = IpAddress
_OspfPmShamNbrLocalIpAddr_Object = MibTableColumn
ospfPmShamNbrLocalIpAddr = _OspfPmShamNbrLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 3),
    _OspfPmShamNbrLocalIpAddr_Type()
)
ospfPmShamNbrLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamNbrLocalIpAddr.setStatus("current")
_OspfPmShamNbrRemoteIpAddr_Type = IpAddress
_OspfPmShamNbrRemoteIpAddr_Object = MibTableColumn
ospfPmShamNbrRemoteIpAddr = _OspfPmShamNbrRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 4),
    _OspfPmShamNbrRemoteIpAddr_Type()
)
ospfPmShamNbrRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamNbrRemoteIpAddr.setStatus("current")
_OspfPmShamNbrRouterId_Type = RouterID
_OspfPmShamNbrRouterId_Object = MibTableColumn
ospfPmShamNbrRouterId = _OspfPmShamNbrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 5),
    _OspfPmShamNbrRouterId_Type()
)
ospfPmShamNbrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrRouterId.setStatus("current")
_OspfPmShamNbrOptions_Type = Integer32
_OspfPmShamNbrOptions_Object = MibTableColumn
ospfPmShamNbrOptions = _OspfPmShamNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 6),
    _OspfPmShamNbrOptions_Type()
)
ospfPmShamNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrOptions.setStatus("current")
_OspfPmShamNbrState_Type = OspfNeighborStates
_OspfPmShamNbrState_Object = MibTableColumn
ospfPmShamNbrState = _OspfPmShamNbrState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 7),
    _OspfPmShamNbrState_Type()
)
ospfPmShamNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrState.setStatus("current")
_OspfPmShamNbrEvents_Type = Counter32
_OspfPmShamNbrEvents_Object = MibTableColumn
ospfPmShamNbrEvents = _OspfPmShamNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 8),
    _OspfPmShamNbrEvents_Type()
)
ospfPmShamNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrEvents.setStatus("current")
_OspfPmShamNbrLsRetransQLen_Type = Gauge32
_OspfPmShamNbrLsRetransQLen_Object = MibTableColumn
ospfPmShamNbrLsRetransQLen = _OspfPmShamNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 9),
    _OspfPmShamNbrLsRetransQLen_Type()
)
ospfPmShamNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrLsRetransQLen.setStatus("current")
_OspfPmShamNbrNumRequests_Type = Unsigned32
_OspfPmShamNbrNumRequests_Object = MibTableColumn
ospfPmShamNbrNumRequests = _OspfPmShamNbrNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 10),
    _OspfPmShamNbrNumRequests_Type()
)
ospfPmShamNbrNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrNumRequests.setStatus("current")
_OspfPmShamNbrDeadTime_Type = PositiveInteger
_OspfPmShamNbrDeadTime_Object = MibTableColumn
ospfPmShamNbrDeadTime = _OspfPmShamNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 11),
    _OspfPmShamNbrDeadTime_Type()
)
ospfPmShamNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrDeadTime.setStatus("current")
_OspfPmShamNbrRestartHelperStatus_Type = OspfRestartHelperStatus
_OspfPmShamNbrRestartHelperStatus_Object = MibTableColumn
ospfPmShamNbrRestartHelperStatus = _OspfPmShamNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 12),
    _OspfPmShamNbrRestartHelperStatus_Type()
)
ospfPmShamNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrRestartHelperStatus.setStatus("current")
_OspfPmShamNbrRestartHelperAge_Type = UpToRefreshInterval
_OspfPmShamNbrRestartHelperAge_Object = MibTableColumn
ospfPmShamNbrRestartHelperAge = _OspfPmShamNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 13),
    _OspfPmShamNbrRestartHelperAge_Type()
)
ospfPmShamNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmShamNbrRestartHelperAge.setUnits("seconds")
_OspfPmShamNbrRestartHelperExit_Type = OspfRestartExitReason
_OspfPmShamNbrRestartHelperExit_Object = MibTableColumn
ospfPmShamNbrRestartHelperExit = _OspfPmShamNbrRestartHelperExit_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 26, 1, 14),
    _OspfPmShamNbrRestartHelperExit_Type()
)
ospfPmShamNbrRestartHelperExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamNbrRestartHelperExit.setStatus("current")
_OspfPmShamLsdbTable_Object = MibTable
ospfPmShamLsdbTable = _OspfPmShamLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27)
)
if mibBuilder.loadTexts:
    ospfPmShamLsdbTable.setStatus("current")
_OspfPmShamLsdbEntry_Object = MibTableRow
ospfPmShamLsdbEntry = _OspfPmShamLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1)
)
ospfPmShamLsdbEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbLocalIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbRemoteIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbLsid"),
    (0, "DC-OSPF-MIB", "ospfPmShamLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfPmShamLsdbEntry.setStatus("current")
_OspfPmShamLsdbApplIndex_Type = OspfPmIndex
_OspfPmShamLsdbApplIndex_Object = MibTableColumn
ospfPmShamLsdbApplIndex = _OspfPmShamLsdbApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 1),
    _OspfPmShamLsdbApplIndex_Type()
)
ospfPmShamLsdbApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbApplIndex.setStatus("current")
_OspfPmShamLsdbAreaId_Type = AreaID
_OspfPmShamLsdbAreaId_Object = MibTableColumn
ospfPmShamLsdbAreaId = _OspfPmShamLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 2),
    _OspfPmShamLsdbAreaId_Type()
)
ospfPmShamLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbAreaId.setStatus("current")
_OspfPmShamLsdbLocalIpAddr_Type = IpAddress
_OspfPmShamLsdbLocalIpAddr_Object = MibTableColumn
ospfPmShamLsdbLocalIpAddr = _OspfPmShamLsdbLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 3),
    _OspfPmShamLsdbLocalIpAddr_Type()
)
ospfPmShamLsdbLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbLocalIpAddr.setStatus("current")
_OspfPmShamLsdbRemoteIpAddr_Type = IpAddress
_OspfPmShamLsdbRemoteIpAddr_Object = MibTableColumn
ospfPmShamLsdbRemoteIpAddr = _OspfPmShamLsdbRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 4),
    _OspfPmShamLsdbRemoteIpAddr_Type()
)
ospfPmShamLsdbRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbRemoteIpAddr.setStatus("current")
_OspfPmShamLsdbType_Type = OspfLinkLsTypes
_OspfPmShamLsdbType_Object = MibTableColumn
ospfPmShamLsdbType = _OspfPmShamLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 5),
    _OspfPmShamLsdbType_Type()
)
ospfPmShamLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbType.setStatus("current")
_OspfPmShamLsdbLsid_Type = IpAddress
_OspfPmShamLsdbLsid_Object = MibTableColumn
ospfPmShamLsdbLsid = _OspfPmShamLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 6),
    _OspfPmShamLsdbLsid_Type()
)
ospfPmShamLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbLsid.setStatus("current")
_OspfPmShamLsdbRouterId_Type = RouterID
_OspfPmShamLsdbRouterId_Object = MibTableColumn
ospfPmShamLsdbRouterId = _OspfPmShamLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 7),
    _OspfPmShamLsdbRouterId_Type()
)
ospfPmShamLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLsdbRouterId.setStatus("current")
_OspfPmShamLsdbSequence_Type = Integer32
_OspfPmShamLsdbSequence_Object = MibTableColumn
ospfPmShamLsdbSequence = _OspfPmShamLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 8),
    _OspfPmShamLsdbSequence_Type()
)
ospfPmShamLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLsdbSequence.setStatus("current")
_OspfPmShamLsdbAge_Type = Integer32
_OspfPmShamLsdbAge_Object = MibTableColumn
ospfPmShamLsdbAge = _OspfPmShamLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 9),
    _OspfPmShamLsdbAge_Type()
)
ospfPmShamLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLsdbAge.setStatus("current")
_OspfPmShamLsdbChecksum_Type = Integer32
_OspfPmShamLsdbChecksum_Object = MibTableColumn
ospfPmShamLsdbChecksum = _OspfPmShamLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 10),
    _OspfPmShamLsdbChecksum_Type()
)
ospfPmShamLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLsdbChecksum.setStatus("current")


class _OspfPmShamLsdbAdvertisement_Type(OctetString):
    """Custom type ospfPmShamLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfPmShamLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfPmShamLsdbAdvertisement_Object = MibTableColumn
ospfPmShamLsdbAdvertisement = _OspfPmShamLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 27, 1, 11),
    _OspfPmShamLsdbAdvertisement_Type()
)
ospfPmShamLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLsdbAdvertisement.setStatus("current")
_OspfPmMultiAreaIfTable_Object = MibTable
ospfPmMultiAreaIfTable = _OspfPmMultiAreaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28)
)
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfTable.setStatus("current")
_OspfPmMultiAreaIfEntry_Object = MibTableRow
ospfPmMultiAreaIfEntry = _OspfPmMultiAreaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1)
)
ospfPmMultiAreaIfEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaIfApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaIfIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaIfAddressLessIf"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaIfAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaIfRemoteAddr"),
)
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfEntry.setStatus("current")
_OspfPmMultiAreaIfApplIndex_Type = OspfPmIndex
_OspfPmMultiAreaIfApplIndex_Object = MibTableColumn
ospfPmMultiAreaIfApplIndex = _OspfPmMultiAreaIfApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 1),
    _OspfPmMultiAreaIfApplIndex_Type()
)
ospfPmMultiAreaIfApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfApplIndex.setStatus("current")
_OspfPmMultiAreaIfIpAddress_Type = IpAddress
_OspfPmMultiAreaIfIpAddress_Object = MibTableColumn
ospfPmMultiAreaIfIpAddress = _OspfPmMultiAreaIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 2),
    _OspfPmMultiAreaIfIpAddress_Type()
)
ospfPmMultiAreaIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfIpAddress.setStatus("current")
_OspfPmMultiAreaIfAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmMultiAreaIfAddressLessIf_Object = MibTableColumn
ospfPmMultiAreaIfAddressLessIf = _OspfPmMultiAreaIfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 3),
    _OspfPmMultiAreaIfAddressLessIf_Type()
)
ospfPmMultiAreaIfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfAddressLessIf.setStatus("current")
_OspfPmMultiAreaIfAreaId_Type = AreaID
_OspfPmMultiAreaIfAreaId_Object = MibTableColumn
ospfPmMultiAreaIfAreaId = _OspfPmMultiAreaIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 4),
    _OspfPmMultiAreaIfAreaId_Type()
)
ospfPmMultiAreaIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfAreaId.setStatus("current")
_OspfPmMultiAreaIfRemoteAddr_Type = IpAddress
_OspfPmMultiAreaIfRemoteAddr_Object = MibTableColumn
ospfPmMultiAreaIfRemoteAddr = _OspfPmMultiAreaIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 5),
    _OspfPmMultiAreaIfRemoteAddr_Type()
)
ospfPmMultiAreaIfRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfRemoteAddr.setStatus("current")
_OspfPmMultiAreaIfStatus_Type = RowStatus
_OspfPmMultiAreaIfStatus_Object = MibTableColumn
ospfPmMultiAreaIfStatus = _OspfPmMultiAreaIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 6),
    _OspfPmMultiAreaIfStatus_Type()
)
ospfPmMultiAreaIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfStatus.setStatus("current")


class _OspfPmMultiAreaIfAdminStat_Type(OspfPmAdminStatus):
    """Custom type ospfPmMultiAreaIfAdminStat based on OspfPmAdminStatus"""
    defaultValue = 1


_OspfPmMultiAreaIfAdminStat_Type.__name__ = "OspfPmAdminStatus"
_OspfPmMultiAreaIfAdminStat_Object = MibTableColumn
ospfPmMultiAreaIfAdminStat = _OspfPmMultiAreaIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 7),
    _OspfPmMultiAreaIfAdminStat_Type()
)
ospfPmMultiAreaIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfAdminStat.setStatus("current")
_OspfPmMultiAreaIfOperStatus_Type = OspfPmOperStatus
_OspfPmMultiAreaIfOperStatus_Object = MibTableColumn
ospfPmMultiAreaIfOperStatus = _OspfPmMultiAreaIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 8),
    _OspfPmMultiAreaIfOperStatus_Type()
)
ospfPmMultiAreaIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfOperStatus.setStatus("current")


class _OspfPmMultiAreaIfState_Type(OspfInterfaceStates):
    """Custom type ospfPmMultiAreaIfState based on OspfInterfaceStates"""
    defaultValue = 1


_OspfPmMultiAreaIfState_Type.__name__ = "OspfInterfaceStates"
_OspfPmMultiAreaIfState_Object = MibTableColumn
ospfPmMultiAreaIfState = _OspfPmMultiAreaIfState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 9),
    _OspfPmMultiAreaIfState_Type()
)
ospfPmMultiAreaIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfState.setStatus("current")
_OspfPmMultiAreaIfEvents_Type = Counter32
_OspfPmMultiAreaIfEvents_Object = MibTableColumn
ospfPmMultiAreaIfEvents = _OspfPmMultiAreaIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 10),
    _OspfPmMultiAreaIfEvents_Type()
)
ospfPmMultiAreaIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfEvents.setStatus("current")


class _OspfPmMultiAreaIfMetricValue_Type(Integer32):
    """Custom type ospfPmMultiAreaIfMetricValue based on Integer32"""
    defaultValue = 1


_OspfPmMultiAreaIfMetricValue_Type.__name__ = "Integer32"
_OspfPmMultiAreaIfMetricValue_Object = MibTableColumn
ospfPmMultiAreaIfMetricValue = _OspfPmMultiAreaIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 11),
    _OspfPmMultiAreaIfMetricValue_Type()
)
ospfPmMultiAreaIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfMetricValue.setStatus("current")


class _OspfPmMultiAreaIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfPmMultiAreaIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfPmMultiAreaIfTransitDelay_Type.__name__ = "UpToMaxAge"
_OspfPmMultiAreaIfTransitDelay_Object = MibTableColumn
ospfPmMultiAreaIfTransitDelay = _OspfPmMultiAreaIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 12),
    _OspfPmMultiAreaIfTransitDelay_Type()
)
ospfPmMultiAreaIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfTransitDelay.setStatus("current")


class _OspfPmMultiAreaIfRetransInt_Type(UpToMaxAge):
    """Custom type ospfPmMultiAreaIfRetransInt based on UpToMaxAge"""
    defaultValue = 5


_OspfPmMultiAreaIfRetransInt_Type.__name__ = "UpToMaxAge"
_OspfPmMultiAreaIfRetransInt_Object = MibTableColumn
ospfPmMultiAreaIfRetransInt = _OspfPmMultiAreaIfRetransInt_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 13),
    _OspfPmMultiAreaIfRetransInt_Type()
)
ospfPmMultiAreaIfRetransInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfRetransInt.setStatus("current")


class _OspfPmMultiAreaIfHelloInt_Type(HelloRange):
    """Custom type ospfPmMultiAreaIfHelloInt based on HelloRange"""
    defaultValue = 10


_OspfPmMultiAreaIfHelloInt_Type.__name__ = "HelloRange"
_OspfPmMultiAreaIfHelloInt_Object = MibTableColumn
ospfPmMultiAreaIfHelloInt = _OspfPmMultiAreaIfHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 14),
    _OspfPmMultiAreaIfHelloInt_Type()
)
ospfPmMultiAreaIfHelloInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfHelloInt.setStatus("current")


class _OspfPmMultiAreaIfRtrDeadInt_Type(PositiveInteger):
    """Custom type ospfPmMultiAreaIfRtrDeadInt based on PositiveInteger"""
    defaultValue = 40


_OspfPmMultiAreaIfRtrDeadInt_Type.__name__ = "PositiveInteger"
_OspfPmMultiAreaIfRtrDeadInt_Object = MibTableColumn
ospfPmMultiAreaIfRtrDeadInt = _OspfPmMultiAreaIfRtrDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 15),
    _OspfPmMultiAreaIfRtrDeadInt_Type()
)
ospfPmMultiAreaIfRtrDeadInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfRtrDeadInt.setStatus("current")


class _OspfPmMultiAreaIfFastHelloMult_Type(FastHelloMultiplierRange):
    """Custom type ospfPmMultiAreaIfFastHelloMult based on FastHelloMultiplierRange"""
    defaultValue = 5


_OspfPmMultiAreaIfFastHelloMult_Type.__name__ = "FastHelloMultiplierRange"
_OspfPmMultiAreaIfFastHelloMult_Object = MibTableColumn
ospfPmMultiAreaIfFastHelloMult = _OspfPmMultiAreaIfFastHelloMult_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 16),
    _OspfPmMultiAreaIfFastHelloMult_Type()
)
ospfPmMultiAreaIfFastHelloMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfFastHelloMult.setStatus("current")


class _OspfPmMultiAreaIfAuthType_Type(OspfAuthTypes):
    """Custom type ospfPmMultiAreaIfAuthType based on OspfAuthTypes"""
    defaultValue = 0


_OspfPmMultiAreaIfAuthType_Type.__name__ = "OspfAuthTypes"
_OspfPmMultiAreaIfAuthType_Object = MibTableColumn
ospfPmMultiAreaIfAuthType = _OspfPmMultiAreaIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 17),
    _OspfPmMultiAreaIfAuthType_Type()
)
ospfPmMultiAreaIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfAuthType.setStatus("current")


class _OspfPmMultiAreaIfAuthKey_Type(OctetString):
    """Custom type ospfPmMultiAreaIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfPmMultiAreaIfAuthKey_Type.__name__ = "OctetString"
_OspfPmMultiAreaIfAuthKey_Object = MibTableColumn
ospfPmMultiAreaIfAuthKey = _OspfPmMultiAreaIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 18),
    _OspfPmMultiAreaIfAuthKey_Type()
)
ospfPmMultiAreaIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfAuthKey.setStatus("current")


class _OspfPmMultiAreaIfAuthUserData_Type(AuthUserDataString):
    """Custom type ospfPmMultiAreaIfAuthUserData based on AuthUserDataString"""
    defaultHexValue = ""


_OspfPmMultiAreaIfAuthUserData_Type.__name__ = "AuthUserDataString"
_OspfPmMultiAreaIfAuthUserData_Object = MibTableColumn
ospfPmMultiAreaIfAuthUserData = _OspfPmMultiAreaIfAuthUserData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 19),
    _OspfPmMultiAreaIfAuthUserData_Type()
)
ospfPmMultiAreaIfAuthUserData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfAuthUserData.setStatus("current")
_OspfPmIfMultiAreaIPMaxPktSize_Type = Integer32
_OspfPmIfMultiAreaIPMaxPktSize_Object = MibTableColumn
ospfPmIfMultiAreaIPMaxPktSize = _OspfPmIfMultiAreaIPMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 20),
    _OspfPmIfMultiAreaIPMaxPktSize_Type()
)
ospfPmIfMultiAreaIPMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfMultiAreaIPMaxPktSize.setStatus("current")


class _OspfPmMultiAreaIfMtuIgnore_Type(TruthValue):
    """Custom type ospfPmMultiAreaIfMtuIgnore based on TruthValue"""
    defaultValue = 2


_OspfPmMultiAreaIfMtuIgnore_Type.__name__ = "TruthValue"
_OspfPmMultiAreaIfMtuIgnore_Object = MibTableColumn
ospfPmMultiAreaIfMtuIgnore = _OspfPmMultiAreaIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 21),
    _OspfPmMultiAreaIfMtuIgnore_Type()
)
ospfPmMultiAreaIfMtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfMtuIgnore.setStatus("current")
_OspfPmMultiAreaIfLsaCount_Type = Gauge32
_OspfPmMultiAreaIfLsaCount_Object = MibTableColumn
ospfPmMultiAreaIfLsaCount = _OspfPmMultiAreaIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 22),
    _OspfPmMultiAreaIfLsaCount_Type()
)
ospfPmMultiAreaIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfLsaCount.setStatus("current")
_OspfPmMultiAreaIfLsaCksumSum_Type = Integer32
_OspfPmMultiAreaIfLsaCksumSum_Object = MibTableColumn
ospfPmMultiAreaIfLsaCksumSum = _OspfPmMultiAreaIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 23),
    _OspfPmMultiAreaIfLsaCksumSum_Type()
)
ospfPmMultiAreaIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfLsaCksumSum.setStatus("current")


class _OspfPmMultiAreaIfTrsmtTmrDelay_Type(Integer32):
    """Custom type ospfPmMultiAreaIfTrsmtTmrDelay based on Integer32"""
    defaultValue = 100


_OspfPmMultiAreaIfTrsmtTmrDelay_Type.__name__ = "Integer32"
_OspfPmMultiAreaIfTrsmtTmrDelay_Object = MibTableColumn
ospfPmMultiAreaIfTrsmtTmrDelay = _OspfPmMultiAreaIfTrsmtTmrDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 24),
    _OspfPmMultiAreaIfTrsmtTmrDelay_Type()
)
ospfPmMultiAreaIfTrsmtTmrDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfTrsmtTmrDelay.setStatus("current")


class _OspfPmMultiAreaIfEnableTeFlood_Type(TruthValue):
    """Custom type ospfPmMultiAreaIfEnableTeFlood based on TruthValue"""
    defaultValue = 1


_OspfPmMultiAreaIfEnableTeFlood_Type.__name__ = "TruthValue"
_OspfPmMultiAreaIfEnableTeFlood_Object = MibTableColumn
ospfPmMultiAreaIfEnableTeFlood = _OspfPmMultiAreaIfEnableTeFlood_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 25),
    _OspfPmMultiAreaIfEnableTeFlood_Type()
)
ospfPmMultiAreaIfEnableTeFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfEnableTeFlood.setStatus("current")


class _OspfPmMultiAreaIfStatsReset_Type(TruthValue):
    """Custom type ospfPmMultiAreaIfStatsReset based on TruthValue"""
    defaultValue = 2


_OspfPmMultiAreaIfStatsReset_Type.__name__ = "TruthValue"
_OspfPmMultiAreaIfStatsReset_Object = MibTableColumn
ospfPmMultiAreaIfStatsReset = _OspfPmMultiAreaIfStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 26),
    _OspfPmMultiAreaIfStatsReset_Type()
)
ospfPmMultiAreaIfStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaIfStatsReset.setStatus("current")


class _OspfPmMultiAreaGraceLsaRsndTmr_Type(Integer32):
    """Custom type ospfPmMultiAreaGraceLsaRsndTmr based on Integer32"""
    defaultValue = 0


_OspfPmMultiAreaGraceLsaRsndTmr_Type.__name__ = "Integer32"
_OspfPmMultiAreaGraceLsaRsndTmr_Object = MibTableColumn
ospfPmMultiAreaGraceLsaRsndTmr = _OspfPmMultiAreaGraceLsaRsndTmr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 27),
    _OspfPmMultiAreaGraceLsaRsndTmr_Type()
)
ospfPmMultiAreaGraceLsaRsndTmr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaGraceLsaRsndTmr.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmMultiAreaGraceLsaRsndTmr.setUnits("seconds")


class _OspfPmMultiAreaGRDelayTimer_Type(Integer32):
    """Custom type ospfPmMultiAreaGRDelayTimer based on Integer32"""
    defaultValue = 10


_OspfPmMultiAreaGRDelayTimer_Type.__name__ = "Integer32"
_OspfPmMultiAreaGRDelayTimer_Object = MibTableColumn
ospfPmMultiAreaGRDelayTimer = _OspfPmMultiAreaGRDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 28, 1, 28),
    _OspfPmMultiAreaGRDelayTimer_Type()
)
ospfPmMultiAreaGRDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfPmMultiAreaGRDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmMultiAreaGRDelayTimer.setUnits("seconds")
_OspfPmMultiAreaNbrTable_Object = MibTable
ospfPmMultiAreaNbrTable = _OspfPmMultiAreaNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29)
)
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrTable.setStatus("current")
_OspfPmMultiAreaNbrEntry_Object = MibTableRow
ospfPmMultiAreaNbrEntry = _OspfPmMultiAreaNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1)
)
ospfPmMultiAreaNbrEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaNbrApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaNbrIfIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaNbrAddrLessIf"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaNbrAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaNbrRemoteAddr"),
)
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrEntry.setStatus("current")
_OspfPmMultiAreaNbrApplIndex_Type = OspfPmIndex
_OspfPmMultiAreaNbrApplIndex_Object = MibTableColumn
ospfPmMultiAreaNbrApplIndex = _OspfPmMultiAreaNbrApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 1),
    _OspfPmMultiAreaNbrApplIndex_Type()
)
ospfPmMultiAreaNbrApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrApplIndex.setStatus("current")
_OspfPmMultiAreaNbrIfIpAddr_Type = IpAddress
_OspfPmMultiAreaNbrIfIpAddr_Object = MibTableColumn
ospfPmMultiAreaNbrIfIpAddr = _OspfPmMultiAreaNbrIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 2),
    _OspfPmMultiAreaNbrIfIpAddr_Type()
)
ospfPmMultiAreaNbrIfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrIfIpAddr.setStatus("current")
_OspfPmMultiAreaNbrAddrLessIf_Type = InterfaceIndexOrZero
_OspfPmMultiAreaNbrAddrLessIf_Object = MibTableColumn
ospfPmMultiAreaNbrAddrLessIf = _OspfPmMultiAreaNbrAddrLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 3),
    _OspfPmMultiAreaNbrAddrLessIf_Type()
)
ospfPmMultiAreaNbrAddrLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrAddrLessIf.setStatus("current")
_OspfPmMultiAreaNbrAreaId_Type = AreaID
_OspfPmMultiAreaNbrAreaId_Object = MibTableColumn
ospfPmMultiAreaNbrAreaId = _OspfPmMultiAreaNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 4),
    _OspfPmMultiAreaNbrAreaId_Type()
)
ospfPmMultiAreaNbrAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrAreaId.setStatus("current")
_OspfPmMultiAreaNbrRemoteAddr_Type = IpAddress
_OspfPmMultiAreaNbrRemoteAddr_Object = MibTableColumn
ospfPmMultiAreaNbrRemoteAddr = _OspfPmMultiAreaNbrRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 5),
    _OspfPmMultiAreaNbrRemoteAddr_Type()
)
ospfPmMultiAreaNbrRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrRemoteAddr.setStatus("current")
_OspfPmMultiAreaNbrSrcIpAddr_Type = IpAddress
_OspfPmMultiAreaNbrSrcIpAddr_Object = MibTableColumn
ospfPmMultiAreaNbrSrcIpAddr = _OspfPmMultiAreaNbrSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 6),
    _OspfPmMultiAreaNbrSrcIpAddr_Type()
)
ospfPmMultiAreaNbrSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrSrcIpAddr.setStatus("current")


class _OspfPmMultiAreaNbrRtrId_Type(RouterID):
    """Custom type ospfPmMultiAreaNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_OspfPmMultiAreaNbrRtrId_Type.__name__ = "RouterID"
_OspfPmMultiAreaNbrRtrId_Object = MibTableColumn
ospfPmMultiAreaNbrRtrId = _OspfPmMultiAreaNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 7),
    _OspfPmMultiAreaNbrRtrId_Type()
)
ospfPmMultiAreaNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrRtrId.setStatus("current")


class _OspfPmMultiAreaNbrOptions_Type(Integer32):
    """Custom type ospfPmMultiAreaNbrOptions based on Integer32"""
    defaultValue = 0


_OspfPmMultiAreaNbrOptions_Type.__name__ = "Integer32"
_OspfPmMultiAreaNbrOptions_Object = MibTableColumn
ospfPmMultiAreaNbrOptions = _OspfPmMultiAreaNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 8),
    _OspfPmMultiAreaNbrOptions_Type()
)
ospfPmMultiAreaNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrOptions.setStatus("current")
_OspfPmMultiAreaNbrState_Type = OspfNeighborStates
_OspfPmMultiAreaNbrState_Object = MibTableColumn
ospfPmMultiAreaNbrState = _OspfPmMultiAreaNbrState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 9),
    _OspfPmMultiAreaNbrState_Type()
)
ospfPmMultiAreaNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrState.setStatus("current")
_OspfPmMultiAreaNbrEvents_Type = Counter32
_OspfPmMultiAreaNbrEvents_Object = MibTableColumn
ospfPmMultiAreaNbrEvents = _OspfPmMultiAreaNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 10),
    _OspfPmMultiAreaNbrEvents_Type()
)
ospfPmMultiAreaNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrEvents.setStatus("current")
_OspfPmMultiAreaNbrLsRetransQLen_Type = Gauge32
_OspfPmMultiAreaNbrLsRetransQLen_Object = MibTableColumn
ospfPmMultiAreaNbrLsRetransQLen = _OspfPmMultiAreaNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 11),
    _OspfPmMultiAreaNbrLsRetransQLen_Type()
)
ospfPmMultiAreaNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrLsRetransQLen.setStatus("current")


class _OspfPmMultiAreaNbrNumRequests_Type(Unsigned32):
    """Custom type ospfPmMultiAreaNbrNumRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OspfPmMultiAreaNbrNumRequests_Type.__name__ = "Unsigned32"
_OspfPmMultiAreaNbrNumRequests_Object = MibTableColumn
ospfPmMultiAreaNbrNumRequests = _OspfPmMultiAreaNbrNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 12),
    _OspfPmMultiAreaNbrNumRequests_Type()
)
ospfPmMultiAreaNbrNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrNumRequests.setStatus("current")
_OspfPmMultiAreaNbrDeadTime_Type = PositiveInteger
_OspfPmMultiAreaNbrDeadTime_Object = MibTableColumn
ospfPmMultiAreaNbrDeadTime = _OspfPmMultiAreaNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 13),
    _OspfPmMultiAreaNbrDeadTime_Type()
)
ospfPmMultiAreaNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrDeadTime.setStatus("current")
_OspfPmMultiAreaNbrRstrtHelpSts_Type = OspfRestartHelperStatus
_OspfPmMultiAreaNbrRstrtHelpSts_Object = MibTableColumn
ospfPmMultiAreaNbrRstrtHelpSts = _OspfPmMultiAreaNbrRstrtHelpSts_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 14),
    _OspfPmMultiAreaNbrRstrtHelpSts_Type()
)
ospfPmMultiAreaNbrRstrtHelpSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrRstrtHelpSts.setStatus("current")
_OspfPmMultiAreaNbrRstrtHelpAge_Type = UpToRefreshInterval
_OspfPmMultiAreaNbrRstrtHelpAge_Object = MibTableColumn
ospfPmMultiAreaNbrRstrtHelpAge = _OspfPmMultiAreaNbrRstrtHelpAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 15),
    _OspfPmMultiAreaNbrRstrtHelpAge_Type()
)
ospfPmMultiAreaNbrRstrtHelpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrRstrtHelpAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrRstrtHelpAge.setUnits("seconds")
_OspfPmMultiAreaNbrRstrtHelpExitR_Type = OspfRestartExitReason
_OspfPmMultiAreaNbrRstrtHelpExitR_Object = MibTableColumn
ospfPmMultiAreaNbrRstrtHelpExitR = _OspfPmMultiAreaNbrRstrtHelpExitR_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 29, 1, 16),
    _OspfPmMultiAreaNbrRstrtHelpExitR_Type()
)
ospfPmMultiAreaNbrRstrtHelpExitR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaNbrRstrtHelpExitR.setStatus("current")
_OspfPmMultiAreaLclLsdbTable_Object = MibTable
ospfPmMultiAreaLclLsdbTable = _OspfPmMultiAreaLclLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30)
)
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbTable.setStatus("current")
_OspfPmMultiAreaLclLsdbEntry_Object = MibTableRow
ospfPmMultiAreaLclLsdbEntry = _OspfPmMultiAreaLclLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1)
)
ospfPmMultiAreaLclLsdbEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbAddrLssIf"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbRemAddr"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbType"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbLsid"),
    (0, "DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbRtrId"),
)
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbEntry.setStatus("current")
_OspfPmMultiAreaLclLsdbApplIndex_Type = OspfPmIndex
_OspfPmMultiAreaLclLsdbApplIndex_Object = MibTableColumn
ospfPmMultiAreaLclLsdbApplIndex = _OspfPmMultiAreaLclLsdbApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 1),
    _OspfPmMultiAreaLclLsdbApplIndex_Type()
)
ospfPmMultiAreaLclLsdbApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbApplIndex.setStatus("current")
_OspfPmMultiAreaLclLsdbIpAddr_Type = IpAddress
_OspfPmMultiAreaLclLsdbIpAddr_Object = MibTableColumn
ospfPmMultiAreaLclLsdbIpAddr = _OspfPmMultiAreaLclLsdbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 2),
    _OspfPmMultiAreaLclLsdbIpAddr_Type()
)
ospfPmMultiAreaLclLsdbIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbIpAddr.setStatus("current")
_OspfPmMultiAreaLclLsdbAddrLssIf_Type = InterfaceIndexOrZero
_OspfPmMultiAreaLclLsdbAddrLssIf_Object = MibTableColumn
ospfPmMultiAreaLclLsdbAddrLssIf = _OspfPmMultiAreaLclLsdbAddrLssIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 3),
    _OspfPmMultiAreaLclLsdbAddrLssIf_Type()
)
ospfPmMultiAreaLclLsdbAddrLssIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbAddrLssIf.setStatus("current")
_OspfPmMultiAreaLclLsdbAreaId_Type = AreaID
_OspfPmMultiAreaLclLsdbAreaId_Object = MibTableColumn
ospfPmMultiAreaLclLsdbAreaId = _OspfPmMultiAreaLclLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 4),
    _OspfPmMultiAreaLclLsdbAreaId_Type()
)
ospfPmMultiAreaLclLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbAreaId.setStatus("current")
_OspfPmMultiAreaLclLsdbRemAddr_Type = IpAddress
_OspfPmMultiAreaLclLsdbRemAddr_Object = MibTableColumn
ospfPmMultiAreaLclLsdbRemAddr = _OspfPmMultiAreaLclLsdbRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 5),
    _OspfPmMultiAreaLclLsdbRemAddr_Type()
)
ospfPmMultiAreaLclLsdbRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbRemAddr.setStatus("current")
_OspfPmMultiAreaLclLsdbType_Type = OspfLinkLsTypes
_OspfPmMultiAreaLclLsdbType_Object = MibTableColumn
ospfPmMultiAreaLclLsdbType = _OspfPmMultiAreaLclLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 6),
    _OspfPmMultiAreaLclLsdbType_Type()
)
ospfPmMultiAreaLclLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbType.setStatus("current")
_OspfPmMultiAreaLclLsdbLsid_Type = IpAddress
_OspfPmMultiAreaLclLsdbLsid_Object = MibTableColumn
ospfPmMultiAreaLclLsdbLsid = _OspfPmMultiAreaLclLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 7),
    _OspfPmMultiAreaLclLsdbLsid_Type()
)
ospfPmMultiAreaLclLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbLsid.setStatus("current")
_OspfPmMultiAreaLclLsdbRtrId_Type = RouterID
_OspfPmMultiAreaLclLsdbRtrId_Object = MibTableColumn
ospfPmMultiAreaLclLsdbRtrId = _OspfPmMultiAreaLclLsdbRtrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 8),
    _OspfPmMultiAreaLclLsdbRtrId_Type()
)
ospfPmMultiAreaLclLsdbRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbRtrId.setStatus("current")
_OspfPmMultiAreaLclLsdbSequence_Type = Integer32
_OspfPmMultiAreaLclLsdbSequence_Object = MibTableColumn
ospfPmMultiAreaLclLsdbSequence = _OspfPmMultiAreaLclLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 9),
    _OspfPmMultiAreaLclLsdbSequence_Type()
)
ospfPmMultiAreaLclLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbSequence.setStatus("current")
_OspfPmMultiAreaLclLsdbAge_Type = Integer32
_OspfPmMultiAreaLclLsdbAge_Object = MibTableColumn
ospfPmMultiAreaLclLsdbAge = _OspfPmMultiAreaLclLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 10),
    _OspfPmMultiAreaLclLsdbAge_Type()
)
ospfPmMultiAreaLclLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbAge.setStatus("current")
_OspfPmMultiAreaLclLsdbChecksum_Type = Integer32
_OspfPmMultiAreaLclLsdbChecksum_Object = MibTableColumn
ospfPmMultiAreaLclLsdbChecksum = _OspfPmMultiAreaLclLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 11),
    _OspfPmMultiAreaLclLsdbChecksum_Type()
)
ospfPmMultiAreaLclLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbChecksum.setStatus("current")


class _OspfPmMultiAreaLclLsdbAdvert_Type(OctetString):
    """Custom type ospfPmMultiAreaLclLsdbAdvert based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfPmMultiAreaLclLsdbAdvert_Type.__name__ = "OctetString"
_OspfPmMultiAreaLclLsdbAdvert_Object = MibTableColumn
ospfPmMultiAreaLclLsdbAdvert = _OspfPmMultiAreaLclLsdbAdvert_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 30, 1, 12),
    _OspfPmMultiAreaLclLsdbAdvert_Type()
)
ospfPmMultiAreaLclLsdbAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMultiAreaLclLsdbAdvert.setStatus("current")
_OspfPmEntStatsTable_Object = MibTable
ospfPmEntStatsTable = _OspfPmEntStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 31)
)
if mibBuilder.loadTexts:
    ospfPmEntStatsTable.setStatus("current")
_OspfPmEntStatsEntry_Object = MibTableRow
ospfPmEntStatsEntry = _OspfPmEntStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 31, 1)
)
ospfPmEntStatsEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmEntStatsIndex"),
)
if mibBuilder.loadTexts:
    ospfPmEntStatsEntry.setStatus("current")
_OspfPmEntStatsIndex_Type = OspfPmIndex
_OspfPmEntStatsIndex_Object = MibTableColumn
ospfPmEntStatsIndex = _OspfPmEntStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 31, 1, 1),
    _OspfPmEntStatsIndex_Type()
)
ospfPmEntStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmEntStatsIndex.setStatus("current")
_OspfPmEntStatsNoIf_Type = Counter32
_OspfPmEntStatsNoIf_Object = MibTableColumn
ospfPmEntStatsNoIf = _OspfPmEntStatsNoIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 31, 1, 2),
    _OspfPmEntStatsNoIf_Type()
)
ospfPmEntStatsNoIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntStatsNoIf.setStatus("current")
_OspfPmEntStatsNoVirtLink_Type = Counter32
_OspfPmEntStatsNoVirtLink_Object = MibTableColumn
ospfPmEntStatsNoVirtLink = _OspfPmEntStatsNoVirtLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 31, 1, 3),
    _OspfPmEntStatsNoVirtLink_Type()
)
ospfPmEntStatsNoVirtLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntStatsNoVirtLink.setStatus("current")
_OspfPmEntStatsBadPacket_Type = Counter32
_OspfPmEntStatsBadPacket_Object = MibTableColumn
ospfPmEntStatsBadPacket = _OspfPmEntStatsBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 31, 1, 4),
    _OspfPmEntStatsBadPacket_Type()
)
ospfPmEntStatsBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmEntStatsBadPacket.setStatus("current")
_OspfPmIfStatsTable_Object = MibTable
ospfPmIfStatsTable = _OspfPmIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32)
)
if mibBuilder.loadTexts:
    ospfPmIfStatsTable.setStatus("current")
_OspfPmIfStatsEntry_Object = MibTableRow
ospfPmIfStatsEntry = _OspfPmIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1)
)
ospfPmIfStatsEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmIfStatsApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmIfStatsIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmIfStatsAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfPmIfStatsEntry.setStatus("current")
_OspfPmIfStatsApplIndex_Type = OspfPmIndex
_OspfPmIfStatsApplIndex_Object = MibTableColumn
ospfPmIfStatsApplIndex = _OspfPmIfStatsApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 1),
    _OspfPmIfStatsApplIndex_Type()
)
ospfPmIfStatsApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfStatsApplIndex.setStatus("current")
_OspfPmIfStatsIpAddress_Type = IpAddress
_OspfPmIfStatsIpAddress_Object = MibTableColumn
ospfPmIfStatsIpAddress = _OspfPmIfStatsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 2),
    _OspfPmIfStatsIpAddress_Type()
)
ospfPmIfStatsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfStatsIpAddress.setStatus("current")
_OspfPmIfStatsAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmIfStatsAddressLessIf_Object = MibTableColumn
ospfPmIfStatsAddressLessIf = _OspfPmIfStatsAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 3),
    _OspfPmIfStatsAddressLessIf_Type()
)
ospfPmIfStatsAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmIfStatsAddressLessIf.setStatus("current")
_OspfPmIfStatsRxInvalid_Type = Counter32
_OspfPmIfStatsRxInvalid_Object = MibTableColumn
ospfPmIfStatsRxInvalid = _OspfPmIfStatsRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 4),
    _OspfPmIfStatsRxInvalid_Type()
)
ospfPmIfStatsRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxInvalid.setStatus("current")
_OspfPmIfStatsRxInvalidByte_Type = Counter32
_OspfPmIfStatsRxInvalidByte_Object = MibTableColumn
ospfPmIfStatsRxInvalidByte = _OspfPmIfStatsRxInvalidByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 5),
    _OspfPmIfStatsRxInvalidByte_Type()
)
ospfPmIfStatsRxInvalidByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxInvalidByte.setStatus("current")
_OspfPmIfStatsRxHello_Type = Counter32
_OspfPmIfStatsRxHello_Object = MibTableColumn
ospfPmIfStatsRxHello = _OspfPmIfStatsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 6),
    _OspfPmIfStatsRxHello_Type()
)
ospfPmIfStatsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxHello.setStatus("current")
_OspfPmIfStatsRxHelloByte_Type = Counter32
_OspfPmIfStatsRxHelloByte_Object = MibTableColumn
ospfPmIfStatsRxHelloByte = _OspfPmIfStatsRxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 7),
    _OspfPmIfStatsRxHelloByte_Type()
)
ospfPmIfStatsRxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxHelloByte.setStatus("current")
_OspfPmIfStatsRxDbDes_Type = Counter32
_OspfPmIfStatsRxDbDes_Object = MibTableColumn
ospfPmIfStatsRxDbDes = _OspfPmIfStatsRxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 8),
    _OspfPmIfStatsRxDbDes_Type()
)
ospfPmIfStatsRxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxDbDes.setStatus("current")
_OspfPmIfStatsRxDbDesByte_Type = Counter32
_OspfPmIfStatsRxDbDesByte_Object = MibTableColumn
ospfPmIfStatsRxDbDesByte = _OspfPmIfStatsRxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 9),
    _OspfPmIfStatsRxDbDesByte_Type()
)
ospfPmIfStatsRxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxDbDesByte.setStatus("current")
_OspfPmIfStatsRxLsReq_Type = Counter32
_OspfPmIfStatsRxLsReq_Object = MibTableColumn
ospfPmIfStatsRxLsReq = _OspfPmIfStatsRxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 10),
    _OspfPmIfStatsRxLsReq_Type()
)
ospfPmIfStatsRxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxLsReq.setStatus("current")
_OspfPmIfStatsRxLsReqByte_Type = Counter32
_OspfPmIfStatsRxLsReqByte_Object = MibTableColumn
ospfPmIfStatsRxLsReqByte = _OspfPmIfStatsRxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 11),
    _OspfPmIfStatsRxLsReqByte_Type()
)
ospfPmIfStatsRxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxLsReqByte.setStatus("current")
_OspfPmIfStatsRxLsUpd_Type = Counter32
_OspfPmIfStatsRxLsUpd_Object = MibTableColumn
ospfPmIfStatsRxLsUpd = _OspfPmIfStatsRxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 12),
    _OspfPmIfStatsRxLsUpd_Type()
)
ospfPmIfStatsRxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxLsUpd.setStatus("current")
_OspfPmIfStatsRxLsUpdByte_Type = Counter32
_OspfPmIfStatsRxLsUpdByte_Object = MibTableColumn
ospfPmIfStatsRxLsUpdByte = _OspfPmIfStatsRxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 13),
    _OspfPmIfStatsRxLsUpdByte_Type()
)
ospfPmIfStatsRxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxLsUpdByte.setStatus("current")
_OspfPmIfStatsRxLsAck_Type = Counter32
_OspfPmIfStatsRxLsAck_Object = MibTableColumn
ospfPmIfStatsRxLsAck = _OspfPmIfStatsRxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 14),
    _OspfPmIfStatsRxLsAck_Type()
)
ospfPmIfStatsRxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxLsAck.setStatus("current")
_OspfPmIfStatsRxLsAckByte_Type = Counter32
_OspfPmIfStatsRxLsAckByte_Object = MibTableColumn
ospfPmIfStatsRxLsAckByte = _OspfPmIfStatsRxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 15),
    _OspfPmIfStatsRxLsAckByte_Type()
)
ospfPmIfStatsRxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsRxLsAckByte.setStatus("current")
_OspfPmIfStatsTxFailed_Type = Counter32
_OspfPmIfStatsTxFailed_Object = MibTableColumn
ospfPmIfStatsTxFailed = _OspfPmIfStatsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 16),
    _OspfPmIfStatsTxFailed_Type()
)
ospfPmIfStatsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxFailed.setStatus("current")
_OspfPmIfStatsTxFailedByte_Type = Counter32
_OspfPmIfStatsTxFailedByte_Object = MibTableColumn
ospfPmIfStatsTxFailedByte = _OspfPmIfStatsTxFailedByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 17),
    _OspfPmIfStatsTxFailedByte_Type()
)
ospfPmIfStatsTxFailedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxFailedByte.setStatus("current")
_OspfPmIfStatsTxHello_Type = Counter32
_OspfPmIfStatsTxHello_Object = MibTableColumn
ospfPmIfStatsTxHello = _OspfPmIfStatsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 18),
    _OspfPmIfStatsTxHello_Type()
)
ospfPmIfStatsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxHello.setStatus("current")
_OspfPmIfStatsTxHelloByte_Type = Counter32
_OspfPmIfStatsTxHelloByte_Object = MibTableColumn
ospfPmIfStatsTxHelloByte = _OspfPmIfStatsTxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 19),
    _OspfPmIfStatsTxHelloByte_Type()
)
ospfPmIfStatsTxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxHelloByte.setStatus("current")
_OspfPmIfStatsTxDbDes_Type = Counter32
_OspfPmIfStatsTxDbDes_Object = MibTableColumn
ospfPmIfStatsTxDbDes = _OspfPmIfStatsTxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 20),
    _OspfPmIfStatsTxDbDes_Type()
)
ospfPmIfStatsTxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxDbDes.setStatus("current")
_OspfPmIfStatsTxDbDesByte_Type = Counter32
_OspfPmIfStatsTxDbDesByte_Object = MibTableColumn
ospfPmIfStatsTxDbDesByte = _OspfPmIfStatsTxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 21),
    _OspfPmIfStatsTxDbDesByte_Type()
)
ospfPmIfStatsTxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxDbDesByte.setStatus("current")
_OspfPmIfStatsTxLsReq_Type = Counter32
_OspfPmIfStatsTxLsReq_Object = MibTableColumn
ospfPmIfStatsTxLsReq = _OspfPmIfStatsTxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 22),
    _OspfPmIfStatsTxLsReq_Type()
)
ospfPmIfStatsTxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxLsReq.setStatus("current")
_OspfPmIfStatsTxLsReqByte_Type = Counter32
_OspfPmIfStatsTxLsReqByte_Object = MibTableColumn
ospfPmIfStatsTxLsReqByte = _OspfPmIfStatsTxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 23),
    _OspfPmIfStatsTxLsReqByte_Type()
)
ospfPmIfStatsTxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxLsReqByte.setStatus("current")
_OspfPmIfStatsTxLsUpd_Type = Counter32
_OspfPmIfStatsTxLsUpd_Object = MibTableColumn
ospfPmIfStatsTxLsUpd = _OspfPmIfStatsTxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 24),
    _OspfPmIfStatsTxLsUpd_Type()
)
ospfPmIfStatsTxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxLsUpd.setStatus("current")
_OspfPmIfStatsTxLsUpdByte_Type = Counter32
_OspfPmIfStatsTxLsUpdByte_Object = MibTableColumn
ospfPmIfStatsTxLsUpdByte = _OspfPmIfStatsTxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 25),
    _OspfPmIfStatsTxLsUpdByte_Type()
)
ospfPmIfStatsTxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxLsUpdByte.setStatus("current")
_OspfPmIfStatsTxLsAck_Type = Counter32
_OspfPmIfStatsTxLsAck_Object = MibTableColumn
ospfPmIfStatsTxLsAck = _OspfPmIfStatsTxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 26),
    _OspfPmIfStatsTxLsAck_Type()
)
ospfPmIfStatsTxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxLsAck.setStatus("current")
_OspfPmIfStatsTxLsAckByte_Type = Counter32
_OspfPmIfStatsTxLsAckByte_Object = MibTableColumn
ospfPmIfStatsTxLsAckByte = _OspfPmIfStatsTxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 27),
    _OspfPmIfStatsTxLsAckByte_Type()
)
ospfPmIfStatsTxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsTxLsAckByte.setStatus("current")
_OspfPmIfStatsLength_Type = Counter32
_OspfPmIfStatsLength_Object = MibTableColumn
ospfPmIfStatsLength = _OspfPmIfStatsLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 28),
    _OspfPmIfStatsLength_Type()
)
ospfPmIfStatsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsLength.setStatus("current")
_OspfPmIfStatsCksum_Type = Counter32
_OspfPmIfStatsCksum_Object = MibTableColumn
ospfPmIfStatsCksum = _OspfPmIfStatsCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 29),
    _OspfPmIfStatsCksum_Type()
)
ospfPmIfStatsCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsCksum.setStatus("current")
_OspfPmIfStatsVersion_Type = Counter32
_OspfPmIfStatsVersion_Object = MibTableColumn
ospfPmIfStatsVersion = _OspfPmIfStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 30),
    _OspfPmIfStatsVersion_Type()
)
ospfPmIfStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsVersion.setStatus("current")
_OspfPmIfStatsBadSrc_Type = Counter32
_OspfPmIfStatsBadSrc_Object = MibTableColumn
ospfPmIfStatsBadSrc = _OspfPmIfStatsBadSrc_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 31),
    _OspfPmIfStatsBadSrc_Type()
)
ospfPmIfStatsBadSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsBadSrc.setStatus("current")
_OspfPmIfStatsAreaMismatch_Type = Counter32
_OspfPmIfStatsAreaMismatch_Object = MibTableColumn
ospfPmIfStatsAreaMismatch = _OspfPmIfStatsAreaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 32),
    _OspfPmIfStatsAreaMismatch_Type()
)
ospfPmIfStatsAreaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsAreaMismatch.setStatus("current")
_OspfPmIfStatsSelfOrig_Type = Counter32
_OspfPmIfStatsSelfOrig_Object = MibTableColumn
ospfPmIfStatsSelfOrig = _OspfPmIfStatsSelfOrig_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 33),
    _OspfPmIfStatsSelfOrig_Type()
)
ospfPmIfStatsSelfOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsSelfOrig.setStatus("current")
_OspfPmIfStatsDupeId_Type = Counter32
_OspfPmIfStatsDupeId_Object = MibTableColumn
ospfPmIfStatsDupeId = _OspfPmIfStatsDupeId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 34),
    _OspfPmIfStatsDupeId_Type()
)
ospfPmIfStatsDupeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsDupeId.setStatus("current")
_OspfPmIfStatsHello_Type = Counter32
_OspfPmIfStatsHello_Object = MibTableColumn
ospfPmIfStatsHello = _OspfPmIfStatsHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 35),
    _OspfPmIfStatsHello_Type()
)
ospfPmIfStatsHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsHello.setStatus("current")
_OspfPmIfStatsMtuMismatch_Type = Counter32
_OspfPmIfStatsMtuMismatch_Object = MibTableColumn
ospfPmIfStatsMtuMismatch = _OspfPmIfStatsMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 36),
    _OspfPmIfStatsMtuMismatch_Type()
)
ospfPmIfStatsMtuMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsMtuMismatch.setStatus("current")
_OspfPmIfStatsNbrIgnored_Type = Counter32
_OspfPmIfStatsNbrIgnored_Object = MibTableColumn
ospfPmIfStatsNbrIgnored = _OspfPmIfStatsNbrIgnored_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 37),
    _OspfPmIfStatsNbrIgnored_Type()
)
ospfPmIfStatsNbrIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsNbrIgnored.setStatus("current")
_OspfPmIfStatsAuth_Type = Counter32
_OspfPmIfStatsAuth_Object = MibTableColumn
ospfPmIfStatsAuth = _OspfPmIfStatsAuth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 38),
    _OspfPmIfStatsAuth_Type()
)
ospfPmIfStatsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsAuth.setStatus("current")
_OspfPmIfStatsWrongProto_Type = Counter32
_OspfPmIfStatsWrongProto_Object = MibTableColumn
ospfPmIfStatsWrongProto = _OspfPmIfStatsWrongProto_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 39),
    _OspfPmIfStatsWrongProto_Type()
)
ospfPmIfStatsWrongProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsWrongProto.setStatus("current")
_OspfPmIfStatsResourceErr_Type = Counter32
_OspfPmIfStatsResourceErr_Object = MibTableColumn
ospfPmIfStatsResourceErr = _OspfPmIfStatsResourceErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 40),
    _OspfPmIfStatsResourceErr_Type()
)
ospfPmIfStatsResourceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsResourceErr.setStatus("current")
_OspfPmIfStatsVirtMaIfClash_Type = Counter32
_OspfPmIfStatsVirtMaIfClash_Object = MibTableColumn
ospfPmIfStatsVirtMaIfClash = _OspfPmIfStatsVirtMaIfClash_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 41),
    _OspfPmIfStatsVirtMaIfClash_Type()
)
ospfPmIfStatsVirtMaIfClash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsVirtMaIfClash.setStatus("current")
_OspfPmIfStatsBadLsaLen_Type = Counter32
_OspfPmIfStatsBadLsaLen_Object = MibTableColumn
ospfPmIfStatsBadLsaLen = _OspfPmIfStatsBadLsaLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 42),
    _OspfPmIfStatsBadLsaLen_Type()
)
ospfPmIfStatsBadLsaLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsBadLsaLen.setStatus("current")
_OspfPmIfStatsLsaBadType_Type = Counter32
_OspfPmIfStatsLsaBadType_Object = MibTableColumn
ospfPmIfStatsLsaBadType = _OspfPmIfStatsLsaBadType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 43),
    _OspfPmIfStatsLsaBadType_Type()
)
ospfPmIfStatsLsaBadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsLsaBadType.setStatus("current")
_OspfPmIfStatsLsaBadLen_Type = Counter32
_OspfPmIfStatsLsaBadLen_Object = MibTableColumn
ospfPmIfStatsLsaBadLen = _OspfPmIfStatsLsaBadLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 44),
    _OspfPmIfStatsLsaBadLen_Type()
)
ospfPmIfStatsLsaBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsLsaBadLen.setStatus("current")
_OspfPmIfStatsLsaBadData_Type = Counter32
_OspfPmIfStatsLsaBadData_Object = MibTableColumn
ospfPmIfStatsLsaBadData = _OspfPmIfStatsLsaBadData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 45),
    _OspfPmIfStatsLsaBadData_Type()
)
ospfPmIfStatsLsaBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsLsaBadData.setStatus("current")
_OspfPmIfStatsLsaBadCksum_Type = Counter32
_OspfPmIfStatsLsaBadCksum_Object = MibTableColumn
ospfPmIfStatsLsaBadCksum = _OspfPmIfStatsLsaBadCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 46),
    _OspfPmIfStatsLsaBadCksum_Type()
)
ospfPmIfStatsLsaBadCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsLsaBadCksum.setStatus("current")
_OspfPmIfStatsIfStandby_Type = Counter32
_OspfPmIfStatsIfStandby_Object = MibTableColumn
ospfPmIfStatsIfStandby = _OspfPmIfStatsIfStandby_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 47),
    _OspfPmIfStatsIfStandby_Type()
)
ospfPmIfStatsIfStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsIfStandby.setStatus("current")
_OspfPmIfStatsUnkNbmaNbr_Type = Counter32
_OspfPmIfStatsUnkNbmaNbr_Object = MibTableColumn
ospfPmIfStatsUnkNbmaNbr = _OspfPmIfStatsUnkNbmaNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 48),
    _OspfPmIfStatsUnkNbmaNbr_Type()
)
ospfPmIfStatsUnkNbmaNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsUnkNbmaNbr.setStatus("current")
_OspfPmIfStatsUnkVirtNbr_Type = Counter32
_OspfPmIfStatsUnkVirtNbr_Object = MibTableColumn
ospfPmIfStatsUnkVirtNbr = _OspfPmIfStatsUnkVirtNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 49),
    _OspfPmIfStatsUnkVirtNbr_Type()
)
ospfPmIfStatsUnkVirtNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsUnkVirtNbr.setStatus("current")
_OspfPmIfStatsAuthMismatch_Type = Counter32
_OspfPmIfStatsAuthMismatch_Object = MibTableColumn
ospfPmIfStatsAuthMismatch = _OspfPmIfStatsAuthMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 50),
    _OspfPmIfStatsAuthMismatch_Type()
)
ospfPmIfStatsAuthMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsAuthMismatch.setStatus("current")
_OspfPmIfStatsAuthFailure_Type = Counter32
_OspfPmIfStatsAuthFailure_Object = MibTableColumn
ospfPmIfStatsAuthFailure = _OspfPmIfStatsAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 51),
    _OspfPmIfStatsAuthFailure_Type()
)
ospfPmIfStatsAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsAuthFailure.setStatus("current")
_OspfPmIfStatsNetmaskMismatch_Type = Counter32
_OspfPmIfStatsNetmaskMismatch_Object = MibTableColumn
ospfPmIfStatsNetmaskMismatch = _OspfPmIfStatsNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 52),
    _OspfPmIfStatsNetmaskMismatch_Type()
)
ospfPmIfStatsNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsNetmaskMismatch.setStatus("current")
_OspfPmIfStatsHelloMismatch_Type = Counter32
_OspfPmIfStatsHelloMismatch_Object = MibTableColumn
ospfPmIfStatsHelloMismatch = _OspfPmIfStatsHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 53),
    _OspfPmIfStatsHelloMismatch_Type()
)
ospfPmIfStatsHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsHelloMismatch.setStatus("current")
_OspfPmIfStatsDeadMismatch_Type = Counter32
_OspfPmIfStatsDeadMismatch_Object = MibTableColumn
ospfPmIfStatsDeadMismatch = _OspfPmIfStatsDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 54),
    _OspfPmIfStatsDeadMismatch_Type()
)
ospfPmIfStatsDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsDeadMismatch.setStatus("current")
_OspfPmIfStatsOptionsMismatch_Type = Counter32
_OspfPmIfStatsOptionsMismatch_Object = MibTableColumn
ospfPmIfStatsOptionsMismatch = _OspfPmIfStatsOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 55),
    _OspfPmIfStatsOptionsMismatch_Type()
)
ospfPmIfStatsOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsOptionsMismatch.setStatus("current")
_OspfPmIfStatsNbrAdminDown_Type = Counter32
_OspfPmIfStatsNbrAdminDown_Object = MibTableColumn
ospfPmIfStatsNbrAdminDown = _OspfPmIfStatsNbrAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 56),
    _OspfPmIfStatsNbrAdminDown_Type()
)
ospfPmIfStatsNbrAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsNbrAdminDown.setStatus("current")
_OspfPmIfStatsPktLocalAddr_Type = Counter32
_OspfPmIfStatsPktLocalAddr_Object = MibTableColumn
ospfPmIfStatsPktLocalAddr = _OspfPmIfStatsPktLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 57),
    _OspfPmIfStatsPktLocalAddr_Type()
)
ospfPmIfStatsPktLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsPktLocalAddr.setStatus("current")
_OspfPmIfStatsMaIfNotP2p_Type = Counter32
_OspfPmIfStatsMaIfNotP2p_Object = MibTableColumn
ospfPmIfStatsMaIfNotP2p = _OspfPmIfStatsMaIfNotP2p_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 58),
    _OspfPmIfStatsMaIfNotP2p_Type()
)
ospfPmIfStatsMaIfNotP2p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsMaIfNotP2p.setStatus("current")
_OspfPmIfStatsBadPacket_Type = Counter32
_OspfPmIfStatsBadPacket_Object = MibTableColumn
ospfPmIfStatsBadPacket = _OspfPmIfStatsBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 32, 1, 59),
    _OspfPmIfStatsBadPacket_Type()
)
ospfPmIfStatsBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmIfStatsBadPacket.setStatus("current")
_OspfPmVirtIfStatsTable_Object = MibTable
ospfPmVirtIfStatsTable = _OspfPmVirtIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33)
)
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTable.setStatus("current")
_OspfPmVirtIfStatsEntry_Object = MibTableRow
ospfPmVirtIfStatsEntry = _OspfPmVirtIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1)
)
ospfPmVirtIfStatsEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmVirtIfStatsApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmVirtIfStatsAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmVirtIfStatsNeighbor"),
)
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsEntry.setStatus("current")
_OspfPmVirtIfStatsApplIndex_Type = OspfPmIndex
_OspfPmVirtIfStatsApplIndex_Object = MibTableColumn
ospfPmVirtIfStatsApplIndex = _OspfPmVirtIfStatsApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 1),
    _OspfPmVirtIfStatsApplIndex_Type()
)
ospfPmVirtIfStatsApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsApplIndex.setStatus("current")
_OspfPmVirtIfStatsAreaId_Type = AreaID
_OspfPmVirtIfStatsAreaId_Object = MibTableColumn
ospfPmVirtIfStatsAreaId = _OspfPmVirtIfStatsAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 2),
    _OspfPmVirtIfStatsAreaId_Type()
)
ospfPmVirtIfStatsAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsAreaId.setStatus("current")
_OspfPmVirtIfStatsNeighbor_Type = RouterID
_OspfPmVirtIfStatsNeighbor_Object = MibTableColumn
ospfPmVirtIfStatsNeighbor = _OspfPmVirtIfStatsNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 3),
    _OspfPmVirtIfStatsNeighbor_Type()
)
ospfPmVirtIfStatsNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsNeighbor.setStatus("current")
_OspfPmVirtIfStatsRxInvalid_Type = Counter32
_OspfPmVirtIfStatsRxInvalid_Object = MibTableColumn
ospfPmVirtIfStatsRxInvalid = _OspfPmVirtIfStatsRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 4),
    _OspfPmVirtIfStatsRxInvalid_Type()
)
ospfPmVirtIfStatsRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxInvalid.setStatus("current")
_OspfPmVirtIfStatsRxInvalidByte_Type = Counter32
_OspfPmVirtIfStatsRxInvalidByte_Object = MibTableColumn
ospfPmVirtIfStatsRxInvalidByte = _OspfPmVirtIfStatsRxInvalidByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 5),
    _OspfPmVirtIfStatsRxInvalidByte_Type()
)
ospfPmVirtIfStatsRxInvalidByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxInvalidByte.setStatus("current")
_OspfPmVirtIfStatsRxHello_Type = Counter32
_OspfPmVirtIfStatsRxHello_Object = MibTableColumn
ospfPmVirtIfStatsRxHello = _OspfPmVirtIfStatsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 6),
    _OspfPmVirtIfStatsRxHello_Type()
)
ospfPmVirtIfStatsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxHello.setStatus("current")
_OspfPmVirtIfStatsRxHelloByte_Type = Counter32
_OspfPmVirtIfStatsRxHelloByte_Object = MibTableColumn
ospfPmVirtIfStatsRxHelloByte = _OspfPmVirtIfStatsRxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 7),
    _OspfPmVirtIfStatsRxHelloByte_Type()
)
ospfPmVirtIfStatsRxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxHelloByte.setStatus("current")
_OspfPmVirtIfStatsRxDbDes_Type = Counter32
_OspfPmVirtIfStatsRxDbDes_Object = MibTableColumn
ospfPmVirtIfStatsRxDbDes = _OspfPmVirtIfStatsRxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 8),
    _OspfPmVirtIfStatsRxDbDes_Type()
)
ospfPmVirtIfStatsRxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxDbDes.setStatus("current")
_OspfPmVirtIfStatsRxDbDesByte_Type = Counter32
_OspfPmVirtIfStatsRxDbDesByte_Object = MibTableColumn
ospfPmVirtIfStatsRxDbDesByte = _OspfPmVirtIfStatsRxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 9),
    _OspfPmVirtIfStatsRxDbDesByte_Type()
)
ospfPmVirtIfStatsRxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxDbDesByte.setStatus("current")
_OspfPmVirtIfStatsRxLsReq_Type = Counter32
_OspfPmVirtIfStatsRxLsReq_Object = MibTableColumn
ospfPmVirtIfStatsRxLsReq = _OspfPmVirtIfStatsRxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 10),
    _OspfPmVirtIfStatsRxLsReq_Type()
)
ospfPmVirtIfStatsRxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxLsReq.setStatus("current")
_OspfPmVirtIfStatsRxLsReqByte_Type = Counter32
_OspfPmVirtIfStatsRxLsReqByte_Object = MibTableColumn
ospfPmVirtIfStatsRxLsReqByte = _OspfPmVirtIfStatsRxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 11),
    _OspfPmVirtIfStatsRxLsReqByte_Type()
)
ospfPmVirtIfStatsRxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxLsReqByte.setStatus("current")
_OspfPmVirtIfStatsRxLsUpd_Type = Counter32
_OspfPmVirtIfStatsRxLsUpd_Object = MibTableColumn
ospfPmVirtIfStatsRxLsUpd = _OspfPmVirtIfStatsRxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 12),
    _OspfPmVirtIfStatsRxLsUpd_Type()
)
ospfPmVirtIfStatsRxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxLsUpd.setStatus("current")
_OspfPmVirtIfStatsRxLsUpdByte_Type = Counter32
_OspfPmVirtIfStatsRxLsUpdByte_Object = MibTableColumn
ospfPmVirtIfStatsRxLsUpdByte = _OspfPmVirtIfStatsRxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 13),
    _OspfPmVirtIfStatsRxLsUpdByte_Type()
)
ospfPmVirtIfStatsRxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxLsUpdByte.setStatus("current")
_OspfPmVirtIfStatsRxLsAck_Type = Counter32
_OspfPmVirtIfStatsRxLsAck_Object = MibTableColumn
ospfPmVirtIfStatsRxLsAck = _OspfPmVirtIfStatsRxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 14),
    _OspfPmVirtIfStatsRxLsAck_Type()
)
ospfPmVirtIfStatsRxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxLsAck.setStatus("current")
_OspfPmVirtIfStatsRxLsAckByte_Type = Counter32
_OspfPmVirtIfStatsRxLsAckByte_Object = MibTableColumn
ospfPmVirtIfStatsRxLsAckByte = _OspfPmVirtIfStatsRxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 15),
    _OspfPmVirtIfStatsRxLsAckByte_Type()
)
ospfPmVirtIfStatsRxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsRxLsAckByte.setStatus("current")
_OspfPmVirtIfStatsTxFailed_Type = Counter32
_OspfPmVirtIfStatsTxFailed_Object = MibTableColumn
ospfPmVirtIfStatsTxFailed = _OspfPmVirtIfStatsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 16),
    _OspfPmVirtIfStatsTxFailed_Type()
)
ospfPmVirtIfStatsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxFailed.setStatus("current")
_OspfPmVirtIfStatsTxFailedByte_Type = Counter32
_OspfPmVirtIfStatsTxFailedByte_Object = MibTableColumn
ospfPmVirtIfStatsTxFailedByte = _OspfPmVirtIfStatsTxFailedByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 17),
    _OspfPmVirtIfStatsTxFailedByte_Type()
)
ospfPmVirtIfStatsTxFailedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxFailedByte.setStatus("current")
_OspfPmVirtIfStatsTxHello_Type = Counter32
_OspfPmVirtIfStatsTxHello_Object = MibTableColumn
ospfPmVirtIfStatsTxHello = _OspfPmVirtIfStatsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 18),
    _OspfPmVirtIfStatsTxHello_Type()
)
ospfPmVirtIfStatsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxHello.setStatus("current")
_OspfPmVirtIfStatsTxHelloByte_Type = Counter32
_OspfPmVirtIfStatsTxHelloByte_Object = MibTableColumn
ospfPmVirtIfStatsTxHelloByte = _OspfPmVirtIfStatsTxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 19),
    _OspfPmVirtIfStatsTxHelloByte_Type()
)
ospfPmVirtIfStatsTxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxHelloByte.setStatus("current")
_OspfPmVirtIfStatsTxDbDes_Type = Counter32
_OspfPmVirtIfStatsTxDbDes_Object = MibTableColumn
ospfPmVirtIfStatsTxDbDes = _OspfPmVirtIfStatsTxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 20),
    _OspfPmVirtIfStatsTxDbDes_Type()
)
ospfPmVirtIfStatsTxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxDbDes.setStatus("current")
_OspfPmVirtIfStatsTxDbDesByte_Type = Counter32
_OspfPmVirtIfStatsTxDbDesByte_Object = MibTableColumn
ospfPmVirtIfStatsTxDbDesByte = _OspfPmVirtIfStatsTxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 21),
    _OspfPmVirtIfStatsTxDbDesByte_Type()
)
ospfPmVirtIfStatsTxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxDbDesByte.setStatus("current")
_OspfPmVirtIfStatsTxLsReq_Type = Counter32
_OspfPmVirtIfStatsTxLsReq_Object = MibTableColumn
ospfPmVirtIfStatsTxLsReq = _OspfPmVirtIfStatsTxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 22),
    _OspfPmVirtIfStatsTxLsReq_Type()
)
ospfPmVirtIfStatsTxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxLsReq.setStatus("current")
_OspfPmVirtIfStatsTxLsReqByte_Type = Counter32
_OspfPmVirtIfStatsTxLsReqByte_Object = MibTableColumn
ospfPmVirtIfStatsTxLsReqByte = _OspfPmVirtIfStatsTxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 23),
    _OspfPmVirtIfStatsTxLsReqByte_Type()
)
ospfPmVirtIfStatsTxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxLsReqByte.setStatus("current")
_OspfPmVirtIfStatsTxLsUpd_Type = Counter32
_OspfPmVirtIfStatsTxLsUpd_Object = MibTableColumn
ospfPmVirtIfStatsTxLsUpd = _OspfPmVirtIfStatsTxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 24),
    _OspfPmVirtIfStatsTxLsUpd_Type()
)
ospfPmVirtIfStatsTxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxLsUpd.setStatus("current")
_OspfPmVirtIfStatsTxLsUpdByte_Type = Counter32
_OspfPmVirtIfStatsTxLsUpdByte_Object = MibTableColumn
ospfPmVirtIfStatsTxLsUpdByte = _OspfPmVirtIfStatsTxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 25),
    _OspfPmVirtIfStatsTxLsUpdByte_Type()
)
ospfPmVirtIfStatsTxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxLsUpdByte.setStatus("current")
_OspfPmVirtIfStatsTxLsAck_Type = Counter32
_OspfPmVirtIfStatsTxLsAck_Object = MibTableColumn
ospfPmVirtIfStatsTxLsAck = _OspfPmVirtIfStatsTxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 26),
    _OspfPmVirtIfStatsTxLsAck_Type()
)
ospfPmVirtIfStatsTxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxLsAck.setStatus("current")
_OspfPmVirtIfStatsTxLsAckByte_Type = Counter32
_OspfPmVirtIfStatsTxLsAckByte_Object = MibTableColumn
ospfPmVirtIfStatsTxLsAckByte = _OspfPmVirtIfStatsTxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 27),
    _OspfPmVirtIfStatsTxLsAckByte_Type()
)
ospfPmVirtIfStatsTxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsTxLsAckByte.setStatus("current")
_OspfPmVirtIfStatsLength_Type = Counter32
_OspfPmVirtIfStatsLength_Object = MibTableColumn
ospfPmVirtIfStatsLength = _OspfPmVirtIfStatsLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 28),
    _OspfPmVirtIfStatsLength_Type()
)
ospfPmVirtIfStatsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsLength.setStatus("current")
_OspfPmVirtIfStatsCksum_Type = Counter32
_OspfPmVirtIfStatsCksum_Object = MibTableColumn
ospfPmVirtIfStatsCksum = _OspfPmVirtIfStatsCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 29),
    _OspfPmVirtIfStatsCksum_Type()
)
ospfPmVirtIfStatsCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsCksum.setStatus("current")
_OspfPmVirtIfStatsVersion_Type = Counter32
_OspfPmVirtIfStatsVersion_Object = MibTableColumn
ospfPmVirtIfStatsVersion = _OspfPmVirtIfStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 30),
    _OspfPmVirtIfStatsVersion_Type()
)
ospfPmVirtIfStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsVersion.setStatus("current")
_OspfPmVirtIfStatsBadSrc_Type = Counter32
_OspfPmVirtIfStatsBadSrc_Object = MibTableColumn
ospfPmVirtIfStatsBadSrc = _OspfPmVirtIfStatsBadSrc_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 31),
    _OspfPmVirtIfStatsBadSrc_Type()
)
ospfPmVirtIfStatsBadSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsBadSrc.setStatus("current")
_OspfPmVirtIfStatsAreaMismatch_Type = Counter32
_OspfPmVirtIfStatsAreaMismatch_Object = MibTableColumn
ospfPmVirtIfStatsAreaMismatch = _OspfPmVirtIfStatsAreaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 32),
    _OspfPmVirtIfStatsAreaMismatch_Type()
)
ospfPmVirtIfStatsAreaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsAreaMismatch.setStatus("current")
_OspfPmVirtIfStatsSelfOrig_Type = Counter32
_OspfPmVirtIfStatsSelfOrig_Object = MibTableColumn
ospfPmVirtIfStatsSelfOrig = _OspfPmVirtIfStatsSelfOrig_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 33),
    _OspfPmVirtIfStatsSelfOrig_Type()
)
ospfPmVirtIfStatsSelfOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsSelfOrig.setStatus("current")
_OspfPmVirtIfStatsDupeId_Type = Counter32
_OspfPmVirtIfStatsDupeId_Object = MibTableColumn
ospfPmVirtIfStatsDupeId = _OspfPmVirtIfStatsDupeId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 34),
    _OspfPmVirtIfStatsDupeId_Type()
)
ospfPmVirtIfStatsDupeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsDupeId.setStatus("current")
_OspfPmVirtIfStatsHello_Type = Counter32
_OspfPmVirtIfStatsHello_Object = MibTableColumn
ospfPmVirtIfStatsHello = _OspfPmVirtIfStatsHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 35),
    _OspfPmVirtIfStatsHello_Type()
)
ospfPmVirtIfStatsHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsHello.setStatus("current")
_OspfPmVirtIfStatsMtuMismatch_Type = Counter32
_OspfPmVirtIfStatsMtuMismatch_Object = MibTableColumn
ospfPmVirtIfStatsMtuMismatch = _OspfPmVirtIfStatsMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 36),
    _OspfPmVirtIfStatsMtuMismatch_Type()
)
ospfPmVirtIfStatsMtuMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsMtuMismatch.setStatus("current")
_OspfPmVirtIfStatsNbrIgnored_Type = Counter32
_OspfPmVirtIfStatsNbrIgnored_Object = MibTableColumn
ospfPmVirtIfStatsNbrIgnored = _OspfPmVirtIfStatsNbrIgnored_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 37),
    _OspfPmVirtIfStatsNbrIgnored_Type()
)
ospfPmVirtIfStatsNbrIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsNbrIgnored.setStatus("current")
_OspfPmVirtIfStatsAuth_Type = Counter32
_OspfPmVirtIfStatsAuth_Object = MibTableColumn
ospfPmVirtIfStatsAuth = _OspfPmVirtIfStatsAuth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 38),
    _OspfPmVirtIfStatsAuth_Type()
)
ospfPmVirtIfStatsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsAuth.setStatus("current")
_OspfPmVirtIfStatsWrongProto_Type = Counter32
_OspfPmVirtIfStatsWrongProto_Object = MibTableColumn
ospfPmVirtIfStatsWrongProto = _OspfPmVirtIfStatsWrongProto_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 39),
    _OspfPmVirtIfStatsWrongProto_Type()
)
ospfPmVirtIfStatsWrongProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsWrongProto.setStatus("current")
_OspfPmVirtIfStatsResourceErr_Type = Counter32
_OspfPmVirtIfStatsResourceErr_Object = MibTableColumn
ospfPmVirtIfStatsResourceErr = _OspfPmVirtIfStatsResourceErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 40),
    _OspfPmVirtIfStatsResourceErr_Type()
)
ospfPmVirtIfStatsResourceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsResourceErr.setStatus("current")
_OspfPmVirtIfStatsVirtMaIfClash_Type = Counter32
_OspfPmVirtIfStatsVirtMaIfClash_Object = MibTableColumn
ospfPmVirtIfStatsVirtMaIfClash = _OspfPmVirtIfStatsVirtMaIfClash_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 41),
    _OspfPmVirtIfStatsVirtMaIfClash_Type()
)
ospfPmVirtIfStatsVirtMaIfClash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsVirtMaIfClash.setStatus("current")
_OspfPmVirtIfStatsBadLsaLen_Type = Counter32
_OspfPmVirtIfStatsBadLsaLen_Object = MibTableColumn
ospfPmVirtIfStatsBadLsaLen = _OspfPmVirtIfStatsBadLsaLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 42),
    _OspfPmVirtIfStatsBadLsaLen_Type()
)
ospfPmVirtIfStatsBadLsaLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsBadLsaLen.setStatus("current")
_OspfPmVirtIfStatsLsaBadType_Type = Counter32
_OspfPmVirtIfStatsLsaBadType_Object = MibTableColumn
ospfPmVirtIfStatsLsaBadType = _OspfPmVirtIfStatsLsaBadType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 43),
    _OspfPmVirtIfStatsLsaBadType_Type()
)
ospfPmVirtIfStatsLsaBadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsLsaBadType.setStatus("current")
_OspfPmVirtIfStatsLsaBadLen_Type = Counter32
_OspfPmVirtIfStatsLsaBadLen_Object = MibTableColumn
ospfPmVirtIfStatsLsaBadLen = _OspfPmVirtIfStatsLsaBadLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 44),
    _OspfPmVirtIfStatsLsaBadLen_Type()
)
ospfPmVirtIfStatsLsaBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsLsaBadLen.setStatus("current")
_OspfPmVirtIfStatsLsaBadData_Type = Counter32
_OspfPmVirtIfStatsLsaBadData_Object = MibTableColumn
ospfPmVirtIfStatsLsaBadData = _OspfPmVirtIfStatsLsaBadData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 45),
    _OspfPmVirtIfStatsLsaBadData_Type()
)
ospfPmVirtIfStatsLsaBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsLsaBadData.setStatus("current")
_OspfPmVirtIfStatsLsaBadCksum_Type = Counter32
_OspfPmVirtIfStatsLsaBadCksum_Object = MibTableColumn
ospfPmVirtIfStatsLsaBadCksum = _OspfPmVirtIfStatsLsaBadCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 46),
    _OspfPmVirtIfStatsLsaBadCksum_Type()
)
ospfPmVirtIfStatsLsaBadCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsLsaBadCksum.setStatus("current")
_OspfPmVirtIfStatsUnkNbmaNbr_Type = Counter32
_OspfPmVirtIfStatsUnkNbmaNbr_Object = MibTableColumn
ospfPmVirtIfStatsUnkNbmaNbr = _OspfPmVirtIfStatsUnkNbmaNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 47),
    _OspfPmVirtIfStatsUnkNbmaNbr_Type()
)
ospfPmVirtIfStatsUnkNbmaNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsUnkNbmaNbr.setStatus("current")
_OspfPmVirtIfStatsUnkVirtNbr_Type = Counter32
_OspfPmVirtIfStatsUnkVirtNbr_Object = MibTableColumn
ospfPmVirtIfStatsUnkVirtNbr = _OspfPmVirtIfStatsUnkVirtNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 48),
    _OspfPmVirtIfStatsUnkVirtNbr_Type()
)
ospfPmVirtIfStatsUnkVirtNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsUnkVirtNbr.setStatus("current")
_OspfPmVirtIfStatsAuthMismatch_Type = Counter32
_OspfPmVirtIfStatsAuthMismatch_Object = MibTableColumn
ospfPmVirtIfStatsAuthMismatch = _OspfPmVirtIfStatsAuthMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 49),
    _OspfPmVirtIfStatsAuthMismatch_Type()
)
ospfPmVirtIfStatsAuthMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsAuthMismatch.setStatus("current")
_OspfPmVirtIfStatsAuthFailure_Type = Counter32
_OspfPmVirtIfStatsAuthFailure_Object = MibTableColumn
ospfPmVirtIfStatsAuthFailure = _OspfPmVirtIfStatsAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 50),
    _OspfPmVirtIfStatsAuthFailure_Type()
)
ospfPmVirtIfStatsAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsAuthFailure.setStatus("current")
_OspfPmVirtIfStatsNetmaskMismatch_Type = Counter32
_OspfPmVirtIfStatsNetmaskMismatch_Object = MibTableColumn
ospfPmVirtIfStatsNetmaskMismatch = _OspfPmVirtIfStatsNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 51),
    _OspfPmVirtIfStatsNetmaskMismatch_Type()
)
ospfPmVirtIfStatsNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsNetmaskMismatch.setStatus("current")
_OspfPmVirtIfStatsHelloMismatch_Type = Counter32
_OspfPmVirtIfStatsHelloMismatch_Object = MibTableColumn
ospfPmVirtIfStatsHelloMismatch = _OspfPmVirtIfStatsHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 52),
    _OspfPmVirtIfStatsHelloMismatch_Type()
)
ospfPmVirtIfStatsHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsHelloMismatch.setStatus("current")
_OspfPmVirtIfStatsDeadMismatch_Type = Counter32
_OspfPmVirtIfStatsDeadMismatch_Object = MibTableColumn
ospfPmVirtIfStatsDeadMismatch = _OspfPmVirtIfStatsDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 53),
    _OspfPmVirtIfStatsDeadMismatch_Type()
)
ospfPmVirtIfStatsDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsDeadMismatch.setStatus("current")
_OspfPmVirtIfStatsOptionsMismatch_Type = Counter32
_OspfPmVirtIfStatsOptionsMismatch_Object = MibTableColumn
ospfPmVirtIfStatsOptionsMismatch = _OspfPmVirtIfStatsOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 54),
    _OspfPmVirtIfStatsOptionsMismatch_Type()
)
ospfPmVirtIfStatsOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsOptionsMismatch.setStatus("current")
_OspfPmVirtIfStatsNbrAdminDown_Type = Counter32
_OspfPmVirtIfStatsNbrAdminDown_Object = MibTableColumn
ospfPmVirtIfStatsNbrAdminDown = _OspfPmVirtIfStatsNbrAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 55),
    _OspfPmVirtIfStatsNbrAdminDown_Type()
)
ospfPmVirtIfStatsNbrAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsNbrAdminDown.setStatus("current")
_OspfPmVirtIfStatsPktLocalAddr_Type = Counter32
_OspfPmVirtIfStatsPktLocalAddr_Object = MibTableColumn
ospfPmVirtIfStatsPktLocalAddr = _OspfPmVirtIfStatsPktLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 56),
    _OspfPmVirtIfStatsPktLocalAddr_Type()
)
ospfPmVirtIfStatsPktLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsPktLocalAddr.setStatus("current")
_OspfPmVirtIfStatsMaIfNotP2p_Type = Counter32
_OspfPmVirtIfStatsMaIfNotP2p_Object = MibTableColumn
ospfPmVirtIfStatsMaIfNotP2p = _OspfPmVirtIfStatsMaIfNotP2p_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 57),
    _OspfPmVirtIfStatsMaIfNotP2p_Type()
)
ospfPmVirtIfStatsMaIfNotP2p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsMaIfNotP2p.setStatus("current")
_OspfPmVirtIfStatsBadPacket_Type = Counter32
_OspfPmVirtIfStatsBadPacket_Object = MibTableColumn
ospfPmVirtIfStatsBadPacket = _OspfPmVirtIfStatsBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 33, 1, 58),
    _OspfPmVirtIfStatsBadPacket_Type()
)
ospfPmVirtIfStatsBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmVirtIfStatsBadPacket.setStatus("current")
_OspfPmShamLinkStatsTable_Object = MibTable
ospfPmShamLinkStatsTable = _OspfPmShamLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34)
)
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTable.setStatus("current")
_OspfPmShamLinkStatsEntry_Object = MibTableRow
ospfPmShamLinkStatsEntry = _OspfPmShamLinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1)
)
ospfPmShamLinkStatsEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmShamLinkStatsApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmShamLinkStatsAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmShamLinkStatsLocalIpAddr"),
    (0, "DC-OSPF-MIB", "ospfPmShamLinkStatsRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsEntry.setStatus("current")
_OspfPmShamLinkStatsApplIndex_Type = OspfPmIndex
_OspfPmShamLinkStatsApplIndex_Object = MibTableColumn
ospfPmShamLinkStatsApplIndex = _OspfPmShamLinkStatsApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 1),
    _OspfPmShamLinkStatsApplIndex_Type()
)
ospfPmShamLinkStatsApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsApplIndex.setStatus("current")
_OspfPmShamLinkStatsAreaId_Type = AreaID
_OspfPmShamLinkStatsAreaId_Object = MibTableColumn
ospfPmShamLinkStatsAreaId = _OspfPmShamLinkStatsAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 2),
    _OspfPmShamLinkStatsAreaId_Type()
)
ospfPmShamLinkStatsAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsAreaId.setStatus("current")
_OspfPmShamLinkStatsLocalIpAddr_Type = IpAddress
_OspfPmShamLinkStatsLocalIpAddr_Object = MibTableColumn
ospfPmShamLinkStatsLocalIpAddr = _OspfPmShamLinkStatsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 3),
    _OspfPmShamLinkStatsLocalIpAddr_Type()
)
ospfPmShamLinkStatsLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsLocalIpAddr.setStatus("current")
_OspfPmShamLinkStatsRemoteIpAddr_Type = IpAddress
_OspfPmShamLinkStatsRemoteIpAddr_Object = MibTableColumn
ospfPmShamLinkStatsRemoteIpAddr = _OspfPmShamLinkStatsRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 4),
    _OspfPmShamLinkStatsRemoteIpAddr_Type()
)
ospfPmShamLinkStatsRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRemoteIpAddr.setStatus("current")
_OspfPmShamLinkStatsRxInvalid_Type = Counter32
_OspfPmShamLinkStatsRxInvalid_Object = MibTableColumn
ospfPmShamLinkStatsRxInvalid = _OspfPmShamLinkStatsRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 5),
    _OspfPmShamLinkStatsRxInvalid_Type()
)
ospfPmShamLinkStatsRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxInvalid.setStatus("current")
_OspfPmShamLinkStatsRxInvalidByte_Type = Counter32
_OspfPmShamLinkStatsRxInvalidByte_Object = MibTableColumn
ospfPmShamLinkStatsRxInvalidByte = _OspfPmShamLinkStatsRxInvalidByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 6),
    _OspfPmShamLinkStatsRxInvalidByte_Type()
)
ospfPmShamLinkStatsRxInvalidByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxInvalidByte.setStatus("current")
_OspfPmShamLinkStatsRxHello_Type = Counter32
_OspfPmShamLinkStatsRxHello_Object = MibTableColumn
ospfPmShamLinkStatsRxHello = _OspfPmShamLinkStatsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 7),
    _OspfPmShamLinkStatsRxHello_Type()
)
ospfPmShamLinkStatsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxHello.setStatus("current")
_OspfPmShamLinkStatsRxHelloByte_Type = Counter32
_OspfPmShamLinkStatsRxHelloByte_Object = MibTableColumn
ospfPmShamLinkStatsRxHelloByte = _OspfPmShamLinkStatsRxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 8),
    _OspfPmShamLinkStatsRxHelloByte_Type()
)
ospfPmShamLinkStatsRxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxHelloByte.setStatus("current")
_OspfPmShamLinkStatsRxDbDes_Type = Counter32
_OspfPmShamLinkStatsRxDbDes_Object = MibTableColumn
ospfPmShamLinkStatsRxDbDes = _OspfPmShamLinkStatsRxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 9),
    _OspfPmShamLinkStatsRxDbDes_Type()
)
ospfPmShamLinkStatsRxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxDbDes.setStatus("current")
_OspfPmShamLinkStatsRxDbDesByte_Type = Counter32
_OspfPmShamLinkStatsRxDbDesByte_Object = MibTableColumn
ospfPmShamLinkStatsRxDbDesByte = _OspfPmShamLinkStatsRxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 10),
    _OspfPmShamLinkStatsRxDbDesByte_Type()
)
ospfPmShamLinkStatsRxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxDbDesByte.setStatus("current")
_OspfPmShamLinkStatsRxLsReq_Type = Counter32
_OspfPmShamLinkStatsRxLsReq_Object = MibTableColumn
ospfPmShamLinkStatsRxLsReq = _OspfPmShamLinkStatsRxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 11),
    _OspfPmShamLinkStatsRxLsReq_Type()
)
ospfPmShamLinkStatsRxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxLsReq.setStatus("current")
_OspfPmShamLinkStatsRxLsReqByte_Type = Counter32
_OspfPmShamLinkStatsRxLsReqByte_Object = MibTableColumn
ospfPmShamLinkStatsRxLsReqByte = _OspfPmShamLinkStatsRxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 12),
    _OspfPmShamLinkStatsRxLsReqByte_Type()
)
ospfPmShamLinkStatsRxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxLsReqByte.setStatus("current")
_OspfPmShamLinkStatsRxLsUpd_Type = Counter32
_OspfPmShamLinkStatsRxLsUpd_Object = MibTableColumn
ospfPmShamLinkStatsRxLsUpd = _OspfPmShamLinkStatsRxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 13),
    _OspfPmShamLinkStatsRxLsUpd_Type()
)
ospfPmShamLinkStatsRxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxLsUpd.setStatus("current")
_OspfPmShamLinkStatsRxLsUpdByte_Type = Counter32
_OspfPmShamLinkStatsRxLsUpdByte_Object = MibTableColumn
ospfPmShamLinkStatsRxLsUpdByte = _OspfPmShamLinkStatsRxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 14),
    _OspfPmShamLinkStatsRxLsUpdByte_Type()
)
ospfPmShamLinkStatsRxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxLsUpdByte.setStatus("current")
_OspfPmShamLinkStatsRxLsAck_Type = Counter32
_OspfPmShamLinkStatsRxLsAck_Object = MibTableColumn
ospfPmShamLinkStatsRxLsAck = _OspfPmShamLinkStatsRxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 15),
    _OspfPmShamLinkStatsRxLsAck_Type()
)
ospfPmShamLinkStatsRxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxLsAck.setStatus("current")
_OspfPmShamLinkStatsRxLsAckByte_Type = Counter32
_OspfPmShamLinkStatsRxLsAckByte_Object = MibTableColumn
ospfPmShamLinkStatsRxLsAckByte = _OspfPmShamLinkStatsRxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 16),
    _OspfPmShamLinkStatsRxLsAckByte_Type()
)
ospfPmShamLinkStatsRxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsRxLsAckByte.setStatus("current")
_OspfPmShamLinkStatsTxFailed_Type = Counter32
_OspfPmShamLinkStatsTxFailed_Object = MibTableColumn
ospfPmShamLinkStatsTxFailed = _OspfPmShamLinkStatsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 17),
    _OspfPmShamLinkStatsTxFailed_Type()
)
ospfPmShamLinkStatsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxFailed.setStatus("current")
_OspfPmShamLinkStatsTxFailedByte_Type = Counter32
_OspfPmShamLinkStatsTxFailedByte_Object = MibTableColumn
ospfPmShamLinkStatsTxFailedByte = _OspfPmShamLinkStatsTxFailedByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 18),
    _OspfPmShamLinkStatsTxFailedByte_Type()
)
ospfPmShamLinkStatsTxFailedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxFailedByte.setStatus("current")
_OspfPmShamLinkStatsTxHello_Type = Counter32
_OspfPmShamLinkStatsTxHello_Object = MibTableColumn
ospfPmShamLinkStatsTxHello = _OspfPmShamLinkStatsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 19),
    _OspfPmShamLinkStatsTxHello_Type()
)
ospfPmShamLinkStatsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxHello.setStatus("current")
_OspfPmShamLinkStatsTxHelloByte_Type = Counter32
_OspfPmShamLinkStatsTxHelloByte_Object = MibTableColumn
ospfPmShamLinkStatsTxHelloByte = _OspfPmShamLinkStatsTxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 20),
    _OspfPmShamLinkStatsTxHelloByte_Type()
)
ospfPmShamLinkStatsTxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxHelloByte.setStatus("current")
_OspfPmShamLinkStatsTxDbDes_Type = Counter32
_OspfPmShamLinkStatsTxDbDes_Object = MibTableColumn
ospfPmShamLinkStatsTxDbDes = _OspfPmShamLinkStatsTxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 21),
    _OspfPmShamLinkStatsTxDbDes_Type()
)
ospfPmShamLinkStatsTxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxDbDes.setStatus("current")
_OspfPmShamLinkStatsTxDbDesByte_Type = Counter32
_OspfPmShamLinkStatsTxDbDesByte_Object = MibTableColumn
ospfPmShamLinkStatsTxDbDesByte = _OspfPmShamLinkStatsTxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 22),
    _OspfPmShamLinkStatsTxDbDesByte_Type()
)
ospfPmShamLinkStatsTxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxDbDesByte.setStatus("current")
_OspfPmShamLinkStatsTxLsReq_Type = Counter32
_OspfPmShamLinkStatsTxLsReq_Object = MibTableColumn
ospfPmShamLinkStatsTxLsReq = _OspfPmShamLinkStatsTxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 23),
    _OspfPmShamLinkStatsTxLsReq_Type()
)
ospfPmShamLinkStatsTxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxLsReq.setStatus("current")
_OspfPmShamLinkStatsTxLsReqByte_Type = Counter32
_OspfPmShamLinkStatsTxLsReqByte_Object = MibTableColumn
ospfPmShamLinkStatsTxLsReqByte = _OspfPmShamLinkStatsTxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 24),
    _OspfPmShamLinkStatsTxLsReqByte_Type()
)
ospfPmShamLinkStatsTxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxLsReqByte.setStatus("current")
_OspfPmShamLinkStatsTxLsUpd_Type = Counter32
_OspfPmShamLinkStatsTxLsUpd_Object = MibTableColumn
ospfPmShamLinkStatsTxLsUpd = _OspfPmShamLinkStatsTxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 25),
    _OspfPmShamLinkStatsTxLsUpd_Type()
)
ospfPmShamLinkStatsTxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxLsUpd.setStatus("current")
_OspfPmShamLinkStatsTxLsUpdByte_Type = Counter32
_OspfPmShamLinkStatsTxLsUpdByte_Object = MibTableColumn
ospfPmShamLinkStatsTxLsUpdByte = _OspfPmShamLinkStatsTxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 26),
    _OspfPmShamLinkStatsTxLsUpdByte_Type()
)
ospfPmShamLinkStatsTxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxLsUpdByte.setStatus("current")
_OspfPmShamLinkStatsTxLsAck_Type = Counter32
_OspfPmShamLinkStatsTxLsAck_Object = MibTableColumn
ospfPmShamLinkStatsTxLsAck = _OspfPmShamLinkStatsTxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 27),
    _OspfPmShamLinkStatsTxLsAck_Type()
)
ospfPmShamLinkStatsTxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxLsAck.setStatus("current")
_OspfPmShamLinkStatsTxLsAckByte_Type = Counter32
_OspfPmShamLinkStatsTxLsAckByte_Object = MibTableColumn
ospfPmShamLinkStatsTxLsAckByte = _OspfPmShamLinkStatsTxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 28),
    _OspfPmShamLinkStatsTxLsAckByte_Type()
)
ospfPmShamLinkStatsTxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsTxLsAckByte.setStatus("current")
_OspfPmShamLinkStatsLength_Type = Counter32
_OspfPmShamLinkStatsLength_Object = MibTableColumn
ospfPmShamLinkStatsLength = _OspfPmShamLinkStatsLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 29),
    _OspfPmShamLinkStatsLength_Type()
)
ospfPmShamLinkStatsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsLength.setStatus("current")
_OspfPmShamLinkStatsCksum_Type = Counter32
_OspfPmShamLinkStatsCksum_Object = MibTableColumn
ospfPmShamLinkStatsCksum = _OspfPmShamLinkStatsCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 30),
    _OspfPmShamLinkStatsCksum_Type()
)
ospfPmShamLinkStatsCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsCksum.setStatus("current")
_OspfPmShamLinkStatsVersion_Type = Counter32
_OspfPmShamLinkStatsVersion_Object = MibTableColumn
ospfPmShamLinkStatsVersion = _OspfPmShamLinkStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 31),
    _OspfPmShamLinkStatsVersion_Type()
)
ospfPmShamLinkStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsVersion.setStatus("current")
_OspfPmShamLinkStatsBadSrc_Type = Counter32
_OspfPmShamLinkStatsBadSrc_Object = MibTableColumn
ospfPmShamLinkStatsBadSrc = _OspfPmShamLinkStatsBadSrc_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 32),
    _OspfPmShamLinkStatsBadSrc_Type()
)
ospfPmShamLinkStatsBadSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsBadSrc.setStatus("current")
_OspfPmShamLinkStatsAreaMismatch_Type = Counter32
_OspfPmShamLinkStatsAreaMismatch_Object = MibTableColumn
ospfPmShamLinkStatsAreaMismatch = _OspfPmShamLinkStatsAreaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 33),
    _OspfPmShamLinkStatsAreaMismatch_Type()
)
ospfPmShamLinkStatsAreaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsAreaMismatch.setStatus("current")
_OspfPmShamLinkStatsSelfOrig_Type = Counter32
_OspfPmShamLinkStatsSelfOrig_Object = MibTableColumn
ospfPmShamLinkStatsSelfOrig = _OspfPmShamLinkStatsSelfOrig_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 34),
    _OspfPmShamLinkStatsSelfOrig_Type()
)
ospfPmShamLinkStatsSelfOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsSelfOrig.setStatus("current")
_OspfPmShamLinkStatsDupeId_Type = Counter32
_OspfPmShamLinkStatsDupeId_Object = MibTableColumn
ospfPmShamLinkStatsDupeId = _OspfPmShamLinkStatsDupeId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 35),
    _OspfPmShamLinkStatsDupeId_Type()
)
ospfPmShamLinkStatsDupeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsDupeId.setStatus("current")
_OspfPmShamLinkStatsHello_Type = Counter32
_OspfPmShamLinkStatsHello_Object = MibTableColumn
ospfPmShamLinkStatsHello = _OspfPmShamLinkStatsHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 36),
    _OspfPmShamLinkStatsHello_Type()
)
ospfPmShamLinkStatsHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsHello.setStatus("current")
_OspfPmShamLinkStatsMtuMismatch_Type = Counter32
_OspfPmShamLinkStatsMtuMismatch_Object = MibTableColumn
ospfPmShamLinkStatsMtuMismatch = _OspfPmShamLinkStatsMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 37),
    _OspfPmShamLinkStatsMtuMismatch_Type()
)
ospfPmShamLinkStatsMtuMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsMtuMismatch.setStatus("current")
_OspfPmShamLinkStatsNbrIgnored_Type = Counter32
_OspfPmShamLinkStatsNbrIgnored_Object = MibTableColumn
ospfPmShamLinkStatsNbrIgnored = _OspfPmShamLinkStatsNbrIgnored_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 38),
    _OspfPmShamLinkStatsNbrIgnored_Type()
)
ospfPmShamLinkStatsNbrIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsNbrIgnored.setStatus("current")
_OspfPmShamLinkStatsAuth_Type = Counter32
_OspfPmShamLinkStatsAuth_Object = MibTableColumn
ospfPmShamLinkStatsAuth = _OspfPmShamLinkStatsAuth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 39),
    _OspfPmShamLinkStatsAuth_Type()
)
ospfPmShamLinkStatsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsAuth.setStatus("current")
_OspfPmShamLinkStatsWrongProto_Type = Counter32
_OspfPmShamLinkStatsWrongProto_Object = MibTableColumn
ospfPmShamLinkStatsWrongProto = _OspfPmShamLinkStatsWrongProto_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 40),
    _OspfPmShamLinkStatsWrongProto_Type()
)
ospfPmShamLinkStatsWrongProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsWrongProto.setStatus("current")
_OspfPmShamLinkStatsResourceErr_Type = Counter32
_OspfPmShamLinkStatsResourceErr_Object = MibTableColumn
ospfPmShamLinkStatsResourceErr = _OspfPmShamLinkStatsResourceErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 41),
    _OspfPmShamLinkStatsResourceErr_Type()
)
ospfPmShamLinkStatsResourceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsResourceErr.setStatus("current")
_OspfPmShamLinkStatsVirtMaIfClash_Type = Counter32
_OspfPmShamLinkStatsVirtMaIfClash_Object = MibTableColumn
ospfPmShamLinkStatsVirtMaIfClash = _OspfPmShamLinkStatsVirtMaIfClash_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 42),
    _OspfPmShamLinkStatsVirtMaIfClash_Type()
)
ospfPmShamLinkStatsVirtMaIfClash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsVirtMaIfClash.setStatus("current")
_OspfPmShamLinkStatsBadLsaLen_Type = Counter32
_OspfPmShamLinkStatsBadLsaLen_Object = MibTableColumn
ospfPmShamLinkStatsBadLsaLen = _OspfPmShamLinkStatsBadLsaLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 43),
    _OspfPmShamLinkStatsBadLsaLen_Type()
)
ospfPmShamLinkStatsBadLsaLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsBadLsaLen.setStatus("current")
_OspfPmShamLinkStatsLsaBadType_Type = Counter32
_OspfPmShamLinkStatsLsaBadType_Object = MibTableColumn
ospfPmShamLinkStatsLsaBadType = _OspfPmShamLinkStatsLsaBadType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 44),
    _OspfPmShamLinkStatsLsaBadType_Type()
)
ospfPmShamLinkStatsLsaBadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsLsaBadType.setStatus("current")
_OspfPmShamLinkStatsLsaBadLen_Type = Counter32
_OspfPmShamLinkStatsLsaBadLen_Object = MibTableColumn
ospfPmShamLinkStatsLsaBadLen = _OspfPmShamLinkStatsLsaBadLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 45),
    _OspfPmShamLinkStatsLsaBadLen_Type()
)
ospfPmShamLinkStatsLsaBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsLsaBadLen.setStatus("current")
_OspfPmShamLinkStatsLsaBadData_Type = Counter32
_OspfPmShamLinkStatsLsaBadData_Object = MibTableColumn
ospfPmShamLinkStatsLsaBadData = _OspfPmShamLinkStatsLsaBadData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 46),
    _OspfPmShamLinkStatsLsaBadData_Type()
)
ospfPmShamLinkStatsLsaBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsLsaBadData.setStatus("current")
_OspfPmShamLinkStatsLsaBadCksum_Type = Counter32
_OspfPmShamLinkStatsLsaBadCksum_Object = MibTableColumn
ospfPmShamLinkStatsLsaBadCksum = _OspfPmShamLinkStatsLsaBadCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 47),
    _OspfPmShamLinkStatsLsaBadCksum_Type()
)
ospfPmShamLinkStatsLsaBadCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsLsaBadCksum.setStatus("current")
_OspfPmShamLinkStatsUnkNbmaNbr_Type = Counter32
_OspfPmShamLinkStatsUnkNbmaNbr_Object = MibTableColumn
ospfPmShamLinkStatsUnkNbmaNbr = _OspfPmShamLinkStatsUnkNbmaNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 48),
    _OspfPmShamLinkStatsUnkNbmaNbr_Type()
)
ospfPmShamLinkStatsUnkNbmaNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsUnkNbmaNbr.setStatus("current")
_OspfPmShamLinkStatsUnkVirtNbr_Type = Counter32
_OspfPmShamLinkStatsUnkVirtNbr_Object = MibTableColumn
ospfPmShamLinkStatsUnkVirtNbr = _OspfPmShamLinkStatsUnkVirtNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 49),
    _OspfPmShamLinkStatsUnkVirtNbr_Type()
)
ospfPmShamLinkStatsUnkVirtNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsUnkVirtNbr.setStatus("current")
_OspfPmShamLinkStatsAuthMismatch_Type = Counter32
_OspfPmShamLinkStatsAuthMismatch_Object = MibTableColumn
ospfPmShamLinkStatsAuthMismatch = _OspfPmShamLinkStatsAuthMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 50),
    _OspfPmShamLinkStatsAuthMismatch_Type()
)
ospfPmShamLinkStatsAuthMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsAuthMismatch.setStatus("current")
_OspfPmShamLinkStatsAuthFailure_Type = Counter32
_OspfPmShamLinkStatsAuthFailure_Object = MibTableColumn
ospfPmShamLinkStatsAuthFailure = _OspfPmShamLinkStatsAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 51),
    _OspfPmShamLinkStatsAuthFailure_Type()
)
ospfPmShamLinkStatsAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsAuthFailure.setStatus("current")
_OspfPmShamLinkStatsNetmaskMsmtch_Type = Counter32
_OspfPmShamLinkStatsNetmaskMsmtch_Object = MibTableColumn
ospfPmShamLinkStatsNetmaskMsmtch = _OspfPmShamLinkStatsNetmaskMsmtch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 52),
    _OspfPmShamLinkStatsNetmaskMsmtch_Type()
)
ospfPmShamLinkStatsNetmaskMsmtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsNetmaskMsmtch.setStatus("current")
_OspfPmShamLinkStatsHelloMismatch_Type = Counter32
_OspfPmShamLinkStatsHelloMismatch_Object = MibTableColumn
ospfPmShamLinkStatsHelloMismatch = _OspfPmShamLinkStatsHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 53),
    _OspfPmShamLinkStatsHelloMismatch_Type()
)
ospfPmShamLinkStatsHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsHelloMismatch.setStatus("current")
_OspfPmShamLinkStatsDeadMismatch_Type = Counter32
_OspfPmShamLinkStatsDeadMismatch_Object = MibTableColumn
ospfPmShamLinkStatsDeadMismatch = _OspfPmShamLinkStatsDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 54),
    _OspfPmShamLinkStatsDeadMismatch_Type()
)
ospfPmShamLinkStatsDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsDeadMismatch.setStatus("current")
_OspfPmShamLinkStatsOptionsMsmtch_Type = Counter32
_OspfPmShamLinkStatsOptionsMsmtch_Object = MibTableColumn
ospfPmShamLinkStatsOptionsMsmtch = _OspfPmShamLinkStatsOptionsMsmtch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 55),
    _OspfPmShamLinkStatsOptionsMsmtch_Type()
)
ospfPmShamLinkStatsOptionsMsmtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsOptionsMsmtch.setStatus("current")
_OspfPmShamLinkStatsNbrAdminDown_Type = Counter32
_OspfPmShamLinkStatsNbrAdminDown_Object = MibTableColumn
ospfPmShamLinkStatsNbrAdminDown = _OspfPmShamLinkStatsNbrAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 56),
    _OspfPmShamLinkStatsNbrAdminDown_Type()
)
ospfPmShamLinkStatsNbrAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsNbrAdminDown.setStatus("current")
_OspfPmShamLinkStatsPktLocalAddr_Type = Counter32
_OspfPmShamLinkStatsPktLocalAddr_Object = MibTableColumn
ospfPmShamLinkStatsPktLocalAddr = _OspfPmShamLinkStatsPktLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 57),
    _OspfPmShamLinkStatsPktLocalAddr_Type()
)
ospfPmShamLinkStatsPktLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsPktLocalAddr.setStatus("current")
_OspfPmShamLinkStatsMaIfNotP2p_Type = Counter32
_OspfPmShamLinkStatsMaIfNotP2p_Object = MibTableColumn
ospfPmShamLinkStatsMaIfNotP2p = _OspfPmShamLinkStatsMaIfNotP2p_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 58),
    _OspfPmShamLinkStatsMaIfNotP2p_Type()
)
ospfPmShamLinkStatsMaIfNotP2p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsMaIfNotP2p.setStatus("current")
_OspfPmShamLinkStatsBadPacket_Type = Counter32
_OspfPmShamLinkStatsBadPacket_Object = MibTableColumn
ospfPmShamLinkStatsBadPacket = _OspfPmShamLinkStatsBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 34, 1, 59),
    _OspfPmShamLinkStatsBadPacket_Type()
)
ospfPmShamLinkStatsBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmShamLinkStatsBadPacket.setStatus("current")
_OspfPmMaIfStatsTable_Object = MibTable
ospfPmMaIfStatsTable = _OspfPmMaIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35)
)
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTable.setStatus("current")
_OspfPmMaIfStatsEntry_Object = MibTableRow
ospfPmMaIfStatsEntry = _OspfPmMaIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1)
)
ospfPmMaIfStatsEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmMaIfStatsApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmMaIfStatsIpAddress"),
    (0, "DC-OSPF-MIB", "ospfPmMaIfStatsAddressLessIf"),
    (0, "DC-OSPF-MIB", "ospfPmMaIfStatsAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmMaIfStatsRemoteAddr"),
)
if mibBuilder.loadTexts:
    ospfPmMaIfStatsEntry.setStatus("current")
_OspfPmMaIfStatsApplIndex_Type = OspfPmIndex
_OspfPmMaIfStatsApplIndex_Object = MibTableColumn
ospfPmMaIfStatsApplIndex = _OspfPmMaIfStatsApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 1),
    _OspfPmMaIfStatsApplIndex_Type()
)
ospfPmMaIfStatsApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsApplIndex.setStatus("current")
_OspfPmMaIfStatsIpAddress_Type = IpAddress
_OspfPmMaIfStatsIpAddress_Object = MibTableColumn
ospfPmMaIfStatsIpAddress = _OspfPmMaIfStatsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 2),
    _OspfPmMaIfStatsIpAddress_Type()
)
ospfPmMaIfStatsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsIpAddress.setStatus("current")
_OspfPmMaIfStatsAddressLessIf_Type = InterfaceIndexOrZero
_OspfPmMaIfStatsAddressLessIf_Object = MibTableColumn
ospfPmMaIfStatsAddressLessIf = _OspfPmMaIfStatsAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 3),
    _OspfPmMaIfStatsAddressLessIf_Type()
)
ospfPmMaIfStatsAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsAddressLessIf.setStatus("current")
_OspfPmMaIfStatsAreaId_Type = AreaID
_OspfPmMaIfStatsAreaId_Object = MibTableColumn
ospfPmMaIfStatsAreaId = _OspfPmMaIfStatsAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 4),
    _OspfPmMaIfStatsAreaId_Type()
)
ospfPmMaIfStatsAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsAreaId.setStatus("current")
_OspfPmMaIfStatsRemoteAddr_Type = IpAddress
_OspfPmMaIfStatsRemoteAddr_Object = MibTableColumn
ospfPmMaIfStatsRemoteAddr = _OspfPmMaIfStatsRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 5),
    _OspfPmMaIfStatsRemoteAddr_Type()
)
ospfPmMaIfStatsRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRemoteAddr.setStatus("current")
_OspfPmMaIfStatsRxInvalid_Type = Counter32
_OspfPmMaIfStatsRxInvalid_Object = MibTableColumn
ospfPmMaIfStatsRxInvalid = _OspfPmMaIfStatsRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 6),
    _OspfPmMaIfStatsRxInvalid_Type()
)
ospfPmMaIfStatsRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxInvalid.setStatus("current")
_OspfPmMaIfStatsRxInvalidByte_Type = Counter32
_OspfPmMaIfStatsRxInvalidByte_Object = MibTableColumn
ospfPmMaIfStatsRxInvalidByte = _OspfPmMaIfStatsRxInvalidByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 7),
    _OspfPmMaIfStatsRxInvalidByte_Type()
)
ospfPmMaIfStatsRxInvalidByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxInvalidByte.setStatus("current")
_OspfPmMaIfStatsRxHello_Type = Counter32
_OspfPmMaIfStatsRxHello_Object = MibTableColumn
ospfPmMaIfStatsRxHello = _OspfPmMaIfStatsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 8),
    _OspfPmMaIfStatsRxHello_Type()
)
ospfPmMaIfStatsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxHello.setStatus("current")
_OspfPmMaIfStatsRxHelloByte_Type = Counter32
_OspfPmMaIfStatsRxHelloByte_Object = MibTableColumn
ospfPmMaIfStatsRxHelloByte = _OspfPmMaIfStatsRxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 9),
    _OspfPmMaIfStatsRxHelloByte_Type()
)
ospfPmMaIfStatsRxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxHelloByte.setStatus("current")
_OspfPmMaIfStatsRxDbDes_Type = Counter32
_OspfPmMaIfStatsRxDbDes_Object = MibTableColumn
ospfPmMaIfStatsRxDbDes = _OspfPmMaIfStatsRxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 10),
    _OspfPmMaIfStatsRxDbDes_Type()
)
ospfPmMaIfStatsRxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxDbDes.setStatus("current")
_OspfPmMaIfStatsRxDbDesByte_Type = Counter32
_OspfPmMaIfStatsRxDbDesByte_Object = MibTableColumn
ospfPmMaIfStatsRxDbDesByte = _OspfPmMaIfStatsRxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 11),
    _OspfPmMaIfStatsRxDbDesByte_Type()
)
ospfPmMaIfStatsRxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxDbDesByte.setStatus("current")
_OspfPmMaIfStatsRxLsReq_Type = Counter32
_OspfPmMaIfStatsRxLsReq_Object = MibTableColumn
ospfPmMaIfStatsRxLsReq = _OspfPmMaIfStatsRxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 12),
    _OspfPmMaIfStatsRxLsReq_Type()
)
ospfPmMaIfStatsRxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxLsReq.setStatus("current")
_OspfPmMaIfStatsRxLsReqByte_Type = Counter32
_OspfPmMaIfStatsRxLsReqByte_Object = MibTableColumn
ospfPmMaIfStatsRxLsReqByte = _OspfPmMaIfStatsRxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 13),
    _OspfPmMaIfStatsRxLsReqByte_Type()
)
ospfPmMaIfStatsRxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxLsReqByte.setStatus("current")
_OspfPmMaIfStatsRxLsUpd_Type = Counter32
_OspfPmMaIfStatsRxLsUpd_Object = MibTableColumn
ospfPmMaIfStatsRxLsUpd = _OspfPmMaIfStatsRxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 14),
    _OspfPmMaIfStatsRxLsUpd_Type()
)
ospfPmMaIfStatsRxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxLsUpd.setStatus("current")
_OspfPmMaIfStatsRxLsUpdByte_Type = Counter32
_OspfPmMaIfStatsRxLsUpdByte_Object = MibTableColumn
ospfPmMaIfStatsRxLsUpdByte = _OspfPmMaIfStatsRxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 15),
    _OspfPmMaIfStatsRxLsUpdByte_Type()
)
ospfPmMaIfStatsRxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxLsUpdByte.setStatus("current")
_OspfPmMaIfStatsRxLsAck_Type = Counter32
_OspfPmMaIfStatsRxLsAck_Object = MibTableColumn
ospfPmMaIfStatsRxLsAck = _OspfPmMaIfStatsRxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 16),
    _OspfPmMaIfStatsRxLsAck_Type()
)
ospfPmMaIfStatsRxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxLsAck.setStatus("current")
_OspfPmMaIfStatsRxLsAckByte_Type = Counter32
_OspfPmMaIfStatsRxLsAckByte_Object = MibTableColumn
ospfPmMaIfStatsRxLsAckByte = _OspfPmMaIfStatsRxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 17),
    _OspfPmMaIfStatsRxLsAckByte_Type()
)
ospfPmMaIfStatsRxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsRxLsAckByte.setStatus("current")
_OspfPmMaIfStatsTxFailed_Type = Counter32
_OspfPmMaIfStatsTxFailed_Object = MibTableColumn
ospfPmMaIfStatsTxFailed = _OspfPmMaIfStatsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 18),
    _OspfPmMaIfStatsTxFailed_Type()
)
ospfPmMaIfStatsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxFailed.setStatus("current")
_OspfPmMaIfStatsTxFailedByte_Type = Counter32
_OspfPmMaIfStatsTxFailedByte_Object = MibTableColumn
ospfPmMaIfStatsTxFailedByte = _OspfPmMaIfStatsTxFailedByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 19),
    _OspfPmMaIfStatsTxFailedByte_Type()
)
ospfPmMaIfStatsTxFailedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxFailedByte.setStatus("current")
_OspfPmMaIfStatsTxHello_Type = Counter32
_OspfPmMaIfStatsTxHello_Object = MibTableColumn
ospfPmMaIfStatsTxHello = _OspfPmMaIfStatsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 20),
    _OspfPmMaIfStatsTxHello_Type()
)
ospfPmMaIfStatsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxHello.setStatus("current")
_OspfPmMaIfStatsTxHelloByte_Type = Counter32
_OspfPmMaIfStatsTxHelloByte_Object = MibTableColumn
ospfPmMaIfStatsTxHelloByte = _OspfPmMaIfStatsTxHelloByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 21),
    _OspfPmMaIfStatsTxHelloByte_Type()
)
ospfPmMaIfStatsTxHelloByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxHelloByte.setStatus("current")
_OspfPmMaIfStatsTxDbDes_Type = Counter32
_OspfPmMaIfStatsTxDbDes_Object = MibTableColumn
ospfPmMaIfStatsTxDbDes = _OspfPmMaIfStatsTxDbDes_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 22),
    _OspfPmMaIfStatsTxDbDes_Type()
)
ospfPmMaIfStatsTxDbDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxDbDes.setStatus("current")
_OspfPmMaIfStatsTxDbDesByte_Type = Counter32
_OspfPmMaIfStatsTxDbDesByte_Object = MibTableColumn
ospfPmMaIfStatsTxDbDesByte = _OspfPmMaIfStatsTxDbDesByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 23),
    _OspfPmMaIfStatsTxDbDesByte_Type()
)
ospfPmMaIfStatsTxDbDesByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxDbDesByte.setStatus("current")
_OspfPmMaIfStatsTxLsReq_Type = Counter32
_OspfPmMaIfStatsTxLsReq_Object = MibTableColumn
ospfPmMaIfStatsTxLsReq = _OspfPmMaIfStatsTxLsReq_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 24),
    _OspfPmMaIfStatsTxLsReq_Type()
)
ospfPmMaIfStatsTxLsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxLsReq.setStatus("current")
_OspfPmMaIfStatsTxLsReqByte_Type = Counter32
_OspfPmMaIfStatsTxLsReqByte_Object = MibTableColumn
ospfPmMaIfStatsTxLsReqByte = _OspfPmMaIfStatsTxLsReqByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 25),
    _OspfPmMaIfStatsTxLsReqByte_Type()
)
ospfPmMaIfStatsTxLsReqByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxLsReqByte.setStatus("current")
_OspfPmMaIfStatsTxLsUpd_Type = Counter32
_OspfPmMaIfStatsTxLsUpd_Object = MibTableColumn
ospfPmMaIfStatsTxLsUpd = _OspfPmMaIfStatsTxLsUpd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 26),
    _OspfPmMaIfStatsTxLsUpd_Type()
)
ospfPmMaIfStatsTxLsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxLsUpd.setStatus("current")
_OspfPmMaIfStatsTxLsUpdByte_Type = Counter32
_OspfPmMaIfStatsTxLsUpdByte_Object = MibTableColumn
ospfPmMaIfStatsTxLsUpdByte = _OspfPmMaIfStatsTxLsUpdByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 27),
    _OspfPmMaIfStatsTxLsUpdByte_Type()
)
ospfPmMaIfStatsTxLsUpdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxLsUpdByte.setStatus("current")
_OspfPmMaIfStatsTxLsAck_Type = Counter32
_OspfPmMaIfStatsTxLsAck_Object = MibTableColumn
ospfPmMaIfStatsTxLsAck = _OspfPmMaIfStatsTxLsAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 28),
    _OspfPmMaIfStatsTxLsAck_Type()
)
ospfPmMaIfStatsTxLsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxLsAck.setStatus("current")
_OspfPmMaIfStatsTxLsAckByte_Type = Counter32
_OspfPmMaIfStatsTxLsAckByte_Object = MibTableColumn
ospfPmMaIfStatsTxLsAckByte = _OspfPmMaIfStatsTxLsAckByte_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 29),
    _OspfPmMaIfStatsTxLsAckByte_Type()
)
ospfPmMaIfStatsTxLsAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsTxLsAckByte.setStatus("current")
_OspfPmMaIfStatsLength_Type = Counter32
_OspfPmMaIfStatsLength_Object = MibTableColumn
ospfPmMaIfStatsLength = _OspfPmMaIfStatsLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 30),
    _OspfPmMaIfStatsLength_Type()
)
ospfPmMaIfStatsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsLength.setStatus("current")
_OspfPmMaIfStatsCksum_Type = Counter32
_OspfPmMaIfStatsCksum_Object = MibTableColumn
ospfPmMaIfStatsCksum = _OspfPmMaIfStatsCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 31),
    _OspfPmMaIfStatsCksum_Type()
)
ospfPmMaIfStatsCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsCksum.setStatus("current")
_OspfPmMaIfStatsVersion_Type = Counter32
_OspfPmMaIfStatsVersion_Object = MibTableColumn
ospfPmMaIfStatsVersion = _OspfPmMaIfStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 32),
    _OspfPmMaIfStatsVersion_Type()
)
ospfPmMaIfStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsVersion.setStatus("current")
_OspfPmMaIfStatsBadSrc_Type = Counter32
_OspfPmMaIfStatsBadSrc_Object = MibTableColumn
ospfPmMaIfStatsBadSrc = _OspfPmMaIfStatsBadSrc_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 33),
    _OspfPmMaIfStatsBadSrc_Type()
)
ospfPmMaIfStatsBadSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsBadSrc.setStatus("current")
_OspfPmMaIfStatsAreaMismatch_Type = Counter32
_OspfPmMaIfStatsAreaMismatch_Object = MibTableColumn
ospfPmMaIfStatsAreaMismatch = _OspfPmMaIfStatsAreaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 34),
    _OspfPmMaIfStatsAreaMismatch_Type()
)
ospfPmMaIfStatsAreaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsAreaMismatch.setStatus("current")
_OspfPmMaIfStatsSelfOrig_Type = Counter32
_OspfPmMaIfStatsSelfOrig_Object = MibTableColumn
ospfPmMaIfStatsSelfOrig = _OspfPmMaIfStatsSelfOrig_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 35),
    _OspfPmMaIfStatsSelfOrig_Type()
)
ospfPmMaIfStatsSelfOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsSelfOrig.setStatus("current")
_OspfPmMaIfStatsDupeId_Type = Counter32
_OspfPmMaIfStatsDupeId_Object = MibTableColumn
ospfPmMaIfStatsDupeId = _OspfPmMaIfStatsDupeId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 36),
    _OspfPmMaIfStatsDupeId_Type()
)
ospfPmMaIfStatsDupeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsDupeId.setStatus("current")
_OspfPmMaIfStatsHello_Type = Counter32
_OspfPmMaIfStatsHello_Object = MibTableColumn
ospfPmMaIfStatsHello = _OspfPmMaIfStatsHello_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 37),
    _OspfPmMaIfStatsHello_Type()
)
ospfPmMaIfStatsHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsHello.setStatus("current")
_OspfPmMaIfStatsMtuMismatch_Type = Counter32
_OspfPmMaIfStatsMtuMismatch_Object = MibTableColumn
ospfPmMaIfStatsMtuMismatch = _OspfPmMaIfStatsMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 38),
    _OspfPmMaIfStatsMtuMismatch_Type()
)
ospfPmMaIfStatsMtuMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsMtuMismatch.setStatus("current")
_OspfPmMaIfStatsNbrIgnored_Type = Counter32
_OspfPmMaIfStatsNbrIgnored_Object = MibTableColumn
ospfPmMaIfStatsNbrIgnored = _OspfPmMaIfStatsNbrIgnored_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 39),
    _OspfPmMaIfStatsNbrIgnored_Type()
)
ospfPmMaIfStatsNbrIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsNbrIgnored.setStatus("current")
_OspfPmMaIfStatsAuth_Type = Counter32
_OspfPmMaIfStatsAuth_Object = MibTableColumn
ospfPmMaIfStatsAuth = _OspfPmMaIfStatsAuth_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 40),
    _OspfPmMaIfStatsAuth_Type()
)
ospfPmMaIfStatsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsAuth.setStatus("current")
_OspfPmMaIfStatsWrongProto_Type = Counter32
_OspfPmMaIfStatsWrongProto_Object = MibTableColumn
ospfPmMaIfStatsWrongProto = _OspfPmMaIfStatsWrongProto_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 41),
    _OspfPmMaIfStatsWrongProto_Type()
)
ospfPmMaIfStatsWrongProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsWrongProto.setStatus("current")
_OspfPmMaIfStatsResourceErr_Type = Counter32
_OspfPmMaIfStatsResourceErr_Object = MibTableColumn
ospfPmMaIfStatsResourceErr = _OspfPmMaIfStatsResourceErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 42),
    _OspfPmMaIfStatsResourceErr_Type()
)
ospfPmMaIfStatsResourceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsResourceErr.setStatus("current")
_OspfPmMaIfStatsVirtMaIfClash_Type = Counter32
_OspfPmMaIfStatsVirtMaIfClash_Object = MibTableColumn
ospfPmMaIfStatsVirtMaIfClash = _OspfPmMaIfStatsVirtMaIfClash_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 43),
    _OspfPmMaIfStatsVirtMaIfClash_Type()
)
ospfPmMaIfStatsVirtMaIfClash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsVirtMaIfClash.setStatus("current")
_OspfPmMaIfStatsBadLsaLen_Type = Counter32
_OspfPmMaIfStatsBadLsaLen_Object = MibTableColumn
ospfPmMaIfStatsBadLsaLen = _OspfPmMaIfStatsBadLsaLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 44),
    _OspfPmMaIfStatsBadLsaLen_Type()
)
ospfPmMaIfStatsBadLsaLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsBadLsaLen.setStatus("current")
_OspfPmMaIfStatsLsaBadType_Type = Counter32
_OspfPmMaIfStatsLsaBadType_Object = MibTableColumn
ospfPmMaIfStatsLsaBadType = _OspfPmMaIfStatsLsaBadType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 45),
    _OspfPmMaIfStatsLsaBadType_Type()
)
ospfPmMaIfStatsLsaBadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsLsaBadType.setStatus("current")
_OspfPmMaIfStatsLsaBadLen_Type = Counter32
_OspfPmMaIfStatsLsaBadLen_Object = MibTableColumn
ospfPmMaIfStatsLsaBadLen = _OspfPmMaIfStatsLsaBadLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 46),
    _OspfPmMaIfStatsLsaBadLen_Type()
)
ospfPmMaIfStatsLsaBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsLsaBadLen.setStatus("current")
_OspfPmMaIfStatsLsaBadData_Type = Counter32
_OspfPmMaIfStatsLsaBadData_Object = MibTableColumn
ospfPmMaIfStatsLsaBadData = _OspfPmMaIfStatsLsaBadData_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 47),
    _OspfPmMaIfStatsLsaBadData_Type()
)
ospfPmMaIfStatsLsaBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsLsaBadData.setStatus("current")
_OspfPmMaIfStatsLsaBadCksum_Type = Counter32
_OspfPmMaIfStatsLsaBadCksum_Object = MibTableColumn
ospfPmMaIfStatsLsaBadCksum = _OspfPmMaIfStatsLsaBadCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 48),
    _OspfPmMaIfStatsLsaBadCksum_Type()
)
ospfPmMaIfStatsLsaBadCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsLsaBadCksum.setStatus("current")
_OspfPmMaIfStatsUnkNbmaNbr_Type = Counter32
_OspfPmMaIfStatsUnkNbmaNbr_Object = MibTableColumn
ospfPmMaIfStatsUnkNbmaNbr = _OspfPmMaIfStatsUnkNbmaNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 49),
    _OspfPmMaIfStatsUnkNbmaNbr_Type()
)
ospfPmMaIfStatsUnkNbmaNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsUnkNbmaNbr.setStatus("current")
_OspfPmMaIfStatsUnkVirtNbr_Type = Counter32
_OspfPmMaIfStatsUnkVirtNbr_Object = MibTableColumn
ospfPmMaIfStatsUnkVirtNbr = _OspfPmMaIfStatsUnkVirtNbr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 50),
    _OspfPmMaIfStatsUnkVirtNbr_Type()
)
ospfPmMaIfStatsUnkVirtNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsUnkVirtNbr.setStatus("current")
_OspfPmMaIfStatsAuthMismatch_Type = Counter32
_OspfPmMaIfStatsAuthMismatch_Object = MibTableColumn
ospfPmMaIfStatsAuthMismatch = _OspfPmMaIfStatsAuthMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 51),
    _OspfPmMaIfStatsAuthMismatch_Type()
)
ospfPmMaIfStatsAuthMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsAuthMismatch.setStatus("current")
_OspfPmMaIfStatsAuthFailure_Type = Counter32
_OspfPmMaIfStatsAuthFailure_Object = MibTableColumn
ospfPmMaIfStatsAuthFailure = _OspfPmMaIfStatsAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 52),
    _OspfPmMaIfStatsAuthFailure_Type()
)
ospfPmMaIfStatsAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsAuthFailure.setStatus("current")
_OspfPmMaIfStatsNetmaskMismatch_Type = Counter32
_OspfPmMaIfStatsNetmaskMismatch_Object = MibTableColumn
ospfPmMaIfStatsNetmaskMismatch = _OspfPmMaIfStatsNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 53),
    _OspfPmMaIfStatsNetmaskMismatch_Type()
)
ospfPmMaIfStatsNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsNetmaskMismatch.setStatus("current")
_OspfPmMaIfStatsHelloMismatch_Type = Counter32
_OspfPmMaIfStatsHelloMismatch_Object = MibTableColumn
ospfPmMaIfStatsHelloMismatch = _OspfPmMaIfStatsHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 54),
    _OspfPmMaIfStatsHelloMismatch_Type()
)
ospfPmMaIfStatsHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsHelloMismatch.setStatus("current")
_OspfPmMaIfStatsDeadMismatch_Type = Counter32
_OspfPmMaIfStatsDeadMismatch_Object = MibTableColumn
ospfPmMaIfStatsDeadMismatch = _OspfPmMaIfStatsDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 55),
    _OspfPmMaIfStatsDeadMismatch_Type()
)
ospfPmMaIfStatsDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsDeadMismatch.setStatus("current")
_OspfPmMaIfStatsOptionsMismatch_Type = Counter32
_OspfPmMaIfStatsOptionsMismatch_Object = MibTableColumn
ospfPmMaIfStatsOptionsMismatch = _OspfPmMaIfStatsOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 56),
    _OspfPmMaIfStatsOptionsMismatch_Type()
)
ospfPmMaIfStatsOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsOptionsMismatch.setStatus("current")
_OspfPmMaIfStatsNbrAdminDown_Type = Counter32
_OspfPmMaIfStatsNbrAdminDown_Object = MibTableColumn
ospfPmMaIfStatsNbrAdminDown = _OspfPmMaIfStatsNbrAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 57),
    _OspfPmMaIfStatsNbrAdminDown_Type()
)
ospfPmMaIfStatsNbrAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsNbrAdminDown.setStatus("current")
_OspfPmMaIfStatsPktLocalAddr_Type = Counter32
_OspfPmMaIfStatsPktLocalAddr_Object = MibTableColumn
ospfPmMaIfStatsPktLocalAddr = _OspfPmMaIfStatsPktLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 58),
    _OspfPmMaIfStatsPktLocalAddr_Type()
)
ospfPmMaIfStatsPktLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsPktLocalAddr.setStatus("current")
_OspfPmMaIfStatsMaIfNotP2p_Type = Counter32
_OspfPmMaIfStatsMaIfNotP2p_Object = MibTableColumn
ospfPmMaIfStatsMaIfNotP2p = _OspfPmMaIfStatsMaIfNotP2p_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 59),
    _OspfPmMaIfStatsMaIfNotP2p_Type()
)
ospfPmMaIfStatsMaIfNotP2p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsMaIfNotP2p.setStatus("current")
_OspfPmMaIfStatsBadPacket_Type = Counter32
_OspfPmMaIfStatsBadPacket_Object = MibTableColumn
ospfPmMaIfStatsBadPacket = _OspfPmMaIfStatsBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 35, 1, 60),
    _OspfPmMaIfStatsBadPacket_Type()
)
ospfPmMaIfStatsBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmMaIfStatsBadPacket.setStatus("current")
_OspfNmEntStatsTable_Object = MibTable
ospfNmEntStatsTable = _OspfNmEntStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36)
)
if mibBuilder.loadTexts:
    ospfNmEntStatsTable.setStatus("current")
_OspfNmEntStatsEntry_Object = MibTableRow
ospfNmEntStatsEntry = _OspfNmEntStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1)
)
ospfNmEntStatsEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfNmEntStatsIndex"),
)
if mibBuilder.loadTexts:
    ospfNmEntStatsEntry.setStatus("current")
_OspfNmEntStatsIndex_Type = OspfPmIndex
_OspfNmEntStatsIndex_Object = MibTableColumn
ospfNmEntStatsIndex = _OspfNmEntStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 1),
    _OspfNmEntStatsIndex_Type()
)
ospfNmEntStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNmEntStatsIndex.setStatus("current")
_OspfNmEntStatsLength_Type = Counter32
_OspfNmEntStatsLength_Object = MibTableColumn
ospfNmEntStatsLength = _OspfNmEntStatsLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 2),
    _OspfNmEntStatsLength_Type()
)
ospfNmEntStatsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsLength.setStatus("current")
_OspfNmEntStatsNoIf_Type = Counter32
_OspfNmEntStatsNoIf_Object = MibTableColumn
ospfNmEntStatsNoIf = _OspfNmEntStatsNoIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 3),
    _OspfNmEntStatsNoIf_Type()
)
ospfNmEntStatsNoIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsNoIf.setStatus("current")
_OspfNmEntStatsNoVirtLink_Type = Counter32
_OspfNmEntStatsNoVirtLink_Object = MibTableColumn
ospfNmEntStatsNoVirtLink = _OspfNmEntStatsNoVirtLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 4),
    _OspfNmEntStatsNoVirtLink_Type()
)
ospfNmEntStatsNoVirtLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsNoVirtLink.setStatus("current")
_OspfNmEntStatsInstanceId_Type = Counter32
_OspfNmEntStatsInstanceId_Object = MibTableColumn
ospfNmEntStatsInstanceId = _OspfNmEntStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 5),
    _OspfNmEntStatsInstanceId_Type()
)
ospfNmEntStatsInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsInstanceId.setStatus("current")
_OspfNmEntStatsBadIpHdrLen_Type = Counter32
_OspfNmEntStatsBadIpHdrLen_Object = MibTableColumn
ospfNmEntStatsBadIpHdrLen = _OspfNmEntStatsBadIpHdrLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 6),
    _OspfNmEntStatsBadIpHdrLen_Type()
)
ospfNmEntStatsBadIpHdrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsBadIpHdrLen.setStatus("current")
_OspfNmEntStatsVersion_Type = Counter32
_OspfNmEntStatsVersion_Object = MibTableColumn
ospfNmEntStatsVersion = _OspfNmEntStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 7),
    _OspfNmEntStatsVersion_Type()
)
ospfNmEntStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsVersion.setStatus("current")
_OspfNmEntStatsBadSrc_Type = Counter32
_OspfNmEntStatsBadSrc_Object = MibTableColumn
ospfNmEntStatsBadSrc = _OspfNmEntStatsBadSrc_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 8),
    _OspfNmEntStatsBadSrc_Type()
)
ospfNmEntStatsBadSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsBadSrc.setStatus("current")
_OspfNmEntStatsResourceErr_Type = Counter32
_OspfNmEntStatsResourceErr_Object = MibTableColumn
ospfNmEntStatsResourceErr = _OspfNmEntStatsResourceErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 9),
    _OspfNmEntStatsResourceErr_Type()
)
ospfNmEntStatsResourceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsResourceErr.setStatus("current")
_OspfNmEntStatsBadPacket_Type = Counter32
_OspfNmEntStatsBadPacket_Object = MibTableColumn
ospfNmEntStatsBadPacket = _OspfNmEntStatsBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 36, 1, 10),
    _OspfNmEntStatsBadPacket_Type()
)
ospfNmEntStatsBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNmEntStatsBadPacket.setStatus("current")
_OspfPmSpfEntryTable_Object = MibTable
ospfPmSpfEntryTable = _OspfPmSpfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37)
)
if mibBuilder.loadTexts:
    ospfPmSpfEntryTable.setStatus("current")
_OspfPmSpfEntryEntry_Object = MibTableRow
ospfPmSpfEntryEntry = _OspfPmSpfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1)
)
ospfPmSpfEntryEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmSpfEntryApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmSpfEntryAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmSpfEntryRtrId"),
    (0, "DC-OSPF-MIB", "ospfPmSpfEntryNextHopIdx"),
)
if mibBuilder.loadTexts:
    ospfPmSpfEntryEntry.setStatus("current")
_OspfPmSpfEntryApplIndex_Type = NumericIndex
_OspfPmSpfEntryApplIndex_Object = MibTableColumn
ospfPmSpfEntryApplIndex = _OspfPmSpfEntryApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 1),
    _OspfPmSpfEntryApplIndex_Type()
)
ospfPmSpfEntryApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSpfEntryApplIndex.setStatus("current")
_OspfPmSpfEntryAreaId_Type = AreaID
_OspfPmSpfEntryAreaId_Object = MibTableColumn
ospfPmSpfEntryAreaId = _OspfPmSpfEntryAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 2),
    _OspfPmSpfEntryAreaId_Type()
)
ospfPmSpfEntryAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSpfEntryAreaId.setStatus("current")
_OspfPmSpfEntryRtrId_Type = RouterID
_OspfPmSpfEntryRtrId_Object = MibTableColumn
ospfPmSpfEntryRtrId = _OspfPmSpfEntryRtrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 3),
    _OspfPmSpfEntryRtrId_Type()
)
ospfPmSpfEntryRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSpfEntryRtrId.setStatus("current")


class _OspfPmSpfEntryNextHopIdx_Type(Unsigned32):
    """Custom type ospfPmSpfEntryNextHopIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OspfPmSpfEntryNextHopIdx_Type.__name__ = "Unsigned32"
_OspfPmSpfEntryNextHopIdx_Object = MibTableColumn
ospfPmSpfEntryNextHopIdx = _OspfPmSpfEntryNextHopIdx_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 4),
    _OspfPmSpfEntryNextHopIdx_Type()
)
ospfPmSpfEntryNextHopIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmSpfEntryNextHopIdx.setStatus("current")
_OspfPmSpfEntryNextHopAddr_Type = IpAddress
_OspfPmSpfEntryNextHopAddr_Object = MibTableColumn
ospfPmSpfEntryNextHopAddr = _OspfPmSpfEntryNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 5),
    _OspfPmSpfEntryNextHopAddr_Type()
)
ospfPmSpfEntryNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryNextHopAddr.setStatus("current")
_OspfPmSpfEntryIfIndex_Type = InterfaceIndex
_OspfPmSpfEntryIfIndex_Object = MibTableColumn
ospfPmSpfEntryIfIndex = _OspfPmSpfEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 6),
    _OspfPmSpfEntryIfIndex_Type()
)
ospfPmSpfEntryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryIfIndex.setStatus("current")
_OspfPmSpfEntryCost_Type = BigMetric
_OspfPmSpfEntryCost_Object = MibTableColumn
ospfPmSpfEntryCost = _OspfPmSpfEntryCost_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 7),
    _OspfPmSpfEntryCost_Type()
)
ospfPmSpfEntryCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryCost.setStatus("current")
_OspfPmSpfEntryIsASBR_Type = TruthValue
_OspfPmSpfEntryIsASBR_Object = MibTableColumn
ospfPmSpfEntryIsASBR = _OspfPmSpfEntryIsASBR_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 8),
    _OspfPmSpfEntryIsASBR_Type()
)
ospfPmSpfEntryIsASBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryIsASBR.setStatus("current")
_OspfPmSpfEntryIsABR_Type = TruthValue
_OspfPmSpfEntryIsABR_Object = MibTableColumn
ospfPmSpfEntryIsABR = _OspfPmSpfEntryIsABR_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 9),
    _OspfPmSpfEntryIsABR_Type()
)
ospfPmSpfEntryIsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryIsABR.setStatus("current")
_OspfPmSpfEntryIsVirtEndpt_Type = TruthValue
_OspfPmSpfEntryIsVirtEndpt_Object = MibTableColumn
ospfPmSpfEntryIsVirtEndpt = _OspfPmSpfEntryIsVirtEndpt_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 10),
    _OspfPmSpfEntryIsVirtEndpt_Type()
)
ospfPmSpfEntryIsVirtEndpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryIsVirtEndpt.setStatus("current")
_OspfPmSpfEntryCalcIndex_Type = Unsigned32
_OspfPmSpfEntryCalcIndex_Object = MibTableColumn
ospfPmSpfEntryCalcIndex = _OspfPmSpfEntryCalcIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 37, 1, 11),
    _OspfPmSpfEntryCalcIndex_Type()
)
ospfPmSpfEntryCalcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmSpfEntryCalcIndex.setStatus("current")
_OspfPmRouteTable_Object = MibTable
ospfPmRouteTable = _OspfPmRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38)
)
if mibBuilder.loadTexts:
    ospfPmRouteTable.setStatus("current")
_OspfPmRouteEntry_Object = MibTableRow
ospfPmRouteEntry = _OspfPmRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1)
)
ospfPmRouteEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmRouteApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmRouteAddrPrefix"),
    (0, "DC-OSPF-MIB", "ospfPmRouteAddrPrefixLen"),
    (0, "DC-OSPF-MIB", "ospfPmRouteNextHopIdx"),
)
if mibBuilder.loadTexts:
    ospfPmRouteEntry.setStatus("current")
_OspfPmRouteApplIndex_Type = NumericIndex
_OspfPmRouteApplIndex_Object = MibTableColumn
ospfPmRouteApplIndex = _OspfPmRouteApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 1),
    _OspfPmRouteApplIndex_Type()
)
ospfPmRouteApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouteApplIndex.setStatus("current")
_OspfPmRouteAddrPrefix_Type = IpAddress
_OspfPmRouteAddrPrefix_Object = MibTableColumn
ospfPmRouteAddrPrefix = _OspfPmRouteAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 2),
    _OspfPmRouteAddrPrefix_Type()
)
ospfPmRouteAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouteAddrPrefix.setStatus("current")


class _OspfPmRouteAddrPrefixLen_Type(Integer32):
    """Custom type ospfPmRouteAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OspfPmRouteAddrPrefixLen_Type.__name__ = "Integer32"
_OspfPmRouteAddrPrefixLen_Object = MibTableColumn
ospfPmRouteAddrPrefixLen = _OspfPmRouteAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 3),
    _OspfPmRouteAddrPrefixLen_Type()
)
ospfPmRouteAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouteAddrPrefixLen.setStatus("current")
_OspfPmRouteNextHopIdx_Type = Unsigned32
_OspfPmRouteNextHopIdx_Object = MibTableColumn
ospfPmRouteNextHopIdx = _OspfPmRouteNextHopIdx_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 4),
    _OspfPmRouteNextHopIdx_Type()
)
ospfPmRouteNextHopIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouteNextHopIdx.setStatus("current")
_OspfPmRouteNextHopAddr_Type = IpAddress
_OspfPmRouteNextHopAddr_Object = MibTableColumn
ospfPmRouteNextHopAddr = _OspfPmRouteNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 5),
    _OspfPmRouteNextHopAddr_Type()
)
ospfPmRouteNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouteNextHopAddr.setStatus("current")
_OspfPmRouteIfIndex_Type = InterfaceIndex
_OspfPmRouteIfIndex_Object = MibTableColumn
ospfPmRouteIfIndex = _OspfPmRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 6),
    _OspfPmRouteIfIndex_Type()
)
ospfPmRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouteIfIndex.setStatus("current")
_OspfPmRouteAreaId_Type = AreaID
_OspfPmRouteAreaId_Object = MibTableColumn
ospfPmRouteAreaId = _OspfPmRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 7),
    _OspfPmRouteAreaId_Type()
)
ospfPmRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouteAreaId.setStatus("current")
_OspfPmRouteCost_Type = BigMetric
_OspfPmRouteCost_Object = MibTableColumn
ospfPmRouteCost = _OspfPmRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 8),
    _OspfPmRouteCost_Type()
)
ospfPmRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouteCost.setStatus("current")
_OspfPmRoutePathType_Type = OspfPathType
_OspfPmRoutePathType_Object = MibTableColumn
ospfPmRoutePathType = _OspfPmRoutePathType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 9),
    _OspfPmRoutePathType_Type()
)
ospfPmRoutePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRoutePathType.setStatus("current")
_OspfPmRouteCalcIndex_Type = Unsigned32
_OspfPmRouteCalcIndex_Object = MibTableColumn
ospfPmRouteCalcIndex = _OspfPmRouteCalcIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 38, 1, 10),
    _OspfPmRouteCalcIndex_Type()
)
ospfPmRouteCalcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouteCalcIndex.setStatus("current")
_OspfPmRouterDestTable_Object = MibTable
ospfPmRouterDestTable = _OspfPmRouterDestTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39)
)
if mibBuilder.loadTexts:
    ospfPmRouterDestTable.setStatus("current")
_OspfPmRouterDestEntry_Object = MibTableRow
ospfPmRouterDestEntry = _OspfPmRouterDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1)
)
ospfPmRouterDestEntry.setIndexNames(
    (0, "DC-OSPF-MIB", "ospfPmRouterDestApplIndex"),
    (0, "DC-OSPF-MIB", "ospfPmRouterDestRouterId"),
    (0, "DC-OSPF-MIB", "ospfPmRouterDestAreaId"),
    (0, "DC-OSPF-MIB", "ospfPmRouterDestNextHopIdx"),
)
if mibBuilder.loadTexts:
    ospfPmRouterDestEntry.setStatus("current")
_OspfPmRouterDestApplIndex_Type = NumericIndex
_OspfPmRouterDestApplIndex_Object = MibTableColumn
ospfPmRouterDestApplIndex = _OspfPmRouterDestApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 1),
    _OspfPmRouterDestApplIndex_Type()
)
ospfPmRouterDestApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouterDestApplIndex.setStatus("current")
_OspfPmRouterDestRouterId_Type = RouterID
_OspfPmRouterDestRouterId_Object = MibTableColumn
ospfPmRouterDestRouterId = _OspfPmRouterDestRouterId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 2),
    _OspfPmRouterDestRouterId_Type()
)
ospfPmRouterDestRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouterDestRouterId.setStatus("current")
_OspfPmRouterDestAreaId_Type = AreaID
_OspfPmRouterDestAreaId_Object = MibTableColumn
ospfPmRouterDestAreaId = _OspfPmRouterDestAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 3),
    _OspfPmRouterDestAreaId_Type()
)
ospfPmRouterDestAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouterDestAreaId.setStatus("current")
_OspfPmRouterDestNextHopIdx_Type = Unsigned32
_OspfPmRouterDestNextHopIdx_Object = MibTableColumn
ospfPmRouterDestNextHopIdx = _OspfPmRouterDestNextHopIdx_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 4),
    _OspfPmRouterDestNextHopIdx_Type()
)
ospfPmRouterDestNextHopIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfPmRouterDestNextHopIdx.setStatus("current")
_OspfPmRouterDestNextHopAddr_Type = IpAddress
_OspfPmRouterDestNextHopAddr_Object = MibTableColumn
ospfPmRouterDestNextHopAddr = _OspfPmRouterDestNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 5),
    _OspfPmRouterDestNextHopAddr_Type()
)
ospfPmRouterDestNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestNextHopAddr.setStatus("current")
_OspfPmRouterDestIfIndex_Type = InterfaceIndex
_OspfPmRouterDestIfIndex_Object = MibTableColumn
ospfPmRouterDestIfIndex = _OspfPmRouterDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 6),
    _OspfPmRouterDestIfIndex_Type()
)
ospfPmRouterDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestIfIndex.setStatus("current")
_OspfPmRouterDestCost_Type = BigMetric
_OspfPmRouterDestCost_Object = MibTableColumn
ospfPmRouterDestCost = _OspfPmRouterDestCost_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 7),
    _OspfPmRouterDestCost_Type()
)
ospfPmRouterDestCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestCost.setStatus("current")
_OspfPmRouterDestIsASBR_Type = TruthValue
_OspfPmRouterDestIsASBR_Object = MibTableColumn
ospfPmRouterDestIsASBR = _OspfPmRouterDestIsASBR_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 8),
    _OspfPmRouterDestIsASBR_Type()
)
ospfPmRouterDestIsASBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestIsASBR.setStatus("current")
_OspfPmRouterDestIsABR_Type = TruthValue
_OspfPmRouterDestIsABR_Object = MibTableColumn
ospfPmRouterDestIsABR = _OspfPmRouterDestIsABR_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 9),
    _OspfPmRouterDestIsABR_Type()
)
ospfPmRouterDestIsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestIsABR.setStatus("current")
_OspfPmRouterDestIsVirtEndpt_Type = TruthValue
_OspfPmRouterDestIsVirtEndpt_Object = MibTableColumn
ospfPmRouterDestIsVirtEndpt = _OspfPmRouterDestIsVirtEndpt_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 10),
    _OspfPmRouterDestIsVirtEndpt_Type()
)
ospfPmRouterDestIsVirtEndpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestIsVirtEndpt.setStatus("current")
_OspfPmRouterDestPathType_Type = OspfPathType
_OspfPmRouterDestPathType_Object = MibTableColumn
ospfPmRouterDestPathType = _OspfPmRouterDestPathType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 11),
    _OspfPmRouterDestPathType_Type()
)
ospfPmRouterDestPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestPathType.setStatus("current")
_OspfPmRouterDestCalcIndex_Type = Unsigned32
_OspfPmRouterDestCalcIndex_Object = MibTableColumn
ospfPmRouterDestCalcIndex = _OspfPmRouterDestCalcIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 1, 39, 1, 12),
    _OspfPmRouterDestCalcIndex_Type()
)
ospfPmRouterDestCalcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPmRouterDestCalcIndex.setStatus("current")
_OspfConformance_ObjectIdentity = ObjectIdentity
ospfConformance = _OspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2)
)
_OspfGroups_ObjectIdentity = ObjectIdentity
ospfGroups = _OspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1)
)
_OspfCompliances_ObjectIdentity = ObjectIdentity
ospfCompliances = _OspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 2)
)
_OspfTrap_ObjectIdentity = ObjectIdentity
ospfTrap = _OspfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3)
)
_OspfTraps_ObjectIdentity = ObjectIdentity
ospfTraps = _OspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0)
)
_OspfTrapControl_ObjectIdentity = ObjectIdentity
ospfTrapControl = _OspfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1)
)


class _OspfConfigErrorType_Type(Integer32):
    """Custom type ospfConfigErrorType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10),
          ("mtuMismatch", 11),
          ("duplicateRouterId", 12))
    )


_OspfConfigErrorType_Type.__name__ = "Integer32"
_OspfConfigErrorType_Object = MibScalar
ospfConfigErrorType = _OspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 1),
    _OspfConfigErrorType_Type()
)
ospfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfConfigErrorType.setStatus("current")


class _OspfPacketType_Type(Integer32):
    """Custom type ospfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5))
    )


_OspfPacketType_Type.__name__ = "Integer32"
_OspfPacketType_Object = MibScalar
ospfPacketType = _OspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 2),
    _OspfPacketType_Type()
)
ospfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPacketType.setStatus("current")
_OspfPacketSrc_Type = IpAddress
_OspfPacketSrc_Object = MibScalar
ospfPacketSrc = _OspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 3),
    _OspfPacketSrc_Type()
)
ospfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPacketSrc.setStatus("current")
_OspfTrapVirtIfAreaId_Type = AreaID
_OspfTrapVirtIfAreaId_Object = MibScalar
ospfTrapVirtIfAreaId = _OspfTrapVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 4),
    _OspfTrapVirtIfAreaId_Type()
)
ospfTrapVirtIfAreaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapVirtIfAreaId.setStatus("current")
_OspfTrapVirtIfNeighbor_Type = RouterID
_OspfTrapVirtIfNeighbor_Object = MibScalar
ospfTrapVirtIfNeighbor = _OspfTrapVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 5),
    _OspfTrapVirtIfNeighbor_Type()
)
ospfTrapVirtIfNeighbor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapVirtIfNeighbor.setStatus("current")
_OspfTrapPmEntIndex_Type = OspfPmIndex
_OspfTrapPmEntIndex_Object = MibScalar
ospfTrapPmEntIndex = _OspfTrapPmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 6),
    _OspfTrapPmEntIndex_Type()
)
ospfTrapPmEntIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapPmEntIndex.setStatus("current")
_OspfTrapNbrIpAddr_Type = IpAddress
_OspfTrapNbrIpAddr_Object = MibScalar
ospfTrapNbrIpAddr = _OspfTrapNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 7),
    _OspfTrapNbrIpAddr_Type()
)
ospfTrapNbrIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapNbrIpAddr.setStatus("current")
_OspfTrapNbrAddressLessIndex_Type = InterfaceIndexOrZero
_OspfTrapNbrAddressLessIndex_Object = MibScalar
ospfTrapNbrAddressLessIndex = _OspfTrapNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 8),
    _OspfTrapNbrAddressLessIndex_Type()
)
ospfTrapNbrAddressLessIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapNbrAddressLessIndex.setStatus("current")
_OspfTrapVirtNbrArea_Type = AreaID
_OspfTrapVirtNbrArea_Object = MibScalar
ospfTrapVirtNbrArea = _OspfTrapVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 9),
    _OspfTrapVirtNbrArea_Type()
)
ospfTrapVirtNbrArea.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapVirtNbrArea.setStatus("current")
_OspfTrapVirtNbrRtrId_Type = RouterID
_OspfTrapVirtNbrRtrId_Object = MibScalar
ospfTrapVirtNbrRtrId = _OspfTrapVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 10),
    _OspfTrapVirtNbrRtrId_Type()
)
ospfTrapVirtNbrRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapVirtNbrRtrId.setStatus("current")
_OspfTrapNmEntIndexValid_Type = TruthValue
_OspfTrapNmEntIndexValid_Object = MibScalar
ospfTrapNmEntIndexValid = _OspfTrapNmEntIndexValid_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 11),
    _OspfTrapNmEntIndexValid_Type()
)
ospfTrapNmEntIndexValid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapNmEntIndexValid.setStatus("current")
_OspfTrapNmEntIndex_Type = OspfPmIndex
_OspfTrapNmEntIndex_Object = MibScalar
ospfTrapNmEntIndex = _OspfTrapNmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 12),
    _OspfTrapNmEntIndex_Type()
)
ospfTrapNmEntIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapNmEntIndex.setStatus("current")
_OspfTrapIfIpAddress_Type = IpAddress
_OspfTrapIfIpAddress_Object = MibScalar
ospfTrapIfIpAddress = _OspfTrapIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 13),
    _OspfTrapIfIpAddress_Type()
)
ospfTrapIfIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapIfIpAddress.setStatus("current")
_OspfTrapAddressLessIf_Type = InterfaceIndexOrZero
_OspfTrapAddressLessIf_Object = MibScalar
ospfTrapAddressLessIf = _OspfTrapAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 14),
    _OspfTrapAddressLessIf_Type()
)
ospfTrapAddressLessIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapAddressLessIf.setStatus("current")
_OspfTrapAreaId_Type = AreaID
_OspfTrapAreaId_Object = MibScalar
ospfTrapAreaId = _OspfTrapAreaId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 1, 15),
    _OspfTrapAreaId_Type()
)
ospfTrapAreaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfTrapAreaId.setStatus("current")
_OspfTrapConformance_ObjectIdentity = ObjectIdentity
ospfTrapConformance = _OspfTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2)
)
_OspfTrapGroups_ObjectIdentity = ObjectIdentity
ospfTrapGroups = _OspfTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2, 1)
)
_OspfTrapCompliances_ObjectIdentity = ObjectIdentity
ospfTrapCompliances = _OspfTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2, 2)
)

# Managed Objects groups

ospfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 1)
)
ospfBasicGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfPmEntAdminStat"),
        ("DC-OSPF-MIB", "ospfPmEntVersionNumber"),
        ("DC-OSPF-MIB", "ospfPmEntAreaBdrRtrStatus"),
        ("DC-OSPF-MIB", "ospfPmEntASBdrRtrStatus"),
        ("DC-OSPF-MIB", "ospfPmEntExternLsaCount"),
        ("DC-OSPF-MIB", "ospfPmEntExternLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmEntTOSSupport"),
        ("DC-OSPF-MIB", "ospfPmEntOriginateNewLsas"),
        ("DC-OSPF-MIB", "ospfPmEntRxNewLsas"),
        ("DC-OSPF-MIB", "ospfPmEntExtLsdbLimit"),
        ("DC-OSPF-MIB", "ospfPmEntMulticastExtns"),
        ("DC-OSPF-MIB", "ospfPmEntExitOverflowIntvl"),
        ("DC-OSPF-MIB", "ospfPmEntDemandExtensions"))
)
if mibBuilder.loadTexts:
    ospfBasicGroup.setStatus("current")

ospfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 2)
)
ospfAreaGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmImportAsExtern"),
        ("DC-OSPF-MIB", "ospfPmSpfRuns"),
        ("DC-OSPF-MIB", "ospfPmAreaBdrRtrCount"),
        ("DC-OSPF-MIB", "ospfPmASBdrRtrCount"),
        ("DC-OSPF-MIB", "ospfPmAreaLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaSummary"),
        ("DC-OSPF-MIB", "ospfPmAreaOperStatus"),
        ("DC-OSPF-MIB", "ospfPmAreaAdminStatus"))
)
if mibBuilder.loadTexts:
    ospfAreaGroup.setStatus("current")

ospfStubAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 3)
)
ospfStubAreaGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmStubMetric"),
        ("DC-OSPF-MIB", "ospfPmStubStatus"),
        ("DC-OSPF-MIB", "ospfPmStubMetricType"))
)
if mibBuilder.loadTexts:
    ospfStubAreaGroup.setStatus("current")

ospfLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 4)
)
ospfLsdbGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmLsdbSequence"),
        ("DC-OSPF-MIB", "ospfPmLsdbAge"),
        ("DC-OSPF-MIB", "ospfPmLsdbChecksum"),
        ("DC-OSPF-MIB", "ospfPmLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfLsdbGroup.setStatus("current")

ospfHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 6)
)
ospfHostGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmHostMetric"),
        ("DC-OSPF-MIB", "ospfPmHostStatus"),
        ("DC-OSPF-MIB", "ospfPmHostAreaID"),
        ("DC-OSPF-MIB", "ospfPmHostOperStatus"),
        ("DC-OSPF-MIB", "ospfPmHostAdminStatus"))
)
if mibBuilder.loadTexts:
    ospfHostGroup.setStatus("current")

ospfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 7)
)
ospfIfGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmIfAreaId"),
        ("DC-OSPF-MIB", "ospfPmIfType"),
        ("DC-OSPF-MIB", "ospfPmIfAdminStat"),
        ("DC-OSPF-MIB", "ospfPmIfRtrPriority"),
        ("DC-OSPF-MIB", "ospfPmIfTransitDelay"),
        ("DC-OSPF-MIB", "ospfPmIfRetransInterval"),
        ("DC-OSPF-MIB", "ospfPmIfHelloInterval"),
        ("DC-OSPF-MIB", "ospfPmIfRtrDeadInterval"),
        ("DC-OSPF-MIB", "ospfPmIfPollInterval"),
        ("DC-OSPF-MIB", "ospfPmIfState"),
        ("DC-OSPF-MIB", "ospfPmIfDesignatedRouter"),
        ("DC-OSPF-MIB", "ospfPmIfBackupDesignatedRouter"),
        ("DC-OSPF-MIB", "ospfPmIfEvents"),
        ("DC-OSPF-MIB", "ospfPmIfAuthType"),
        ("DC-OSPF-MIB", "ospfPmIfAuthKey"),
        ("DC-OSPF-MIB", "ospfPmIfStatus"),
        ("DC-OSPF-MIB", "ospfPmIfMulticastForwarding"),
        ("DC-OSPF-MIB", "ospfPmIfDemand"))
)
if mibBuilder.loadTexts:
    ospfIfGroup.setStatus("current")

ospfIfMetricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 8)
)
ospfIfMetricGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmIfMetricValue"),
        ("DC-OSPF-MIB", "ospfPmIfMetricStatus"))
)
if mibBuilder.loadTexts:
    ospfIfMetricGroup.setStatus("current")

ospfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 9)
)
ospfVirtIfGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmVirtIfTransitDelay"),
        ("DC-OSPF-MIB", "ospfPmVirtIfRetransInterval"),
        ("DC-OSPF-MIB", "ospfPmVirtIfHelloInterval"),
        ("DC-OSPF-MIB", "ospfPmVirtIfRtrDeadInterval"),
        ("DC-OSPF-MIB", "ospfPmVirtIfState"),
        ("DC-OSPF-MIB", "ospfPmVirtIfEvents"),
        ("DC-OSPF-MIB", "ospfPmVirtIfAuthType"),
        ("DC-OSPF-MIB", "ospfPmVirtIfAuthKey"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatus"))
)
if mibBuilder.loadTexts:
    ospfVirtIfGroup.setStatus("current")

ospfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 10)
)
ospfNbrGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmNbrRtrId"),
        ("DC-OSPF-MIB", "ospfPmNbrOptions"),
        ("DC-OSPF-MIB", "ospfPmNbrPriority"),
        ("DC-OSPF-MIB", "ospfPmNbrState"),
        ("DC-OSPF-MIB", "ospfPmNbrEvents"),
        ("DC-OSPF-MIB", "ospfPmNbrLsRetransQLen"),
        ("DC-OSPF-MIB", "ospfPmNbrOperStatus"),
        ("DC-OSPF-MIB", "ospfPmNbrAdminStatus"),
        ("DC-OSPF-MIB", "ospfPmNbrPermanence"),
        ("DC-OSPF-MIB", "ospfPmNbrHelloSuppressed"),
        ("DC-OSPF-MIB", "ospfPmNbrNumRequests"),
        ("DC-OSPF-MIB", "ospfPmNbrStatus"),
        ("DC-OSPF-MIB", "ospfPmNbrIfIpAddr"),
        ("DC-OSPF-MIB", "ospfPmNbrDeadTime"),
        ("DC-OSPF-MIB", "ospfPmNbrAreaId"),
        ("DC-OSPF-MIB", "ospfPmNbrRestartHelperStatus"),
        ("DC-OSPF-MIB", "ospfPmNbrRestartHelperAge"),
        ("DC-OSPF-MIB", "ospfPmNbrRestartHelperExitReason"),
        ("DC-OSPF-MIB", "ospfPmNbrConfiguredPriority"),
        ("DC-OSPF-MIB", "ospfPmNbrDesignatedRtrState"))
)
if mibBuilder.loadTexts:
    ospfNbrGroup.setStatus("current")

ospfVirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 11)
)
ospfVirtNbrGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmVirtNbrIpAddr"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrOptions"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrState"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrEvents"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrLsRetransQLen"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrHelloSuppressed"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrNumRequests"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrDeadTime"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrRestartHelperStatus"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrRestartHelperAge"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrRestartHelperExit"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrGroup.setStatus("current")

ospfExtLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 12)
)
ospfExtLsdbGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmExtLsdbSequence"),
        ("DC-OSPF-MIB", "ospfPmExtLsdbAge"),
        ("DC-OSPF-MIB", "ospfPmExtLsdbChecksum"),
        ("DC-OSPF-MIB", "ospfPmExtLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfExtLsdbGroup.setStatus("current")

ospfAreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 13)
)
ospfAreaAggregateGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmAreaAggregateEffect"),
        ("DC-OSPF-MIB", "ospfPmAreaAggregateStatus"))
)
if mibBuilder.loadTexts:
    ospfAreaAggregateGroup.setStatus("current")

ospfPropLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 14)
)
ospfPropLocalLsdbGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmLocalLsdbSequence"),
        ("DC-OSPF-MIB", "ospfPmLocalLsdbAge"),
        ("DC-OSPF-MIB", "ospfPmLocalLsdbChecksum"),
        ("DC-OSPF-MIB", "ospfPmLocalLsdbAdvertisement"),
        ("DC-OSPF-MIB", "ospfPmLocalLsdbAreaId"))
)
if mibBuilder.loadTexts:
    ospfPropLocalLsdbGroup.setStatus("current")

ospfPropVirtLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 15)
)
ospfPropVirtLocalLsdbGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmVirtLocalLsdbSequence"),
        ("DC-OSPF-MIB", "ospfPmVirtLocalLsdbAge"),
        ("DC-OSPF-MIB", "ospfPmVirtLocalLsdbChecksum"),
        ("DC-OSPF-MIB", "ospfPmVirtLocalLsdbAdv"))
)
if mibBuilder.loadTexts:
    ospfPropVirtLocalLsdbGroup.setStatus("current")

ospfPropMjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 16)
)
ospfPropMjGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmMjRowStatus"),
        ("DC-OSPF-MIB", "ospfPmMjAdminStatus"),
        ("DC-OSPF-MIB", "ospfPmMjOperStatus"),
        ("DC-OSPF-MIB", "ospfPmMjJoinStatus"))
)
if mibBuilder.loadTexts:
    ospfPropMjGroup.setStatus("current")

ospfPropSjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 17)
)
ospfPropSjGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmSjJoinIndex"),
        ("DC-OSPF-MIB", "ospfPmSjJoinStatus"))
)
if mibBuilder.loadTexts:
    ospfPropSjGroup.setStatus("current")

ospfPropIfSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 18)
)
ospfPropIfSwitchGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth0"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth0"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth1"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth1"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth2"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth2"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth3"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth3"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth4"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth4"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth5"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth5"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth6"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth6"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMaxLSPBwidth7"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMaxLSPBwidth7"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMinLSPBwidth"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMinLSPBwidth"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchMTUSize"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchLastMTUSize"),
        ("DC-OSPF-MIB", "ospfPmIfSwitchSonetSdhSupport"))
)
if mibBuilder.loadTexts:
    ospfPropIfSwitchGroup.setStatus("current")

ospfPropAreaObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 19)
)
ospfPropAreaObsoleteGroup.setObjects(
    ("DC-OSPF-MIB", "ospfPmAuthType")
)
if mibBuilder.loadTexts:
    ospfPropAreaObsoleteGroup.setStatus("obsolete")

ospfPropVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 20)
)
ospfPropVirtIfGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmVirtIfLsaCount"),
        ("DC-OSPF-MIB", "ospfPmVirtIfLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmVirtIfAdminStatus"),
        ("DC-OSPF-MIB", "ospfPmVirtIfOperStatus"),
        ("DC-OSPF-MIB", "ospfPmVirtIfResourceClass"),
        ("DC-OSPF-MIB", "ospfPmVirtIfTransmitTimerDelay"),
        ("DC-OSPF-MIB", "ospfPmVirtIfIPMaxPacketSize"),
        ("DC-OSPF-MIB", "ospfPmVirtIfPassive"),
        ("DC-OSPF-MIB", "ospfPmVirtIfLsaRefreshIntvl"),
        ("DC-OSPF-MIB", "ospfPmVirtIfHelperModePolicy"),
        ("DC-OSPF-MIB", "ospfPmVirtIfMaxHtlssGracePeriod"),
        ("DC-OSPF-MIB", "ospfPmVirtIfEnableTeFlooding"),
        ("DC-OSPF-MIB", "ospfPmVirtIfInterfaceName"),
        ("DC-OSPF-MIB", "ospfPmVirtIfAuthUserData"),
        ("DC-OSPF-MIB", "ospfPmVirtIfFastHelloMultiplier"),
        ("DC-OSPF-MIB", "ospfPmVirtIfMtuIgnore"),
        ("DC-OSPF-MIB", "ospfPmVirtIfNmEntity"),
        ("DC-OSPF-MIB", "ospfPmVirtIfBfdDesired"),
        ("DC-OSPF-MIB", "ospfPmVirtIfRstHlprStrictLsaChk"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsReset"),
        ("DC-OSPF-MIB", "ospfPmVirtIfGRDelayTimer"))
)
if mibBuilder.loadTexts:
    ospfPropVirtIfGroup.setStatus("current")

ospfPropIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 21)
)
ospfPropIfGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmIfLsaCount"),
        ("DC-OSPF-MIB", "ospfPmIfLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmIfOperStatus"),
        ("DC-OSPF-MIB", "ospfPmIfNetMask"),
        ("DC-OSPF-MIB", "ospfPmIfResourceClass"),
        ("DC-OSPF-MIB", "ospfPmIfTransmitTimerDelay"),
        ("DC-OSPF-MIB", "ospfPmIfIPMaxPacketSize"),
        ("DC-OSPF-MIB", "ospfPmIfPassive"),
        ("DC-OSPF-MIB", "ospfPmIfLsaRefreshIntvl"),
        ("DC-OSPF-MIB", "ospfPmIfQOSSupport"),
        ("DC-OSPF-MIB", "ospfPmIfTEMetricPcntge"),
        ("DC-OSPF-MIB", "ospfPmIfTEMetric"),
        ("DC-OSPF-MIB", "ospfPmIfLastTEMetric"),
        ("DC-OSPF-MIB", "ospfPmIfMaxBwidthPcntge"),
        ("DC-OSPF-MIB", "ospfPmIfMaxBandwidth"),
        ("DC-OSPF-MIB", "ospfPmIfLastMaxBwidth"),
        ("DC-OSPF-MIB", "ospfPmIfMaxResBwidthPcntge"),
        ("DC-OSPF-MIB", "ospfPmIfMaxResBwidth"),
        ("DC-OSPF-MIB", "ospfPmIfLastMaxResBwidth"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidthPcntge"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth0"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth0"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth1"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth1"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth2"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth2"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth3"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth3"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth4"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth4"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth5"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth5"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth6"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth6"),
        ("DC-OSPF-MIB", "ospfPmIfUnresBwidth7"),
        ("DC-OSPF-MIB", "ospfPmIfLastUnresBwidth7"),
        ("DC-OSPF-MIB", "ospfPmIfRemoteIfIndex"),
        ("DC-OSPF-MIB", "ospfPmIfLinkProtectionType"),
        ("DC-OSPF-MIB", "ospfPmIfMaxLSPBwidthPcntge"),
        ("DC-OSPF-MIB", "ospfPmIfMinLSPBwidthPcntge"),
        ("DC-OSPF-MIB", "ospfPmIfMTUSizePcntge"),
        ("DC-OSPF-MIB", "ospfPmIfHelperModePolicy"),
        ("DC-OSPF-MIB", "ospfPmIfMaxHitlessGracePeriod"),
        ("DC-OSPF-MIB", "ospfPmIfEnableTeFlooding"),
        ("DC-OSPF-MIB", "ospfPmIfInterfaceName"),
        ("DC-OSPF-MIB", "ospfPmIfIfIndex"),
        ("DC-OSPF-MIB", "ospfPmIfSRLG"),
        ("DC-OSPF-MIB", "ospfPmIfAuthUserData"),
        ("DC-OSPF-MIB", "ospfPmIfFastHelloMultiplier"),
        ("DC-OSPF-MIB", "ospfPmIfAutoDeleteNbr"),
        ("DC-OSPF-MIB", "ospfPmIfNumBwidthCnstrnts"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrntModel"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt0"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt1"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt2"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt3"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt4"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt5"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt6"),
        ("DC-OSPF-MIB", "ospfPmIfBwidthCnstrnt7"),
        ("DC-OSPF-MIB", "ospfPmIfMtuIgnore"),
        ("DC-OSPF-MIB", "ospfPmIfNmEntity"),
        ("DC-OSPF-MIB", "ospfPmIfBfdDesired"),
        ("DC-OSPF-MIB", "ospfPmIfRstHlprStrictLsaChk"),
        ("DC-OSPF-MIB", "ospfPmIfStatsReset"),
        ("DC-OSPF-MIB", "ospfPmIfGraceLsaResendTimer"),
        ("DC-OSPF-MIB", "ospfPmIfGRDelayTimer"))
)
if mibBuilder.loadTexts:
    ospfPropIfGroup.setStatus("current")

ospfPropAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 22)
)
ospfPropAreaGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmAreaNssaTranslatorRole"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaTranslatorState"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaTranStabIntvl"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaTranslatorEvents"),
        ("DC-OSPF-MIB", "ospfPmAreaTransitCapability"),
        ("DC-OSPF-MIB", "ospfPmAreaLsaRfshIntvl"),
        ("DC-OSPF-MIB", "ospfPmAreaRtrLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaRtrLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaNetLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaNetLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaSummLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaSummLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaSummAsLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaSummAsLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaOpLsaCount"),
        ("DC-OSPF-MIB", "ospfPmAreaOpLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmAreaStatus"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaNoExtRedist"))
)
if mibBuilder.loadTexts:
    ospfPropAreaGroup.setStatus("current")

ospfPropEntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 23)
)
ospfPropEntGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRFC1583Comp"),
        ("DC-OSPF-MIB", "ospfPmEntOpaqueLsaSupport"),
        ("DC-OSPF-MIB", "ospfPmEntTrafficEngSupport"),
        ("DC-OSPF-MIB", "ospfPmEntOperStatus"),
        ("DC-OSPF-MIB", "ospfPmEntCalcMaxDelay"),
        ("DC-OSPF-MIB", "ospfPmEntCalcThrshUpdStart"),
        ("DC-OSPF-MIB", "ospfPmEntCalcThrshUpdRestart"),
        ("DC-OSPF-MIB", "ospfPmEntCalcThrshIncUpdates"),
        ("DC-OSPF-MIB", "ospfPmEntCalcThrshIncSpfUpd"),
        ("DC-OSPF-MIB", "ospfPmEntCalcPauseFreq"),
        ("DC-OSPF-MIB", "ospfPmEntRteMaxEqCostPaths"),
        ("DC-OSPF-MIB", "ospfPmEntCheckAge"),
        ("DC-OSPF-MIB", "ospfPmEntExtLsaRfshIntvl"),
        ("DC-OSPF-MIB", "ospfPmEntExtOpLsaCount"),
        ("DC-OSPF-MIB", "ospfPmEntExtOpLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmEntNumUpdPending"),
        ("DC-OSPF-MIB", "ospfPmEntNumUpdMerged"),
        ("DC-OSPF-MIB", "ospfPmEntNumCksumsPending"),
        ("DC-OSPF-MIB", "ospfPmEntDoGraceHitless"),
        ("DC-OSPF-MIB", "ospfPmEntDoGraceUnplannedHitless"),
        ("DC-OSPF-MIB", "ospfPmEntHitlessGracePeriod"),
        ("DC-OSPF-MIB", "ospfPmEntHitlessRestartReason"),
        ("DC-OSPF-MIB", "ospfPmEntTERouterId"),
        ("DC-OSPF-MIB", "ospfPmEntPrivateData"),
        ("DC-OSPF-MIB", "ospfPmEntSupportEnniRouting"),
        ("DC-OSPF-MIB", "ospfPmEntRowStatus"),
        ("DC-OSPF-MIB", "ospfPmEntRestartStatus"),
        ("DC-OSPF-MIB", "ospfPmEntRestartAge"),
        ("DC-OSPF-MIB", "ospfPmEntRestartExitReason"),
        ("DC-OSPF-MIB", "ospfPmEntCurrentRouterId"),
        ("DC-OSPF-MIB", "ospfPmEntCurrentTERouterId"),
        ("DC-OSPF-MIB", "ospfPmEntCalcSoonAfterIfChng"),
        ("DC-OSPF-MIB", "ospfPmEntI3EntIndex"),
        ("DC-OSPF-MIB", "ospfPmEntEnableIgpShortcut"),
        ("DC-OSPF-MIB", "ospfPmEntVpnPeCeSupport"),
        ("DC-OSPF-MIB", "ospfPmEntVpnRouteTag"),
        ("DC-OSPF-MIB", "ospfPmEntVpnRouterIdAttr"),
        ("DC-OSPF-MIB", "ospfPmEntDfltExtType1Metric"),
        ("DC-OSPF-MIB", "ospfPmEntDfltExtType2Metric"),
        ("DC-OSPF-MIB", "ospfPmEntRtmPurgeTime"),
        ("DC-OSPF-MIB", "ospfPmEntMinLsInterval"),
        ("DC-OSPF-MIB", "ospfPmEntMinLsArrival"),
        ("DC-OSPF-MIB", "ospfPmEntVpnDfltShamLinkMetric"),
        ("DC-OSPF-MIB", "ospfPmEntInstanceId"),
        ("DC-OSPF-MIB", "ospfPmEntStatsReset"),
        ("DC-OSPF-MIB", "ospfPmEntEnableTrapSupport"))
)
if mibBuilder.loadTexts:
    ospfPropEntGroup.setStatus("current")

ospfPropNmEntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 24)
)
ospfPropNmEntGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfNmEntRowStatus"),
        ("DC-OSPF-MIB", "ospfNmEntAdminStatus"),
        ("DC-OSPF-MIB", "ospfNmEntOperStatus"),
        ("DC-OSPF-MIB", "ospfNmMjEntityIndex"),
        ("DC-OSPF-MIB", "ospfNmSckEntityIndex"),
        ("DC-OSPF-MIB", "ospfNmEntNmiJoinOperStatus"),
        ("DC-OSPF-MIB", "ospfNmEntSckJoinOperStatus"),
        ("DC-OSPF-MIB", "ospfNmEntBfdEntityIndex"),
        ("DC-OSPF-MIB", "ospfNmEntBfdJoinOperStatus"),
        ("DC-OSPF-MIB", "ospfNmEntStatsReset"),
        ("DC-OSPF-MIB", "ospfNmEntEnableTrapSupport"))
)
if mibBuilder.loadTexts:
    ospfPropNmEntGroup.setStatus("current")

ospfPropIgpShortcutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 25)
)
ospfPropIgpShortcutGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmShortcutRemoteAddress"),
        ("DC-OSPF-MIB", "ospfPmShortcutMetricType"),
        ("DC-OSPF-MIB", "ospfPmShortcutMetricValue"),
        ("DC-OSPF-MIB", "ospfPmShortcutOperStatus"))
)
if mibBuilder.loadTexts:
    ospfPropIgpShortcutGroup.setStatus("current")

ospfPropDomainIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 26)
)
ospfPropDomainIdGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmDomainIdRowStatus"),
        ("DC-OSPF-MIB", "ospfPmDomainIdRole"),
        ("DC-OSPF-MIB", "ospfPmDomainIdStatus"))
)
if mibBuilder.loadTexts:
    ospfPropDomainIdGroup.setStatus("current")

ospfPropShamLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 27)
)
ospfPropShamLinkGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmShamLinkRowStatus"),
        ("DC-OSPF-MIB", "ospfPmShamLinkIfIndex"),
        ("DC-OSPF-MIB", "ospfPmShamLinkMetric"),
        ("DC-OSPF-MIB", "ospfPmShamLinkTransitDelay"),
        ("DC-OSPF-MIB", "ospfPmShamLinkRetransInterval"),
        ("DC-OSPF-MIB", "ospfPmShamLinkHelloInterval"),
        ("DC-OSPF-MIB", "ospfPmShamLinkRtrDeadInterval"),
        ("DC-OSPF-MIB", "ospfPmShamLinkState"),
        ("DC-OSPF-MIB", "ospfPmShamLinkEvents"),
        ("DC-OSPF-MIB", "ospfPmShamLinkAuthType"),
        ("DC-OSPF-MIB", "ospfPmShamLinkAuthKey"),
        ("DC-OSPF-MIB", "ospfPmShamLinkLsaCount"),
        ("DC-OSPF-MIB", "ospfPmShamLinkLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmShamLinkAdminStatus"),
        ("DC-OSPF-MIB", "ospfPmShamLinkOperStatus"),
        ("DC-OSPF-MIB", "ospfPmShamLinkTransmitDelay"),
        ("DC-OSPF-MIB", "ospfPmShamLinkIPMaxPacketSize"),
        ("DC-OSPF-MIB", "ospfPmShamLinkInterfaceName"),
        ("DC-OSPF-MIB", "ospfPmShamLinkLsaRefreshIntvl"),
        ("DC-OSPF-MIB", "ospfPmShamLinkHelperModePolicy"),
        ("DC-OSPF-MIB", "ospfPmShamLinkMaxGracePeriod"),
        ("DC-OSPF-MIB", "ospfPmShamLinkEnableTeFlooding"),
        ("DC-OSPF-MIB", "ospfPmShamLinkAuthUserData"),
        ("DC-OSPF-MIB", "ospfPmShamLinkFastHelloMult"),
        ("DC-OSPF-MIB", "ospfPmShamLinkMtuIgnore"),
        ("DC-OSPF-MIB", "ospfPmShamLinkNmEntity"),
        ("DC-OSPF-MIB", "ospfPmShamLinkRstStrictLsaChk"),
        ("DC-OSPF-MIB", "ospfPmShamLinkIpAddrConflict"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsReset"),
        ("DC-OSPF-MIB", "ospfPmShamLinkGrcLsaRsndTmr"),
        ("DC-OSPF-MIB", "ospfPmShamLinkGRDelayTimer"))
)
if mibBuilder.loadTexts:
    ospfPropShamLinkGroup.setStatus("current")

ospfPropShamNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 28)
)
ospfPropShamNbrGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmShamNbrRouterId"),
        ("DC-OSPF-MIB", "ospfPmShamNbrOptions"),
        ("DC-OSPF-MIB", "ospfPmShamNbrState"),
        ("DC-OSPF-MIB", "ospfPmShamNbrEvents"),
        ("DC-OSPF-MIB", "ospfPmShamNbrLsRetransQLen"),
        ("DC-OSPF-MIB", "ospfPmShamNbrNumRequests"),
        ("DC-OSPF-MIB", "ospfPmShamNbrDeadTime"),
        ("DC-OSPF-MIB", "ospfPmShamNbrRestartHelperStatus"),
        ("DC-OSPF-MIB", "ospfPmShamNbrRestartHelperAge"),
        ("DC-OSPF-MIB", "ospfPmShamNbrRestartHelperExit"))
)
if mibBuilder.loadTexts:
    ospfPropShamNbrGroup.setStatus("current")

ospfPropShamLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 29)
)
ospfPropShamLsdbGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmShamLsdbSequence"),
        ("DC-OSPF-MIB", "ospfPmShamLsdbAge"),
        ("DC-OSPF-MIB", "ospfPmShamLsdbChecksum"),
        ("DC-OSPF-MIB", "ospfPmShamLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfPropShamLsdbGroup.setStatus("current")

ospfPropMultiAreaIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 30)
)
ospfPropMultiAreaIfGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmMultiAreaIfStatus"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfAdminStat"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfOperStatus"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfState"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfEvents"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfMetricValue"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfTransitDelay"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfRetransInt"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfHelloInt"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfRtrDeadInt"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfFastHelloMult"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfAuthType"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfAuthKey"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfAuthUserData"),
        ("DC-OSPF-MIB", "ospfPmIfMultiAreaIPMaxPktSize"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfMtuIgnore"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfLsaCount"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfLsaCksumSum"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfTrsmtTmrDelay"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfEnableTeFlood"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaIfStatsReset"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaGraceLsaRsndTmr"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaGRDelayTimer"))
)
if mibBuilder.loadTexts:
    ospfPropMultiAreaIfGroup.setStatus("current")

ospfPropMultiAreaNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 31)
)
ospfPropMultiAreaNbrGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmMultiAreaNbrSrcIpAddr"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrRtrId"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrOptions"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrState"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrEvents"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrLsRetransQLen"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrNumRequests"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrDeadTime"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrRstrtHelpSts"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrRstrtHelpAge"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaNbrRstrtHelpExitR"))
)
if mibBuilder.loadTexts:
    ospfPropMultiAreaNbrGroup.setStatus("current")

ospfPropMultiAreaLclLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 32)
)
ospfPropMultiAreaLclLsdbGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbSequence"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbAge"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbChecksum"),
        ("DC-OSPF-MIB", "ospfPmMultiAreaLclLsdbAdvert"))
)
if mibBuilder.loadTexts:
    ospfPropMultiAreaLclLsdbGroup.setStatus("current")

ospfPropPmEntStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 33)
)
ospfPropPmEntStatsGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntStatsNoIf"),
        ("DC-OSPF-MIB", "ospfPmEntStatsNoVirtLink"),
        ("DC-OSPF-MIB", "ospfPmEntStatsBadPacket"))
)
if mibBuilder.loadTexts:
    ospfPropPmEntStatsGroup.setStatus("current")

ospfPropIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 34)
)
ospfPropIfStatsGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmIfStatsRxInvalid"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxInvalidByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxHello"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxDbDes"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxLsReq"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxLsAck"),
        ("DC-OSPF-MIB", "ospfPmIfStatsRxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxFailed"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxFailedByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxHello"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxDbDes"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxLsReq"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxLsAck"),
        ("DC-OSPF-MIB", "ospfPmIfStatsTxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmIfStatsLength"),
        ("DC-OSPF-MIB", "ospfPmIfStatsCksum"),
        ("DC-OSPF-MIB", "ospfPmIfStatsVersion"),
        ("DC-OSPF-MIB", "ospfPmIfStatsBadSrc"),
        ("DC-OSPF-MIB", "ospfPmIfStatsAreaMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsSelfOrig"),
        ("DC-OSPF-MIB", "ospfPmIfStatsDupeId"),
        ("DC-OSPF-MIB", "ospfPmIfStatsHello"),
        ("DC-OSPF-MIB", "ospfPmIfStatsMtuMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsNbrIgnored"),
        ("DC-OSPF-MIB", "ospfPmIfStatsAuth"),
        ("DC-OSPF-MIB", "ospfPmIfStatsWrongProto"),
        ("DC-OSPF-MIB", "ospfPmIfStatsResourceErr"),
        ("DC-OSPF-MIB", "ospfPmIfStatsVirtMaIfClash"),
        ("DC-OSPF-MIB", "ospfPmIfStatsBadLsaLen"),
        ("DC-OSPF-MIB", "ospfPmIfStatsLsaBadType"),
        ("DC-OSPF-MIB", "ospfPmIfStatsLsaBadLen"),
        ("DC-OSPF-MIB", "ospfPmIfStatsLsaBadData"),
        ("DC-OSPF-MIB", "ospfPmIfStatsLsaBadCksum"),
        ("DC-OSPF-MIB", "ospfPmIfStatsIfStandby"),
        ("DC-OSPF-MIB", "ospfPmIfStatsUnkNbmaNbr"),
        ("DC-OSPF-MIB", "ospfPmIfStatsUnkVirtNbr"),
        ("DC-OSPF-MIB", "ospfPmIfStatsAuthMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsAuthFailure"),
        ("DC-OSPF-MIB", "ospfPmIfStatsHelloMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsDeadMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsNetmaskMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsOptionsMismatch"),
        ("DC-OSPF-MIB", "ospfPmIfStatsNbrAdminDown"),
        ("DC-OSPF-MIB", "ospfPmIfStatsPktLocalAddr"),
        ("DC-OSPF-MIB", "ospfPmIfStatsMaIfNotP2p"),
        ("DC-OSPF-MIB", "ospfPmIfStatsBadPacket"))
)
if mibBuilder.loadTexts:
    ospfPropIfStatsGroup.setStatus("current")

ospfPropVirtIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 35)
)
ospfPropVirtIfStatsGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmVirtIfStatsRxInvalid"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxInvalidByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxHello"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxDbDes"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxLsReq"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxLsAck"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsRxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxFailed"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxFailedByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxHello"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxDbDes"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxLsReq"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxLsAck"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsTxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsLength"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsCksum"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsVersion"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsBadSrc"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsAreaMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsSelfOrig"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsDupeId"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsHello"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsMtuMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsNbrIgnored"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsAuth"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsWrongProto"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsResourceErr"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsVirtMaIfClash"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsBadLsaLen"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsLsaBadType"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsLsaBadLen"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsLsaBadData"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsLsaBadCksum"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsUnkNbmaNbr"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsUnkVirtNbr"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsAuthMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsAuthFailure"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsHelloMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsDeadMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsNetmaskMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsOptionsMismatch"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsNbrAdminDown"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsPktLocalAddr"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsMaIfNotP2p"),
        ("DC-OSPF-MIB", "ospfPmVirtIfStatsBadPacket"))
)
if mibBuilder.loadTexts:
    ospfPropVirtIfStatsGroup.setStatus("current")

ospfPropShamLinkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 36)
)
ospfPropShamLinkStatsGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmShamLinkStatsRxInvalid"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxInvalidByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxHello"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxDbDes"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxLsReq"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxLsAck"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsRxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxFailed"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxFailedByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxHello"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxDbDes"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxLsReq"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxLsAck"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsTxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsLength"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsCksum"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsVersion"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsBadSrc"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsAreaMismatch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsSelfOrig"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsDupeId"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsHello"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsMtuMismatch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsNbrIgnored"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsAuth"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsWrongProto"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsResourceErr"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsVirtMaIfClash"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsBadLsaLen"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsLsaBadType"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsLsaBadLen"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsLsaBadData"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsLsaBadCksum"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsUnkNbmaNbr"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsUnkVirtNbr"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsAuthMismatch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsAuthFailure"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsNetmaskMsmtch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsHelloMismatch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsDeadMismatch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsOptionsMsmtch"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsNbrAdminDown"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsPktLocalAddr"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsMaIfNotP2p"),
        ("DC-OSPF-MIB", "ospfPmShamLinkStatsBadPacket"))
)
if mibBuilder.loadTexts:
    ospfPropShamLinkStatsGroup.setStatus("current")

ospfPmMaIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 37)
)
ospfPmMaIfStatsGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmMaIfStatsRxInvalid"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxInvalidByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxHello"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxDbDes"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxLsReq"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxLsAck"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsRxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxFailed"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxFailedByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxHello"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxHelloByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxDbDes"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxDbDesByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxLsReq"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxLsReqByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxLsUpd"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxLsUpdByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxLsAck"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsTxLsAckByte"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsLength"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsCksum"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsVersion"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsBadSrc"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsAreaMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsSelfOrig"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsDupeId"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsHello"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsMtuMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsNbrIgnored"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsAuth"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsWrongProto"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsResourceErr"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsVirtMaIfClash"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsBadLsaLen"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsLsaBadType"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsLsaBadLen"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsLsaBadData"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsLsaBadCksum"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsUnkNbmaNbr"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsUnkVirtNbr"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsAuthMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsAuthFailure"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsHelloMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsDeadMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsNetmaskMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsOptionsMismatch"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsNbrAdminDown"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsPktLocalAddr"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsMaIfNotP2p"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsBadPacket"))
)
if mibBuilder.loadTexts:
    ospfPmMaIfStatsGroup.setStatus("current")

ospfPropNmEntStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 38)
)
ospfPropNmEntStatsGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfNmEntStatsLength"),
        ("DC-OSPF-MIB", "ospfNmEntStatsNoIf"),
        ("DC-OSPF-MIB", "ospfNmEntStatsNoVirtLink"),
        ("DC-OSPF-MIB", "ospfNmEntStatsInstanceId"),
        ("DC-OSPF-MIB", "ospfNmEntStatsBadIpHdrLen"),
        ("DC-OSPF-MIB", "ospfNmEntStatsVersion"),
        ("DC-OSPF-MIB", "ospfNmEntStatsBadSrc"),
        ("DC-OSPF-MIB", "ospfNmEntStatsResourceErr"),
        ("DC-OSPF-MIB", "ospfNmEntStatsBadPacket"))
)
if mibBuilder.loadTexts:
    ospfPropNmEntStatsGroup.setStatus("current")

ospfPmSpfEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 39)
)
ospfPmSpfEntryGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmSpfEntryNextHopAddr"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryIfIndex"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryCost"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryIsASBR"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryIsABR"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryIsVirtEndpt"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryCalcIndex"))
)
if mibBuilder.loadTexts:
    ospfPmSpfEntryGroup.setStatus("current")

ospfPmRouteTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 40)
)
ospfPmRouteTableGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmRouteNextHopAddr"),
        ("DC-OSPF-MIB", "ospfPmRouteIfIndex"),
        ("DC-OSPF-MIB", "ospfPmRouteAreaId"),
        ("DC-OSPF-MIB", "ospfPmRouteCost"),
        ("DC-OSPF-MIB", "ospfPmRoutePathType"),
        ("DC-OSPF-MIB", "ospfPmRouteCalcIndex"))
)
if mibBuilder.loadTexts:
    ospfPmRouteTableGroup.setStatus("current")

ospfPmRouterDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 1, 41)
)
ospfPmRouterDestGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfPmRouterDestNextHopAddr"),
        ("DC-OSPF-MIB", "ospfPmRouterDestIfIndex"),
        ("DC-OSPF-MIB", "ospfPmRouterDestCost"),
        ("DC-OSPF-MIB", "ospfPmRouterDestIsASBR"),
        ("DC-OSPF-MIB", "ospfPmRouterDestIsABR"),
        ("DC-OSPF-MIB", "ospfPmRouterDestIsVirtEndpt"),
        ("DC-OSPF-MIB", "ospfPmRouterDestPathType"),
        ("DC-OSPF-MIB", "ospfPmRouterDestCalcIndex"))
)
if mibBuilder.loadTexts:
    ospfPmRouterDestGroup.setStatus("current")

ospfTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2, 1, 2)
)
ospfTrapControlGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfConfigErrorType"),
        ("DC-OSPF-MIB", "ospfPacketType"),
        ("DC-OSPF-MIB", "ospfPacketSrc"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfAreaId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfNeighbor"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"),
        ("DC-OSPF-MIB", "ospfTrapNbrIpAddr"),
        ("DC-OSPF-MIB", "ospfTrapNbrAddressLessIndex"),
        ("DC-OSPF-MIB", "ospfTrapVirtNbrArea"),
        ("DC-OSPF-MIB", "ospfTrapVirtNbrRtrId"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndexValid"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndex"),
        ("DC-OSPF-MIB", "ospfTrapIfIpAddress"),
        ("DC-OSPF-MIB", "ospfTrapAddressLessIf"),
        ("DC-OSPF-MIB", "ospfTrapAreaId"))
)
if mibBuilder.loadTexts:
    ospfTrapControlGroup.setStatus("current")


# Notification objects

ospfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 1)
)
ospfVirtIfStateChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfAreaId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfNeighbor"),
        ("DC-OSPF-MIB", "ospfPmVirtIfState"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfVirtIfStateChange.setStatus(
        "current"
    )

ospfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 2)
)
ospfNbrStateChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapNbrIpAddr"),
        ("DC-OSPF-MIB", "ospfTrapNbrAddressLessIndex"),
        ("DC-OSPF-MIB", "ospfPmNbrRtrId"),
        ("DC-OSPF-MIB", "ospfPmNbrState"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfNbrStateChange.setStatus(
        "current"
    )

ospfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 3)
)
ospfVirtNbrStateChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapVirtNbrArea"),
        ("DC-OSPF-MIB", "ospfTrapVirtNbrRtrId"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrState"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrStateChange.setStatus(
        "current"
    )

ospfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 4)
)
ospfIfConfigError.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapIfIpAddress"),
        ("DC-OSPF-MIB", "ospfTrapAddressLessIf"),
        ("DC-OSPF-MIB", "ospfPacketSrc"),
        ("DC-OSPF-MIB", "ospfConfigErrorType"),
        ("DC-OSPF-MIB", "ospfPacketType"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndexValid"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfIfConfigError.setStatus(
        "current"
    )

ospfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 5)
)
ospfVirtIfConfigError.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfAreaId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfNeighbor"),
        ("DC-OSPF-MIB", "ospfConfigErrorType"),
        ("DC-OSPF-MIB", "ospfPacketType"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndexValid"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfVirtIfConfigError.setStatus(
        "current"
    )

ospfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 6)
)
ospfIfAuthFailure.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapIfIpAddress"),
        ("DC-OSPF-MIB", "ospfTrapAddressLessIf"),
        ("DC-OSPF-MIB", "ospfPacketSrc"),
        ("DC-OSPF-MIB", "ospfConfigErrorType"),
        ("DC-OSPF-MIB", "ospfPacketType"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndex"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfIfAuthFailure.setStatus(
        "current"
    )

ospfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 7)
)
ospfVirtIfAuthFailure.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfAreaId"),
        ("DC-OSPF-MIB", "ospfTrapVirtIfNeighbor"),
        ("DC-OSPF-MIB", "ospfConfigErrorType"),
        ("DC-OSPF-MIB", "ospfPacketType"),
        ("DC-OSPF-MIB", "ospfTrapNmEntIndex"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfVirtIfAuthFailure.setStatus(
        "current"
    )

ospfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 8)
)
ospfIfStateChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapIfIpAddress"),
        ("DC-OSPF-MIB", "ospfTrapAddressLessIf"),
        ("DC-OSPF-MIB", "ospfPmIfState"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfIfStateChange.setStatus(
        "current"
    )

ospfNssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 9)
)
ospfNssaTranslatorStatusChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapAreaId"),
        ("DC-OSPF-MIB", "ospfPmAreaNssaTranslatorState"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfNssaTranslatorStatusChange.setStatus(
        "current"
    )

ospfNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 10)
)
ospfNbrRestartHelperStatusChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapNbrIpAddr"),
        ("DC-OSPF-MIB", "ospfTrapNbrAddressLessIndex"),
        ("DC-OSPF-MIB", "ospfPmNbrRtrId"),
        ("DC-OSPF-MIB", "ospfPmNbrRestartHelperStatus"),
        ("DC-OSPF-MIB", "ospfPmNbrRestartHelperAge"),
        ("DC-OSPF-MIB", "ospfPmNbrRestartHelperExitReason"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfNbrRestartHelperStatusChange.setStatus(
        "current"
    )

ospfVirtNbrRstrtHelperStatusChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 11)
)
ospfVirtNbrRstrtHelperStatusChng.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfTrapVirtNbrArea"),
        ("DC-OSPF-MIB", "ospfTrapVirtNbrRtrId"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrRestartHelperStatus"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrRestartHelperAge"),
        ("DC-OSPF-MIB", "ospfPmVirtNbrRestartHelperExit"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrRstrtHelperStatusChng.setStatus(
        "current"
    )

ospfPmOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 0, 12)
)
ospfPmOperStateChange.setObjects(
      *(("DC-OSPF-MIB", "ospfPmEntRouterId"),
        ("DC-OSPF-MIB", "ospfPmEntOperStatus"),
        ("DC-OSPF-MIB", "ospfTrapPmEntIndex"))
)
if mibBuilder.loadTexts:
    ospfPmOperStateChange.setStatus(
        "current"
    )


# Notifications groups

ospfTrapEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2, 1, 1)
)
ospfTrapEventGroup.setObjects(
      *(("DC-OSPF-MIB", "ospfVirtIfStateChange"),
        ("DC-OSPF-MIB", "ospfNbrStateChange"),
        ("DC-OSPF-MIB", "ospfVirtNbrStateChange"),
        ("DC-OSPF-MIB", "ospfIfConfigError"),
        ("DC-OSPF-MIB", "ospfVirtIfConfigError"),
        ("DC-OSPF-MIB", "ospfIfAuthFailure"),
        ("DC-OSPF-MIB", "ospfVirtIfAuthFailure"),
        ("DC-OSPF-MIB", "ospfIfStateChange"),
        ("DC-OSPF-MIB", "ospfNssaTranslatorStatusChange"),
        ("DC-OSPF-MIB", "ospfNbrRestartHelperStatusChange"),
        ("DC-OSPF-MIB", "ospfVirtNbrRstrtHelperStatusChng"),
        ("DC-OSPF-MIB", "ospfPmOperStateChange"))
)
if mibBuilder.loadTexts:
    ospfTrapEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ospfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 2, 2, 1)
)
ospfCompliance.setObjects(
      *(("DC-OSPF-MIB", "ospfBasicGroup"),
        ("DC-OSPF-MIB", "ospfAreaGroup"),
        ("DC-OSPF-MIB", "ospfStubAreaGroup"),
        ("DC-OSPF-MIB", "ospfIfGroup"),
        ("DC-OSPF-MIB", "ospfIfMetricGroup"),
        ("DC-OSPF-MIB", "ospfVirtIfGroup"),
        ("DC-OSPF-MIB", "ospfNbrGroup"),
        ("DC-OSPF-MIB", "ospfVirtNbrGroup"),
        ("DC-OSPF-MIB", "ospfAreaAggregateGroup"),
        ("DC-OSPF-MIB", "ospfLsdbGroup"),
        ("DC-OSPF-MIB", "ospfHostGroup"),
        ("DC-OSPF-MIB", "ospfExtLsdbGroup"),
        ("DC-OSPF-MIB", "ospfPropLocalLsdbGroup"),
        ("DC-OSPF-MIB", "ospfPropVirtLocalLsdbGroup"),
        ("DC-OSPF-MIB", "ospfPropMjGroup"),
        ("DC-OSPF-MIB", "ospfPropSjGroup"),
        ("DC-OSPF-MIB", "ospfPropIfSwitchGroup"),
        ("DC-OSPF-MIB", "ospfPropVirtIfGroup"),
        ("DC-OSPF-MIB", "ospfPropIfGroup"),
        ("DC-OSPF-MIB", "ospfPropAreaGroup"),
        ("DC-OSPF-MIB", "ospfPropEntGroup"),
        ("DC-OSPF-MIB", "ospfPropNmEntGroup"),
        ("DC-OSPF-MIB", "ospfPropIgpShortcutGroup"),
        ("DC-OSPF-MIB", "ospfPropDomainIdGroup"),
        ("DC-OSPF-MIB", "ospfPropShamLinkGroup"),
        ("DC-OSPF-MIB", "ospfPropShamNbrGroup"),
        ("DC-OSPF-MIB", "ospfPropShamLsdbGroup"),
        ("DC-OSPF-MIB", "ospfPropMultiAreaIfGroup"),
        ("DC-OSPF-MIB", "ospfPropMultiAreaNbrGroup"),
        ("DC-OSPF-MIB", "ospfPropMultiAreaLclLsdbGroup"),
        ("DC-OSPF-MIB", "ospfPropPmEntStatsGroup"),
        ("DC-OSPF-MIB", "ospfPropIfStatsGroup"),
        ("DC-OSPF-MIB", "ospfPropVirtIfStatsGroup"),
        ("DC-OSPF-MIB", "ospfPropShamLinkStatsGroup"),
        ("DC-OSPF-MIB", "ospfPmMaIfStatsGroup"),
        ("DC-OSPF-MIB", "ospfPmSpfEntryGroup"),
        ("DC-OSPF-MIB", "ospfPmRouteTableGroup"),
        ("DC-OSPF-MIB", "ospfPmRouterDestGroup"),
        ("DC-OSPF-MIB", "ospfPropNmEntStatsGroup"))
)
if mibBuilder.loadTexts:
    ospfCompliance.setStatus(
        "current"
    )

ospfTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2, 2, 1)
)
ospfTrapCompliance.setObjects(
      *(("DC-OSPF-MIB", "ospfTrapControlGroup"),
        ("DC-OSPF-MIB", "ospfTrapControlGroup"))
)
if mibBuilder.loadTexts:
    ospfTrapCompliance.setStatus(
        "obsolete"
    )

ospfTrapCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 3, 3, 2, 2, 2)
)
ospfTrapCompliance2.setObjects(
    ("DC-OSPF-MIB", "ospfTrapEventGroup")
)
if mibBuilder.loadTexts:
    ospfTrapCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-OSPF-MIB",
    **{"OspfPmAdminStatus": OspfPmAdminStatus,
       "OspfPmOperStatus": OspfPmOperStatus,
       "OspfPmIndex": OspfPmIndex,
       "OspfPmMjStatus": OspfPmMjStatus,
       "OspfPmSjStatus": OspfPmSjStatus,
       "OspfPmInterfaceId": OspfPmInterfaceId,
       "OspfPmSlaveInterfaceId": OspfPmSlaveInterfaceId,
       "AreaID": AreaID,
       "RouterID": RouterID,
       "OspfVersionNumber": OspfVersionNumber,
       "OspfAuthTypes": OspfAuthTypes,
       "OspfImportTypes": OspfImportTypes,
       "OspfSummaryTypes": OspfSummaryTypes,
       "OspfTransRoles": OspfTransRoles,
       "OspfTransStates": OspfTransStates,
       "OspfMetricTypes": OspfMetricTypes,
       "OspfExtLsTypes": OspfExtLsTypes,
       "OspfAreaLsTypes": OspfAreaLsTypes,
       "OspfLinkLsTypes": OspfLinkLsTypes,
       "OspfAggLsTypes": OspfAggLsTypes,
       "OspfNetworkTypes": OspfNetworkTypes,
       "OspfInterfaceStates": OspfInterfaceStates,
       "OspfMulticastFwardTypes": OspfMulticastFwardTypes,
       "OspfNeighborStates": OspfNeighborStates,
       "OspfNbrPermanence": OspfNbrPermanence,
       "OspfAggregateEffects": OspfAggregateEffects,
       "OspfHitlessRestartReasons": OspfHitlessRestartReasons,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "FastHelloMultiplierRange": FastHelloMultiplierRange,
       "UpToMaxAge": UpToMaxAge,
       "UpToRefreshInterval": UpToRefreshInterval,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "OspfPmIfLinkProtValue": OspfPmIfLinkProtValue,
       "OspfPmIfSwitchCapValue": OspfPmIfSwitchCapValue,
       "OspfPmIfSwitchEncodingValue": OspfPmIfSwitchEncodingValue,
       "OspfPmIfSwitchSonetSdhValue": OspfPmIfSwitchSonetSdhValue,
       "OspfPmEntPrivateDataType": OspfPmEntPrivateDataType,
       "OspfHelperModePolicy": OspfHelperModePolicy,
       "OspfRestartHelperStatus": OspfRestartHelperStatus,
       "OspfRestartExitReason": OspfRestartExitReason,
       "OspfShamConflictFlags": OspfShamConflictFlags,
       "OspfPathType": OspfPathType,
       "OspfDesignatedRtrState": OspfDesignatedRtrState,
       "nbase": nbase,
       "opx": opx,
       "ospfMib": ospfMib,
       "ospfObjects": ospfObjects,
       "ospfPmEntTable": ospfPmEntTable,
       "ospfPmEntEntry": ospfPmEntEntry,
       "ospfPmEntRouterId": ospfPmEntRouterId,
       "ospfPmEntAdminStat": ospfPmEntAdminStat,
       "ospfPmEntVersionNumber": ospfPmEntVersionNumber,
       "ospfPmEntAreaBdrRtrStatus": ospfPmEntAreaBdrRtrStatus,
       "ospfPmEntASBdrRtrStatus": ospfPmEntASBdrRtrStatus,
       "ospfPmEntExternLsaCount": ospfPmEntExternLsaCount,
       "ospfPmEntExternLsaCksumSum": ospfPmEntExternLsaCksumSum,
       "ospfPmEntTOSSupport": ospfPmEntTOSSupport,
       "ospfPmEntOriginateNewLsas": ospfPmEntOriginateNewLsas,
       "ospfPmEntRxNewLsas": ospfPmEntRxNewLsas,
       "ospfPmEntExtLsdbLimit": ospfPmEntExtLsdbLimit,
       "ospfPmEntMulticastExtns": ospfPmEntMulticastExtns,
       "ospfPmEntExitOverflowIntvl": ospfPmEntExitOverflowIntvl,
       "ospfPmEntDemandExtensions": ospfPmEntDemandExtensions,
       "ospfPmEntRFC1583Comp": ospfPmEntRFC1583Comp,
       "ospfPmEntOpaqueLsaSupport": ospfPmEntOpaqueLsaSupport,
       "ospfPmEntTrafficEngSupport": ospfPmEntTrafficEngSupport,
       "ospfPmEntIndex": ospfPmEntIndex,
       "ospfPmEntOperStatus": ospfPmEntOperStatus,
       "ospfPmEntRowStatus": ospfPmEntRowStatus,
       "ospfPmEntCalcMaxDelay": ospfPmEntCalcMaxDelay,
       "ospfPmEntCalcThrshUpdStart": ospfPmEntCalcThrshUpdStart,
       "ospfPmEntCalcThrshUpdRestart": ospfPmEntCalcThrshUpdRestart,
       "ospfPmEntCalcThrshIncUpdates": ospfPmEntCalcThrshIncUpdates,
       "ospfPmEntCalcThrshIncSpfUpd": ospfPmEntCalcThrshIncSpfUpd,
       "ospfPmEntCalcPauseFreq": ospfPmEntCalcPauseFreq,
       "ospfPmEntRteMaxEqCostPaths": ospfPmEntRteMaxEqCostPaths,
       "ospfPmEntCheckAge": ospfPmEntCheckAge,
       "ospfPmEntExtLsaRfshIntvl": ospfPmEntExtLsaRfshIntvl,
       "ospfPmEntExtOpLsaCount": ospfPmEntExtOpLsaCount,
       "ospfPmEntExtOpLsaCksumSum": ospfPmEntExtOpLsaCksumSum,
       "ospfPmEntNumUpdPending": ospfPmEntNumUpdPending,
       "ospfPmEntNumUpdMerged": ospfPmEntNumUpdMerged,
       "ospfPmEntNumCksumsPending": ospfPmEntNumCksumsPending,
       "ospfPmEntDoGraceHitless": ospfPmEntDoGraceHitless,
       "ospfPmEntDoGraceUnplannedHitless": ospfPmEntDoGraceUnplannedHitless,
       "ospfPmEntHitlessGracePeriod": ospfPmEntHitlessGracePeriod,
       "ospfPmEntHitlessRestartReason": ospfPmEntHitlessRestartReason,
       "ospfPmEntTERouterId": ospfPmEntTERouterId,
       "ospfPmEntPrivateData": ospfPmEntPrivateData,
       "ospfPmEntSupportEnniRouting": ospfPmEntSupportEnniRouting,
       "ospfPmEntRestartStatus": ospfPmEntRestartStatus,
       "ospfPmEntRestartAge": ospfPmEntRestartAge,
       "ospfPmEntRestartExitReason": ospfPmEntRestartExitReason,
       "ospfPmEntCurrentRouterId": ospfPmEntCurrentRouterId,
       "ospfPmEntCurrentTERouterId": ospfPmEntCurrentTERouterId,
       "ospfPmEntCalcSoonAfterIfChng": ospfPmEntCalcSoonAfterIfChng,
       "ospfPmEntI3EntIndex": ospfPmEntI3EntIndex,
       "ospfPmEntEnableIgpShortcut": ospfPmEntEnableIgpShortcut,
       "ospfPmEntVpnPeCeSupport": ospfPmEntVpnPeCeSupport,
       "ospfPmEntVpnRouteTag": ospfPmEntVpnRouteTag,
       "ospfPmEntVpnRouterIdAttr": ospfPmEntVpnRouterIdAttr,
       "ospfPmEntDfltExtType1Metric": ospfPmEntDfltExtType1Metric,
       "ospfPmEntDfltExtType2Metric": ospfPmEntDfltExtType2Metric,
       "ospfPmEntRtmPurgeTime": ospfPmEntRtmPurgeTime,
       "ospfPmEntMinLsInterval": ospfPmEntMinLsInterval,
       "ospfPmEntMinLsArrival": ospfPmEntMinLsArrival,
       "ospfPmEntVpnDfltShamLinkMetric": ospfPmEntVpnDfltShamLinkMetric,
       "ospfPmEntInstanceId": ospfPmEntInstanceId,
       "ospfPmEntStatsReset": ospfPmEntStatsReset,
       "ospfPmEntEnableTrapSupport": ospfPmEntEnableTrapSupport,
       "ospfPmAreaTable": ospfPmAreaTable,
       "ospfPmAreaEntry": ospfPmAreaEntry,
       "ospfPmAreaId": ospfPmAreaId,
       "ospfPmAuthType": ospfPmAuthType,
       "ospfPmImportAsExtern": ospfPmImportAsExtern,
       "ospfPmSpfRuns": ospfPmSpfRuns,
       "ospfPmAreaBdrRtrCount": ospfPmAreaBdrRtrCount,
       "ospfPmASBdrRtrCount": ospfPmASBdrRtrCount,
       "ospfPmAreaLsaCount": ospfPmAreaLsaCount,
       "ospfPmAreaLsaCksumSum": ospfPmAreaLsaCksumSum,
       "ospfPmAreaSummary": ospfPmAreaSummary,
       "ospfPmAreaStatus": ospfPmAreaStatus,
       "ospfPmAreaNssaTranslatorRole": ospfPmAreaNssaTranslatorRole,
       "ospfPmAreaNssaTranslatorState": ospfPmAreaNssaTranslatorState,
       "ospfPmAreaNssaTranStabIntvl": ospfPmAreaNssaTranStabIntvl,
       "ospfPmAreaNssaTranslatorEvents": ospfPmAreaNssaTranslatorEvents,
       "ospfPmAreaApplIndex": ospfPmAreaApplIndex,
       "ospfPmAreaAdminStatus": ospfPmAreaAdminStatus,
       "ospfPmAreaOperStatus": ospfPmAreaOperStatus,
       "ospfPmAreaTransitCapability": ospfPmAreaTransitCapability,
       "ospfPmAreaLsaRfshIntvl": ospfPmAreaLsaRfshIntvl,
       "ospfPmAreaRtrLsaCount": ospfPmAreaRtrLsaCount,
       "ospfPmAreaRtrLsaCksumSum": ospfPmAreaRtrLsaCksumSum,
       "ospfPmAreaNetLsaCount": ospfPmAreaNetLsaCount,
       "ospfPmAreaNetLsaCksumSum": ospfPmAreaNetLsaCksumSum,
       "ospfPmAreaSummLsaCount": ospfPmAreaSummLsaCount,
       "ospfPmAreaSummLsaCksumSum": ospfPmAreaSummLsaCksumSum,
       "ospfPmAreaSummAsLsaCount": ospfPmAreaSummAsLsaCount,
       "ospfPmAreaSummAsLsaCksumSum": ospfPmAreaSummAsLsaCksumSum,
       "ospfPmAreaNssaLsaCount": ospfPmAreaNssaLsaCount,
       "ospfPmAreaNssaLsaCksumSum": ospfPmAreaNssaLsaCksumSum,
       "ospfPmAreaOpLsaCount": ospfPmAreaOpLsaCount,
       "ospfPmAreaOpLsaCksumSum": ospfPmAreaOpLsaCksumSum,
       "ospfPmAreaNssaNoExtRedist": ospfPmAreaNssaNoExtRedist,
       "ospfPmStubAreaTable": ospfPmStubAreaTable,
       "ospfPmStubAreaEntry": ospfPmStubAreaEntry,
       "ospfPmStubAreaId": ospfPmStubAreaId,
       "ospfPmStubTOS": ospfPmStubTOS,
       "ospfPmStubMetric": ospfPmStubMetric,
       "ospfPmStubStatus": ospfPmStubStatus,
       "ospfPmStubMetricType": ospfPmStubMetricType,
       "ospfPmStubApplIndex": ospfPmStubApplIndex,
       "ospfPmLsdbTable": ospfPmLsdbTable,
       "ospfPmLsdbEntry": ospfPmLsdbEntry,
       "ospfPmLsdbAreaId": ospfPmLsdbAreaId,
       "ospfPmLsdbType": ospfPmLsdbType,
       "ospfPmLsdbLsid": ospfPmLsdbLsid,
       "ospfPmLsdbRouterId": ospfPmLsdbRouterId,
       "ospfPmLsdbSequence": ospfPmLsdbSequence,
       "ospfPmLsdbAge": ospfPmLsdbAge,
       "ospfPmLsdbChecksum": ospfPmLsdbChecksum,
       "ospfPmLsdbAdvertisement": ospfPmLsdbAdvertisement,
       "ospfPmLsdbApplIndex": ospfPmLsdbApplIndex,
       "ospfPmHostTable": ospfPmHostTable,
       "ospfPmHostEntry": ospfPmHostEntry,
       "ospfPmHostIpAddress": ospfPmHostIpAddress,
       "ospfPmHostTOS": ospfPmHostTOS,
       "ospfPmHostMetric": ospfPmHostMetric,
       "ospfPmHostStatus": ospfPmHostStatus,
       "ospfPmHostAreaID": ospfPmHostAreaID,
       "ospfPmHostApplIndex": ospfPmHostApplIndex,
       "ospfPmHostAdminStatus": ospfPmHostAdminStatus,
       "ospfPmHostOperStatus": ospfPmHostOperStatus,
       "ospfPmIfTable": ospfPmIfTable,
       "ospfPmIfEntry": ospfPmIfEntry,
       "ospfPmIfIpAddress": ospfPmIfIpAddress,
       "ospfPmAddressLessIf": ospfPmAddressLessIf,
       "ospfPmIfAreaId": ospfPmIfAreaId,
       "ospfPmIfType": ospfPmIfType,
       "ospfPmIfAdminStat": ospfPmIfAdminStat,
       "ospfPmIfRtrPriority": ospfPmIfRtrPriority,
       "ospfPmIfTransitDelay": ospfPmIfTransitDelay,
       "ospfPmIfRetransInterval": ospfPmIfRetransInterval,
       "ospfPmIfHelloInterval": ospfPmIfHelloInterval,
       "ospfPmIfRtrDeadInterval": ospfPmIfRtrDeadInterval,
       "ospfPmIfPollInterval": ospfPmIfPollInterval,
       "ospfPmIfState": ospfPmIfState,
       "ospfPmIfDesignatedRouter": ospfPmIfDesignatedRouter,
       "ospfPmIfBackupDesignatedRouter": ospfPmIfBackupDesignatedRouter,
       "ospfPmIfEvents": ospfPmIfEvents,
       "ospfPmIfAuthKey": ospfPmIfAuthKey,
       "ospfPmIfStatus": ospfPmIfStatus,
       "ospfPmIfMulticastForwarding": ospfPmIfMulticastForwarding,
       "ospfPmIfDemand": ospfPmIfDemand,
       "ospfPmIfAuthType": ospfPmIfAuthType,
       "ospfPmIfLsaCount": ospfPmIfLsaCount,
       "ospfPmIfLsaCksumSum": ospfPmIfLsaCksumSum,
       "ospfPmIfApplIndex": ospfPmIfApplIndex,
       "ospfPmIfOperStatus": ospfPmIfOperStatus,
       "ospfPmIfNetMask": ospfPmIfNetMask,
       "ospfPmIfResourceClass": ospfPmIfResourceClass,
       "ospfPmIfTransmitTimerDelay": ospfPmIfTransmitTimerDelay,
       "ospfPmIfIPMaxPacketSize": ospfPmIfIPMaxPacketSize,
       "ospfPmIfPassive": ospfPmIfPassive,
       "ospfPmIfInterfaceName": ospfPmIfInterfaceName,
       "ospfPmIfLsaRefreshIntvl": ospfPmIfLsaRefreshIntvl,
       "ospfPmIfQOSSupport": ospfPmIfQOSSupport,
       "ospfPmIfTEMetricPcntge": ospfPmIfTEMetricPcntge,
       "ospfPmIfTEMetric": ospfPmIfTEMetric,
       "ospfPmIfLastTEMetric": ospfPmIfLastTEMetric,
       "ospfPmIfMaxBwidthPcntge": ospfPmIfMaxBwidthPcntge,
       "ospfPmIfMaxBandwidth": ospfPmIfMaxBandwidth,
       "ospfPmIfLastMaxBwidth": ospfPmIfLastMaxBwidth,
       "ospfPmIfMaxResBwidthPcntge": ospfPmIfMaxResBwidthPcntge,
       "ospfPmIfMaxResBwidth": ospfPmIfMaxResBwidth,
       "ospfPmIfLastMaxResBwidth": ospfPmIfLastMaxResBwidth,
       "ospfPmIfUnresBwidthPcntge": ospfPmIfUnresBwidthPcntge,
       "ospfPmIfUnresBwidth0": ospfPmIfUnresBwidth0,
       "ospfPmIfLastUnresBwidth0": ospfPmIfLastUnresBwidth0,
       "ospfPmIfUnresBwidth1": ospfPmIfUnresBwidth1,
       "ospfPmIfLastUnresBwidth1": ospfPmIfLastUnresBwidth1,
       "ospfPmIfUnresBwidth2": ospfPmIfUnresBwidth2,
       "ospfPmIfLastUnresBwidth2": ospfPmIfLastUnresBwidth2,
       "ospfPmIfUnresBwidth3": ospfPmIfUnresBwidth3,
       "ospfPmIfLastUnresBwidth3": ospfPmIfLastUnresBwidth3,
       "ospfPmIfUnresBwidth4": ospfPmIfUnresBwidth4,
       "ospfPmIfLastUnresBwidth4": ospfPmIfLastUnresBwidth4,
       "ospfPmIfUnresBwidth5": ospfPmIfUnresBwidth5,
       "ospfPmIfLastUnresBwidth5": ospfPmIfLastUnresBwidth5,
       "ospfPmIfUnresBwidth6": ospfPmIfUnresBwidth6,
       "ospfPmIfLastUnresBwidth6": ospfPmIfLastUnresBwidth6,
       "ospfPmIfUnresBwidth7": ospfPmIfUnresBwidth7,
       "ospfPmIfLastUnresBwidth7": ospfPmIfLastUnresBwidth7,
       "ospfPmIfIfIndex": ospfPmIfIfIndex,
       "ospfPmIfRemoteIfIndex": ospfPmIfRemoteIfIndex,
       "ospfPmIfLinkProtectionType": ospfPmIfLinkProtectionType,
       "ospfPmIfSRLG": ospfPmIfSRLG,
       "ospfPmIfMaxLSPBwidthPcntge": ospfPmIfMaxLSPBwidthPcntge,
       "ospfPmIfMinLSPBwidthPcntge": ospfPmIfMinLSPBwidthPcntge,
       "ospfPmIfMTUSizePcntge": ospfPmIfMTUSizePcntge,
       "ospfPmIfHelperModePolicy": ospfPmIfHelperModePolicy,
       "ospfPmIfMaxHitlessGracePeriod": ospfPmIfMaxHitlessGracePeriod,
       "ospfPmIfEnableTeFlooding": ospfPmIfEnableTeFlooding,
       "ospfPmIfAuthUserData": ospfPmIfAuthUserData,
       "ospfPmIfFastHelloMultiplier": ospfPmIfFastHelloMultiplier,
       "ospfPmIfAutoDeleteNbr": ospfPmIfAutoDeleteNbr,
       "ospfPmIfNumBwidthCnstrnts": ospfPmIfNumBwidthCnstrnts,
       "ospfPmIfBwidthCnstrntModel": ospfPmIfBwidthCnstrntModel,
       "ospfPmIfBwidthCnstrnt0": ospfPmIfBwidthCnstrnt0,
       "ospfPmIfBwidthCnstrnt1": ospfPmIfBwidthCnstrnt1,
       "ospfPmIfBwidthCnstrnt2": ospfPmIfBwidthCnstrnt2,
       "ospfPmIfBwidthCnstrnt3": ospfPmIfBwidthCnstrnt3,
       "ospfPmIfBwidthCnstrnt4": ospfPmIfBwidthCnstrnt4,
       "ospfPmIfBwidthCnstrnt5": ospfPmIfBwidthCnstrnt5,
       "ospfPmIfBwidthCnstrnt6": ospfPmIfBwidthCnstrnt6,
       "ospfPmIfBwidthCnstrnt7": ospfPmIfBwidthCnstrnt7,
       "ospfPmIfMtuIgnore": ospfPmIfMtuIgnore,
       "ospfPmIfNmEntity": ospfPmIfNmEntity,
       "ospfPmIfBfdDesired": ospfPmIfBfdDesired,
       "ospfPmIfRstHlprStrictLsaChk": ospfPmIfRstHlprStrictLsaChk,
       "ospfPmIfStatsReset": ospfPmIfStatsReset,
       "ospfPmIfGraceLsaResendTimer": ospfPmIfGraceLsaResendTimer,
       "ospfPmIfGRDelayTimer": ospfPmIfGRDelayTimer,
       "ospfPmIfMetricTable": ospfPmIfMetricTable,
       "ospfPmIfMetricEntry": ospfPmIfMetricEntry,
       "ospfPmIfMetricIpAddress": ospfPmIfMetricIpAddress,
       "ospfPmIfMetricAddressLessIf": ospfPmIfMetricAddressLessIf,
       "ospfPmIfMetricTOS": ospfPmIfMetricTOS,
       "ospfPmIfMetricValue": ospfPmIfMetricValue,
       "ospfPmIfMetricStatus": ospfPmIfMetricStatus,
       "ospfPmIfMetricApplIndex": ospfPmIfMetricApplIndex,
       "ospfPmVirtIfTable": ospfPmVirtIfTable,
       "ospfPmVirtIfEntry": ospfPmVirtIfEntry,
       "ospfPmVirtIfAreaId": ospfPmVirtIfAreaId,
       "ospfPmVirtIfNeighbor": ospfPmVirtIfNeighbor,
       "ospfPmVirtIfTransitDelay": ospfPmVirtIfTransitDelay,
       "ospfPmVirtIfRetransInterval": ospfPmVirtIfRetransInterval,
       "ospfPmVirtIfHelloInterval": ospfPmVirtIfHelloInterval,
       "ospfPmVirtIfRtrDeadInterval": ospfPmVirtIfRtrDeadInterval,
       "ospfPmVirtIfState": ospfPmVirtIfState,
       "ospfPmVirtIfEvents": ospfPmVirtIfEvents,
       "ospfPmVirtIfAuthKey": ospfPmVirtIfAuthKey,
       "ospfPmVirtIfStatus": ospfPmVirtIfStatus,
       "ospfPmVirtIfAuthType": ospfPmVirtIfAuthType,
       "ospfPmVirtIfLsaCount": ospfPmVirtIfLsaCount,
       "ospfPmVirtIfLsaCksumSum": ospfPmVirtIfLsaCksumSum,
       "ospfPmVirtIfApplIndex": ospfPmVirtIfApplIndex,
       "ospfPmVirtIfAdminStatus": ospfPmVirtIfAdminStatus,
       "ospfPmVirtIfOperStatus": ospfPmVirtIfOperStatus,
       "ospfPmVirtIfResourceClass": ospfPmVirtIfResourceClass,
       "ospfPmVirtIfTransmitTimerDelay": ospfPmVirtIfTransmitTimerDelay,
       "ospfPmVirtIfIPMaxPacketSize": ospfPmVirtIfIPMaxPacketSize,
       "ospfPmVirtIfPassive": ospfPmVirtIfPassive,
       "ospfPmVirtIfInterfaceName": ospfPmVirtIfInterfaceName,
       "ospfPmVirtIfLsaRefreshIntvl": ospfPmVirtIfLsaRefreshIntvl,
       "ospfPmVirtIfHelperModePolicy": ospfPmVirtIfHelperModePolicy,
       "ospfPmVirtIfMaxHtlssGracePeriod": ospfPmVirtIfMaxHtlssGracePeriod,
       "ospfPmVirtIfEnableTeFlooding": ospfPmVirtIfEnableTeFlooding,
       "ospfPmVirtIfAuthUserData": ospfPmVirtIfAuthUserData,
       "ospfPmVirtIfFastHelloMultiplier": ospfPmVirtIfFastHelloMultiplier,
       "ospfPmVirtIfMtuIgnore": ospfPmVirtIfMtuIgnore,
       "ospfPmVirtIfNmEntity": ospfPmVirtIfNmEntity,
       "ospfPmVirtIfBfdDesired": ospfPmVirtIfBfdDesired,
       "ospfPmVirtIfRstHlprStrictLsaChk": ospfPmVirtIfRstHlprStrictLsaChk,
       "ospfPmVirtIfStatsReset": ospfPmVirtIfStatsReset,
       "ospfPmVirtIfGRDelayTimer": ospfPmVirtIfGRDelayTimer,
       "ospfPmNbrTable": ospfPmNbrTable,
       "ospfPmNbrEntry": ospfPmNbrEntry,
       "ospfPmNbrIpAddr": ospfPmNbrIpAddr,
       "ospfPmNbrAddressLessIndex": ospfPmNbrAddressLessIndex,
       "ospfPmNbrRtrId": ospfPmNbrRtrId,
       "ospfPmNbrOptions": ospfPmNbrOptions,
       "ospfPmNbrPriority": ospfPmNbrPriority,
       "ospfPmNbrState": ospfPmNbrState,
       "ospfPmNbrEvents": ospfPmNbrEvents,
       "ospfPmNbrLsRetransQLen": ospfPmNbrLsRetransQLen,
       "ospfPmNbrStatus": ospfPmNbrStatus,
       "ospfPmNbrPermanence": ospfPmNbrPermanence,
       "ospfPmNbrHelloSuppressed": ospfPmNbrHelloSuppressed,
       "ospfPmNbrApplIndex": ospfPmNbrApplIndex,
       "ospfPmNbrAdminStatus": ospfPmNbrAdminStatus,
       "ospfPmNbrOperStatus": ospfPmNbrOperStatus,
       "ospfPmNbrNumRequests": ospfPmNbrNumRequests,
       "ospfPmNbrIfIpAddr": ospfPmNbrIfIpAddr,
       "ospfPmNbrDeadTime": ospfPmNbrDeadTime,
       "ospfPmNbrAreaId": ospfPmNbrAreaId,
       "ospfPmNbrRestartHelperStatus": ospfPmNbrRestartHelperStatus,
       "ospfPmNbrRestartHelperAge": ospfPmNbrRestartHelperAge,
       "ospfPmNbrRestartHelperExitReason": ospfPmNbrRestartHelperExitReason,
       "ospfPmNbrConfiguredPriority": ospfPmNbrConfiguredPriority,
       "ospfPmNbrDesignatedRtrState": ospfPmNbrDesignatedRtrState,
       "ospfPmVirtNbrTable": ospfPmVirtNbrTable,
       "ospfPmVirtNbrEntry": ospfPmVirtNbrEntry,
       "ospfPmVirtNbrArea": ospfPmVirtNbrArea,
       "ospfPmVirtNbrRtrId": ospfPmVirtNbrRtrId,
       "ospfPmVirtNbrIpAddr": ospfPmVirtNbrIpAddr,
       "ospfPmVirtNbrOptions": ospfPmVirtNbrOptions,
       "ospfPmVirtNbrState": ospfPmVirtNbrState,
       "ospfPmVirtNbrEvents": ospfPmVirtNbrEvents,
       "ospfPmVirtNbrLsRetransQLen": ospfPmVirtNbrLsRetransQLen,
       "ospfPmVirtNbrHelloSuppressed": ospfPmVirtNbrHelloSuppressed,
       "ospfPmVirtNbrApplIndex": ospfPmVirtNbrApplIndex,
       "ospfPmVirtNbrNumRequests": ospfPmVirtNbrNumRequests,
       "ospfPmVirtNbrDeadTime": ospfPmVirtNbrDeadTime,
       "ospfPmVirtNbrRestartHelperStatus": ospfPmVirtNbrRestartHelperStatus,
       "ospfPmVirtNbrRestartHelperAge": ospfPmVirtNbrRestartHelperAge,
       "ospfPmVirtNbrRestartHelperExit": ospfPmVirtNbrRestartHelperExit,
       "ospfPmExtLsdbTable": ospfPmExtLsdbTable,
       "ospfPmExtLsdbEntry": ospfPmExtLsdbEntry,
       "ospfPmExtLsdbType": ospfPmExtLsdbType,
       "ospfPmExtLsdbLsid": ospfPmExtLsdbLsid,
       "ospfPmExtLsdbRouterId": ospfPmExtLsdbRouterId,
       "ospfPmExtLsdbSequence": ospfPmExtLsdbSequence,
       "ospfPmExtLsdbAge": ospfPmExtLsdbAge,
       "ospfPmExtLsdbChecksum": ospfPmExtLsdbChecksum,
       "ospfPmExtLsdbAdvertisement": ospfPmExtLsdbAdvertisement,
       "ospfPmExtLsdbApplIndex": ospfPmExtLsdbApplIndex,
       "ospfPmRouteGroup": ospfPmRouteGroup,
       "ospfPmIntraArea": ospfPmIntraArea,
       "ospfPmInterArea": ospfPmInterArea,
       "ospfPmExternalType1": ospfPmExternalType1,
       "ospfPmExternalType2": ospfPmExternalType2,
       "ospfPmAreaAggregateTable": ospfPmAreaAggregateTable,
       "ospfPmAreaAggregateEntry": ospfPmAreaAggregateEntry,
       "ospfPmAreaAggregateAreaID": ospfPmAreaAggregateAreaID,
       "ospfPmAreaAggregateLsdbType": ospfPmAreaAggregateLsdbType,
       "ospfPmAreaAggregateNet": ospfPmAreaAggregateNet,
       "ospfPmAreaAggregateMask": ospfPmAreaAggregateMask,
       "ospfPmAreaAggregateStatus": ospfPmAreaAggregateStatus,
       "ospfPmAreaAggregateEffect": ospfPmAreaAggregateEffect,
       "ospfPmAreaAggregateApplIndex": ospfPmAreaAggregateApplIndex,
       "ospfPmLocalLsdbTable": ospfPmLocalLsdbTable,
       "ospfPmLocalLsdbEntry": ospfPmLocalLsdbEntry,
       "ospfPmLocalLsdbIpAddress": ospfPmLocalLsdbIpAddress,
       "ospfPmLocalLsdbAddressLessIf": ospfPmLocalLsdbAddressLessIf,
       "ospfPmLocalLsdbType": ospfPmLocalLsdbType,
       "ospfPmLocalLsdbLsid": ospfPmLocalLsdbLsid,
       "ospfPmLocalLsdbRouterId": ospfPmLocalLsdbRouterId,
       "ospfPmLocalLsdbSequence": ospfPmLocalLsdbSequence,
       "ospfPmLocalLsdbAge": ospfPmLocalLsdbAge,
       "ospfPmLocalLsdbChecksum": ospfPmLocalLsdbChecksum,
       "ospfPmLocalLsdbAdvertisement": ospfPmLocalLsdbAdvertisement,
       "ospfPmLocalLsdbApplIndex": ospfPmLocalLsdbApplIndex,
       "ospfPmLocalLsdbAreaId": ospfPmLocalLsdbAreaId,
       "ospfPmVirtLocalLsdbTable": ospfPmVirtLocalLsdbTable,
       "ospfPmVirtLocalLsdbEntry": ospfPmVirtLocalLsdbEntry,
       "ospfPmVirtLocalLsdbTransitArea": ospfPmVirtLocalLsdbTransitArea,
       "ospfPmVirtLocalLsdbNeighbor": ospfPmVirtLocalLsdbNeighbor,
       "ospfPmVirtLocalLsdbType": ospfPmVirtLocalLsdbType,
       "ospfPmVirtLocalLsdbLsid": ospfPmVirtLocalLsdbLsid,
       "ospfPmVirtLocalLsdbRouterId": ospfPmVirtLocalLsdbRouterId,
       "ospfPmVirtLocalLsdbSequence": ospfPmVirtLocalLsdbSequence,
       "ospfPmVirtLocalLsdbAge": ospfPmVirtLocalLsdbAge,
       "ospfPmVirtLocalLsdbChecksum": ospfPmVirtLocalLsdbChecksum,
       "ospfPmVirtLocalLsdbAdv": ospfPmVirtLocalLsdbAdv,
       "ospfPmVirtLocalLsdbApplIndex": ospfPmVirtLocalLsdbApplIndex,
       "ospfPmMjTable": ospfPmMjTable,
       "ospfPmMjEntry": ospfPmMjEntry,
       "ospfPmMjApplIndex": ospfPmMjApplIndex,
       "ospfPmMjInterfaceId": ospfPmMjInterfaceId,
       "ospfPmMjPartnerIndex": ospfPmMjPartnerIndex,
       "ospfPmMjRowStatus": ospfPmMjRowStatus,
       "ospfPmMjAdminStatus": ospfPmMjAdminStatus,
       "ospfPmMjOperStatus": ospfPmMjOperStatus,
       "ospfPmMjJoinStatus": ospfPmMjJoinStatus,
       "ospfPmSjTable": ospfPmSjTable,
       "ospfPmSjEntry": ospfPmSjEntry,
       "ospfPmSjApplIndex": ospfPmSjApplIndex,
       "ospfPmSjMasterIndex": ospfPmSjMasterIndex,
       "ospfPmSjJoinIndex": ospfPmSjJoinIndex,
       "ospfPmSjJoinStatus": ospfPmSjJoinStatus,
       "ospfPmSjInterfaceId": ospfPmSjInterfaceId,
       "ospfPmIfSwitchTable": ospfPmIfSwitchTable,
       "ospfPmIfSwitchEntry": ospfPmIfSwitchEntry,
       "ospfPmIfSwitchApplIndex": ospfPmIfSwitchApplIndex,
       "ospfPmIfSwitchIpAddress": ospfPmIfSwitchIpAddress,
       "ospfPmIfSwitchAddressLessIf": ospfPmIfSwitchAddressLessIf,
       "ospfPmIfSwitchingCap": ospfPmIfSwitchingCap,
       "ospfPmIfSwitchEncoding": ospfPmIfSwitchEncoding,
       "ospfPmIfSwitchMaxLSPBwidth0": ospfPmIfSwitchMaxLSPBwidth0,
       "ospfPmIfSwitchLastMaxLSPBwidth0": ospfPmIfSwitchLastMaxLSPBwidth0,
       "ospfPmIfSwitchMaxLSPBwidth1": ospfPmIfSwitchMaxLSPBwidth1,
       "ospfPmIfSwitchLastMaxLSPBwidth1": ospfPmIfSwitchLastMaxLSPBwidth1,
       "ospfPmIfSwitchMaxLSPBwidth2": ospfPmIfSwitchMaxLSPBwidth2,
       "ospfPmIfSwitchLastMaxLSPBwidth2": ospfPmIfSwitchLastMaxLSPBwidth2,
       "ospfPmIfSwitchMaxLSPBwidth3": ospfPmIfSwitchMaxLSPBwidth3,
       "ospfPmIfSwitchLastMaxLSPBwidth3": ospfPmIfSwitchLastMaxLSPBwidth3,
       "ospfPmIfSwitchMaxLSPBwidth4": ospfPmIfSwitchMaxLSPBwidth4,
       "ospfPmIfSwitchLastMaxLSPBwidth4": ospfPmIfSwitchLastMaxLSPBwidth4,
       "ospfPmIfSwitchMaxLSPBwidth5": ospfPmIfSwitchMaxLSPBwidth5,
       "ospfPmIfSwitchLastMaxLSPBwidth5": ospfPmIfSwitchLastMaxLSPBwidth5,
       "ospfPmIfSwitchMaxLSPBwidth6": ospfPmIfSwitchMaxLSPBwidth6,
       "ospfPmIfSwitchLastMaxLSPBwidth6": ospfPmIfSwitchLastMaxLSPBwidth6,
       "ospfPmIfSwitchMaxLSPBwidth7": ospfPmIfSwitchMaxLSPBwidth7,
       "ospfPmIfSwitchLastMaxLSPBwidth7": ospfPmIfSwitchLastMaxLSPBwidth7,
       "ospfPmIfSwitchMinLSPBwidth": ospfPmIfSwitchMinLSPBwidth,
       "ospfPmIfSwitchLastMinLSPBwidth": ospfPmIfSwitchLastMinLSPBwidth,
       "ospfPmIfSwitchMTUSize": ospfPmIfSwitchMTUSize,
       "ospfPmIfSwitchLastMTUSize": ospfPmIfSwitchLastMTUSize,
       "ospfPmIfSwitchSonetSdhSupport": ospfPmIfSwitchSonetSdhSupport,
       "ospfPmIfSwitchISDIndex": ospfPmIfSwitchISDIndex,
       "ospfNmEntTable": ospfNmEntTable,
       "ospfNmEntEntry": ospfNmEntEntry,
       "ospfNmEntIndex": ospfNmEntIndex,
       "ospfNmEntRowStatus": ospfNmEntRowStatus,
       "ospfNmEntAdminStatus": ospfNmEntAdminStatus,
       "ospfNmEntOperStatus": ospfNmEntOperStatus,
       "ospfNmMjEntityIndex": ospfNmMjEntityIndex,
       "ospfNmSckEntityIndex": ospfNmSckEntityIndex,
       "ospfNmEntNmiJoinOperStatus": ospfNmEntNmiJoinOperStatus,
       "ospfNmEntSckJoinOperStatus": ospfNmEntSckJoinOperStatus,
       "ospfNmEntBfdEntityIndex": ospfNmEntBfdEntityIndex,
       "ospfNmEntBfdJoinOperStatus": ospfNmEntBfdJoinOperStatus,
       "ospfNmEntStatsReset": ospfNmEntStatsReset,
       "ospfNmEntEnableTrapSupport": ospfNmEntEnableTrapSupport,
       "ospfPmIgpShortcutTable": ospfPmIgpShortcutTable,
       "ospfPmIgpShortcutEntry": ospfPmIgpShortcutEntry,
       "ospfPmShortcutApplIndex": ospfPmShortcutApplIndex,
       "ospfPmShortcutIfIndex": ospfPmShortcutIfIndex,
       "ospfPmShortcutRemoteAddress": ospfPmShortcutRemoteAddress,
       "ospfPmShortcutMetricType": ospfPmShortcutMetricType,
       "ospfPmShortcutMetricValue": ospfPmShortcutMetricValue,
       "ospfPmShortcutOperStatus": ospfPmShortcutOperStatus,
       "ospfPmDomainIdTable": ospfPmDomainIdTable,
       "ospfPmDomainIdEntry": ospfPmDomainIdEntry,
       "ospfPmDomainIdApplIndex": ospfPmDomainIdApplIndex,
       "ospfPmDomainIdValue": ospfPmDomainIdValue,
       "ospfPmDomainIdRowStatus": ospfPmDomainIdRowStatus,
       "ospfPmDomainIdRole": ospfPmDomainIdRole,
       "ospfPmDomainIdStatus": ospfPmDomainIdStatus,
       "ospfPmShamLinkTable": ospfPmShamLinkTable,
       "ospfPmShamLinkEntry": ospfPmShamLinkEntry,
       "ospfPmShamLinkApplIndex": ospfPmShamLinkApplIndex,
       "ospfPmShamLinkAreaId": ospfPmShamLinkAreaId,
       "ospfPmShamLinkLocalIpAddr": ospfPmShamLinkLocalIpAddr,
       "ospfPmShamLinkRemoteIpAddr": ospfPmShamLinkRemoteIpAddr,
       "ospfPmShamLinkRowStatus": ospfPmShamLinkRowStatus,
       "ospfPmShamLinkIfIndex": ospfPmShamLinkIfIndex,
       "ospfPmShamLinkMetric": ospfPmShamLinkMetric,
       "ospfPmShamLinkTransitDelay": ospfPmShamLinkTransitDelay,
       "ospfPmShamLinkRetransInterval": ospfPmShamLinkRetransInterval,
       "ospfPmShamLinkHelloInterval": ospfPmShamLinkHelloInterval,
       "ospfPmShamLinkRtrDeadInterval": ospfPmShamLinkRtrDeadInterval,
       "ospfPmShamLinkState": ospfPmShamLinkState,
       "ospfPmShamLinkEvents": ospfPmShamLinkEvents,
       "ospfPmShamLinkAuthType": ospfPmShamLinkAuthType,
       "ospfPmShamLinkAuthKey": ospfPmShamLinkAuthKey,
       "ospfPmShamLinkLsaCount": ospfPmShamLinkLsaCount,
       "ospfPmShamLinkLsaCksumSum": ospfPmShamLinkLsaCksumSum,
       "ospfPmShamLinkAdminStatus": ospfPmShamLinkAdminStatus,
       "ospfPmShamLinkOperStatus": ospfPmShamLinkOperStatus,
       "ospfPmShamLinkTransmitDelay": ospfPmShamLinkTransmitDelay,
       "ospfPmShamLinkIPMaxPacketSize": ospfPmShamLinkIPMaxPacketSize,
       "ospfPmShamLinkInterfaceName": ospfPmShamLinkInterfaceName,
       "ospfPmShamLinkLsaRefreshIntvl": ospfPmShamLinkLsaRefreshIntvl,
       "ospfPmShamLinkHelperModePolicy": ospfPmShamLinkHelperModePolicy,
       "ospfPmShamLinkMaxGracePeriod": ospfPmShamLinkMaxGracePeriod,
       "ospfPmShamLinkEnableTeFlooding": ospfPmShamLinkEnableTeFlooding,
       "ospfPmShamLinkAuthUserData": ospfPmShamLinkAuthUserData,
       "ospfPmShamLinkFastHelloMult": ospfPmShamLinkFastHelloMult,
       "ospfPmShamLinkMtuIgnore": ospfPmShamLinkMtuIgnore,
       "ospfPmShamLinkNmEntity": ospfPmShamLinkNmEntity,
       "ospfPmShamLinkRstStrictLsaChk": ospfPmShamLinkRstStrictLsaChk,
       "ospfPmShamLinkIpAddrConflict": ospfPmShamLinkIpAddrConflict,
       "ospfPmShamLinkStatsReset": ospfPmShamLinkStatsReset,
       "ospfPmShamLinkGrcLsaRsndTmr": ospfPmShamLinkGrcLsaRsndTmr,
       "ospfPmShamLinkGRDelayTimer": ospfPmShamLinkGRDelayTimer,
       "ospfPmShamNbrTable": ospfPmShamNbrTable,
       "ospfPmShamNbrEntry": ospfPmShamNbrEntry,
       "ospfPmShamNbrApplIndex": ospfPmShamNbrApplIndex,
       "ospfPmShamNbrAreaId": ospfPmShamNbrAreaId,
       "ospfPmShamNbrLocalIpAddr": ospfPmShamNbrLocalIpAddr,
       "ospfPmShamNbrRemoteIpAddr": ospfPmShamNbrRemoteIpAddr,
       "ospfPmShamNbrRouterId": ospfPmShamNbrRouterId,
       "ospfPmShamNbrOptions": ospfPmShamNbrOptions,
       "ospfPmShamNbrState": ospfPmShamNbrState,
       "ospfPmShamNbrEvents": ospfPmShamNbrEvents,
       "ospfPmShamNbrLsRetransQLen": ospfPmShamNbrLsRetransQLen,
       "ospfPmShamNbrNumRequests": ospfPmShamNbrNumRequests,
       "ospfPmShamNbrDeadTime": ospfPmShamNbrDeadTime,
       "ospfPmShamNbrRestartHelperStatus": ospfPmShamNbrRestartHelperStatus,
       "ospfPmShamNbrRestartHelperAge": ospfPmShamNbrRestartHelperAge,
       "ospfPmShamNbrRestartHelperExit": ospfPmShamNbrRestartHelperExit,
       "ospfPmShamLsdbTable": ospfPmShamLsdbTable,
       "ospfPmShamLsdbEntry": ospfPmShamLsdbEntry,
       "ospfPmShamLsdbApplIndex": ospfPmShamLsdbApplIndex,
       "ospfPmShamLsdbAreaId": ospfPmShamLsdbAreaId,
       "ospfPmShamLsdbLocalIpAddr": ospfPmShamLsdbLocalIpAddr,
       "ospfPmShamLsdbRemoteIpAddr": ospfPmShamLsdbRemoteIpAddr,
       "ospfPmShamLsdbType": ospfPmShamLsdbType,
       "ospfPmShamLsdbLsid": ospfPmShamLsdbLsid,
       "ospfPmShamLsdbRouterId": ospfPmShamLsdbRouterId,
       "ospfPmShamLsdbSequence": ospfPmShamLsdbSequence,
       "ospfPmShamLsdbAge": ospfPmShamLsdbAge,
       "ospfPmShamLsdbChecksum": ospfPmShamLsdbChecksum,
       "ospfPmShamLsdbAdvertisement": ospfPmShamLsdbAdvertisement,
       "ospfPmMultiAreaIfTable": ospfPmMultiAreaIfTable,
       "ospfPmMultiAreaIfEntry": ospfPmMultiAreaIfEntry,
       "ospfPmMultiAreaIfApplIndex": ospfPmMultiAreaIfApplIndex,
       "ospfPmMultiAreaIfIpAddress": ospfPmMultiAreaIfIpAddress,
       "ospfPmMultiAreaIfAddressLessIf": ospfPmMultiAreaIfAddressLessIf,
       "ospfPmMultiAreaIfAreaId": ospfPmMultiAreaIfAreaId,
       "ospfPmMultiAreaIfRemoteAddr": ospfPmMultiAreaIfRemoteAddr,
       "ospfPmMultiAreaIfStatus": ospfPmMultiAreaIfStatus,
       "ospfPmMultiAreaIfAdminStat": ospfPmMultiAreaIfAdminStat,
       "ospfPmMultiAreaIfOperStatus": ospfPmMultiAreaIfOperStatus,
       "ospfPmMultiAreaIfState": ospfPmMultiAreaIfState,
       "ospfPmMultiAreaIfEvents": ospfPmMultiAreaIfEvents,
       "ospfPmMultiAreaIfMetricValue": ospfPmMultiAreaIfMetricValue,
       "ospfPmMultiAreaIfTransitDelay": ospfPmMultiAreaIfTransitDelay,
       "ospfPmMultiAreaIfRetransInt": ospfPmMultiAreaIfRetransInt,
       "ospfPmMultiAreaIfHelloInt": ospfPmMultiAreaIfHelloInt,
       "ospfPmMultiAreaIfRtrDeadInt": ospfPmMultiAreaIfRtrDeadInt,
       "ospfPmMultiAreaIfFastHelloMult": ospfPmMultiAreaIfFastHelloMult,
       "ospfPmMultiAreaIfAuthType": ospfPmMultiAreaIfAuthType,
       "ospfPmMultiAreaIfAuthKey": ospfPmMultiAreaIfAuthKey,
       "ospfPmMultiAreaIfAuthUserData": ospfPmMultiAreaIfAuthUserData,
       "ospfPmIfMultiAreaIPMaxPktSize": ospfPmIfMultiAreaIPMaxPktSize,
       "ospfPmMultiAreaIfMtuIgnore": ospfPmMultiAreaIfMtuIgnore,
       "ospfPmMultiAreaIfLsaCount": ospfPmMultiAreaIfLsaCount,
       "ospfPmMultiAreaIfLsaCksumSum": ospfPmMultiAreaIfLsaCksumSum,
       "ospfPmMultiAreaIfTrsmtTmrDelay": ospfPmMultiAreaIfTrsmtTmrDelay,
       "ospfPmMultiAreaIfEnableTeFlood": ospfPmMultiAreaIfEnableTeFlood,
       "ospfPmMultiAreaIfStatsReset": ospfPmMultiAreaIfStatsReset,
       "ospfPmMultiAreaGraceLsaRsndTmr": ospfPmMultiAreaGraceLsaRsndTmr,
       "ospfPmMultiAreaGRDelayTimer": ospfPmMultiAreaGRDelayTimer,
       "ospfPmMultiAreaNbrTable": ospfPmMultiAreaNbrTable,
       "ospfPmMultiAreaNbrEntry": ospfPmMultiAreaNbrEntry,
       "ospfPmMultiAreaNbrApplIndex": ospfPmMultiAreaNbrApplIndex,
       "ospfPmMultiAreaNbrIfIpAddr": ospfPmMultiAreaNbrIfIpAddr,
       "ospfPmMultiAreaNbrAddrLessIf": ospfPmMultiAreaNbrAddrLessIf,
       "ospfPmMultiAreaNbrAreaId": ospfPmMultiAreaNbrAreaId,
       "ospfPmMultiAreaNbrRemoteAddr": ospfPmMultiAreaNbrRemoteAddr,
       "ospfPmMultiAreaNbrSrcIpAddr": ospfPmMultiAreaNbrSrcIpAddr,
       "ospfPmMultiAreaNbrRtrId": ospfPmMultiAreaNbrRtrId,
       "ospfPmMultiAreaNbrOptions": ospfPmMultiAreaNbrOptions,
       "ospfPmMultiAreaNbrState": ospfPmMultiAreaNbrState,
       "ospfPmMultiAreaNbrEvents": ospfPmMultiAreaNbrEvents,
       "ospfPmMultiAreaNbrLsRetransQLen": ospfPmMultiAreaNbrLsRetransQLen,
       "ospfPmMultiAreaNbrNumRequests": ospfPmMultiAreaNbrNumRequests,
       "ospfPmMultiAreaNbrDeadTime": ospfPmMultiAreaNbrDeadTime,
       "ospfPmMultiAreaNbrRstrtHelpSts": ospfPmMultiAreaNbrRstrtHelpSts,
       "ospfPmMultiAreaNbrRstrtHelpAge": ospfPmMultiAreaNbrRstrtHelpAge,
       "ospfPmMultiAreaNbrRstrtHelpExitR": ospfPmMultiAreaNbrRstrtHelpExitR,
       "ospfPmMultiAreaLclLsdbTable": ospfPmMultiAreaLclLsdbTable,
       "ospfPmMultiAreaLclLsdbEntry": ospfPmMultiAreaLclLsdbEntry,
       "ospfPmMultiAreaLclLsdbApplIndex": ospfPmMultiAreaLclLsdbApplIndex,
       "ospfPmMultiAreaLclLsdbIpAddr": ospfPmMultiAreaLclLsdbIpAddr,
       "ospfPmMultiAreaLclLsdbAddrLssIf": ospfPmMultiAreaLclLsdbAddrLssIf,
       "ospfPmMultiAreaLclLsdbAreaId": ospfPmMultiAreaLclLsdbAreaId,
       "ospfPmMultiAreaLclLsdbRemAddr": ospfPmMultiAreaLclLsdbRemAddr,
       "ospfPmMultiAreaLclLsdbType": ospfPmMultiAreaLclLsdbType,
       "ospfPmMultiAreaLclLsdbLsid": ospfPmMultiAreaLclLsdbLsid,
       "ospfPmMultiAreaLclLsdbRtrId": ospfPmMultiAreaLclLsdbRtrId,
       "ospfPmMultiAreaLclLsdbSequence": ospfPmMultiAreaLclLsdbSequence,
       "ospfPmMultiAreaLclLsdbAge": ospfPmMultiAreaLclLsdbAge,
       "ospfPmMultiAreaLclLsdbChecksum": ospfPmMultiAreaLclLsdbChecksum,
       "ospfPmMultiAreaLclLsdbAdvert": ospfPmMultiAreaLclLsdbAdvert,
       "ospfPmEntStatsTable": ospfPmEntStatsTable,
       "ospfPmEntStatsEntry": ospfPmEntStatsEntry,
       "ospfPmEntStatsIndex": ospfPmEntStatsIndex,
       "ospfPmEntStatsNoIf": ospfPmEntStatsNoIf,
       "ospfPmEntStatsNoVirtLink": ospfPmEntStatsNoVirtLink,
       "ospfPmEntStatsBadPacket": ospfPmEntStatsBadPacket,
       "ospfPmIfStatsTable": ospfPmIfStatsTable,
       "ospfPmIfStatsEntry": ospfPmIfStatsEntry,
       "ospfPmIfStatsApplIndex": ospfPmIfStatsApplIndex,
       "ospfPmIfStatsIpAddress": ospfPmIfStatsIpAddress,
       "ospfPmIfStatsAddressLessIf": ospfPmIfStatsAddressLessIf,
       "ospfPmIfStatsRxInvalid": ospfPmIfStatsRxInvalid,
       "ospfPmIfStatsRxInvalidByte": ospfPmIfStatsRxInvalidByte,
       "ospfPmIfStatsRxHello": ospfPmIfStatsRxHello,
       "ospfPmIfStatsRxHelloByte": ospfPmIfStatsRxHelloByte,
       "ospfPmIfStatsRxDbDes": ospfPmIfStatsRxDbDes,
       "ospfPmIfStatsRxDbDesByte": ospfPmIfStatsRxDbDesByte,
       "ospfPmIfStatsRxLsReq": ospfPmIfStatsRxLsReq,
       "ospfPmIfStatsRxLsReqByte": ospfPmIfStatsRxLsReqByte,
       "ospfPmIfStatsRxLsUpd": ospfPmIfStatsRxLsUpd,
       "ospfPmIfStatsRxLsUpdByte": ospfPmIfStatsRxLsUpdByte,
       "ospfPmIfStatsRxLsAck": ospfPmIfStatsRxLsAck,
       "ospfPmIfStatsRxLsAckByte": ospfPmIfStatsRxLsAckByte,
       "ospfPmIfStatsTxFailed": ospfPmIfStatsTxFailed,
       "ospfPmIfStatsTxFailedByte": ospfPmIfStatsTxFailedByte,
       "ospfPmIfStatsTxHello": ospfPmIfStatsTxHello,
       "ospfPmIfStatsTxHelloByte": ospfPmIfStatsTxHelloByte,
       "ospfPmIfStatsTxDbDes": ospfPmIfStatsTxDbDes,
       "ospfPmIfStatsTxDbDesByte": ospfPmIfStatsTxDbDesByte,
       "ospfPmIfStatsTxLsReq": ospfPmIfStatsTxLsReq,
       "ospfPmIfStatsTxLsReqByte": ospfPmIfStatsTxLsReqByte,
       "ospfPmIfStatsTxLsUpd": ospfPmIfStatsTxLsUpd,
       "ospfPmIfStatsTxLsUpdByte": ospfPmIfStatsTxLsUpdByte,
       "ospfPmIfStatsTxLsAck": ospfPmIfStatsTxLsAck,
       "ospfPmIfStatsTxLsAckByte": ospfPmIfStatsTxLsAckByte,
       "ospfPmIfStatsLength": ospfPmIfStatsLength,
       "ospfPmIfStatsCksum": ospfPmIfStatsCksum,
       "ospfPmIfStatsVersion": ospfPmIfStatsVersion,
       "ospfPmIfStatsBadSrc": ospfPmIfStatsBadSrc,
       "ospfPmIfStatsAreaMismatch": ospfPmIfStatsAreaMismatch,
       "ospfPmIfStatsSelfOrig": ospfPmIfStatsSelfOrig,
       "ospfPmIfStatsDupeId": ospfPmIfStatsDupeId,
       "ospfPmIfStatsHello": ospfPmIfStatsHello,
       "ospfPmIfStatsMtuMismatch": ospfPmIfStatsMtuMismatch,
       "ospfPmIfStatsNbrIgnored": ospfPmIfStatsNbrIgnored,
       "ospfPmIfStatsAuth": ospfPmIfStatsAuth,
       "ospfPmIfStatsWrongProto": ospfPmIfStatsWrongProto,
       "ospfPmIfStatsResourceErr": ospfPmIfStatsResourceErr,
       "ospfPmIfStatsVirtMaIfClash": ospfPmIfStatsVirtMaIfClash,
       "ospfPmIfStatsBadLsaLen": ospfPmIfStatsBadLsaLen,
       "ospfPmIfStatsLsaBadType": ospfPmIfStatsLsaBadType,
       "ospfPmIfStatsLsaBadLen": ospfPmIfStatsLsaBadLen,
       "ospfPmIfStatsLsaBadData": ospfPmIfStatsLsaBadData,
       "ospfPmIfStatsLsaBadCksum": ospfPmIfStatsLsaBadCksum,
       "ospfPmIfStatsIfStandby": ospfPmIfStatsIfStandby,
       "ospfPmIfStatsUnkNbmaNbr": ospfPmIfStatsUnkNbmaNbr,
       "ospfPmIfStatsUnkVirtNbr": ospfPmIfStatsUnkVirtNbr,
       "ospfPmIfStatsAuthMismatch": ospfPmIfStatsAuthMismatch,
       "ospfPmIfStatsAuthFailure": ospfPmIfStatsAuthFailure,
       "ospfPmIfStatsNetmaskMismatch": ospfPmIfStatsNetmaskMismatch,
       "ospfPmIfStatsHelloMismatch": ospfPmIfStatsHelloMismatch,
       "ospfPmIfStatsDeadMismatch": ospfPmIfStatsDeadMismatch,
       "ospfPmIfStatsOptionsMismatch": ospfPmIfStatsOptionsMismatch,
       "ospfPmIfStatsNbrAdminDown": ospfPmIfStatsNbrAdminDown,
       "ospfPmIfStatsPktLocalAddr": ospfPmIfStatsPktLocalAddr,
       "ospfPmIfStatsMaIfNotP2p": ospfPmIfStatsMaIfNotP2p,
       "ospfPmIfStatsBadPacket": ospfPmIfStatsBadPacket,
       "ospfPmVirtIfStatsTable": ospfPmVirtIfStatsTable,
       "ospfPmVirtIfStatsEntry": ospfPmVirtIfStatsEntry,
       "ospfPmVirtIfStatsApplIndex": ospfPmVirtIfStatsApplIndex,
       "ospfPmVirtIfStatsAreaId": ospfPmVirtIfStatsAreaId,
       "ospfPmVirtIfStatsNeighbor": ospfPmVirtIfStatsNeighbor,
       "ospfPmVirtIfStatsRxInvalid": ospfPmVirtIfStatsRxInvalid,
       "ospfPmVirtIfStatsRxInvalidByte": ospfPmVirtIfStatsRxInvalidByte,
       "ospfPmVirtIfStatsRxHello": ospfPmVirtIfStatsRxHello,
       "ospfPmVirtIfStatsRxHelloByte": ospfPmVirtIfStatsRxHelloByte,
       "ospfPmVirtIfStatsRxDbDes": ospfPmVirtIfStatsRxDbDes,
       "ospfPmVirtIfStatsRxDbDesByte": ospfPmVirtIfStatsRxDbDesByte,
       "ospfPmVirtIfStatsRxLsReq": ospfPmVirtIfStatsRxLsReq,
       "ospfPmVirtIfStatsRxLsReqByte": ospfPmVirtIfStatsRxLsReqByte,
       "ospfPmVirtIfStatsRxLsUpd": ospfPmVirtIfStatsRxLsUpd,
       "ospfPmVirtIfStatsRxLsUpdByte": ospfPmVirtIfStatsRxLsUpdByte,
       "ospfPmVirtIfStatsRxLsAck": ospfPmVirtIfStatsRxLsAck,
       "ospfPmVirtIfStatsRxLsAckByte": ospfPmVirtIfStatsRxLsAckByte,
       "ospfPmVirtIfStatsTxFailed": ospfPmVirtIfStatsTxFailed,
       "ospfPmVirtIfStatsTxFailedByte": ospfPmVirtIfStatsTxFailedByte,
       "ospfPmVirtIfStatsTxHello": ospfPmVirtIfStatsTxHello,
       "ospfPmVirtIfStatsTxHelloByte": ospfPmVirtIfStatsTxHelloByte,
       "ospfPmVirtIfStatsTxDbDes": ospfPmVirtIfStatsTxDbDes,
       "ospfPmVirtIfStatsTxDbDesByte": ospfPmVirtIfStatsTxDbDesByte,
       "ospfPmVirtIfStatsTxLsReq": ospfPmVirtIfStatsTxLsReq,
       "ospfPmVirtIfStatsTxLsReqByte": ospfPmVirtIfStatsTxLsReqByte,
       "ospfPmVirtIfStatsTxLsUpd": ospfPmVirtIfStatsTxLsUpd,
       "ospfPmVirtIfStatsTxLsUpdByte": ospfPmVirtIfStatsTxLsUpdByte,
       "ospfPmVirtIfStatsTxLsAck": ospfPmVirtIfStatsTxLsAck,
       "ospfPmVirtIfStatsTxLsAckByte": ospfPmVirtIfStatsTxLsAckByte,
       "ospfPmVirtIfStatsLength": ospfPmVirtIfStatsLength,
       "ospfPmVirtIfStatsCksum": ospfPmVirtIfStatsCksum,
       "ospfPmVirtIfStatsVersion": ospfPmVirtIfStatsVersion,
       "ospfPmVirtIfStatsBadSrc": ospfPmVirtIfStatsBadSrc,
       "ospfPmVirtIfStatsAreaMismatch": ospfPmVirtIfStatsAreaMismatch,
       "ospfPmVirtIfStatsSelfOrig": ospfPmVirtIfStatsSelfOrig,
       "ospfPmVirtIfStatsDupeId": ospfPmVirtIfStatsDupeId,
       "ospfPmVirtIfStatsHello": ospfPmVirtIfStatsHello,
       "ospfPmVirtIfStatsMtuMismatch": ospfPmVirtIfStatsMtuMismatch,
       "ospfPmVirtIfStatsNbrIgnored": ospfPmVirtIfStatsNbrIgnored,
       "ospfPmVirtIfStatsAuth": ospfPmVirtIfStatsAuth,
       "ospfPmVirtIfStatsWrongProto": ospfPmVirtIfStatsWrongProto,
       "ospfPmVirtIfStatsResourceErr": ospfPmVirtIfStatsResourceErr,
       "ospfPmVirtIfStatsVirtMaIfClash": ospfPmVirtIfStatsVirtMaIfClash,
       "ospfPmVirtIfStatsBadLsaLen": ospfPmVirtIfStatsBadLsaLen,
       "ospfPmVirtIfStatsLsaBadType": ospfPmVirtIfStatsLsaBadType,
       "ospfPmVirtIfStatsLsaBadLen": ospfPmVirtIfStatsLsaBadLen,
       "ospfPmVirtIfStatsLsaBadData": ospfPmVirtIfStatsLsaBadData,
       "ospfPmVirtIfStatsLsaBadCksum": ospfPmVirtIfStatsLsaBadCksum,
       "ospfPmVirtIfStatsUnkNbmaNbr": ospfPmVirtIfStatsUnkNbmaNbr,
       "ospfPmVirtIfStatsUnkVirtNbr": ospfPmVirtIfStatsUnkVirtNbr,
       "ospfPmVirtIfStatsAuthMismatch": ospfPmVirtIfStatsAuthMismatch,
       "ospfPmVirtIfStatsAuthFailure": ospfPmVirtIfStatsAuthFailure,
       "ospfPmVirtIfStatsNetmaskMismatch": ospfPmVirtIfStatsNetmaskMismatch,
       "ospfPmVirtIfStatsHelloMismatch": ospfPmVirtIfStatsHelloMismatch,
       "ospfPmVirtIfStatsDeadMismatch": ospfPmVirtIfStatsDeadMismatch,
       "ospfPmVirtIfStatsOptionsMismatch": ospfPmVirtIfStatsOptionsMismatch,
       "ospfPmVirtIfStatsNbrAdminDown": ospfPmVirtIfStatsNbrAdminDown,
       "ospfPmVirtIfStatsPktLocalAddr": ospfPmVirtIfStatsPktLocalAddr,
       "ospfPmVirtIfStatsMaIfNotP2p": ospfPmVirtIfStatsMaIfNotP2p,
       "ospfPmVirtIfStatsBadPacket": ospfPmVirtIfStatsBadPacket,
       "ospfPmShamLinkStatsTable": ospfPmShamLinkStatsTable,
       "ospfPmShamLinkStatsEntry": ospfPmShamLinkStatsEntry,
       "ospfPmShamLinkStatsApplIndex": ospfPmShamLinkStatsApplIndex,
       "ospfPmShamLinkStatsAreaId": ospfPmShamLinkStatsAreaId,
       "ospfPmShamLinkStatsLocalIpAddr": ospfPmShamLinkStatsLocalIpAddr,
       "ospfPmShamLinkStatsRemoteIpAddr": ospfPmShamLinkStatsRemoteIpAddr,
       "ospfPmShamLinkStatsRxInvalid": ospfPmShamLinkStatsRxInvalid,
       "ospfPmShamLinkStatsRxInvalidByte": ospfPmShamLinkStatsRxInvalidByte,
       "ospfPmShamLinkStatsRxHello": ospfPmShamLinkStatsRxHello,
       "ospfPmShamLinkStatsRxHelloByte": ospfPmShamLinkStatsRxHelloByte,
       "ospfPmShamLinkStatsRxDbDes": ospfPmShamLinkStatsRxDbDes,
       "ospfPmShamLinkStatsRxDbDesByte": ospfPmShamLinkStatsRxDbDesByte,
       "ospfPmShamLinkStatsRxLsReq": ospfPmShamLinkStatsRxLsReq,
       "ospfPmShamLinkStatsRxLsReqByte": ospfPmShamLinkStatsRxLsReqByte,
       "ospfPmShamLinkStatsRxLsUpd": ospfPmShamLinkStatsRxLsUpd,
       "ospfPmShamLinkStatsRxLsUpdByte": ospfPmShamLinkStatsRxLsUpdByte,
       "ospfPmShamLinkStatsRxLsAck": ospfPmShamLinkStatsRxLsAck,
       "ospfPmShamLinkStatsRxLsAckByte": ospfPmShamLinkStatsRxLsAckByte,
       "ospfPmShamLinkStatsTxFailed": ospfPmShamLinkStatsTxFailed,
       "ospfPmShamLinkStatsTxFailedByte": ospfPmShamLinkStatsTxFailedByte,
       "ospfPmShamLinkStatsTxHello": ospfPmShamLinkStatsTxHello,
       "ospfPmShamLinkStatsTxHelloByte": ospfPmShamLinkStatsTxHelloByte,
       "ospfPmShamLinkStatsTxDbDes": ospfPmShamLinkStatsTxDbDes,
       "ospfPmShamLinkStatsTxDbDesByte": ospfPmShamLinkStatsTxDbDesByte,
       "ospfPmShamLinkStatsTxLsReq": ospfPmShamLinkStatsTxLsReq,
       "ospfPmShamLinkStatsTxLsReqByte": ospfPmShamLinkStatsTxLsReqByte,
       "ospfPmShamLinkStatsTxLsUpd": ospfPmShamLinkStatsTxLsUpd,
       "ospfPmShamLinkStatsTxLsUpdByte": ospfPmShamLinkStatsTxLsUpdByte,
       "ospfPmShamLinkStatsTxLsAck": ospfPmShamLinkStatsTxLsAck,
       "ospfPmShamLinkStatsTxLsAckByte": ospfPmShamLinkStatsTxLsAckByte,
       "ospfPmShamLinkStatsLength": ospfPmShamLinkStatsLength,
       "ospfPmShamLinkStatsCksum": ospfPmShamLinkStatsCksum,
       "ospfPmShamLinkStatsVersion": ospfPmShamLinkStatsVersion,
       "ospfPmShamLinkStatsBadSrc": ospfPmShamLinkStatsBadSrc,
       "ospfPmShamLinkStatsAreaMismatch": ospfPmShamLinkStatsAreaMismatch,
       "ospfPmShamLinkStatsSelfOrig": ospfPmShamLinkStatsSelfOrig,
       "ospfPmShamLinkStatsDupeId": ospfPmShamLinkStatsDupeId,
       "ospfPmShamLinkStatsHello": ospfPmShamLinkStatsHello,
       "ospfPmShamLinkStatsMtuMismatch": ospfPmShamLinkStatsMtuMismatch,
       "ospfPmShamLinkStatsNbrIgnored": ospfPmShamLinkStatsNbrIgnored,
       "ospfPmShamLinkStatsAuth": ospfPmShamLinkStatsAuth,
       "ospfPmShamLinkStatsWrongProto": ospfPmShamLinkStatsWrongProto,
       "ospfPmShamLinkStatsResourceErr": ospfPmShamLinkStatsResourceErr,
       "ospfPmShamLinkStatsVirtMaIfClash": ospfPmShamLinkStatsVirtMaIfClash,
       "ospfPmShamLinkStatsBadLsaLen": ospfPmShamLinkStatsBadLsaLen,
       "ospfPmShamLinkStatsLsaBadType": ospfPmShamLinkStatsLsaBadType,
       "ospfPmShamLinkStatsLsaBadLen": ospfPmShamLinkStatsLsaBadLen,
       "ospfPmShamLinkStatsLsaBadData": ospfPmShamLinkStatsLsaBadData,
       "ospfPmShamLinkStatsLsaBadCksum": ospfPmShamLinkStatsLsaBadCksum,
       "ospfPmShamLinkStatsUnkNbmaNbr": ospfPmShamLinkStatsUnkNbmaNbr,
       "ospfPmShamLinkStatsUnkVirtNbr": ospfPmShamLinkStatsUnkVirtNbr,
       "ospfPmShamLinkStatsAuthMismatch": ospfPmShamLinkStatsAuthMismatch,
       "ospfPmShamLinkStatsAuthFailure": ospfPmShamLinkStatsAuthFailure,
       "ospfPmShamLinkStatsNetmaskMsmtch": ospfPmShamLinkStatsNetmaskMsmtch,
       "ospfPmShamLinkStatsHelloMismatch": ospfPmShamLinkStatsHelloMismatch,
       "ospfPmShamLinkStatsDeadMismatch": ospfPmShamLinkStatsDeadMismatch,
       "ospfPmShamLinkStatsOptionsMsmtch": ospfPmShamLinkStatsOptionsMsmtch,
       "ospfPmShamLinkStatsNbrAdminDown": ospfPmShamLinkStatsNbrAdminDown,
       "ospfPmShamLinkStatsPktLocalAddr": ospfPmShamLinkStatsPktLocalAddr,
       "ospfPmShamLinkStatsMaIfNotP2p": ospfPmShamLinkStatsMaIfNotP2p,
       "ospfPmShamLinkStatsBadPacket": ospfPmShamLinkStatsBadPacket,
       "ospfPmMaIfStatsTable": ospfPmMaIfStatsTable,
       "ospfPmMaIfStatsEntry": ospfPmMaIfStatsEntry,
       "ospfPmMaIfStatsApplIndex": ospfPmMaIfStatsApplIndex,
       "ospfPmMaIfStatsIpAddress": ospfPmMaIfStatsIpAddress,
       "ospfPmMaIfStatsAddressLessIf": ospfPmMaIfStatsAddressLessIf,
       "ospfPmMaIfStatsAreaId": ospfPmMaIfStatsAreaId,
       "ospfPmMaIfStatsRemoteAddr": ospfPmMaIfStatsRemoteAddr,
       "ospfPmMaIfStatsRxInvalid": ospfPmMaIfStatsRxInvalid,
       "ospfPmMaIfStatsRxInvalidByte": ospfPmMaIfStatsRxInvalidByte,
       "ospfPmMaIfStatsRxHello": ospfPmMaIfStatsRxHello,
       "ospfPmMaIfStatsRxHelloByte": ospfPmMaIfStatsRxHelloByte,
       "ospfPmMaIfStatsRxDbDes": ospfPmMaIfStatsRxDbDes,
       "ospfPmMaIfStatsRxDbDesByte": ospfPmMaIfStatsRxDbDesByte,
       "ospfPmMaIfStatsRxLsReq": ospfPmMaIfStatsRxLsReq,
       "ospfPmMaIfStatsRxLsReqByte": ospfPmMaIfStatsRxLsReqByte,
       "ospfPmMaIfStatsRxLsUpd": ospfPmMaIfStatsRxLsUpd,
       "ospfPmMaIfStatsRxLsUpdByte": ospfPmMaIfStatsRxLsUpdByte,
       "ospfPmMaIfStatsRxLsAck": ospfPmMaIfStatsRxLsAck,
       "ospfPmMaIfStatsRxLsAckByte": ospfPmMaIfStatsRxLsAckByte,
       "ospfPmMaIfStatsTxFailed": ospfPmMaIfStatsTxFailed,
       "ospfPmMaIfStatsTxFailedByte": ospfPmMaIfStatsTxFailedByte,
       "ospfPmMaIfStatsTxHello": ospfPmMaIfStatsTxHello,
       "ospfPmMaIfStatsTxHelloByte": ospfPmMaIfStatsTxHelloByte,
       "ospfPmMaIfStatsTxDbDes": ospfPmMaIfStatsTxDbDes,
       "ospfPmMaIfStatsTxDbDesByte": ospfPmMaIfStatsTxDbDesByte,
       "ospfPmMaIfStatsTxLsReq": ospfPmMaIfStatsTxLsReq,
       "ospfPmMaIfStatsTxLsReqByte": ospfPmMaIfStatsTxLsReqByte,
       "ospfPmMaIfStatsTxLsUpd": ospfPmMaIfStatsTxLsUpd,
       "ospfPmMaIfStatsTxLsUpdByte": ospfPmMaIfStatsTxLsUpdByte,
       "ospfPmMaIfStatsTxLsAck": ospfPmMaIfStatsTxLsAck,
       "ospfPmMaIfStatsTxLsAckByte": ospfPmMaIfStatsTxLsAckByte,
       "ospfPmMaIfStatsLength": ospfPmMaIfStatsLength,
       "ospfPmMaIfStatsCksum": ospfPmMaIfStatsCksum,
       "ospfPmMaIfStatsVersion": ospfPmMaIfStatsVersion,
       "ospfPmMaIfStatsBadSrc": ospfPmMaIfStatsBadSrc,
       "ospfPmMaIfStatsAreaMismatch": ospfPmMaIfStatsAreaMismatch,
       "ospfPmMaIfStatsSelfOrig": ospfPmMaIfStatsSelfOrig,
       "ospfPmMaIfStatsDupeId": ospfPmMaIfStatsDupeId,
       "ospfPmMaIfStatsHello": ospfPmMaIfStatsHello,
       "ospfPmMaIfStatsMtuMismatch": ospfPmMaIfStatsMtuMismatch,
       "ospfPmMaIfStatsNbrIgnored": ospfPmMaIfStatsNbrIgnored,
       "ospfPmMaIfStatsAuth": ospfPmMaIfStatsAuth,
       "ospfPmMaIfStatsWrongProto": ospfPmMaIfStatsWrongProto,
       "ospfPmMaIfStatsResourceErr": ospfPmMaIfStatsResourceErr,
       "ospfPmMaIfStatsVirtMaIfClash": ospfPmMaIfStatsVirtMaIfClash,
       "ospfPmMaIfStatsBadLsaLen": ospfPmMaIfStatsBadLsaLen,
       "ospfPmMaIfStatsLsaBadType": ospfPmMaIfStatsLsaBadType,
       "ospfPmMaIfStatsLsaBadLen": ospfPmMaIfStatsLsaBadLen,
       "ospfPmMaIfStatsLsaBadData": ospfPmMaIfStatsLsaBadData,
       "ospfPmMaIfStatsLsaBadCksum": ospfPmMaIfStatsLsaBadCksum,
       "ospfPmMaIfStatsUnkNbmaNbr": ospfPmMaIfStatsUnkNbmaNbr,
       "ospfPmMaIfStatsUnkVirtNbr": ospfPmMaIfStatsUnkVirtNbr,
       "ospfPmMaIfStatsAuthMismatch": ospfPmMaIfStatsAuthMismatch,
       "ospfPmMaIfStatsAuthFailure": ospfPmMaIfStatsAuthFailure,
       "ospfPmMaIfStatsNetmaskMismatch": ospfPmMaIfStatsNetmaskMismatch,
       "ospfPmMaIfStatsHelloMismatch": ospfPmMaIfStatsHelloMismatch,
       "ospfPmMaIfStatsDeadMismatch": ospfPmMaIfStatsDeadMismatch,
       "ospfPmMaIfStatsOptionsMismatch": ospfPmMaIfStatsOptionsMismatch,
       "ospfPmMaIfStatsNbrAdminDown": ospfPmMaIfStatsNbrAdminDown,
       "ospfPmMaIfStatsPktLocalAddr": ospfPmMaIfStatsPktLocalAddr,
       "ospfPmMaIfStatsMaIfNotP2p": ospfPmMaIfStatsMaIfNotP2p,
       "ospfPmMaIfStatsBadPacket": ospfPmMaIfStatsBadPacket,
       "ospfNmEntStatsTable": ospfNmEntStatsTable,
       "ospfNmEntStatsEntry": ospfNmEntStatsEntry,
       "ospfNmEntStatsIndex": ospfNmEntStatsIndex,
       "ospfNmEntStatsLength": ospfNmEntStatsLength,
       "ospfNmEntStatsNoIf": ospfNmEntStatsNoIf,
       "ospfNmEntStatsNoVirtLink": ospfNmEntStatsNoVirtLink,
       "ospfNmEntStatsInstanceId": ospfNmEntStatsInstanceId,
       "ospfNmEntStatsBadIpHdrLen": ospfNmEntStatsBadIpHdrLen,
       "ospfNmEntStatsVersion": ospfNmEntStatsVersion,
       "ospfNmEntStatsBadSrc": ospfNmEntStatsBadSrc,
       "ospfNmEntStatsResourceErr": ospfNmEntStatsResourceErr,
       "ospfNmEntStatsBadPacket": ospfNmEntStatsBadPacket,
       "ospfPmSpfEntryTable": ospfPmSpfEntryTable,
       "ospfPmSpfEntryEntry": ospfPmSpfEntryEntry,
       "ospfPmSpfEntryApplIndex": ospfPmSpfEntryApplIndex,
       "ospfPmSpfEntryAreaId": ospfPmSpfEntryAreaId,
       "ospfPmSpfEntryRtrId": ospfPmSpfEntryRtrId,
       "ospfPmSpfEntryNextHopIdx": ospfPmSpfEntryNextHopIdx,
       "ospfPmSpfEntryNextHopAddr": ospfPmSpfEntryNextHopAddr,
       "ospfPmSpfEntryIfIndex": ospfPmSpfEntryIfIndex,
       "ospfPmSpfEntryCost": ospfPmSpfEntryCost,
       "ospfPmSpfEntryIsASBR": ospfPmSpfEntryIsASBR,
       "ospfPmSpfEntryIsABR": ospfPmSpfEntryIsABR,
       "ospfPmSpfEntryIsVirtEndpt": ospfPmSpfEntryIsVirtEndpt,
       "ospfPmSpfEntryCalcIndex": ospfPmSpfEntryCalcIndex,
       "ospfPmRouteTable": ospfPmRouteTable,
       "ospfPmRouteEntry": ospfPmRouteEntry,
       "ospfPmRouteApplIndex": ospfPmRouteApplIndex,
       "ospfPmRouteAddrPrefix": ospfPmRouteAddrPrefix,
       "ospfPmRouteAddrPrefixLen": ospfPmRouteAddrPrefixLen,
       "ospfPmRouteNextHopIdx": ospfPmRouteNextHopIdx,
       "ospfPmRouteNextHopAddr": ospfPmRouteNextHopAddr,
       "ospfPmRouteIfIndex": ospfPmRouteIfIndex,
       "ospfPmRouteAreaId": ospfPmRouteAreaId,
       "ospfPmRouteCost": ospfPmRouteCost,
       "ospfPmRoutePathType": ospfPmRoutePathType,
       "ospfPmRouteCalcIndex": ospfPmRouteCalcIndex,
       "ospfPmRouterDestTable": ospfPmRouterDestTable,
       "ospfPmRouterDestEntry": ospfPmRouterDestEntry,
       "ospfPmRouterDestApplIndex": ospfPmRouterDestApplIndex,
       "ospfPmRouterDestRouterId": ospfPmRouterDestRouterId,
       "ospfPmRouterDestAreaId": ospfPmRouterDestAreaId,
       "ospfPmRouterDestNextHopIdx": ospfPmRouterDestNextHopIdx,
       "ospfPmRouterDestNextHopAddr": ospfPmRouterDestNextHopAddr,
       "ospfPmRouterDestIfIndex": ospfPmRouterDestIfIndex,
       "ospfPmRouterDestCost": ospfPmRouterDestCost,
       "ospfPmRouterDestIsASBR": ospfPmRouterDestIsASBR,
       "ospfPmRouterDestIsABR": ospfPmRouterDestIsABR,
       "ospfPmRouterDestIsVirtEndpt": ospfPmRouterDestIsVirtEndpt,
       "ospfPmRouterDestPathType": ospfPmRouterDestPathType,
       "ospfPmRouterDestCalcIndex": ospfPmRouterDestCalcIndex,
       "ospfConformance": ospfConformance,
       "ospfGroups": ospfGroups,
       "ospfBasicGroup": ospfBasicGroup,
       "ospfAreaGroup": ospfAreaGroup,
       "ospfStubAreaGroup": ospfStubAreaGroup,
       "ospfLsdbGroup": ospfLsdbGroup,
       "ospfHostGroup": ospfHostGroup,
       "ospfIfGroup": ospfIfGroup,
       "ospfIfMetricGroup": ospfIfMetricGroup,
       "ospfVirtIfGroup": ospfVirtIfGroup,
       "ospfNbrGroup": ospfNbrGroup,
       "ospfVirtNbrGroup": ospfVirtNbrGroup,
       "ospfExtLsdbGroup": ospfExtLsdbGroup,
       "ospfAreaAggregateGroup": ospfAreaAggregateGroup,
       "ospfPropLocalLsdbGroup": ospfPropLocalLsdbGroup,
       "ospfPropVirtLocalLsdbGroup": ospfPropVirtLocalLsdbGroup,
       "ospfPropMjGroup": ospfPropMjGroup,
       "ospfPropSjGroup": ospfPropSjGroup,
       "ospfPropIfSwitchGroup": ospfPropIfSwitchGroup,
       "ospfPropAreaObsoleteGroup": ospfPropAreaObsoleteGroup,
       "ospfPropVirtIfGroup": ospfPropVirtIfGroup,
       "ospfPropIfGroup": ospfPropIfGroup,
       "ospfPropAreaGroup": ospfPropAreaGroup,
       "ospfPropEntGroup": ospfPropEntGroup,
       "ospfPropNmEntGroup": ospfPropNmEntGroup,
       "ospfPropIgpShortcutGroup": ospfPropIgpShortcutGroup,
       "ospfPropDomainIdGroup": ospfPropDomainIdGroup,
       "ospfPropShamLinkGroup": ospfPropShamLinkGroup,
       "ospfPropShamNbrGroup": ospfPropShamNbrGroup,
       "ospfPropShamLsdbGroup": ospfPropShamLsdbGroup,
       "ospfPropMultiAreaIfGroup": ospfPropMultiAreaIfGroup,
       "ospfPropMultiAreaNbrGroup": ospfPropMultiAreaNbrGroup,
       "ospfPropMultiAreaLclLsdbGroup": ospfPropMultiAreaLclLsdbGroup,
       "ospfPropPmEntStatsGroup": ospfPropPmEntStatsGroup,
       "ospfPropIfStatsGroup": ospfPropIfStatsGroup,
       "ospfPropVirtIfStatsGroup": ospfPropVirtIfStatsGroup,
       "ospfPropShamLinkStatsGroup": ospfPropShamLinkStatsGroup,
       "ospfPmMaIfStatsGroup": ospfPmMaIfStatsGroup,
       "ospfPropNmEntStatsGroup": ospfPropNmEntStatsGroup,
       "ospfPmSpfEntryGroup": ospfPmSpfEntryGroup,
       "ospfPmRouteTableGroup": ospfPmRouteTableGroup,
       "ospfPmRouterDestGroup": ospfPmRouterDestGroup,
       "ospfCompliances": ospfCompliances,
       "ospfCompliance": ospfCompliance,
       "ospfTrap": ospfTrap,
       "ospfTraps": ospfTraps,
       "ospfVirtIfStateChange": ospfVirtIfStateChange,
       "ospfNbrStateChange": ospfNbrStateChange,
       "ospfVirtNbrStateChange": ospfVirtNbrStateChange,
       "ospfIfConfigError": ospfIfConfigError,
       "ospfVirtIfConfigError": ospfVirtIfConfigError,
       "ospfIfAuthFailure": ospfIfAuthFailure,
       "ospfVirtIfAuthFailure": ospfVirtIfAuthFailure,
       "ospfIfStateChange": ospfIfStateChange,
       "ospfNssaTranslatorStatusChange": ospfNssaTranslatorStatusChange,
       "ospfNbrRestartHelperStatusChange": ospfNbrRestartHelperStatusChange,
       "ospfVirtNbrRstrtHelperStatusChng": ospfVirtNbrRstrtHelperStatusChng,
       "ospfPmOperStateChange": ospfPmOperStateChange,
       "ospfTrapControl": ospfTrapControl,
       "ospfConfigErrorType": ospfConfigErrorType,
       "ospfPacketType": ospfPacketType,
       "ospfPacketSrc": ospfPacketSrc,
       "ospfTrapVirtIfAreaId": ospfTrapVirtIfAreaId,
       "ospfTrapVirtIfNeighbor": ospfTrapVirtIfNeighbor,
       "ospfTrapPmEntIndex": ospfTrapPmEntIndex,
       "ospfTrapNbrIpAddr": ospfTrapNbrIpAddr,
       "ospfTrapNbrAddressLessIndex": ospfTrapNbrAddressLessIndex,
       "ospfTrapVirtNbrArea": ospfTrapVirtNbrArea,
       "ospfTrapVirtNbrRtrId": ospfTrapVirtNbrRtrId,
       "ospfTrapNmEntIndexValid": ospfTrapNmEntIndexValid,
       "ospfTrapNmEntIndex": ospfTrapNmEntIndex,
       "ospfTrapIfIpAddress": ospfTrapIfIpAddress,
       "ospfTrapAddressLessIf": ospfTrapAddressLessIf,
       "ospfTrapAreaId": ospfTrapAreaId,
       "ospfTrapConformance": ospfTrapConformance,
       "ospfTrapGroups": ospfTrapGroups,
       "ospfTrapEventGroup": ospfTrapEventGroup,
       "ospfTrapControlGroup": ospfTrapControlGroup,
       "ospfTrapCompliances": ospfTrapCompliances,
       "ospfTrapCompliance": ospfTrapCompliance,
       "ospfTrapCompliance2": ospfTrapCompliance2}
)
