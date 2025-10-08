#
# PySNMP MIB module DC-MASTER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/DC-MASTER-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dcMasterTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 10, 13))
dcMasterTc.setRevisions(('2014-12-21 00:00',))
if mibBuilder.loadTexts: dcMasterTc.setLastUpdated('201412210000Z')
if mibBuilder.loadTexts: dcMasterTc.setOrganization('MRV Communications.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
opx = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 10))
class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

class BaseOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5), ("operStatusQuiescing", 6), ("operStatusNotReady", 7), ("operStatusFailed", 8), ("operStatusPrntFailed", 9), ("operStatusFailedPerm", 10), ("operStatusFailing", 11))

class NpgOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 8, 10, 11))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5), ("operStatusFailed", 8), ("operStatusFailedPerm", 10), ("operStatusFailing", 11))

class Unsigned32NonZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NumericIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NumericIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class EntityIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class EntityIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AuthUserDataString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 160)

class StdAccessListListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class StdAccessListListIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class StdAccessListRuleIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ExtAccessListListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ExtAccessListListIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ExtAccessListRuleIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class RouteAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("routeActionLocal", 1), ("routeActionForward", 2), ("routeActionReject", 3), ("routeActionDiscard", 4), ("routeActionTunnel", 5))

class AdminDistance(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PathType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 65536, 131072, 131073, 131074, 196608, 262144, 327680, 393216, 458752, 524288, 589824, 589825, 589826, 589827, 655360, 720896, 786432, 851968, 851969, 851970, 851971, 917504, 917505, 917506, 983040, 1048576, 1048577, 1048578, 1114112))
    namedValues = NamedValues(("pathTypeNone", 0), ("pathTypeOther", 65536), ("pathTypeConnected", 131072), ("pathTypeConfiguredLocal", 131073), ("pathTypeConfiguredConnected", 131074), ("pathTypeStatic", 196608), ("pathTypeIcmp", 262144), ("pathTypeEgp", 327680), ("pathTypeGgp", 393216), ("pathTypeHello", 458752), ("pathTypeRip", 524288), ("pathTypeIsisLevel1Int", 589824), ("pathTypeIsisLevel2Int", 589825), ("pathTypeIsisLevel1Ext", 589826), ("pathTypeIsisLevel2Ext", 589827), ("pathTypeEsis", 655360), ("pathTypeIgrp", 720896), ("pathTypeBbnspfigp", 786432), ("pathTypeOspfIntraArea", 851968), ("pathTypeOspfInterArea", 851969), ("pathTypeOspfType1Ext", 851970), ("pathTypeOspfType2Ext", 851971), ("pathTypeBgpInt", 917504), ("pathTypeBgpExt", 917505), ("pathTypeBgpVpn", 917506), ("pathTypeIdpr", 983040), ("pathTypeEigrp", 1048576), ("pathTypeEigrpInt", 1048577), ("pathTypeEigrpExt", 1048578), ("pathTypeDvmrp", 1114112))

class EntityProcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(553779200, 587268096, 1023475712, 1040252928, 1040318464, 1057030144, 1057095680, 1090584576, 1090650112, 1174470656, 1241579520, 1241645056))
    namedValues = NamedValues(("entityRsvp", 553779200), ("entityLdpSc", 587268096), ("entityRtm", 1023475712), ("entityOspfPm", 1040252928), ("entityOspfNm", 1040318464), ("entityIsisPm", 1057030144), ("entityIsisSdc", 1057095680), ("entityBgpRm", 1090584576), ("entityBgpNm", 1090650112), ("entityRipPm", 1174470656), ("entityOspfv3Pm", 1241579520), ("entityOspfv3Nm", 1241645056))

class InetSubAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("unicast", 1), ("multicast", 2))

class BfdSessionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("bfdSessNotRequired", 0), ("bfdSessInitial", 1), ("bfdSessActivating", 2), ("bfdSessActive", 3), ("bfdSessInactive", 4), ("bfdSessAdminDown", 5), ("bfdSessNoContact", 6))

class IgpShortcutMetricType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("metricTypeAbsolute", 1), ("metricTypeRelative", 2))

class IfOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class MjStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("mjNotJoined", 1), ("mjSentAddJoin", 2), ("mjSentRegister", 3), ("mjJoinActive", 4), ("mjSentUnregister", 5), ("mjSentDelJoin", 6), ("mjFailedToAdd", 7), ("mjFailedToRegister", 8), ("mjFailingOver", 9), ("mjFailed", 10), ("mjUnavailable", 11))

class SjStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("sjNotJoined", 1), ("sjJoined", 2), ("sjRcvdRegister", 3), ("sjJoinActive", 4), ("sjFailingOver", 5), ("sjFailed", 6), ("sjRcvdUnregister", 7), ("sjUnregDone", 8))

class InterfaceScope(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 3)

mibBuilder.exportSymbols("DC-MASTER-TC", PathType=PathType, AdminStatus=AdminStatus, BaseOperStatus=BaseOperStatus, InetSubAddressType=InetSubAddressType, nbase=nbase, dcMasterTc=dcMasterTc, NumericIndexOrZero=NumericIndexOrZero, ExtAccessListListIndex=ExtAccessListListIndex, StdAccessListListIndex=StdAccessListListIndex, AdminDistance=AdminDistance, SjStatus=SjStatus, EntityProcType=EntityProcType, NpgOperStatus=NpgOperStatus, EntityIndex=EntityIndex, EntityIndexOrZero=EntityIndexOrZero, StdAccessListRuleIndex=StdAccessListRuleIndex, ExtAccessListListIndexOrZero=ExtAccessListListIndexOrZero, MjStatus=MjStatus, OperStatus=OperStatus, PYSNMP_MODULE_ID=dcMasterTc, ExtAccessListRuleIndex=ExtAccessListRuleIndex, IgpShortcutMetricType=IgpShortcutMetricType, AuthUserDataString=AuthUserDataString, Unsigned32NonZero=Unsigned32NonZero, RouteAction=RouteAction, BfdSessionStatus=BfdSessionStatus, StdAccessListListIndexOrZero=StdAccessListListIndexOrZero, IfOperStatus=IfOperStatus, opx=opx, InterfaceScope=InterfaceScope, NumericIndex=NumericIndex)
