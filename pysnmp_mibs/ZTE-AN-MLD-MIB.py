# SNMP MIB module (ZTE-AN-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-MLD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:07 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(ZxAnIdList,
 ZxAnIfindex,
 ZxAnPortList,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIdList",
    "ZxAnIfindex",
    "ZxAnPortList",
    "zxAn")


# MODULE-IDENTITY

zxAnMldMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnMldObjects_ObjectIdentity = ObjectIdentity
zxAnMldObjects = _ZxAnMldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1)
)
_ZxAnMld_ObjectIdentity = ObjectIdentity
zxAnMld = _ZxAnMld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1)
)
_ZxAnMldGlobal_ObjectIdentity = ObjectIdentity
zxAnMldGlobal = _ZxAnMldGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1)
)


class _ZxAnMldAdminStatus_Type(Integer32):
    """Custom type zxAnMldAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldAdminStatus_Type.__name__ = "Integer32"
_ZxAnMldAdminStatus_Object = MibScalar
zxAnMldAdminStatus = _ZxAnMldAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 1),
    _ZxAnMldAdminStatus_Type()
)
zxAnMldAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldAdminStatus.setStatus("current")


class _ZxAnMldAging_Type(Integer32):
    """Custom type zxAnMldAging based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_ZxAnMldAging_Type.__name__ = "Integer32"
_ZxAnMldAging_Object = MibScalar
zxAnMldAging = _ZxAnMldAging_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 2),
    _ZxAnMldAging_Type()
)
zxAnMldAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldAging.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldAging.setUnits("seconds")


class _ZxAnMldWorkingMode_Type(Integer32):
    """Custom type zxAnMldWorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 1),
          ("routing", 2),
          ("snooping", 3))
    )


_ZxAnMldWorkingMode_Type.__name__ = "Integer32"
_ZxAnMldWorkingMode_Object = MibScalar
zxAnMldWorkingMode = _ZxAnMldWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 3),
    _ZxAnMldWorkingMode_Type()
)
zxAnMldWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldWorkingMode.setStatus("deprecated")


class _ZxAnMldMcastInAllVlan_Type(Integer32):
    """Custom type zxAnMldMcastInAllVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldMcastInAllVlan_Type.__name__ = "Integer32"
_ZxAnMldMcastInAllVlan_Object = MibScalar
zxAnMldMcastInAllVlan = _ZxAnMldMcastInAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 4),
    _ZxAnMldMcastInAllVlan_Type()
)
zxAnMldMcastInAllVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldMcastInAllVlan.setStatus("current")


class _ZxAnMldDefaultMvlan_Type(Integer32):
    """Custom type zxAnMldDefaultMvlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZxAnMldDefaultMvlan_Type.__name__ = "Integer32"
_ZxAnMldDefaultMvlan_Object = MibScalar
zxAnMldDefaultMvlan = _ZxAnMldDefaultMvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 5),
    _ZxAnMldDefaultMvlan_Type()
)
zxAnMldDefaultMvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldDefaultMvlan.setStatus("current")


class _ZxAnMldAutoConfigGrpToDefaultMvlan_Type(Integer32):
    """Custom type zxAnMldAutoConfigGrpToDefaultMvlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldAutoConfigGrpToDefaultMvlan_Type.__name__ = "Integer32"
_ZxAnMldAutoConfigGrpToDefaultMvlan_Object = MibScalar
zxAnMldAutoConfigGrpToDefaultMvlan = _ZxAnMldAutoConfigGrpToDefaultMvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 6),
    _ZxAnMldAutoConfigGrpToDefaultMvlan_Type()
)
zxAnMldAutoConfigGrpToDefaultMvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldAutoConfigGrpToDefaultMvlan.setStatus("current")
_ZxAnMldUserSideRoutingIp_Type = InetAddress
_ZxAnMldUserSideRoutingIp_Object = MibScalar
zxAnMldUserSideRoutingIp = _ZxAnMldUserSideRoutingIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 7),
    _ZxAnMldUserSideRoutingIp_Type()
)
zxAnMldUserSideRoutingIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldUserSideRoutingIp.setStatus("current")


class _ZxAnMldBandwidthCtrl_Type(Integer32):
    """Custom type zxAnMldBandwidthCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldBandwidthCtrl_Type.__name__ = "Integer32"
_ZxAnMldBandwidthCtrl_Object = MibScalar
zxAnMldBandwidthCtrl = _ZxAnMldBandwidthCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 8),
    _ZxAnMldBandwidthCtrl_Type()
)
zxAnMldBandwidthCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldBandwidthCtrl.setStatus("current")


class _ZxAnMldRobustnessVariable_Type(Integer32):
    """Custom type zxAnMldRobustnessVariable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ZxAnMldRobustnessVariable_Type.__name__ = "Integer32"
_ZxAnMldRobustnessVariable_Object = MibScalar
zxAnMldRobustnessVariable = _ZxAnMldRobustnessVariable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 9),
    _ZxAnMldRobustnessVariable_Type()
)
zxAnMldRobustnessVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldRobustnessVariable.setStatus("current")


class _ZxAnMldQueryInterval_Type(Integer32):
    """Custom type zxAnMldQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_ZxAnMldQueryInterval_Type.__name__ = "Integer32"
_ZxAnMldQueryInterval_Object = MibScalar
zxAnMldQueryInterval = _ZxAnMldQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 10),
    _ZxAnMldQueryInterval_Type()
)
zxAnMldQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldQueryInterval.setStatus("current")


class _ZxAnMldQueryMaxResponseTime_Type(Integer32):
    """Custom type zxAnMldQueryMaxResponseTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_ZxAnMldQueryMaxResponseTime_Type.__name__ = "Integer32"
_ZxAnMldQueryMaxResponseTime_Object = MibScalar
zxAnMldQueryMaxResponseTime = _ZxAnMldQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 11),
    _ZxAnMldQueryMaxResponseTime_Type()
)
zxAnMldQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldQueryMaxResponseTime.setUnits("0.1second")


class _ZxAnMldLastMembQueryInterval_Type(Integer32):
    """Custom type zxAnMldLastMembQueryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnMldLastMembQueryInterval_Type.__name__ = "Integer32"
_ZxAnMldLastMembQueryInterval_Object = MibScalar
zxAnMldLastMembQueryInterval = _ZxAnMldLastMembQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 12),
    _ZxAnMldLastMembQueryInterval_Type()
)
zxAnMldLastMembQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldLastMembQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldLastMembQueryInterval.setUnits("0.1second")


class _ZxAnMldLastMembQueryCount_Type(Integer32):
    """Custom type zxAnMldLastMembQueryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ZxAnMldLastMembQueryCount_Type.__name__ = "Integer32"
_ZxAnMldLastMembQueryCount_Object = MibScalar
zxAnMldLastMembQueryCount = _ZxAnMldLastMembQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 13),
    _ZxAnMldLastMembQueryCount_Type()
)
zxAnMldLastMembQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldLastMembQueryCount.setStatus("current")


class _ZxAnMldUnsolicitedReportInterval_Type(Integer32):
    """Custom type zxAnMldUnsolicitedReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnMldUnsolicitedReportInterval_Type.__name__ = "Integer32"
_ZxAnMldUnsolicitedReportInterval_Object = MibScalar
zxAnMldUnsolicitedReportInterval = _ZxAnMldUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 14),
    _ZxAnMldUnsolicitedReportInterval_Type()
)
zxAnMldUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldUnsolicitedReportInterval.setUnits("seconds")
_ZxAnMldNetworkSideHostIp_Type = InetAddress
_ZxAnMldNetworkSideHostIp_Object = MibScalar
zxAnMldNetworkSideHostIp = _ZxAnMldNetworkSideHostIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 15),
    _ZxAnMldNetworkSideHostIp_Type()
)
zxAnMldNetworkSideHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldNetworkSideHostIp.setStatus("current")


class _ZxAnMldForwCvlanOnOff_Type(Integer32):
    """Custom type zxAnMldForwCvlanOnOff based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldForwCvlanOnOff_Type.__name__ = "Integer32"
_ZxAnMldForwCvlanOnOff_Object = MibScalar
zxAnMldForwCvlanOnOff = _ZxAnMldForwCvlanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 16),
    _ZxAnMldForwCvlanOnOff_Type()
)
zxAnMldForwCvlanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldForwCvlanOnOff.setStatus("current")


class _ZxAnMldHostTrackOnOff_Type(Integer32):
    """Custom type zxAnMldHostTrackOnOff based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldHostTrackOnOff_Type.__name__ = "Integer32"
_ZxAnMldHostTrackOnOff_Object = MibScalar
zxAnMldHostTrackOnOff = _ZxAnMldHostTrackOnOff_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 17),
    _ZxAnMldHostTrackOnOff_Type()
)
zxAnMldHostTrackOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldHostTrackOnOff.setStatus("current")


class _ZxAnMldNonMatchGroup_Type(Integer32):
    """Custom type zxAnMldNonMatchGroup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("drop", 2))
    )


_ZxAnMldNonMatchGroup_Type.__name__ = "Integer32"
_ZxAnMldNonMatchGroup_Object = MibScalar
zxAnMldNonMatchGroup = _ZxAnMldNonMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 18),
    _ZxAnMldNonMatchGroup_Type()
)
zxAnMldNonMatchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldNonMatchGroup.setStatus("current")
_ZxAnMldGeneralLeaveGrpAddr_Type = InetAddress
_ZxAnMldGeneralLeaveGrpAddr_Object = MibScalar
zxAnMldGeneralLeaveGrpAddr = _ZxAnMldGeneralLeaveGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 19),
    _ZxAnMldGeneralLeaveGrpAddr_Type()
)
zxAnMldGeneralLeaveGrpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldGeneralLeaveGrpAddr.setStatus("current")


class _ZxAnMldLogOnOff_Type(Integer32):
    """Custom type zxAnMldLogOnOff based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldLogOnOff_Type.__name__ = "Integer32"
_ZxAnMldLogOnOff_Object = MibScalar
zxAnMldLogOnOff = _ZxAnMldLogOnOff_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 20),
    _ZxAnMldLogOnOff_Type()
)
zxAnMldLogOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldLogOnOff.setStatus("current")


class _ZxAnMldGroupThreshold_Type(Integer32):
    """Custom type zxAnMldGroupThreshold based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ZxAnMldGroupThreshold_Type.__name__ = "Integer32"
_ZxAnMldGroupThreshold_Object = MibScalar
zxAnMldGroupThreshold = _ZxAnMldGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 21),
    _ZxAnMldGroupThreshold_Type()
)
zxAnMldGroupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldGroupThreshold.setStatus("current")


class _ZxAnMldMulticastServiceModel_Type(Integer32):
    """Custom type zxAnMldMulticastServiceModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asm", 1),
          ("ssm", 2),
          ("asmAndSsm", 3))
    )


_ZxAnMldMulticastServiceModel_Type.__name__ = "Integer32"
_ZxAnMldMulticastServiceModel_Object = MibScalar
zxAnMldMulticastServiceModel = _ZxAnMldMulticastServiceModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 22),
    _ZxAnMldMulticastServiceModel_Type()
)
zxAnMldMulticastServiceModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldMulticastServiceModel.setStatus("current")


class _ZxAnMldV1AdminStatus_Type(Integer32):
    """Custom type zxAnMldV1AdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 2),
          ("drop", 3))
    )


_ZxAnMldV1AdminStatus_Type.__name__ = "Integer32"
_ZxAnMldV1AdminStatus_Object = MibScalar
zxAnMldV1AdminStatus = _ZxAnMldV1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 23),
    _ZxAnMldV1AdminStatus_Type()
)
zxAnMldV1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldV1AdminStatus.setStatus("current")


class _ZxAnMldV2AdminStatus_Type(Integer32):
    """Custom type zxAnMldV2AdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 2),
          ("drop", 3))
    )


_ZxAnMldV2AdminStatus_Type.__name__ = "Integer32"
_ZxAnMldV2AdminStatus_Object = MibScalar
zxAnMldV2AdminStatus = _ZxAnMldV2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 1, 24),
    _ZxAnMldV2AdminStatus_Type()
)
zxAnMldV2AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldV2AdminStatus.setStatus("current")
_ZxAnMldPortTable_Object = MibTable
zxAnMldPortTable = _ZxAnMldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnMldPortTable.setStatus("current")
_ZxAnMldPortEntry_Object = MibTableRow
zxAnMldPortEntry = _ZxAnMldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1)
)
zxAnMldPortEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnMldPortEntry.setStatus("current")
_ZxAnMldIfIndex_Type = ZxAnIfindex
_ZxAnMldIfIndex_Object = MibTableColumn
zxAnMldIfIndex = _ZxAnMldIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 1),
    _ZxAnMldIfIndex_Type()
)
zxAnMldIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldIfIndex.setStatus("current")


class _ZxAnMldPortAdminStatus_Type(Integer32):
    """Custom type zxAnMldPortAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("drop", 3))
    )


_ZxAnMldPortAdminStatus_Type.__name__ = "Integer32"
_ZxAnMldPortAdminStatus_Object = MibTableColumn
zxAnMldPortAdminStatus = _ZxAnMldPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 2),
    _ZxAnMldPortAdminStatus_Type()
)
zxAnMldPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortAdminStatus.setStatus("current")


class _ZxAnMldPortProtoVersion_Type(Integer32):
    """Custom type zxAnMldPortProtoVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mldv1", 1),
          ("mldv2", 2))
    )


_ZxAnMldPortProtoVersion_Type.__name__ = "Integer32"
_ZxAnMldPortProtoVersion_Object = MibTableColumn
zxAnMldPortProtoVersion = _ZxAnMldPortProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 3),
    _ZxAnMldPortProtoVersion_Type()
)
zxAnMldPortProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortProtoVersion.setStatus("current")


class _ZxAnMldPortFastLeaveEnable_Type(TruthValue):
    """Custom type zxAnMldPortFastLeaveEnable based on TruthValue"""
    defaultValue = 1


_ZxAnMldPortFastLeaveEnable_Type.__name__ = "TruthValue"
_ZxAnMldPortFastLeaveEnable_Object = MibTableColumn
zxAnMldPortFastLeaveEnable = _ZxAnMldPortFastLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 4),
    _ZxAnMldPortFastLeaveEnable_Type()
)
zxAnMldPortFastLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortFastLeaveEnable.setStatus("current")
_ZxAnMldPortProxyIp_Type = InetAddress
_ZxAnMldPortProxyIp_Object = MibTableColumn
zxAnMldPortProxyIp = _ZxAnMldPortProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 5),
    _ZxAnMldPortProxyIp_Type()
)
zxAnMldPortProxyIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortProxyIp.setStatus("current")
_ZxAnMldPortPacketLimit_Type = Integer32
_ZxAnMldPortPacketLimit_Object = MibTableColumn
zxAnMldPortPacketLimit = _ZxAnMldPortPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 6),
    _ZxAnMldPortPacketLimit_Type()
)
zxAnMldPortPacketLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortPacketLimit.setStatus("current")


class _ZxAnMldPortMaxBandwidth_Type(Integer32):
    """Custom type zxAnMldPortMaxBandwidth based on Integer32"""
    defaultValue = 2048


_ZxAnMldPortMaxBandwidth_Type.__name__ = "Integer32"
_ZxAnMldPortMaxBandwidth_Object = MibTableColumn
zxAnMldPortMaxBandwidth = _ZxAnMldPortMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 7),
    _ZxAnMldPortMaxBandwidth_Type()
)
zxAnMldPortMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldPortMaxBandwidth.setUnits("kbps")


class _ZxAnMldPortMaxConcurrGroups_Type(Integer32):
    """Custom type zxAnMldPortMaxConcurrGroups based on Integer32"""
    defaultValue = 1


_ZxAnMldPortMaxConcurrGroups_Type.__name__ = "Integer32"
_ZxAnMldPortMaxConcurrGroups_Object = MibTableColumn
zxAnMldPortMaxConcurrGroups = _ZxAnMldPortMaxConcurrGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 8),
    _ZxAnMldPortMaxConcurrGroups_Type()
)
zxAnMldPortMaxConcurrGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortMaxConcurrGroups.setStatus("current")
_ZxAnMldPortCurrActGroups_Type = Gauge32
_ZxAnMldPortCurrActGroups_Object = MibTableColumn
zxAnMldPortCurrActGroups = _ZxAnMldPortCurrActGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 9),
    _ZxAnMldPortCurrActGroups_Type()
)
zxAnMldPortCurrActGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldPortCurrActGroups.setStatus("current")


class _ZxAnMldPortQueryInterval_Type(Integer32):
    """Custom type zxAnMldPortQueryInterval based on Integer32"""
    defaultValue = 125


_ZxAnMldPortQueryInterval_Type.__name__ = "Integer32"
_ZxAnMldPortQueryInterval_Object = MibTableColumn
zxAnMldPortQueryInterval = _ZxAnMldPortQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 10),
    _ZxAnMldPortQueryInterval_Type()
)
zxAnMldPortQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortQueryInterval.setStatus("current")


class _ZxAnMldPortLastMembQueryIntvl_Type(Integer32):
    """Custom type zxAnMldPortLastMembQueryIntvl based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_ZxAnMldPortLastMembQueryIntvl_Type.__name__ = "Integer32"
_ZxAnMldPortLastMembQueryIntvl_Object = MibTableColumn
zxAnMldPortLastMembQueryIntvl = _ZxAnMldPortLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 11),
    _ZxAnMldPortLastMembQueryIntvl_Type()
)
zxAnMldPortLastMembQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldPortLastMembQueryIntvl.setUnits("milli-seconds")


class _ZxAnMldPortQueryMaxResponseTime_Type(Integer32):
    """Custom type zxAnMldPortQueryMaxResponseTime based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_ZxAnMldPortQueryMaxResponseTime_Type.__name__ = "Integer32"
_ZxAnMldPortQueryMaxResponseTime_Object = MibTableColumn
zxAnMldPortQueryMaxResponseTime = _ZxAnMldPortQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 12),
    _ZxAnMldPortQueryMaxResponseTime_Type()
)
zxAnMldPortQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldPortQueryMaxResponseTime.setUnits("milli-seconds")


class _ZxAnMldPortEtherPriority_Type(Integer32):
    """Custom type zxAnMldPortEtherPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnMldPortEtherPriority_Type.__name__ = "Integer32"
_ZxAnMldPortEtherPriority_Object = MibTableColumn
zxAnMldPortEtherPriority = _ZxAnMldPortEtherPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 13),
    _ZxAnMldPortEtherPriority_Type()
)
zxAnMldPortEtherPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortEtherPriority.setStatus("current")


class _ZxAnMldPortRobustness_Type(Integer32):
    """Custom type zxAnMldPortRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnMldPortRobustness_Type.__name__ = "Integer32"
_ZxAnMldPortRobustness_Object = MibTableColumn
zxAnMldPortRobustness = _ZxAnMldPortRobustness_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 14),
    _ZxAnMldPortRobustness_Type()
)
zxAnMldPortRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldPortRobustness.setStatus("current")


class _ZxAnMldMvlanAutoTranslateEnable_Type(Integer32):
    """Custom type zxAnMldMvlanAutoTranslateEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMldMvlanAutoTranslateEnable_Type.__name__ = "Integer32"
_ZxAnMldMvlanAutoTranslateEnable_Object = MibTableColumn
zxAnMldMvlanAutoTranslateEnable = _ZxAnMldMvlanAutoTranslateEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 2, 1, 15),
    _ZxAnMldMvlanAutoTranslateEnable_Type()
)
zxAnMldMvlanAutoTranslateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldMvlanAutoTranslateEnable.setStatus("current")
_ZxAnMldMvlanTable_Object = MibTable
zxAnMldMvlanTable = _ZxAnMldMvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnMldMvlanTable.setStatus("current")
_ZxAnMldMvlanEntry_Object = MibTableRow
zxAnMldMvlanEntry = _ZxAnMldMvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1)
)
zxAnMldMvlanEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
)
if mibBuilder.loadTexts:
    zxAnMldMvlanEntry.setStatus("current")


class _ZxAnMldVlanId_Type(Integer32):
    """Custom type zxAnMldVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnMldVlanId_Type.__name__ = "Integer32"
_ZxAnMldVlanId_Object = MibTableColumn
zxAnMldVlanId = _ZxAnMldVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 1),
    _ZxAnMldVlanId_Type()
)
zxAnMldVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldVlanId.setStatus("current")


class _ZxAnMldMvlanAdminStatus_Type(Integer32):
    """Custom type zxAnMldMvlanAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("drop", 3))
    )


_ZxAnMldMvlanAdminStatus_Type.__name__ = "Integer32"
_ZxAnMldMvlanAdminStatus_Object = MibTableColumn
zxAnMldMvlanAdminStatus = _ZxAnMldMvlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 2),
    _ZxAnMldMvlanAdminStatus_Type()
)
zxAnMldMvlanAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanAdminStatus.setStatus("current")


class _ZxAnMldMvlanWorkMode_Type(Integer32):
    """Custom type zxAnMldMvlanWorkMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snooping", 1),
          ("router", 2),
          ("proxy", 3))
    )


_ZxAnMldMvlanWorkMode_Type.__name__ = "Integer32"
_ZxAnMldMvlanWorkMode_Object = MibTableColumn
zxAnMldMvlanWorkMode = _ZxAnMldMvlanWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 3),
    _ZxAnMldMvlanWorkMode_Type()
)
zxAnMldMvlanWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanWorkMode.setStatus("current")
_ZxAnMldMvlanNetworkSideHostIp_Type = InetAddress
_ZxAnMldMvlanNetworkSideHostIp_Object = MibTableColumn
zxAnMldMvlanNetworkSideHostIp = _ZxAnMldMvlanNetworkSideHostIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 4),
    _ZxAnMldMvlanNetworkSideHostIp_Type()
)
zxAnMldMvlanNetworkSideHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanNetworkSideHostIp.setStatus("current")
_ZxAnMldMvlanGroupFilterEnable_Type = TruthValue
_ZxAnMldMvlanGroupFilterEnable_Object = MibTableColumn
zxAnMldMvlanGroupFilterEnable = _ZxAnMldMvlanGroupFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 5),
    _ZxAnMldMvlanGroupFilterEnable_Type()
)
zxAnMldMvlanGroupFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanGroupFilterEnable.setStatus("current")


class _ZxAnMldMvlanMaxGroups_Type(Integer32):
    """Custom type zxAnMldMvlanMaxGroups based on Integer32"""
    defaultValue = 512


_ZxAnMldMvlanMaxGroups_Type.__name__ = "Integer32"
_ZxAnMldMvlanMaxGroups_Object = MibTableColumn
zxAnMldMvlanMaxGroups = _ZxAnMldMvlanMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 6),
    _ZxAnMldMvlanMaxGroups_Type()
)
zxAnMldMvlanMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanMaxGroups.setStatus("current")
_ZxAnMldMvlanCurrActGroups_Type = Gauge32
_ZxAnMldMvlanCurrActGroups_Object = MibTableColumn
zxAnMldMvlanCurrActGroups = _ZxAnMldMvlanCurrActGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 7),
    _ZxAnMldMvlanCurrActGroups_Type()
)
zxAnMldMvlanCurrActGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldMvlanCurrActGroups.setStatus("current")


class _ZxAnMldMvlanPriority_Type(Integer32):
    """Custom type zxAnMldMvlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnMldMvlanPriority_Type.__name__ = "Integer32"
_ZxAnMldMvlanPriority_Object = MibTableColumn
zxAnMldMvlanPriority = _ZxAnMldMvlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 8),
    _ZxAnMldMvlanPriority_Type()
)
zxAnMldMvlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanPriority.setStatus("current")


class _ZxAnMldMvlanHostVersion_Type(Integer32):
    """Custom type zxAnMldMvlanHostVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mldv1", 2),
          ("mldv2", 3))
    )


_ZxAnMldMvlanHostVersion_Type.__name__ = "Integer32"
_ZxAnMldMvlanHostVersion_Object = MibTableColumn
zxAnMldMvlanHostVersion = _ZxAnMldMvlanHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 9),
    _ZxAnMldMvlanHostVersion_Type()
)
zxAnMldMvlanHostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanHostVersion.setStatus("current")
_ZxAnMldMvlanRowStatus_Type = RowStatus
_ZxAnMldMvlanRowStatus_Object = MibTableColumn
zxAnMldMvlanRowStatus = _ZxAnMldMvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 3, 1, 20),
    _ZxAnMldMvlanRowStatus_Type()
)
zxAnMldMvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanRowStatus.setStatus("current")
_ZxAnMldMvlanPortListTable_Object = MibTable
zxAnMldMvlanPortListTable = _ZxAnMldMvlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnMldMvlanPortListTable.setStatus("current")
_ZxAnMldMvlanPortListEntry_Object = MibTableRow
zxAnMldMvlanPortListEntry = _ZxAnMldMvlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 4, 1)
)
zxAnMldMvlanPortListEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldMvlanPortListShelf"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldMvlanPortListCard"),
)
if mibBuilder.loadTexts:
    zxAnMldMvlanPortListEntry.setStatus("current")
_ZxAnMldMvlanPortListShelf_Type = Integer32
_ZxAnMldMvlanPortListShelf_Object = MibTableColumn
zxAnMldMvlanPortListShelf = _ZxAnMldMvlanPortListShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 4, 1, 1),
    _ZxAnMldMvlanPortListShelf_Type()
)
zxAnMldMvlanPortListShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldMvlanPortListShelf.setStatus("current")
_ZxAnMldMvlanPortListCard_Type = Integer32
_ZxAnMldMvlanPortListCard_Object = MibTableColumn
zxAnMldMvlanPortListCard = _ZxAnMldMvlanPortListCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 4, 1, 2),
    _ZxAnMldMvlanPortListCard_Type()
)
zxAnMldMvlanPortListCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldMvlanPortListCard.setStatus("current")
_ZxAnMldMvlanPortSrcPortList_Type = ZxAnPortList
_ZxAnMldMvlanPortSrcPortList_Object = MibTableColumn
zxAnMldMvlanPortSrcPortList = _ZxAnMldMvlanPortSrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 4, 1, 3),
    _ZxAnMldMvlanPortSrcPortList_Type()
)
zxAnMldMvlanPortSrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanPortSrcPortList.setStatus("current")
_ZxAnMldMvlanPortRecvPortList_Type = ZxAnPortList
_ZxAnMldMvlanPortRecvPortList_Object = MibTableColumn
zxAnMldMvlanPortRecvPortList = _ZxAnMldMvlanPortRecvPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 4, 1, 4),
    _ZxAnMldMvlanPortRecvPortList_Type()
)
zxAnMldMvlanPortRecvPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldMvlanPortRecvPortList.setStatus("current")
_ZxAnMldGroupTable_Object = MibTable
zxAnMldGroupTable = _ZxAnMldGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnMldGroupTable.setStatus("current")
_ZxAnMldGroupEntry_Object = MibTableRow
zxAnMldGroupEntry = _ZxAnMldGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1)
)
zxAnMldGroupEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldSrcIp"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldGrpIp"),
)
if mibBuilder.loadTexts:
    zxAnMldGroupEntry.setStatus("current")
_ZxAnMldSrcIp_Type = InetAddress
_ZxAnMldSrcIp_Object = MibTableColumn
zxAnMldSrcIp = _ZxAnMldSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 1),
    _ZxAnMldSrcIp_Type()
)
zxAnMldSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldSrcIp.setStatus("current")
_ZxAnMldGrpIp_Type = InetAddress
_ZxAnMldGrpIp_Object = MibTableColumn
zxAnMldGrpIp = _ZxAnMldGrpIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 2),
    _ZxAnMldGrpIp_Type()
)
zxAnMldGrpIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldGrpIp.setStatus("current")


class _ZxAnMldGroupBandwidthCost_Type(Integer32):
    """Custom type zxAnMldGroupBandwidthCost based on Integer32"""
    defaultValue = 2048


_ZxAnMldGroupBandwidthCost_Type.__name__ = "Integer32"
_ZxAnMldGroupBandwidthCost_Object = MibTableColumn
zxAnMldGroupBandwidthCost = _ZxAnMldGroupBandwidthCost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 3),
    _ZxAnMldGroupBandwidthCost_Type()
)
zxAnMldGroupBandwidthCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldGroupBandwidthCost.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMldGroupBandwidthCost.setUnits("kbps")


class _ZxAnMldGroupPrejoinEnable_Type(TruthValue):
    """Custom type zxAnMldGroupPrejoinEnable based on TruthValue"""
    defaultValue = 2


_ZxAnMldGroupPrejoinEnable_Type.__name__ = "TruthValue"
_ZxAnMldGroupPrejoinEnable_Object = MibTableColumn
zxAnMldGroupPrejoinEnable = _ZxAnMldGroupPrejoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 4),
    _ZxAnMldGroupPrejoinEnable_Type()
)
zxAnMldGroupPrejoinEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldGroupPrejoinEnable.setStatus("current")
_ZxAnMldGroupMaxHosts_Type = Integer32
_ZxAnMldGroupMaxHosts_Object = MibTableColumn
zxAnMldGroupMaxHosts = _ZxAnMldGroupMaxHosts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 5),
    _ZxAnMldGroupMaxHosts_Type()
)
zxAnMldGroupMaxHosts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldGroupMaxHosts.setStatus("current")
_ZxAnMldGroupActHosts_Type = Integer32
_ZxAnMldGroupActHosts_Object = MibTableColumn
zxAnMldGroupActHosts = _ZxAnMldGroupActHosts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 6),
    _ZxAnMldGroupActHosts_Type()
)
zxAnMldGroupActHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldGroupActHosts.setStatus("current")
_ZxAnMldGroupSrcIp_Type = InetAddress
_ZxAnMldGroupSrcIp_Object = MibTableColumn
zxAnMldGroupSrcIp = _ZxAnMldGroupSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 7),
    _ZxAnMldGroupSrcIp_Type()
)
zxAnMldGroupSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldGroupSrcIp.setStatus("current")


class _ZxAnMldGroupHostState_Type(Integer32):
    """Custom type zxAnMldGroupHostState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonMember", 1),
          ("idleMember", 2),
          ("delayingMember", 3))
    )


_ZxAnMldGroupHostState_Type.__name__ = "Integer32"
_ZxAnMldGroupHostState_Object = MibTableColumn
zxAnMldGroupHostState = _ZxAnMldGroupHostState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 8),
    _ZxAnMldGroupHostState_Type()
)
zxAnMldGroupHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldGroupHostState.setStatus("current")
_ZxAnMldGroupRowStatus_Type = RowStatus
_ZxAnMldGroupRowStatus_Object = MibTableColumn
zxAnMldGroupRowStatus = _ZxAnMldGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 5, 1, 15),
    _ZxAnMldGroupRowStatus_Type()
)
zxAnMldGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldGroupRowStatus.setStatus("current")
_ZxAnMldGroupPortListTable_Object = MibTable
zxAnMldGroupPortListTable = _ZxAnMldGroupPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnMldGroupPortListTable.setStatus("current")
_ZxAnMldGroupPortListEntry_Object = MibTableRow
zxAnMldGroupPortListEntry = _ZxAnMldGroupPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 6, 1)
)
zxAnMldGroupPortListEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldSrcIp"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldGrpIp"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldMvlanPortListShelf"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldMvlanPortListCard"),
)
if mibBuilder.loadTexts:
    zxAnMldGroupPortListEntry.setStatus("current")
_ZxAnMldGroupStaticPortList_Type = ZxAnPortList
_ZxAnMldGroupStaticPortList_Object = MibTableColumn
zxAnMldGroupStaticPortList = _ZxAnMldGroupStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 6, 1, 1),
    _ZxAnMldGroupStaticPortList_Type()
)
zxAnMldGroupStaticPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldGroupStaticPortList.setStatus("current")
_ZxAnMldGroupDynamicPortList_Type = ZxAnPortList
_ZxAnMldGroupDynamicPortList_Object = MibTableColumn
zxAnMldGroupDynamicPortList = _ZxAnMldGroupDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 6, 1, 2),
    _ZxAnMldGroupDynamicPortList_Type()
)
zxAnMldGroupDynamicPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldGroupDynamicPortList.setStatus("current")
_ZxAnMldPortActiveGroupTable_Object = MibTable
zxAnMldPortActiveGroupTable = _ZxAnMldPortActiveGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnMldPortActiveGroupTable.setStatus("current")
_ZxAnMldPortActiveGroupEntry_Object = MibTableRow
zxAnMldPortActiveGroupEntry = _ZxAnMldPortActiveGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 7, 1)
)
zxAnMldPortActiveGroupEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldIfIndex"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldGrpIp"),
)
if mibBuilder.loadTexts:
    zxAnMldPortActiveGroupEntry.setStatus("current")


class _ZxAnMldPortTypeInGroup_Type(Integer32):
    """Custom type zxAnMldPortTypeInGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_ZxAnMldPortTypeInGroup_Type.__name__ = "Integer32"
_ZxAnMldPortTypeInGroup_Object = MibTableColumn
zxAnMldPortTypeInGroup = _ZxAnMldPortTypeInGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 7, 1, 1),
    _ZxAnMldPortTypeInGroup_Type()
)
zxAnMldPortTypeInGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldPortTypeInGroup.setStatus("current")
_ZxAnMldParamListCmdTable_Object = MibTable
zxAnMldParamListCmdTable = _ZxAnMldParamListCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnMldParamListCmdTable.setStatus("current")
_ZxAnMldParamListCmdEntry_Object = MibTableRow
zxAnMldParamListCmdEntry = _ZxAnMldParamListCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 8, 1)
)
zxAnMldParamListCmdEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldParamListCmd"),
)
if mibBuilder.loadTexts:
    zxAnMldParamListCmdEntry.setStatus("current")


class _ZxAnMldParamListCmd_Type(Integer32):
    """Custom type zxAnMldParamListCmd based on Integer32"""
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
        *(("addSrcPortToMvlan", 1),
          ("delSrcPortFromMvlan", 2),
          ("addRecPortToMvlan", 3),
          ("delRecPortFromMvlan", 4),
          ("addStaticGroup", 5),
          ("delStaticGroup", 6))
    )


_ZxAnMldParamListCmd_Type.__name__ = "Integer32"
_ZxAnMldParamListCmd_Object = MibTableColumn
zxAnMldParamListCmd = _ZxAnMldParamListCmd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 8, 1, 1),
    _ZxAnMldParamListCmd_Type()
)
zxAnMldParamListCmd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldParamListCmd.setStatus("current")
_ZxAnMldParamObject_Type = ObjectIdentifier
_ZxAnMldParamObject_Object = MibTableColumn
zxAnMldParamObject = _ZxAnMldParamObject_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 8, 1, 2),
    _ZxAnMldParamObject_Type()
)
zxAnMldParamObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldParamObject.setStatus("current")
_ZxAnMldCounterTable_Object = MibTable
zxAnMldCounterTable = _ZxAnMldCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9)
)
if mibBuilder.loadTexts:
    zxAnMldCounterTable.setStatus("current")
_ZxAnMldCounterEntry_Object = MibTableRow
zxAnMldCounterEntry = _ZxAnMldCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1)
)
zxAnMldCounterEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnMldCounterEntry.setStatus("current")
_ZxAnMldCounterReset_Type = Integer32
_ZxAnMldCounterReset_Object = MibTableColumn
zxAnMldCounterReset = _ZxAnMldCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 1),
    _ZxAnMldCounterReset_Type()
)
zxAnMldCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMldCounterReset.setStatus("current")
_ZxAnMldCounterRxCommQuery_Type = Counter32
_ZxAnMldCounterRxCommQuery_Object = MibTableColumn
zxAnMldCounterRxCommQuery = _ZxAnMldCounterRxCommQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 2),
    _ZxAnMldCounterRxCommQuery_Type()
)
zxAnMldCounterRxCommQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxCommQuery.setStatus("current")
_ZxAnMldCounterRxSpecialQuery_Type = Counter32
_ZxAnMldCounterRxSpecialQuery_Object = MibTableColumn
zxAnMldCounterRxSpecialQuery = _ZxAnMldCounterRxSpecialQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 3),
    _ZxAnMldCounterRxSpecialQuery_Type()
)
zxAnMldCounterRxSpecialQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxSpecialQuery.setStatus("current")
_ZxAnMldCounterRxV1Report_Type = Counter32
_ZxAnMldCounterRxV1Report_Object = MibTableColumn
zxAnMldCounterRxV1Report = _ZxAnMldCounterRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 4),
    _ZxAnMldCounterRxV1Report_Type()
)
zxAnMldCounterRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxV1Report.setStatus("current")
_ZxAnMldCounterRxV2Report_Type = Counter32
_ZxAnMldCounterRxV2Report_Object = MibTableColumn
zxAnMldCounterRxV2Report = _ZxAnMldCounterRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 5),
    _ZxAnMldCounterRxV2Report_Type()
)
zxAnMldCounterRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxV2Report.setStatus("current")
_ZxAnMldCounterRxLeave_Type = Counter32
_ZxAnMldCounterRxLeave_Object = MibTableColumn
zxAnMldCounterRxLeave = _ZxAnMldCounterRxLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 6),
    _ZxAnMldCounterRxLeave_Type()
)
zxAnMldCounterRxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxLeave.setStatus("current")
_ZxAnMldCounterRxError_Type = Counter32
_ZxAnMldCounterRxError_Object = MibTableColumn
zxAnMldCounterRxError = _ZxAnMldCounterRxError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 7),
    _ZxAnMldCounterRxError_Type()
)
zxAnMldCounterRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxError.setStatus("current")
_ZxAnMldCounterRxUnknown_Type = Counter32
_ZxAnMldCounterRxUnknown_Object = MibTableColumn
zxAnMldCounterRxUnknown = _ZxAnMldCounterRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 8),
    _ZxAnMldCounterRxUnknown_Type()
)
zxAnMldCounterRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterRxUnknown.setStatus("current")
_ZxAnMldCounterTxCommQuery_Type = Counter32
_ZxAnMldCounterTxCommQuery_Object = MibTableColumn
zxAnMldCounterTxCommQuery = _ZxAnMldCounterTxCommQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 9),
    _ZxAnMldCounterTxCommQuery_Type()
)
zxAnMldCounterTxCommQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterTxCommQuery.setStatus("current")
_ZxAnMldCounterTxSpecialQuery_Type = Counter32
_ZxAnMldCounterTxSpecialQuery_Object = MibTableColumn
zxAnMldCounterTxSpecialQuery = _ZxAnMldCounterTxSpecialQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 10),
    _ZxAnMldCounterTxSpecialQuery_Type()
)
zxAnMldCounterTxSpecialQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterTxSpecialQuery.setStatus("current")
_ZxAnMldCounterTxV1Report_Type = Counter32
_ZxAnMldCounterTxV1Report_Object = MibTableColumn
zxAnMldCounterTxV1Report = _ZxAnMldCounterTxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 11),
    _ZxAnMldCounterTxV1Report_Type()
)
zxAnMldCounterTxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterTxV1Report.setStatus("current")
_ZxAnMldCounterTxV2Report_Type = Counter32
_ZxAnMldCounterTxV2Report_Object = MibTableColumn
zxAnMldCounterTxV2Report = _ZxAnMldCounterTxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 12),
    _ZxAnMldCounterTxV2Report_Type()
)
zxAnMldCounterTxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterTxV2Report.setStatus("current")
_ZxAnMldCounterTxLeave_Type = Counter32
_ZxAnMldCounterTxLeave_Object = MibTableColumn
zxAnMldCounterTxLeave = _ZxAnMldCounterTxLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 13),
    _ZxAnMldCounterTxLeave_Type()
)
zxAnMldCounterTxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterTxLeave.setStatus("current")
_ZxAnMldCounterDropRxCommQuery_Type = Counter32
_ZxAnMldCounterDropRxCommQuery_Object = MibTableColumn
zxAnMldCounterDropRxCommQuery = _ZxAnMldCounterDropRxCommQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 14),
    _ZxAnMldCounterDropRxCommQuery_Type()
)
zxAnMldCounterDropRxCommQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterDropRxCommQuery.setStatus("current")
_ZxAnMldCounterDropRxSpecialQuery_Type = Counter32
_ZxAnMldCounterDropRxSpecialQuery_Object = MibTableColumn
zxAnMldCounterDropRxSpecialQuery = _ZxAnMldCounterDropRxSpecialQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 15),
    _ZxAnMldCounterDropRxSpecialQuery_Type()
)
zxAnMldCounterDropRxSpecialQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterDropRxSpecialQuery.setStatus("current")
_ZxAnMldCounterDropRxV1Report_Type = Counter32
_ZxAnMldCounterDropRxV1Report_Object = MibTableColumn
zxAnMldCounterDropRxV1Report = _ZxAnMldCounterDropRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 16),
    _ZxAnMldCounterDropRxV1Report_Type()
)
zxAnMldCounterDropRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterDropRxV1Report.setStatus("current")
_ZxAnMldCounterDropRxV2Report_Type = Counter32
_ZxAnMldCounterDropRxV2Report_Object = MibTableColumn
zxAnMldCounterDropRxV2Report = _ZxAnMldCounterDropRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 17),
    _ZxAnMldCounterDropRxV2Report_Type()
)
zxAnMldCounterDropRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterDropRxV2Report.setStatus("current")
_ZxAnMldCounterDropRxLeave_Type = Counter32
_ZxAnMldCounterDropRxLeave_Object = MibTableColumn
zxAnMldCounterDropRxLeave = _ZxAnMldCounterDropRxLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 18),
    _ZxAnMldCounterDropRxLeave_Type()
)
zxAnMldCounterDropRxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterDropRxLeave.setStatus("current")
_ZxAnMldCounterDropRxUnknown_Type = Counter32
_ZxAnMldCounterDropRxUnknown_Object = MibTableColumn
zxAnMldCounterDropRxUnknown = _ZxAnMldCounterDropRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 19),
    _ZxAnMldCounterDropRxUnknown_Type()
)
zxAnMldCounterDropRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterDropRxUnknown.setStatus("current")
_ZxAnMldCounterJoinSuccess_Type = Counter32
_ZxAnMldCounterJoinSuccess_Object = MibTableColumn
zxAnMldCounterJoinSuccess = _ZxAnMldCounterJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 20),
    _ZxAnMldCounterJoinSuccess_Type()
)
zxAnMldCounterJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterJoinSuccess.setStatus("current")
_ZxAnMldCounterJoinFailure_Type = Counter32
_ZxAnMldCounterJoinFailure_Object = MibTableColumn
zxAnMldCounterJoinFailure = _ZxAnMldCounterJoinFailure_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 9, 1, 21),
    _ZxAnMldCounterJoinFailure_Type()
)
zxAnMldCounterJoinFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMldCounterJoinFailure.setStatus("current")
_ZxAnMldVplsMulticastObjects_ObjectIdentity = ObjectIdentity
zxAnMldVplsMulticastObjects = _ZxAnMldVplsMulticastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 50)
)
_ZxAnMldVplsMvlanSrcPwTable_Object = MibTable
zxAnMldVplsMvlanSrcPwTable = _ZxAnMldVplsMvlanSrcPwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 50, 1)
)
if mibBuilder.loadTexts:
    zxAnMldVplsMvlanSrcPwTable.setStatus("current")
_ZxAnMldVplsMvlanSrcPwEntry_Object = MibTableRow
zxAnMldVplsMvlanSrcPwEntry = _ZxAnMldVplsMvlanSrcPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 50, 1, 1)
)
zxAnMldVplsMvlanSrcPwEntry.setIndexNames(
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVlanId"),
    (0, "ZTE-AN-MLD-MIB", "zxAnMldVplsMvlanSrcPwName"),
)
if mibBuilder.loadTexts:
    zxAnMldVplsMvlanSrcPwEntry.setStatus("current")


class _ZxAnMldVplsMvlanSrcPwName_Type(DisplayString):
    """Custom type zxAnMldVplsMvlanSrcPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_ZxAnMldVplsMvlanSrcPwName_Type.__name__ = "DisplayString"
_ZxAnMldVplsMvlanSrcPwName_Object = MibTableColumn
zxAnMldVplsMvlanSrcPwName = _ZxAnMldVplsMvlanSrcPwName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 50, 1, 1, 1),
    _ZxAnMldVplsMvlanSrcPwName_Type()
)
zxAnMldVplsMvlanSrcPwName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMldVplsMvlanSrcPwName.setStatus("current")
_ZxAnMldVplsMvlanSrcPwRowStatus_Type = RowStatus
_ZxAnMldVplsMvlanSrcPwRowStatus_Object = MibTableColumn
zxAnMldVplsMvlanSrcPwRowStatus = _ZxAnMldVplsMvlanSrcPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 1, 1, 50, 1, 1, 20),
    _ZxAnMldVplsMvlanSrcPwRowStatus_Type()
)
zxAnMldVplsMvlanSrcPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMldVplsMvlanSrcPwRowStatus.setStatus("current")
_ZxAnMldTrapObjects_ObjectIdentity = ObjectIdentity
zxAnMldTrapObjects = _ZxAnMldTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 2)
)

# Managed Objects groups


# Notification objects

zxAnMldGroupThreshExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 2, 1)
)
zxAnMldGroupThreshExceeded.setObjects(
    ("ZTE-AN-MLD-MIB", "zxAnMldGroupThreshold")
)
if mibBuilder.loadTexts:
    zxAnMldGroupThreshExceeded.setStatus(
        "current"
    )

zxAnMldGroupThreshExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 29, 2, 2)
)
zxAnMldGroupThreshExceededCleared.setObjects(
    ("ZTE-AN-MLD-MIB", "zxAnMldGroupThreshold")
)
if mibBuilder.loadTexts:
    zxAnMldGroupThreshExceededCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-MLD-MIB",
    **{"zxAnMldMib": zxAnMldMib,
       "zxAnMldObjects": zxAnMldObjects,
       "zxAnMld": zxAnMld,
       "zxAnMldGlobal": zxAnMldGlobal,
       "zxAnMldAdminStatus": zxAnMldAdminStatus,
       "zxAnMldAging": zxAnMldAging,
       "zxAnMldWorkingMode": zxAnMldWorkingMode,
       "zxAnMldMcastInAllVlan": zxAnMldMcastInAllVlan,
       "zxAnMldDefaultMvlan": zxAnMldDefaultMvlan,
       "zxAnMldAutoConfigGrpToDefaultMvlan": zxAnMldAutoConfigGrpToDefaultMvlan,
       "zxAnMldUserSideRoutingIp": zxAnMldUserSideRoutingIp,
       "zxAnMldBandwidthCtrl": zxAnMldBandwidthCtrl,
       "zxAnMldRobustnessVariable": zxAnMldRobustnessVariable,
       "zxAnMldQueryInterval": zxAnMldQueryInterval,
       "zxAnMldQueryMaxResponseTime": zxAnMldQueryMaxResponseTime,
       "zxAnMldLastMembQueryInterval": zxAnMldLastMembQueryInterval,
       "zxAnMldLastMembQueryCount": zxAnMldLastMembQueryCount,
       "zxAnMldUnsolicitedReportInterval": zxAnMldUnsolicitedReportInterval,
       "zxAnMldNetworkSideHostIp": zxAnMldNetworkSideHostIp,
       "zxAnMldForwCvlanOnOff": zxAnMldForwCvlanOnOff,
       "zxAnMldHostTrackOnOff": zxAnMldHostTrackOnOff,
       "zxAnMldNonMatchGroup": zxAnMldNonMatchGroup,
       "zxAnMldGeneralLeaveGrpAddr": zxAnMldGeneralLeaveGrpAddr,
       "zxAnMldLogOnOff": zxAnMldLogOnOff,
       "zxAnMldGroupThreshold": zxAnMldGroupThreshold,
       "zxAnMldMulticastServiceModel": zxAnMldMulticastServiceModel,
       "zxAnMldV1AdminStatus": zxAnMldV1AdminStatus,
       "zxAnMldV2AdminStatus": zxAnMldV2AdminStatus,
       "zxAnMldPortTable": zxAnMldPortTable,
       "zxAnMldPortEntry": zxAnMldPortEntry,
       "zxAnMldIfIndex": zxAnMldIfIndex,
       "zxAnMldPortAdminStatus": zxAnMldPortAdminStatus,
       "zxAnMldPortProtoVersion": zxAnMldPortProtoVersion,
       "zxAnMldPortFastLeaveEnable": zxAnMldPortFastLeaveEnable,
       "zxAnMldPortProxyIp": zxAnMldPortProxyIp,
       "zxAnMldPortPacketLimit": zxAnMldPortPacketLimit,
       "zxAnMldPortMaxBandwidth": zxAnMldPortMaxBandwidth,
       "zxAnMldPortMaxConcurrGroups": zxAnMldPortMaxConcurrGroups,
       "zxAnMldPortCurrActGroups": zxAnMldPortCurrActGroups,
       "zxAnMldPortQueryInterval": zxAnMldPortQueryInterval,
       "zxAnMldPortLastMembQueryIntvl": zxAnMldPortLastMembQueryIntvl,
       "zxAnMldPortQueryMaxResponseTime": zxAnMldPortQueryMaxResponseTime,
       "zxAnMldPortEtherPriority": zxAnMldPortEtherPriority,
       "zxAnMldPortRobustness": zxAnMldPortRobustness,
       "zxAnMldMvlanAutoTranslateEnable": zxAnMldMvlanAutoTranslateEnable,
       "zxAnMldMvlanTable": zxAnMldMvlanTable,
       "zxAnMldMvlanEntry": zxAnMldMvlanEntry,
       "zxAnMldVlanId": zxAnMldVlanId,
       "zxAnMldMvlanAdminStatus": zxAnMldMvlanAdminStatus,
       "zxAnMldMvlanWorkMode": zxAnMldMvlanWorkMode,
       "zxAnMldMvlanNetworkSideHostIp": zxAnMldMvlanNetworkSideHostIp,
       "zxAnMldMvlanGroupFilterEnable": zxAnMldMvlanGroupFilterEnable,
       "zxAnMldMvlanMaxGroups": zxAnMldMvlanMaxGroups,
       "zxAnMldMvlanCurrActGroups": zxAnMldMvlanCurrActGroups,
       "zxAnMldMvlanPriority": zxAnMldMvlanPriority,
       "zxAnMldMvlanHostVersion": zxAnMldMvlanHostVersion,
       "zxAnMldMvlanRowStatus": zxAnMldMvlanRowStatus,
       "zxAnMldMvlanPortListTable": zxAnMldMvlanPortListTable,
       "zxAnMldMvlanPortListEntry": zxAnMldMvlanPortListEntry,
       "zxAnMldMvlanPortListShelf": zxAnMldMvlanPortListShelf,
       "zxAnMldMvlanPortListCard": zxAnMldMvlanPortListCard,
       "zxAnMldMvlanPortSrcPortList": zxAnMldMvlanPortSrcPortList,
       "zxAnMldMvlanPortRecvPortList": zxAnMldMvlanPortRecvPortList,
       "zxAnMldGroupTable": zxAnMldGroupTable,
       "zxAnMldGroupEntry": zxAnMldGroupEntry,
       "zxAnMldSrcIp": zxAnMldSrcIp,
       "zxAnMldGrpIp": zxAnMldGrpIp,
       "zxAnMldGroupBandwidthCost": zxAnMldGroupBandwidthCost,
       "zxAnMldGroupPrejoinEnable": zxAnMldGroupPrejoinEnable,
       "zxAnMldGroupMaxHosts": zxAnMldGroupMaxHosts,
       "zxAnMldGroupActHosts": zxAnMldGroupActHosts,
       "zxAnMldGroupSrcIp": zxAnMldGroupSrcIp,
       "zxAnMldGroupHostState": zxAnMldGroupHostState,
       "zxAnMldGroupRowStatus": zxAnMldGroupRowStatus,
       "zxAnMldGroupPortListTable": zxAnMldGroupPortListTable,
       "zxAnMldGroupPortListEntry": zxAnMldGroupPortListEntry,
       "zxAnMldGroupStaticPortList": zxAnMldGroupStaticPortList,
       "zxAnMldGroupDynamicPortList": zxAnMldGroupDynamicPortList,
       "zxAnMldPortActiveGroupTable": zxAnMldPortActiveGroupTable,
       "zxAnMldPortActiveGroupEntry": zxAnMldPortActiveGroupEntry,
       "zxAnMldPortTypeInGroup": zxAnMldPortTypeInGroup,
       "zxAnMldParamListCmdTable": zxAnMldParamListCmdTable,
       "zxAnMldParamListCmdEntry": zxAnMldParamListCmdEntry,
       "zxAnMldParamListCmd": zxAnMldParamListCmd,
       "zxAnMldParamObject": zxAnMldParamObject,
       "zxAnMldCounterTable": zxAnMldCounterTable,
       "zxAnMldCounterEntry": zxAnMldCounterEntry,
       "zxAnMldCounterReset": zxAnMldCounterReset,
       "zxAnMldCounterRxCommQuery": zxAnMldCounterRxCommQuery,
       "zxAnMldCounterRxSpecialQuery": zxAnMldCounterRxSpecialQuery,
       "zxAnMldCounterRxV1Report": zxAnMldCounterRxV1Report,
       "zxAnMldCounterRxV2Report": zxAnMldCounterRxV2Report,
       "zxAnMldCounterRxLeave": zxAnMldCounterRxLeave,
       "zxAnMldCounterRxError": zxAnMldCounterRxError,
       "zxAnMldCounterRxUnknown": zxAnMldCounterRxUnknown,
       "zxAnMldCounterTxCommQuery": zxAnMldCounterTxCommQuery,
       "zxAnMldCounterTxSpecialQuery": zxAnMldCounterTxSpecialQuery,
       "zxAnMldCounterTxV1Report": zxAnMldCounterTxV1Report,
       "zxAnMldCounterTxV2Report": zxAnMldCounterTxV2Report,
       "zxAnMldCounterTxLeave": zxAnMldCounterTxLeave,
       "zxAnMldCounterDropRxCommQuery": zxAnMldCounterDropRxCommQuery,
       "zxAnMldCounterDropRxSpecialQuery": zxAnMldCounterDropRxSpecialQuery,
       "zxAnMldCounterDropRxV1Report": zxAnMldCounterDropRxV1Report,
       "zxAnMldCounterDropRxV2Report": zxAnMldCounterDropRxV2Report,
       "zxAnMldCounterDropRxLeave": zxAnMldCounterDropRxLeave,
       "zxAnMldCounterDropRxUnknown": zxAnMldCounterDropRxUnknown,
       "zxAnMldCounterJoinSuccess": zxAnMldCounterJoinSuccess,
       "zxAnMldCounterJoinFailure": zxAnMldCounterJoinFailure,
       "zxAnMldVplsMulticastObjects": zxAnMldVplsMulticastObjects,
       "zxAnMldVplsMvlanSrcPwTable": zxAnMldVplsMvlanSrcPwTable,
       "zxAnMldVplsMvlanSrcPwEntry": zxAnMldVplsMvlanSrcPwEntry,
       "zxAnMldVplsMvlanSrcPwName": zxAnMldVplsMvlanSrcPwName,
       "zxAnMldVplsMvlanSrcPwRowStatus": zxAnMldVplsMvlanSrcPwRowStatus,
       "zxAnMldTrapObjects": zxAnMldTrapObjects,
       "zxAnMldGroupThreshExceeded": zxAnMldGroupThreshExceeded,
       "zxAnMldGroupThreshExceededCleared": zxAnMldGroupThreshExceededCleared}
)
