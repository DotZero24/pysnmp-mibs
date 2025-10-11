# SNMP MIB module (ZTE-AN-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:54 2025
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

zxAnIgmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnIgmpObjects_ObjectIdentity = ObjectIdentity
zxAnIgmpObjects = _ZxAnIgmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1)
)
_ZxAnIgmp_ObjectIdentity = ObjectIdentity
zxAnIgmp = _ZxAnIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1)
)
_ZxAnIgmpGlobal_ObjectIdentity = ObjectIdentity
zxAnIgmpGlobal = _ZxAnIgmpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1)
)


class _ZxAnIgmpEnable_Type(Integer32):
    """Custom type zxAnIgmpEnable based on Integer32"""
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


_ZxAnIgmpEnable_Type.__name__ = "Integer32"
_ZxAnIgmpEnable_Object = MibScalar
zxAnIgmpEnable = _ZxAnIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 1),
    _ZxAnIgmpEnable_Type()
)
zxAnIgmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpEnable.setStatus("current")


class _ZxAnIgmpSnoopingAgingTime_Type(Integer32):
    """Custom type zxAnIgmpSnoopingAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_ZxAnIgmpSnoopingAgingTime_Type.__name__ = "Integer32"
_ZxAnIgmpSnoopingAgingTime_Object = MibScalar
zxAnIgmpSnoopingAgingTime = _ZxAnIgmpSnoopingAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 2),
    _ZxAnIgmpSnoopingAgingTime_Type()
)
zxAnIgmpSnoopingAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpSnoopingAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpSnoopingAgingTime.setUnits("seconds")


class _ZxAnIgmpWorkingMode_Type(Integer32):
    """Custom type zxAnIgmpWorkingMode based on Integer32"""
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


_ZxAnIgmpWorkingMode_Type.__name__ = "Integer32"
_ZxAnIgmpWorkingMode_Object = MibScalar
zxAnIgmpWorkingMode = _ZxAnIgmpWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 3),
    _ZxAnIgmpWorkingMode_Type()
)
zxAnIgmpWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpWorkingMode.setStatus("current")


class _ZxAnIgmpSpanVlanEnable_Type(Integer32):
    """Custom type zxAnIgmpSpanVlanEnable based on Integer32"""
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


_ZxAnIgmpSpanVlanEnable_Type.__name__ = "Integer32"
_ZxAnIgmpSpanVlanEnable_Object = MibScalar
zxAnIgmpSpanVlanEnable = _ZxAnIgmpSpanVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 4),
    _ZxAnIgmpSpanVlanEnable_Type()
)
zxAnIgmpSpanVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpSpanVlanEnable.setStatus("current")


class _ZxAnIgmpDefaultMvlan_Type(Integer32):
    """Custom type zxAnIgmpDefaultMvlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZxAnIgmpDefaultMvlan_Type.__name__ = "Integer32"
_ZxAnIgmpDefaultMvlan_Object = MibScalar
zxAnIgmpDefaultMvlan = _ZxAnIgmpDefaultMvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 5),
    _ZxAnIgmpDefaultMvlan_Type()
)
zxAnIgmpDefaultMvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpDefaultMvlan.setStatus("current")


class _ZxAnIgmpAutoConfigGrpToDefaultMvlan_Type(Integer32):
    """Custom type zxAnIgmpAutoConfigGrpToDefaultMvlan based on Integer32"""
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


_ZxAnIgmpAutoConfigGrpToDefaultMvlan_Type.__name__ = "Integer32"
_ZxAnIgmpAutoConfigGrpToDefaultMvlan_Object = MibScalar
zxAnIgmpAutoConfigGrpToDefaultMvlan = _ZxAnIgmpAutoConfigGrpToDefaultMvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 6),
    _ZxAnIgmpAutoConfigGrpToDefaultMvlan_Type()
)
zxAnIgmpAutoConfigGrpToDefaultMvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpAutoConfigGrpToDefaultMvlan.setStatus("current")


class _ZxAnIgmpFastQureyBasedIpPool_Type(Integer32):
    """Custom type zxAnIgmpFastQureyBasedIpPool based on Integer32"""
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


_ZxAnIgmpFastQureyBasedIpPool_Type.__name__ = "Integer32"
_ZxAnIgmpFastQureyBasedIpPool_Object = MibScalar
zxAnIgmpFastQureyBasedIpPool = _ZxAnIgmpFastQureyBasedIpPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 7),
    _ZxAnIgmpFastQureyBasedIpPool_Type()
)
zxAnIgmpFastQureyBasedIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpFastQureyBasedIpPool.setStatus("current")


class _ZxAnIgmpGeneralLeaveEnable_Type(Integer32):
    """Custom type zxAnIgmpGeneralLeaveEnable based on Integer32"""
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


_ZxAnIgmpGeneralLeaveEnable_Type.__name__ = "Integer32"
_ZxAnIgmpGeneralLeaveEnable_Object = MibScalar
zxAnIgmpGeneralLeaveEnable = _ZxAnIgmpGeneralLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 8),
    _ZxAnIgmpGeneralLeaveEnable_Type()
)
zxAnIgmpGeneralLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpGeneralLeaveEnable.setStatus("current")
_ZxAnIgmpUserSideRoutingIp_Type = IpAddress
_ZxAnIgmpUserSideRoutingIp_Object = MibScalar
zxAnIgmpUserSideRoutingIp = _ZxAnIgmpUserSideRoutingIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 9),
    _ZxAnIgmpUserSideRoutingIp_Type()
)
zxAnIgmpUserSideRoutingIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpUserSideRoutingIp.setStatus("current")


class _ZxAnIgmpMVlanIgmpV1OperMode_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpV1OperMode based on Integer32"""
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


_ZxAnIgmpMVlanIgmpV1OperMode_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpV1OperMode_Object = MibScalar
zxAnIgmpMVlanIgmpV1OperMode = _ZxAnIgmpMVlanIgmpV1OperMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 10),
    _ZxAnIgmpMVlanIgmpV1OperMode_Type()
)
zxAnIgmpMVlanIgmpV1OperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpV1OperMode.setStatus("current")


class _ZxAnIgmpMVlanIgmpV2OperMode_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpV2OperMode based on Integer32"""
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


_ZxAnIgmpMVlanIgmpV2OperMode_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpV2OperMode_Object = MibScalar
zxAnIgmpMVlanIgmpV2OperMode = _ZxAnIgmpMVlanIgmpV2OperMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 11),
    _ZxAnIgmpMVlanIgmpV2OperMode_Type()
)
zxAnIgmpMVlanIgmpV2OperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpV2OperMode.setStatus("current")


class _ZxAnIgmpMVlanIgmpV3OperMode_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpV3OperMode based on Integer32"""
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


_ZxAnIgmpMVlanIgmpV3OperMode_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpV3OperMode_Object = MibScalar
zxAnIgmpMVlanIgmpV3OperMode = _ZxAnIgmpMVlanIgmpV3OperMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 12),
    _ZxAnIgmpMVlanIgmpV3OperMode_Type()
)
zxAnIgmpMVlanIgmpV3OperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpV3OperMode.setStatus("current")


class _ZxAnIgmpBandwidthCtrlEnable_Type(Integer32):
    """Custom type zxAnIgmpBandwidthCtrlEnable based on Integer32"""
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


_ZxAnIgmpBandwidthCtrlEnable_Type.__name__ = "Integer32"
_ZxAnIgmpBandwidthCtrlEnable_Object = MibScalar
zxAnIgmpBandwidthCtrlEnable = _ZxAnIgmpBandwidthCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 13),
    _ZxAnIgmpBandwidthCtrlEnable_Type()
)
zxAnIgmpBandwidthCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpBandwidthCtrlEnable.setStatus("current")


class _ZxAnIgmpRobustnessVariable_Type(Integer32):
    """Custom type zxAnIgmpRobustnessVariable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ZxAnIgmpRobustnessVariable_Type.__name__ = "Integer32"
_ZxAnIgmpRobustnessVariable_Object = MibScalar
zxAnIgmpRobustnessVariable = _ZxAnIgmpRobustnessVariable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 14),
    _ZxAnIgmpRobustnessVariable_Type()
)
zxAnIgmpRobustnessVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpRobustnessVariable.setStatus("current")


class _ZxAnIgmpQryInterval_Type(Integer32):
    """Custom type zxAnIgmpQryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_ZxAnIgmpQryInterval_Type.__name__ = "Integer32"
_ZxAnIgmpQryInterval_Object = MibScalar
zxAnIgmpQryInterval = _ZxAnIgmpQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 15),
    _ZxAnIgmpQryInterval_Type()
)
zxAnIgmpQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpQryInterval.setStatus("current")


class _ZxAnIgmpQryRespInterval_Type(Integer32):
    """Custom type zxAnIgmpQryRespInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_ZxAnIgmpQryRespInterval_Type.__name__ = "Integer32"
_ZxAnIgmpQryRespInterval_Object = MibScalar
zxAnIgmpQryRespInterval = _ZxAnIgmpQryRespInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 16),
    _ZxAnIgmpQryRespInterval_Type()
)
zxAnIgmpQryRespInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpQryRespInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpQryRespInterval.setUnits("0.1second")


class _ZxAnIgmpLastMemberQryInterval_Type(Integer32):
    """Custom type zxAnIgmpLastMemberQryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnIgmpLastMemberQryInterval_Type.__name__ = "Integer32"
_ZxAnIgmpLastMemberQryInterval_Object = MibScalar
zxAnIgmpLastMemberQryInterval = _ZxAnIgmpLastMemberQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 17),
    _ZxAnIgmpLastMemberQryInterval_Type()
)
zxAnIgmpLastMemberQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpLastMemberQryInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpLastMemberQryInterval.setUnits("0.1second")


class _ZxAnIgmpLastMemberQryCount_Type(Integer32):
    """Custom type zxAnIgmpLastMemberQryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ZxAnIgmpLastMemberQryCount_Type.__name__ = "Integer32"
_ZxAnIgmpLastMemberQryCount_Object = MibScalar
zxAnIgmpLastMemberQryCount = _ZxAnIgmpLastMemberQryCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 18),
    _ZxAnIgmpLastMemberQryCount_Type()
)
zxAnIgmpLastMemberQryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpLastMemberQryCount.setStatus("current")


class _ZxAnIgmpV1QuerierTimeout_Type(Integer32):
    """Custom type zxAnIgmpV1QuerierTimeout based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_ZxAnIgmpV1QuerierTimeout_Type.__name__ = "Integer32"
_ZxAnIgmpV1QuerierTimeout_Object = MibScalar
zxAnIgmpV1QuerierTimeout = _ZxAnIgmpV1QuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 19),
    _ZxAnIgmpV1QuerierTimeout_Type()
)
zxAnIgmpV1QuerierTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpV1QuerierTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpV1QuerierTimeout.setUnits("0.1second")


class _ZxAnIgmpUnsolicitReportInterval_Type(Integer32):
    """Custom type zxAnIgmpUnsolicitReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ZxAnIgmpUnsolicitReportInterval_Type.__name__ = "Integer32"
_ZxAnIgmpUnsolicitReportInterval_Object = MibScalar
zxAnIgmpUnsolicitReportInterval = _ZxAnIgmpUnsolicitReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 20),
    _ZxAnIgmpUnsolicitReportInterval_Type()
)
zxAnIgmpUnsolicitReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpUnsolicitReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpUnsolicitReportInterval.setUnits("seconds")
_ZxAnIgmpNetworkSideHostIp_Type = IpAddress
_ZxAnIgmpNetworkSideHostIp_Object = MibScalar
zxAnIgmpNetworkSideHostIp = _ZxAnIgmpNetworkSideHostIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 21),
    _ZxAnIgmpNetworkSideHostIp_Type()
)
zxAnIgmpNetworkSideHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpNetworkSideHostIp.setStatus("current")


class _ZxAnIgmpForwCvlanOnOff_Type(Integer32):
    """Custom type zxAnIgmpForwCvlanOnOff based on Integer32"""
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


_ZxAnIgmpForwCvlanOnOff_Type.__name__ = "Integer32"
_ZxAnIgmpForwCvlanOnOff_Object = MibScalar
zxAnIgmpForwCvlanOnOff = _ZxAnIgmpForwCvlanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 22),
    _ZxAnIgmpForwCvlanOnOff_Type()
)
zxAnIgmpForwCvlanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpForwCvlanOnOff.setStatus("current")


class _ZxAnIgmpHostTrackEnable_Type(Integer32):
    """Custom type zxAnIgmpHostTrackEnable based on Integer32"""
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


_ZxAnIgmpHostTrackEnable_Type.__name__ = "Integer32"
_ZxAnIgmpHostTrackEnable_Object = MibScalar
zxAnIgmpHostTrackEnable = _ZxAnIgmpHostTrackEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 23),
    _ZxAnIgmpHostTrackEnable_Type()
)
zxAnIgmpHostTrackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpHostTrackEnable.setStatus("current")


class _ZxAnIgmpNonMatchGroup_Type(Integer32):
    """Custom type zxAnIgmpNonMatchGroup based on Integer32"""
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


_ZxAnIgmpNonMatchGroup_Type.__name__ = "Integer32"
_ZxAnIgmpNonMatchGroup_Object = MibScalar
zxAnIgmpNonMatchGroup = _ZxAnIgmpNonMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 24),
    _ZxAnIgmpNonMatchGroup_Type()
)
zxAnIgmpNonMatchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpNonMatchGroup.setStatus("current")


class _ZxAnIgmpStartUpQryInterval_Type(Integer32):
    """Custom type zxAnIgmpStartUpQryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ZxAnIgmpStartUpQryInterval_Type.__name__ = "Integer32"
_ZxAnIgmpStartUpQryInterval_Object = MibScalar
zxAnIgmpStartUpQryInterval = _ZxAnIgmpStartUpQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 25),
    _ZxAnIgmpStartUpQryInterval_Type()
)
zxAnIgmpStartUpQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpStartUpQryInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpStartUpQryInterval.setUnits("seconds")


class _ZxAnIgmpStartUpQryCount_Type(Integer32):
    """Custom type zxAnIgmpStartUpQryCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ZxAnIgmpStartUpQryCount_Type.__name__ = "Integer32"
_ZxAnIgmpStartUpQryCount_Object = MibScalar
zxAnIgmpStartUpQryCount = _ZxAnIgmpStartUpQryCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 26),
    _ZxAnIgmpStartUpQryCount_Type()
)
zxAnIgmpStartUpQryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpStartUpQryCount.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpStartUpQryCount.setUnits("seconds")


class _ZxAnIgmpRouterAlert_Type(Integer32):
    """Custom type zxAnIgmpRouterAlert based on Integer32"""
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


_ZxAnIgmpRouterAlert_Type.__name__ = "Integer32"
_ZxAnIgmpRouterAlert_Object = MibScalar
zxAnIgmpRouterAlert = _ZxAnIgmpRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 27),
    _ZxAnIgmpRouterAlert_Type()
)
zxAnIgmpRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpRouterAlert.setStatus("current")
_ZxAnIgmpGeneralLeaveGrpIp_Type = IpAddress
_ZxAnIgmpGeneralLeaveGrpIp_Object = MibScalar
zxAnIgmpGeneralLeaveGrpIp = _ZxAnIgmpGeneralLeaveGrpIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 28),
    _ZxAnIgmpGeneralLeaveGrpIp_Type()
)
zxAnIgmpGeneralLeaveGrpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpGeneralLeaveGrpIp.setStatus("current")


class _ZxAnIgmpLogEnable_Type(Integer32):
    """Custom type zxAnIgmpLogEnable based on Integer32"""
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


_ZxAnIgmpLogEnable_Type.__name__ = "Integer32"
_ZxAnIgmpLogEnable_Object = MibScalar
zxAnIgmpLogEnable = _ZxAnIgmpLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 29),
    _ZxAnIgmpLogEnable_Type()
)
zxAnIgmpLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpLogEnable.setStatus("current")


class _ZxAnIgmpGroupThreshold_Type(Integer32):
    """Custom type zxAnIgmpGroupThreshold based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ZxAnIgmpGroupThreshold_Type.__name__ = "Integer32"
_ZxAnIgmpGroupThreshold_Object = MibScalar
zxAnIgmpGroupThreshold = _ZxAnIgmpGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 30),
    _ZxAnIgmpGroupThreshold_Type()
)
zxAnIgmpGroupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpGroupThreshold.setStatus("current")


class _ZxAnIgmpMVlanIgmpSsmCtrlModel_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpSsmCtrlModel based on Integer32"""
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


_ZxAnIgmpMVlanIgmpSsmCtrlModel_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpSsmCtrlModel_Object = MibScalar
zxAnIgmpMVlanIgmpSsmCtrlModel = _ZxAnIgmpMVlanIgmpSsmCtrlModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 31),
    _ZxAnIgmpMVlanIgmpSsmCtrlModel_Type()
)
zxAnIgmpMVlanIgmpSsmCtrlModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpSsmCtrlModel.setStatus("current")


class _ZxAnIgmpCapabilities_Type(Bits):
    """Custom type zxAnIgmpCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("supportIgmpPacketCos", 0),
          ("supportIgmpSignalingVid", 1),
          ("supportIgmpMaxBandwidth", 2),
          ("supportIgmpMVlanRecvIfTable", 3))
    )

_ZxAnIgmpCapabilities_Type.__name__ = "Bits"
_ZxAnIgmpCapabilities_Object = MibScalar
zxAnIgmpCapabilities = _ZxAnIgmpCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 1, 32),
    _ZxAnIgmpCapabilities_Type()
)
zxAnIgmpCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCapabilities.setStatus("current")
_ZxAnIgmpPortTable_Object = MibTable
zxAnIgmpPortTable = _ZxAnIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21)
)
if mibBuilder.loadTexts:
    zxAnIgmpPortTable.setStatus("current")
_ZxAnIgmpPortEntry_Object = MibTableRow
zxAnIgmpPortEntry = _ZxAnIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1)
)
zxAnIgmpPortEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnIgmpPortEntry.setStatus("current")
_ZxAnIgmpIfIndex_Type = ZxAnIfindex
_ZxAnIgmpIfIndex_Object = MibTableColumn
zxAnIgmpIfIndex = _ZxAnIgmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 1),
    _ZxAnIgmpIfIndex_Type()
)
zxAnIgmpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpIfIndex.setStatus("current")


class _ZxAnIgmpIfAdminStatus_Type(Integer32):
    """Custom type zxAnIgmpIfAdminStatus based on Integer32"""
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


_ZxAnIgmpIfAdminStatus_Type.__name__ = "Integer32"
_ZxAnIgmpIfAdminStatus_Object = MibTableColumn
zxAnIgmpIfAdminStatus = _ZxAnIgmpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 2),
    _ZxAnIgmpIfAdminStatus_Type()
)
zxAnIgmpIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfAdminStatus.setStatus("current")


class _ZxAnIgmpIfProtoVersion_Type(Integer32):
    """Custom type zxAnIgmpIfProtoVersion based on Integer32"""
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
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_ZxAnIgmpIfProtoVersion_Type.__name__ = "Integer32"
_ZxAnIgmpIfProtoVersion_Object = MibTableColumn
zxAnIgmpIfProtoVersion = _ZxAnIgmpIfProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 3),
    _ZxAnIgmpIfProtoVersion_Type()
)
zxAnIgmpIfProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfProtoVersion.setStatus("current")


class _ZxAnIgmpIfFastLeaveEnable_Type(TruthValue):
    """Custom type zxAnIgmpIfFastLeaveEnable based on TruthValue"""
    defaultValue = 1


_ZxAnIgmpIfFastLeaveEnable_Type.__name__ = "TruthValue"
_ZxAnIgmpIfFastLeaveEnable_Object = MibTableColumn
zxAnIgmpIfFastLeaveEnable = _ZxAnIgmpIfFastLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 4),
    _ZxAnIgmpIfFastLeaveEnable_Type()
)
zxAnIgmpIfFastLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfFastLeaveEnable.setStatus("current")


class _ZxAnIgmpPortUsage_Type(Integer32):
    """Custom type zxAnIgmpPortUsage based on Integer32"""
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
        *(("all", 1),
          ("igmp", 2),
          ("data", 3))
    )


_ZxAnIgmpPortUsage_Type.__name__ = "Integer32"
_ZxAnIgmpPortUsage_Object = MibTableColumn
zxAnIgmpPortUsage = _ZxAnIgmpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 5),
    _ZxAnIgmpPortUsage_Type()
)
zxAnIgmpPortUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpPortUsage.setStatus("current")
_ZxAnIgmpDataPort_Type = ZxAnIfindex
_ZxAnIgmpDataPort_Object = MibTableColumn
zxAnIgmpDataPort = _ZxAnIgmpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 6),
    _ZxAnIgmpDataPort_Type()
)
zxAnIgmpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpDataPort.setStatus("current")
_ZxAnIgmpIfProxyIpAddr_Type = IpAddress
_ZxAnIgmpIfProxyIpAddr_Object = MibTableColumn
zxAnIgmpIfProxyIpAddr = _ZxAnIgmpIfProxyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 7),
    _ZxAnIgmpIfProxyIpAddr_Type()
)
zxAnIgmpIfProxyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfProxyIpAddr.setStatus("current")
_ZxAnIgmpPortPacketLimit_Type = Integer32
_ZxAnIgmpPortPacketLimit_Object = MibTableColumn
zxAnIgmpPortPacketLimit = _ZxAnIgmpPortPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 8),
    _ZxAnIgmpPortPacketLimit_Type()
)
zxAnIgmpPortPacketLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpPortPacketLimit.setStatus("current")


class _ZxAnIgmpPortMaxBandwidth_Type(Integer32):
    """Custom type zxAnIgmpPortMaxBandwidth based on Integer32"""
    defaultValue = 2048


_ZxAnIgmpPortMaxBandwidth_Type.__name__ = "Integer32"
_ZxAnIgmpPortMaxBandwidth_Object = MibTableColumn
zxAnIgmpPortMaxBandwidth = _ZxAnIgmpPortMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 9),
    _ZxAnIgmpPortMaxBandwidth_Type()
)
zxAnIgmpPortMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpPortMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpPortMaxBandwidth.setUnits("kbps")


class _ZxAnIgmpIfMaxConcurrentGroups_Type(Integer32):
    """Custom type zxAnIgmpIfMaxConcurrentGroups based on Integer32"""
    defaultValue = 1


_ZxAnIgmpIfMaxConcurrentGroups_Type.__name__ = "Integer32"
_ZxAnIgmpIfMaxConcurrentGroups_Object = MibTableColumn
zxAnIgmpIfMaxConcurrentGroups = _ZxAnIgmpIfMaxConcurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 10),
    _ZxAnIgmpIfMaxConcurrentGroups_Type()
)
zxAnIgmpIfMaxConcurrentGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfMaxConcurrentGroups.setStatus("current")
_ZxAnIgmpIfCurrActGroups_Type = Gauge32
_ZxAnIgmpIfCurrActGroups_Object = MibTableColumn
zxAnIgmpIfCurrActGroups = _ZxAnIgmpIfCurrActGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 11),
    _ZxAnIgmpIfCurrActGroups_Type()
)
zxAnIgmpIfCurrActGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpIfCurrActGroups.setStatus("current")


class _ZxAnIgmpIfQryInterval_Type(Integer32):
    """Custom type zxAnIgmpIfQryInterval based on Integer32"""
    defaultValue = 125


_ZxAnIgmpIfQryInterval_Type.__name__ = "Integer32"
_ZxAnIgmpIfQryInterval_Object = MibTableColumn
zxAnIgmpIfQryInterval = _ZxAnIgmpIfQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 12),
    _ZxAnIgmpIfQryInterval_Type()
)
zxAnIgmpIfQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfQryInterval.setStatus("current")


class _ZxAnIgmpIfLastMemberQryInterval_Type(Integer32):
    """Custom type zxAnIgmpIfLastMemberQryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnIgmpIfLastMemberQryInterval_Type.__name__ = "Integer32"
_ZxAnIgmpIfLastMemberQryInterval_Object = MibTableColumn
zxAnIgmpIfLastMemberQryInterval = _ZxAnIgmpIfLastMemberQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 13),
    _ZxAnIgmpIfLastMemberQryInterval_Type()
)
zxAnIgmpIfLastMemberQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfLastMemberQryInterval.setStatus("current")


class _ZxAnIgmpIfQryResponseInterval_Type(Integer32):
    """Custom type zxAnIgmpIfQryResponseInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnIgmpIfQryResponseInterval_Type.__name__ = "Integer32"
_ZxAnIgmpIfQryResponseInterval_Object = MibTableColumn
zxAnIgmpIfQryResponseInterval = _ZxAnIgmpIfQryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 14),
    _ZxAnIgmpIfQryResponseInterval_Type()
)
zxAnIgmpIfQryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfQryResponseInterval.setStatus("current")


class _ZxAnIgmpPortEtherPriority_Type(Integer32):
    """Custom type zxAnIgmpPortEtherPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnIgmpPortEtherPriority_Type.__name__ = "Integer32"
_ZxAnIgmpPortEtherPriority_Object = MibTableColumn
zxAnIgmpPortEtherPriority = _ZxAnIgmpPortEtherPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 15),
    _ZxAnIgmpPortEtherPriority_Type()
)
zxAnIgmpPortEtherPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpPortEtherPriority.setStatus("current")


class _ZxAnIgmpIfRobustnessVariable_Type(Integer32):
    """Custom type zxAnIgmpIfRobustnessVariable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnIgmpIfRobustnessVariable_Type.__name__ = "Integer32"
_ZxAnIgmpIfRobustnessVariable_Object = MibTableColumn
zxAnIgmpIfRobustnessVariable = _ZxAnIgmpIfRobustnessVariable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 16),
    _ZxAnIgmpIfRobustnessVariable_Type()
)
zxAnIgmpIfRobustnessVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpIfRobustnessVariable.setStatus("current")


class _ZxAnIgmpMvlanAutoTranslateEnable_Type(Integer32):
    """Custom type zxAnIgmpMvlanAutoTranslateEnable based on Integer32"""
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


_ZxAnIgmpMvlanAutoTranslateEnable_Type.__name__ = "Integer32"
_ZxAnIgmpMvlanAutoTranslateEnable_Object = MibTableColumn
zxAnIgmpMvlanAutoTranslateEnable = _ZxAnIgmpMvlanAutoTranslateEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 17),
    _ZxAnIgmpMvlanAutoTranslateEnable_Type()
)
zxAnIgmpMvlanAutoTranslateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpMvlanAutoTranslateEnable.setStatus("current")


class _ZxAnIgmpPortQueryPacketCos_Type(Integer32):
    """Custom type zxAnIgmpPortQueryPacketCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnIgmpPortQueryPacketCos_Type.__name__ = "Integer32"
_ZxAnIgmpPortQueryPacketCos_Object = MibTableColumn
zxAnIgmpPortQueryPacketCos = _ZxAnIgmpPortQueryPacketCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 21, 1, 18),
    _ZxAnIgmpPortQueryPacketCos_Type()
)
zxAnIgmpPortQueryPacketCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpPortQueryPacketCos.setStatus("current")
_ZxAnIgmpMvlanTable_Object = MibTable
zxAnIgmpMvlanTable = _ZxAnIgmpMvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22)
)
if mibBuilder.loadTexts:
    zxAnIgmpMvlanTable.setStatus("current")
_ZxAnIgmpMvlanEntry_Object = MibTableRow
zxAnIgmpMvlanEntry = _ZxAnIgmpMvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1)
)
zxAnIgmpMvlanEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
)
if mibBuilder.loadTexts:
    zxAnIgmpMvlanEntry.setStatus("current")


class _ZxAnIgmpMVid_Type(Integer32):
    """Custom type zxAnIgmpMVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnIgmpMVid_Type.__name__ = "Integer32"
_ZxAnIgmpMVid_Object = MibTableColumn
zxAnIgmpMVid = _ZxAnIgmpMVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 1),
    _ZxAnIgmpMVid_Type()
)
zxAnIgmpMVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpMVid.setStatus("current")


class _ZxAnIgmpMVlanIgmpAdminStatus_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpAdminStatus based on Integer32"""
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


_ZxAnIgmpMVlanIgmpAdminStatus_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpAdminStatus_Object = MibTableColumn
zxAnIgmpMVlanIgmpAdminStatus = _ZxAnIgmpMVlanIgmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 2),
    _ZxAnIgmpMVlanIgmpAdminStatus_Type()
)
zxAnIgmpMVlanIgmpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpAdminStatus.setStatus("current")


class _ZxAnIgmpMVlanIgmpWorkMode_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpWorkMode based on Integer32"""
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


_ZxAnIgmpMVlanIgmpWorkMode_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpWorkMode_Object = MibTableColumn
zxAnIgmpMVlanIgmpWorkMode = _ZxAnIgmpMVlanIgmpWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 3),
    _ZxAnIgmpMVlanIgmpWorkMode_Type()
)
zxAnIgmpMVlanIgmpWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpWorkMode.setStatus("current")
_ZxAnIgmpMVlanHostIpAddr_Type = IpAddress
_ZxAnIgmpMVlanHostIpAddr_Object = MibTableColumn
zxAnIgmpMVlanHostIpAddr = _ZxAnIgmpMVlanHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 4),
    _ZxAnIgmpMVlanHostIpAddr_Type()
)
zxAnIgmpMVlanHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanHostIpAddr.setStatus("current")
_ZxAnIgmpMVlanGroupPreConfEnable_Type = TruthValue
_ZxAnIgmpMVlanGroupPreConfEnable_Object = MibTableColumn
zxAnIgmpMVlanGroupPreConfEnable = _ZxAnIgmpMVlanGroupPreConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 5),
    _ZxAnIgmpMVlanGroupPreConfEnable_Type()
)
zxAnIgmpMVlanGroupPreConfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanGroupPreConfEnable.setStatus("current")


class _ZxAnIgmpMVlanMaxConcurrentGroups_Type(Integer32):
    """Custom type zxAnIgmpMVlanMaxConcurrentGroups based on Integer32"""
    defaultValue = 512


_ZxAnIgmpMVlanMaxConcurrentGroups_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanMaxConcurrentGroups_Object = MibTableColumn
zxAnIgmpMVlanMaxConcurrentGroups = _ZxAnIgmpMVlanMaxConcurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 6),
    _ZxAnIgmpMVlanMaxConcurrentGroups_Type()
)
zxAnIgmpMVlanMaxConcurrentGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanMaxConcurrentGroups.setStatus("current")
_ZxAnIgmpMVlanCurrActGroups_Type = Gauge32
_ZxAnIgmpMVlanCurrActGroups_Object = MibTableColumn
zxAnIgmpMVlanCurrActGroups = _ZxAnIgmpMVlanCurrActGroups_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 7),
    _ZxAnIgmpMVlanCurrActGroups_Type()
)
zxAnIgmpMVlanCurrActGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanCurrActGroups.setStatus("current")


class _ZxAnIgmpMVlanIgmpPacketPriority_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpPacketPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnIgmpMVlanIgmpPacketPriority_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpPacketPriority_Object = MibTableColumn
zxAnIgmpMVlanIgmpPacketPriority = _ZxAnIgmpMVlanIgmpPacketPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 8),
    _ZxAnIgmpMVlanIgmpPacketPriority_Type()
)
zxAnIgmpMVlanIgmpPacketPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpPacketPriority.setStatus("current")


class _ZxAnIgmpMVlanHostVersion_Type(Integer32):
    """Custom type zxAnIgmpMVlanHostVersion based on Integer32"""
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
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_ZxAnIgmpMVlanHostVersion_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanHostVersion_Object = MibTableColumn
zxAnIgmpMVlanHostVersion = _ZxAnIgmpMVlanHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 9),
    _ZxAnIgmpMVlanHostVersion_Type()
)
zxAnIgmpMVlanHostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanHostVersion.setStatus("current")
_ZxAnMvlanActHosts_Type = Gauge32
_ZxAnMvlanActHosts_Object = MibTableColumn
zxAnMvlanActHosts = _ZxAnMvlanActHosts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 10),
    _ZxAnMvlanActHosts_Type()
)
zxAnMvlanActHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMvlanActHosts.setStatus("current")


class _ZxAnIgmpMVlanCVid_Type(Integer32):
    """Custom type zxAnIgmpMVlanCVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZxAnIgmpMVlanCVid_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanCVid_Object = MibTableColumn
zxAnIgmpMVlanCVid = _ZxAnIgmpMVlanCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 11),
    _ZxAnIgmpMVlanCVid_Type()
)
zxAnIgmpMVlanCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanCVid.setStatus("current")


class _ZxAnMvlanReportAndLeavePacketCos_Type(Integer32):
    """Custom type zxAnMvlanReportAndLeavePacketCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnMvlanReportAndLeavePacketCos_Type.__name__ = "Integer32"
_ZxAnMvlanReportAndLeavePacketCos_Object = MibTableColumn
zxAnMvlanReportAndLeavePacketCos = _ZxAnMvlanReportAndLeavePacketCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 12),
    _ZxAnMvlanReportAndLeavePacketCos_Type()
)
zxAnMvlanReportAndLeavePacketCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMvlanReportAndLeavePacketCos.setStatus("current")


class _ZxAnIgmpMVlanIgmpMessageVid_Type(Integer32):
    """Custom type zxAnIgmpMVlanIgmpMessageVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnIgmpMVlanIgmpMessageVid_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanIgmpMessageVid_Object = MibTableColumn
zxAnIgmpMVlanIgmpMessageVid = _ZxAnIgmpMVlanIgmpMessageVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 13),
    _ZxAnIgmpMVlanIgmpMessageVid_Type()
)
zxAnIgmpMVlanIgmpMessageVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanIgmpMessageVid.setStatus("current")


class _ZxAnIgmpMVlanMaxBandwidth_Type(Integer32):
    """Custom type zxAnIgmpMVlanMaxBandwidth based on Integer32"""
    defaultValue = 1048576000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048576000),
    )


_ZxAnIgmpMVlanMaxBandwidth_Type.__name__ = "Integer32"
_ZxAnIgmpMVlanMaxBandwidth_Object = MibTableColumn
zxAnIgmpMVlanMaxBandwidth = _ZxAnIgmpMVlanMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 14),
    _ZxAnIgmpMVlanMaxBandwidth_Type()
)
zxAnIgmpMVlanMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanMaxBandwidth.setUnits("kpbs")
_ZxAnIgmpMgmtMVlanRowStatus_Type = RowStatus
_ZxAnIgmpMgmtMVlanRowStatus_Object = MibTableColumn
zxAnIgmpMgmtMVlanRowStatus = _ZxAnIgmpMgmtMVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 22, 1, 20),
    _ZxAnIgmpMgmtMVlanRowStatus_Type()
)
zxAnIgmpMgmtMVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMgmtMVlanRowStatus.setStatus("current")
_ZxAnIgmpMvlanPortListTable_Object = MibTable
zxAnIgmpMvlanPortListTable = _ZxAnIgmpMvlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 23)
)
if mibBuilder.loadTexts:
    zxAnIgmpMvlanPortListTable.setStatus("current")
_ZxAnIgmpMvlanPortListEntry_Object = MibTableRow
zxAnIgmpMvlanPortListEntry = _ZxAnIgmpMvlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 23, 1)
)
zxAnIgmpMvlanPortListEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVlanPortListShelf"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVlanPortListSlot"),
)
if mibBuilder.loadTexts:
    zxAnIgmpMvlanPortListEntry.setStatus("current")
_ZxAnIgmpMVlanPortListShelf_Type = Integer32
_ZxAnIgmpMVlanPortListShelf_Object = MibTableColumn
zxAnIgmpMVlanPortListShelf = _ZxAnIgmpMVlanPortListShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 23, 1, 1),
    _ZxAnIgmpMVlanPortListShelf_Type()
)
zxAnIgmpMVlanPortListShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanPortListShelf.setStatus("current")
_ZxAnIgmpMVlanPortListSlot_Type = Integer32
_ZxAnIgmpMVlanPortListSlot_Object = MibTableColumn
zxAnIgmpMVlanPortListSlot = _ZxAnIgmpMVlanPortListSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 23, 1, 2),
    _ZxAnIgmpMVlanPortListSlot_Type()
)
zxAnIgmpMVlanPortListSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanPortListSlot.setStatus("current")
_ZxAnIgmpMVlanSrcPortList_Type = ZxAnPortList
_ZxAnIgmpMVlanSrcPortList_Object = MibTableColumn
zxAnIgmpMVlanSrcPortList = _ZxAnIgmpMVlanSrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 23, 1, 3),
    _ZxAnIgmpMVlanSrcPortList_Type()
)
zxAnIgmpMVlanSrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanSrcPortList.setStatus("current")
_ZxAnIgmpMVlanRecvPortList_Type = ZxAnPortList
_ZxAnIgmpMVlanRecvPortList_Object = MibTableColumn
zxAnIgmpMVlanRecvPortList = _ZxAnIgmpMVlanRecvPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 23, 1, 4),
    _ZxAnIgmpMVlanRecvPortList_Type()
)
zxAnIgmpMVlanRecvPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMVlanRecvPortList.setStatus("current")
_ZxAnIgmpGroupTable_Object = MibTable
zxAnIgmpGroupTable = _ZxAnIgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24)
)
if mibBuilder.loadTexts:
    zxAnIgmpGroupTable.setStatus("current")
_ZxAnIgmpGroupEntry_Object = MibTableRow
zxAnIgmpGroupEntry = _ZxAnIgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1)
)
zxAnIgmpGroupEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpSourceIpAddr"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpGroupIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnIgmpGroupEntry.setStatus("current")
_ZxAnIgmpSourceIpAddr_Type = IpAddress
_ZxAnIgmpSourceIpAddr_Object = MibTableColumn
zxAnIgmpSourceIpAddr = _ZxAnIgmpSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 1),
    _ZxAnIgmpSourceIpAddr_Type()
)
zxAnIgmpSourceIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpSourceIpAddr.setStatus("current")
_ZxAnIgmpGroupIpAddr_Type = IpAddress
_ZxAnIgmpGroupIpAddr_Object = MibTableColumn
zxAnIgmpGroupIpAddr = _ZxAnIgmpGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 2),
    _ZxAnIgmpGroupIpAddr_Type()
)
zxAnIgmpGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpGroupIpAddr.setStatus("current")


class _ZxAnIgmpGroupBandwidthCost_Type(Integer32):
    """Custom type zxAnIgmpGroupBandwidthCost based on Integer32"""
    defaultValue = 2048


_ZxAnIgmpGroupBandwidthCost_Type.__name__ = "Integer32"
_ZxAnIgmpGroupBandwidthCost_Object = MibTableColumn
zxAnIgmpGroupBandwidthCost = _ZxAnIgmpGroupBandwidthCost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 3),
    _ZxAnIgmpGroupBandwidthCost_Type()
)
zxAnIgmpGroupBandwidthCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpGroupBandwidthCost.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpGroupBandwidthCost.setUnits("kbps")


class _ZxAnIgmpGroupPrejoinEnable_Type(TruthValue):
    """Custom type zxAnIgmpGroupPrejoinEnable based on TruthValue"""
    defaultValue = 2


_ZxAnIgmpGroupPrejoinEnable_Type.__name__ = "TruthValue"
_ZxAnIgmpGroupPrejoinEnable_Object = MibTableColumn
zxAnIgmpGroupPrejoinEnable = _ZxAnIgmpGroupPrejoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 4),
    _ZxAnIgmpGroupPrejoinEnable_Type()
)
zxAnIgmpGroupPrejoinEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpGroupPrejoinEnable.setStatus("current")
_ZxAnIgmpGroupMaxHosts_Type = Integer32
_ZxAnIgmpGroupMaxHosts_Object = MibTableColumn
zxAnIgmpGroupMaxHosts = _ZxAnIgmpGroupMaxHosts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 5),
    _ZxAnIgmpGroupMaxHosts_Type()
)
zxAnIgmpGroupMaxHosts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpGroupMaxHosts.setStatus("current")
_ZxAnIgmpGroupCurrActHosts_Type = Integer32
_ZxAnIgmpGroupCurrActHosts_Object = MibTableColumn
zxAnIgmpGroupCurrActHosts = _ZxAnIgmpGroupCurrActHosts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 6),
    _ZxAnIgmpGroupCurrActHosts_Type()
)
zxAnIgmpGroupCurrActHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpGroupCurrActHosts.setStatus("current")
_ZxAnIgmpGroupV3SrcIp_Type = IpAddress
_ZxAnIgmpGroupV3SrcIp_Object = MibTableColumn
zxAnIgmpGroupV3SrcIp = _ZxAnIgmpGroupV3SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 7),
    _ZxAnIgmpGroupV3SrcIp_Type()
)
zxAnIgmpGroupV3SrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpGroupV3SrcIp.setStatus("current")


class _ZxAnIgmpGroupHostState_Type(Integer32):
    """Custom type zxAnIgmpGroupHostState based on Integer32"""
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


_ZxAnIgmpGroupHostState_Type.__name__ = "Integer32"
_ZxAnIgmpGroupHostState_Object = MibTableColumn
zxAnIgmpGroupHostState = _ZxAnIgmpGroupHostState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 8),
    _ZxAnIgmpGroupHostState_Type()
)
zxAnIgmpGroupHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpGroupHostState.setStatus("current")
_ZxAnIgmpMgmtGroupRowStatus_Type = RowStatus
_ZxAnIgmpMgmtGroupRowStatus_Object = MibTableColumn
zxAnIgmpMgmtGroupRowStatus = _ZxAnIgmpMgmtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 24, 1, 15),
    _ZxAnIgmpMgmtGroupRowStatus_Type()
)
zxAnIgmpMgmtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMgmtGroupRowStatus.setStatus("current")
_ZxAnIgmpGroupPortListTable_Object = MibTable
zxAnIgmpGroupPortListTable = _ZxAnIgmpGroupPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 25)
)
if mibBuilder.loadTexts:
    zxAnIgmpGroupPortListTable.setStatus("current")
_ZxAnIgmpGroupPortListEntry_Object = MibTableRow
zxAnIgmpGroupPortListEntry = _ZxAnIgmpGroupPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 25, 1)
)
zxAnIgmpGroupPortListEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpSourceIpAddr"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpGroupIpAddr"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVlanPortListShelf"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVlanPortListSlot"),
)
if mibBuilder.loadTexts:
    zxAnIgmpGroupPortListEntry.setStatus("current")
_ZxAnIgmpGroupStaticPortList_Type = ZxAnPortList
_ZxAnIgmpGroupStaticPortList_Object = MibTableColumn
zxAnIgmpGroupStaticPortList = _ZxAnIgmpGroupStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 25, 1, 1),
    _ZxAnIgmpGroupStaticPortList_Type()
)
zxAnIgmpGroupStaticPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpGroupStaticPortList.setStatus("current")
_ZxAnIgmpGroupDynamicPortList_Type = ZxAnPortList
_ZxAnIgmpGroupDynamicPortList_Object = MibTableColumn
zxAnIgmpGroupDynamicPortList = _ZxAnIgmpGroupDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 25, 1, 2),
    _ZxAnIgmpGroupDynamicPortList_Type()
)
zxAnIgmpGroupDynamicPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpGroupDynamicPortList.setStatus("current")
_ZxAnIgmpParamListCmdTable_Object = MibTable
zxAnIgmpParamListCmdTable = _ZxAnIgmpParamListCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 26)
)
if mibBuilder.loadTexts:
    zxAnIgmpParamListCmdTable.setStatus("current")
_ZxAnIgmpParamListCmdEntry_Object = MibTableRow
zxAnIgmpParamListCmdEntry = _ZxAnIgmpParamListCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 26, 1)
)
zxAnIgmpParamListCmdEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpParamListCmd"),
)
if mibBuilder.loadTexts:
    zxAnIgmpParamListCmdEntry.setStatus("current")


class _ZxAnIgmpParamListCmd_Type(Integer32):
    """Custom type zxAnIgmpParamListCmd based on Integer32"""
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


_ZxAnIgmpParamListCmd_Type.__name__ = "Integer32"
_ZxAnIgmpParamListCmd_Object = MibTableColumn
zxAnIgmpParamListCmd = _ZxAnIgmpParamListCmd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 26, 1, 1),
    _ZxAnIgmpParamListCmd_Type()
)
zxAnIgmpParamListCmd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpParamListCmd.setStatus("current")
_ZxAnIgmpParamObject_Type = ObjectIdentifier
_ZxAnIgmpParamObject_Object = MibTableColumn
zxAnIgmpParamObject = _ZxAnIgmpParamObject_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 26, 1, 2),
    _ZxAnIgmpParamObject_Type()
)
zxAnIgmpParamObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpParamObject.setStatus("current")
_ZxAnIgmpCounterTable_Object = MibTable
zxAnIgmpCounterTable = _ZxAnIgmpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27)
)
if mibBuilder.loadTexts:
    zxAnIgmpCounterTable.setStatus("current")
_ZxAnIgmpCounterEntry_Object = MibTableRow
zxAnIgmpCounterEntry = _ZxAnIgmpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1)
)
zxAnIgmpCounterEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnIgmpCounterEntry.setStatus("current")
_ZxAnIgmpCounterReset_Type = Integer32
_ZxAnIgmpCounterReset_Object = MibTableColumn
zxAnIgmpCounterReset = _ZxAnIgmpCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 1),
    _ZxAnIgmpCounterReset_Type()
)
zxAnIgmpCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpCounterReset.setStatus("current")
_ZxAnIgmpCounterRxCommQuery_Type = Counter32
_ZxAnIgmpCounterRxCommQuery_Object = MibTableColumn
zxAnIgmpCounterRxCommQuery = _ZxAnIgmpCounterRxCommQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 2),
    _ZxAnIgmpCounterRxCommQuery_Type()
)
zxAnIgmpCounterRxCommQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxCommQuery.setStatus("current")
_ZxAnIgmpCounterRxSpecialQuery_Type = Counter32
_ZxAnIgmpCounterRxSpecialQuery_Object = MibTableColumn
zxAnIgmpCounterRxSpecialQuery = _ZxAnIgmpCounterRxSpecialQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 3),
    _ZxAnIgmpCounterRxSpecialQuery_Type()
)
zxAnIgmpCounterRxSpecialQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxSpecialQuery.setStatus("current")
_ZxAnIgmpCounterRxV1Report_Type = Counter32
_ZxAnIgmpCounterRxV1Report_Object = MibTableColumn
zxAnIgmpCounterRxV1Report = _ZxAnIgmpCounterRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 4),
    _ZxAnIgmpCounterRxV1Report_Type()
)
zxAnIgmpCounterRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxV1Report.setStatus("current")
_ZxAnIgmpCounterRxV2Report_Type = Counter32
_ZxAnIgmpCounterRxV2Report_Object = MibTableColumn
zxAnIgmpCounterRxV2Report = _ZxAnIgmpCounterRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 5),
    _ZxAnIgmpCounterRxV2Report_Type()
)
zxAnIgmpCounterRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxV2Report.setStatus("current")
_ZxAnIgmpCounterRxV3Report_Type = Counter32
_ZxAnIgmpCounterRxV3Report_Object = MibTableColumn
zxAnIgmpCounterRxV3Report = _ZxAnIgmpCounterRxV3Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 6),
    _ZxAnIgmpCounterRxV3Report_Type()
)
zxAnIgmpCounterRxV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxV3Report.setStatus("current")
_ZxAnIgmpCounterRxLeave_Type = Counter32
_ZxAnIgmpCounterRxLeave_Object = MibTableColumn
zxAnIgmpCounterRxLeave = _ZxAnIgmpCounterRxLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 7),
    _ZxAnIgmpCounterRxLeave_Type()
)
zxAnIgmpCounterRxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxLeave.setStatus("current")
_ZxAnIgmpCounterRxError_Type = Counter32
_ZxAnIgmpCounterRxError_Object = MibTableColumn
zxAnIgmpCounterRxError = _ZxAnIgmpCounterRxError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 8),
    _ZxAnIgmpCounterRxError_Type()
)
zxAnIgmpCounterRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxError.setStatus("current")
_ZxAnIgmpCounterRxUnknown_Type = Counter32
_ZxAnIgmpCounterRxUnknown_Object = MibTableColumn
zxAnIgmpCounterRxUnknown = _ZxAnIgmpCounterRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 9),
    _ZxAnIgmpCounterRxUnknown_Type()
)
zxAnIgmpCounterRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterRxUnknown.setStatus("current")
_ZxAnIgmpCounterTxCommQuery_Type = Counter32
_ZxAnIgmpCounterTxCommQuery_Object = MibTableColumn
zxAnIgmpCounterTxCommQuery = _ZxAnIgmpCounterTxCommQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 10),
    _ZxAnIgmpCounterTxCommQuery_Type()
)
zxAnIgmpCounterTxCommQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterTxCommQuery.setStatus("current")
_ZxAnIgmpCounterTxSpecialQuery_Type = Counter32
_ZxAnIgmpCounterTxSpecialQuery_Object = MibTableColumn
zxAnIgmpCounterTxSpecialQuery = _ZxAnIgmpCounterTxSpecialQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 11),
    _ZxAnIgmpCounterTxSpecialQuery_Type()
)
zxAnIgmpCounterTxSpecialQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterTxSpecialQuery.setStatus("current")
_ZxAnIgmpCounterTxV1Report_Type = Counter32
_ZxAnIgmpCounterTxV1Report_Object = MibTableColumn
zxAnIgmpCounterTxV1Report = _ZxAnIgmpCounterTxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 12),
    _ZxAnIgmpCounterTxV1Report_Type()
)
zxAnIgmpCounterTxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterTxV1Report.setStatus("current")
_ZxAnIgmpCounterTxV2Report_Type = Counter32
_ZxAnIgmpCounterTxV2Report_Object = MibTableColumn
zxAnIgmpCounterTxV2Report = _ZxAnIgmpCounterTxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 13),
    _ZxAnIgmpCounterTxV2Report_Type()
)
zxAnIgmpCounterTxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterTxV2Report.setStatus("current")
_ZxAnIgmpCounterTxV3Report_Type = Counter32
_ZxAnIgmpCounterTxV3Report_Object = MibTableColumn
zxAnIgmpCounterTxV3Report = _ZxAnIgmpCounterTxV3Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 14),
    _ZxAnIgmpCounterTxV3Report_Type()
)
zxAnIgmpCounterTxV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterTxV3Report.setStatus("current")
_ZxAnIgmpCounterTxLeave_Type = Counter32
_ZxAnIgmpCounterTxLeave_Object = MibTableColumn
zxAnIgmpCounterTxLeave = _ZxAnIgmpCounterTxLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 15),
    _ZxAnIgmpCounterTxLeave_Type()
)
zxAnIgmpCounterTxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterTxLeave.setStatus("current")
_ZxAnIgmpCounterDropRxCommQuery_Type = Counter32
_ZxAnIgmpCounterDropRxCommQuery_Object = MibTableColumn
zxAnIgmpCounterDropRxCommQuery = _ZxAnIgmpCounterDropRxCommQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 16),
    _ZxAnIgmpCounterDropRxCommQuery_Type()
)
zxAnIgmpCounterDropRxCommQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxCommQuery.setStatus("current")
_ZxAnIgmpCounterDropRxSpecialQuery_Type = Counter32
_ZxAnIgmpCounterDropRxSpecialQuery_Object = MibTableColumn
zxAnIgmpCounterDropRxSpecialQuery = _ZxAnIgmpCounterDropRxSpecialQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 17),
    _ZxAnIgmpCounterDropRxSpecialQuery_Type()
)
zxAnIgmpCounterDropRxSpecialQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxSpecialQuery.setStatus("current")
_ZxAnIgmpCounterDropRxV1Report_Type = Counter32
_ZxAnIgmpCounterDropRxV1Report_Object = MibTableColumn
zxAnIgmpCounterDropRxV1Report = _ZxAnIgmpCounterDropRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 18),
    _ZxAnIgmpCounterDropRxV1Report_Type()
)
zxAnIgmpCounterDropRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxV1Report.setStatus("current")
_ZxAnIgmpCounterDropRxV2Report_Type = Counter32
_ZxAnIgmpCounterDropRxV2Report_Object = MibTableColumn
zxAnIgmpCounterDropRxV2Report = _ZxAnIgmpCounterDropRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 19),
    _ZxAnIgmpCounterDropRxV2Report_Type()
)
zxAnIgmpCounterDropRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxV2Report.setStatus("current")
_ZxAnIgmpCounterDropRxV3Report_Type = Counter32
_ZxAnIgmpCounterDropRxV3Report_Object = MibTableColumn
zxAnIgmpCounterDropRxV3Report = _ZxAnIgmpCounterDropRxV3Report_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 20),
    _ZxAnIgmpCounterDropRxV3Report_Type()
)
zxAnIgmpCounterDropRxV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxV3Report.setStatus("current")
_ZxAnIgmpCounterDropRxLeave_Type = Counter32
_ZxAnIgmpCounterDropRxLeave_Object = MibTableColumn
zxAnIgmpCounterDropRxLeave = _ZxAnIgmpCounterDropRxLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 21),
    _ZxAnIgmpCounterDropRxLeave_Type()
)
zxAnIgmpCounterDropRxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxLeave.setStatus("current")
_ZxAnIgmpCounterDropRxUnknown_Type = Counter32
_ZxAnIgmpCounterDropRxUnknown_Object = MibTableColumn
zxAnIgmpCounterDropRxUnknown = _ZxAnIgmpCounterDropRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 22),
    _ZxAnIgmpCounterDropRxUnknown_Type()
)
zxAnIgmpCounterDropRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterDropRxUnknown.setStatus("current")
_ZxAnIgmpCounterJoinSuccess_Type = Counter32
_ZxAnIgmpCounterJoinSuccess_Object = MibTableColumn
zxAnIgmpCounterJoinSuccess = _ZxAnIgmpCounterJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 23),
    _ZxAnIgmpCounterJoinSuccess_Type()
)
zxAnIgmpCounterJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterJoinSuccess.setStatus("current")
_ZxAnIgmpCounterJoinFailure_Type = Counter32
_ZxAnIgmpCounterJoinFailure_Object = MibTableColumn
zxAnIgmpCounterJoinFailure = _ZxAnIgmpCounterJoinFailure_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 27, 1, 24),
    _ZxAnIgmpCounterJoinFailure_Type()
)
zxAnIgmpCounterJoinFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpCounterJoinFailure.setStatus("current")
_ZxAnMVlanTranslateTable_Object = MibTable
zxAnMVlanTranslateTable = _ZxAnMVlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 28)
)
if mibBuilder.loadTexts:
    zxAnMVlanTranslateTable.setStatus("current")
_ZxAnMVlanTranslateEntry_Object = MibTableRow
zxAnMVlanTranslateEntry = _ZxAnMVlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 28, 1)
)
zxAnMVlanTranslateEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnMVlanTranslatePortIndex"),
)
if mibBuilder.loadTexts:
    zxAnMVlanTranslateEntry.setStatus("current")
_ZxAnMVlanTranslatePortIndex_Type = ZxAnIfindex
_ZxAnMVlanTranslatePortIndex_Object = MibTableColumn
zxAnMVlanTranslatePortIndex = _ZxAnMVlanTranslatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 28, 1, 1),
    _ZxAnMVlanTranslatePortIndex_Type()
)
zxAnMVlanTranslatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMVlanTranslatePortIndex.setStatus("current")


class _ZxAnMVlanTranslateEn_Type(Integer32):
    """Custom type zxAnMVlanTranslateEn based on Integer32"""
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


_ZxAnMVlanTranslateEn_Type.__name__ = "Integer32"
_ZxAnMVlanTranslateEn_Object = MibTableColumn
zxAnMVlanTranslateEn = _ZxAnMVlanTranslateEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 28, 1, 2),
    _ZxAnMVlanTranslateEn_Type()
)
zxAnMVlanTranslateEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMVlanTranslateEn.setStatus("current")


class _ZxAnMVlanTranslateCVlan_Type(Integer32):
    """Custom type zxAnMVlanTranslateCVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnMVlanTranslateCVlan_Type.__name__ = "Integer32"
_ZxAnMVlanTranslateCVlan_Object = MibTableColumn
zxAnMVlanTranslateCVlan = _ZxAnMVlanTranslateCVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 28, 1, 3),
    _ZxAnMVlanTranslateCVlan_Type()
)
zxAnMVlanTranslateCVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMVlanTranslateCVlan.setStatus("current")
_ZxAnIgmpPortActiveGroupTable_Object = MibTable
zxAnIgmpPortActiveGroupTable = _ZxAnIgmpPortActiveGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 29)
)
if mibBuilder.loadTexts:
    zxAnIgmpPortActiveGroupTable.setStatus("current")
_ZxAnIgmpPortActiveGroupEntry_Object = MibTableRow
zxAnIgmpPortActiveGroupEntry = _ZxAnIgmpPortActiveGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 29, 1)
)
zxAnIgmpPortActiveGroupEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpGroupIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnIgmpPortActiveGroupEntry.setStatus("current")


class _ZxAnIgmpPortTypeInGroup_Type(Integer32):
    """Custom type zxAnIgmpPortTypeInGroup based on Integer32"""
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


_ZxAnIgmpPortTypeInGroup_Type.__name__ = "Integer32"
_ZxAnIgmpPortTypeInGroup_Object = MibTableColumn
zxAnIgmpPortTypeInGroup = _ZxAnIgmpPortTypeInGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 29, 1, 1),
    _ZxAnIgmpPortTypeInGroup_Type()
)
zxAnIgmpPortTypeInGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpPortTypeInGroup.setStatus("current")
_ZxAnIgmpPMGlobal_ObjectIdentity = ObjectIdentity
zxAnIgmpPMGlobal = _ZxAnIgmpPMGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 30)
)
_ZxAnIgmpGlobalCounterReset_Type = Integer32
_ZxAnIgmpGlobalCounterReset_Object = MibScalar
zxAnIgmpGlobalCounterReset = _ZxAnIgmpGlobalCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 30, 1),
    _ZxAnIgmpGlobalCounterReset_Type()
)
zxAnIgmpGlobalCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIgmpGlobalCounterReset.setStatus("current")


class _ZxAnMvlanCounterReset_Type(Integer32):
    """Custom type zxAnMvlanCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnMvlanCounterReset_Type.__name__ = "Integer32"
_ZxAnMvlanCounterReset_Object = MibScalar
zxAnMvlanCounterReset = _ZxAnMvlanCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 30, 2),
    _ZxAnMvlanCounterReset_Type()
)
zxAnMvlanCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMvlanCounterReset.setStatus("current")
_ZxAnIgmpIfMulticastStatsTable_Object = MibTable
zxAnIgmpIfMulticastStatsTable = _ZxAnIgmpIfMulticastStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 31)
)
if mibBuilder.loadTexts:
    zxAnIgmpIfMulticastStatsTable.setStatus("current")
_ZxAnIgmpIfMulticastStatsEntry_Object = MibTableRow
zxAnIgmpIfMulticastStatsEntry = _ZxAnIgmpIfMulticastStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 31, 1)
)
zxAnIgmpIfMulticastStatsEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnIgmpIfMulticastStatsEntry.setStatus("current")
_ZxAnIgmpIfMulticastTxPktRate_Type = Integer32
_ZxAnIgmpIfMulticastTxPktRate_Object = MibTableColumn
zxAnIgmpIfMulticastTxPktRate = _ZxAnIgmpIfMulticastTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 31, 1, 1),
    _ZxAnIgmpIfMulticastTxPktRate_Type()
)
zxAnIgmpIfMulticastTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpIfMulticastTxPktRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIgmpIfMulticastTxPktRate.setUnits("pps")
_ZxAnIgmpMgmtMVlanRecvIfTable_Object = MibTable
zxAnIgmpMgmtMVlanRecvIfTable = _ZxAnIgmpMgmtMVlanRecvIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 32)
)
if mibBuilder.loadTexts:
    zxAnIgmpMgmtMVlanRecvIfTable.setStatus("current")
_ZxAnIgmpMgmtMVlanRecvIfEntry_Object = MibTableRow
zxAnIgmpMgmtMVlanRecvIfEntry = _ZxAnIgmpMgmtMVlanRecvIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 32, 1)
)
zxAnIgmpMgmtMVlanRecvIfEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnIgmpMgmtMVlanRecvIfEntry.setStatus("current")
_ZxAnIgmpMgmtMVlanRecvIfRowStatus_Type = RowStatus
_ZxAnIgmpMgmtMVlanRecvIfRowStatus_Object = MibTableColumn
zxAnIgmpMgmtMVlanRecvIfRowStatus = _ZxAnIgmpMgmtMVlanRecvIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 32, 1, 50),
    _ZxAnIgmpMgmtMVlanRecvIfRowStatus_Type()
)
zxAnIgmpMgmtMVlanRecvIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpMgmtMVlanRecvIfRowStatus.setStatus("current")
_ZxAnIgmpMgmtGroupUserTable_Object = MibTable
zxAnIgmpMgmtGroupUserTable = _ZxAnIgmpMgmtGroupUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 33)
)
if mibBuilder.loadTexts:
    zxAnIgmpMgmtGroupUserTable.setStatus("current")
_ZxAnIgmpMgmtGroupUserEntry_Object = MibTableRow
zxAnIgmpMgmtGroupUserEntry = _ZxAnIgmpMgmtGroupUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 33, 1)
)
zxAnIgmpMgmtGroupUserEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpGroupIpAddr"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpUserIpAddr"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpSourceIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnIgmpMgmtGroupUserEntry.setStatus("current")
_ZxAnIgmpUserIpAddr_Type = IpAddress
_ZxAnIgmpUserIpAddr_Object = MibTableColumn
zxAnIgmpUserIpAddr = _ZxAnIgmpUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 33, 1, 1),
    _ZxAnIgmpUserIpAddr_Type()
)
zxAnIgmpUserIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpUserIpAddr.setStatus("current")


class _ZxAnIgmpGrpUserSrcFilterMode_Type(Integer32):
    """Custom type zxAnIgmpGrpUserSrcFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_ZxAnIgmpGrpUserSrcFilterMode_Type.__name__ = "Integer32"
_ZxAnIgmpGrpUserSrcFilterMode_Object = MibTableColumn
zxAnIgmpGrpUserSrcFilterMode = _ZxAnIgmpGrpUserSrcFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 33, 1, 2),
    _ZxAnIgmpGrpUserSrcFilterMode_Type()
)
zxAnIgmpGrpUserSrcFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIgmpGrpUserSrcFilterMode.setStatus("current")
_ZxAnIgmpMgmtStaticGroupUserTable_Object = MibTable
zxAnIgmpMgmtStaticGroupUserTable = _ZxAnIgmpMgmtStaticGroupUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 34)
)
if mibBuilder.loadTexts:
    zxAnIgmpMgmtStaticGroupUserTable.setStatus("current")
_ZxAnIgmpMgmtStaticGroupUserEntry_Object = MibTableRow
zxAnIgmpMgmtStaticGroupUserEntry = _ZxAnIgmpMgmtStaticGroupUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 34, 1)
)
zxAnIgmpMgmtStaticGroupUserEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpGroupIpAddr"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpIfIndex"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpSourceIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnIgmpMgmtStaticGroupUserEntry.setStatus("current")
_ZxAnIgmpStaticGrpUserRowStatus_Type = RowStatus
_ZxAnIgmpStaticGrpUserRowStatus_Object = MibTableColumn
zxAnIgmpStaticGrpUserRowStatus = _ZxAnIgmpStaticGrpUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 34, 1, 50),
    _ZxAnIgmpStaticGrpUserRowStatus_Type()
)
zxAnIgmpStaticGrpUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpStaticGrpUserRowStatus.setStatus("current")
_ZxAnIgmpVplsMulticastObjects_ObjectIdentity = ObjectIdentity
zxAnIgmpVplsMulticastObjects = _ZxAnIgmpVplsMulticastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 50)
)
_ZxAnIgmpVplsMvlanSrcPwTable_Object = MibTable
zxAnIgmpVplsMvlanSrcPwTable = _ZxAnIgmpVplsMvlanSrcPwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 50, 1)
)
if mibBuilder.loadTexts:
    zxAnIgmpVplsMvlanSrcPwTable.setStatus("current")
_ZxAnIgmpVplsMvlanSrcPwEntry_Object = MibTableRow
zxAnIgmpVplsMvlanSrcPwEntry = _ZxAnIgmpVplsMvlanSrcPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 50, 1, 1)
)
zxAnIgmpVplsMvlanSrcPwEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnIgmpVplsMVlanSrcPwName"),
)
if mibBuilder.loadTexts:
    zxAnIgmpVplsMvlanSrcPwEntry.setStatus("current")


class _ZxAnIgmpVplsMVlanSrcPwName_Type(DisplayString):
    """Custom type zxAnIgmpVplsMVlanSrcPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_ZxAnIgmpVplsMVlanSrcPwName_Type.__name__ = "DisplayString"
_ZxAnIgmpVplsMVlanSrcPwName_Object = MibTableColumn
zxAnIgmpVplsMVlanSrcPwName = _ZxAnIgmpVplsMVlanSrcPwName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 50, 1, 1, 1),
    _ZxAnIgmpVplsMVlanSrcPwName_Type()
)
zxAnIgmpVplsMVlanSrcPwName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIgmpVplsMVlanSrcPwName.setStatus("current")
_ZxAnIgmpVplsMVlanSrcPwRowStatus_Type = RowStatus
_ZxAnIgmpVplsMVlanSrcPwRowStatus_Object = MibTableColumn
zxAnIgmpVplsMVlanSrcPwRowStatus = _ZxAnIgmpVplsMVlanSrcPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 50, 1, 1, 20),
    _ZxAnIgmpVplsMVlanSrcPwRowStatus_Type()
)
zxAnIgmpVplsMVlanSrcPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIgmpVplsMVlanSrcPwRowStatus.setStatus("current")
_ZxAnMulticastStatsObjects_ObjectIdentity = ObjectIdentity
zxAnMulticastStatsObjects = _ZxAnMulticastStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51)
)
_ZxAnMulticastGroupStatsTable_Object = MibTable
zxAnMulticastGroupStatsTable = _ZxAnMulticastGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2)
)
if mibBuilder.loadTexts:
    zxAnMulticastGroupStatsTable.setStatus("current")
_ZxAnMulticastGroupStatsEntry_Object = MibTableRow
zxAnMulticastGroupStatsEntry = _ZxAnMulticastGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1)
)
zxAnMulticastGroupStatsEntry.setIndexNames(
    (0, "ZTE-AN-IGMP-MIB", "zxAnMCastGrpStatsMVid"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnMCastGrpStatsGroupIpType"),
    (0, "ZTE-AN-IGMP-MIB", "zxAnMCastGrpStatsGroupIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnMulticastGroupStatsEntry.setStatus("current")


class _ZxAnMCastGrpStatsMVid_Type(Integer32):
    """Custom type zxAnMCastGrpStatsMVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnMCastGrpStatsMVid_Type.__name__ = "Integer32"
_ZxAnMCastGrpStatsMVid_Object = MibTableColumn
zxAnMCastGrpStatsMVid = _ZxAnMCastGrpStatsMVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1, 1),
    _ZxAnMCastGrpStatsMVid_Type()
)
zxAnMCastGrpStatsMVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMCastGrpStatsMVid.setStatus("current")
_ZxAnMCastGrpStatsGroupIpType_Type = InetAddressType
_ZxAnMCastGrpStatsGroupIpType_Object = MibTableColumn
zxAnMCastGrpStatsGroupIpType = _ZxAnMCastGrpStatsGroupIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1, 2),
    _ZxAnMCastGrpStatsGroupIpType_Type()
)
zxAnMCastGrpStatsGroupIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMCastGrpStatsGroupIpType.setStatus("current")
_ZxAnMCastGrpStatsGroupIpAddr_Type = InetAddress
_ZxAnMCastGrpStatsGroupIpAddr_Object = MibTableColumn
zxAnMCastGrpStatsGroupIpAddr = _ZxAnMCastGrpStatsGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1, 3),
    _ZxAnMCastGrpStatsGroupIpAddr_Type()
)
zxAnMCastGrpStatsGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMCastGrpStatsGroupIpAddr.setStatus("current")
_ZxAnMCastGrpStatsBandwidth_Type = Integer32
_ZxAnMCastGrpStatsBandwidth_Object = MibTableColumn
zxAnMCastGrpStatsBandwidth = _ZxAnMCastGrpStatsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1, 4),
    _ZxAnMCastGrpStatsBandwidth_Type()
)
zxAnMCastGrpStatsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpStatsBandwidth.setStatus("current")


class _ZxAnMCastGrpStatsBandwidthUnit_Type(Integer32):
    """Custom type zxAnMCastGrpStatsBandwidthUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("kbps", 2))
    )


_ZxAnMCastGrpStatsBandwidthUnit_Type.__name__ = "Integer32"
_ZxAnMCastGrpStatsBandwidthUnit_Object = MibTableColumn
zxAnMCastGrpStatsBandwidthUnit = _ZxAnMCastGrpStatsBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1, 5),
    _ZxAnMCastGrpStatsBandwidthUnit_Type()
)
zxAnMCastGrpStatsBandwidthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpStatsBandwidthUnit.setStatus("current")
_ZxAnMCastGrpStatsRowStatus_Type = RowStatus
_ZxAnMCastGrpStatsRowStatus_Object = MibTableColumn
zxAnMCastGrpStatsRowStatus = _ZxAnMCastGrpStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 1, 1, 51, 2, 1, 50),
    _ZxAnMCastGrpStatsRowStatus_Type()
)
zxAnMCastGrpStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMCastGrpStatsRowStatus.setStatus("current")
_ZxAnIgmpTrapObjects_ObjectIdentity = ObjectIdentity
zxAnIgmpTrapObjects = _ZxAnIgmpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 2)
)

# Managed Objects groups


# Notification objects

zxAnIgmpGroupThreshExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 2, 1)
)
zxAnIgmpGroupThreshExceeded.setObjects(
    ("ZTE-AN-IGMP-MIB", "zxAnIgmpGroupThreshold")
)
if mibBuilder.loadTexts:
    zxAnIgmpGroupThreshExceeded.setStatus(
        "current"
    )

zxAnIgmpGroupThreshExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 2, 2)
)
zxAnIgmpGroupThreshExceededCleared.setObjects(
    ("ZTE-AN-IGMP-MIB", "zxAnIgmpGroupThreshold")
)
if mibBuilder.loadTexts:
    zxAnIgmpGroupThreshExceededCleared.setStatus(
        "current"
    )

zxAnIgmpPktRateLimitExceededAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 2, 3)
)
zxAnIgmpPktRateLimitExceededAlm.setObjects(
    ("ZTE-AN-IGMP-MIB", "zxAnIgmpPortPacketLimit")
)
if mibBuilder.loadTexts:
    zxAnIgmpPktRateLimitExceededAlm.setStatus(
        "current"
    )

zxAnIgmpPktRateLimitExceededClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 31, 2, 4)
)
zxAnIgmpPktRateLimitExceededClr.setObjects(
    ("ZTE-AN-IGMP-MIB", "zxAnIgmpPortPacketLimit")
)
if mibBuilder.loadTexts:
    zxAnIgmpPktRateLimitExceededClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-IGMP-MIB",
    **{"zxAnIgmpMib": zxAnIgmpMib,
       "zxAnIgmpObjects": zxAnIgmpObjects,
       "zxAnIgmp": zxAnIgmp,
       "zxAnIgmpGlobal": zxAnIgmpGlobal,
       "zxAnIgmpEnable": zxAnIgmpEnable,
       "zxAnIgmpSnoopingAgingTime": zxAnIgmpSnoopingAgingTime,
       "zxAnIgmpWorkingMode": zxAnIgmpWorkingMode,
       "zxAnIgmpSpanVlanEnable": zxAnIgmpSpanVlanEnable,
       "zxAnIgmpDefaultMvlan": zxAnIgmpDefaultMvlan,
       "zxAnIgmpAutoConfigGrpToDefaultMvlan": zxAnIgmpAutoConfigGrpToDefaultMvlan,
       "zxAnIgmpFastQureyBasedIpPool": zxAnIgmpFastQureyBasedIpPool,
       "zxAnIgmpGeneralLeaveEnable": zxAnIgmpGeneralLeaveEnable,
       "zxAnIgmpUserSideRoutingIp": zxAnIgmpUserSideRoutingIp,
       "zxAnIgmpMVlanIgmpV1OperMode": zxAnIgmpMVlanIgmpV1OperMode,
       "zxAnIgmpMVlanIgmpV2OperMode": zxAnIgmpMVlanIgmpV2OperMode,
       "zxAnIgmpMVlanIgmpV3OperMode": zxAnIgmpMVlanIgmpV3OperMode,
       "zxAnIgmpBandwidthCtrlEnable": zxAnIgmpBandwidthCtrlEnable,
       "zxAnIgmpRobustnessVariable": zxAnIgmpRobustnessVariable,
       "zxAnIgmpQryInterval": zxAnIgmpQryInterval,
       "zxAnIgmpQryRespInterval": zxAnIgmpQryRespInterval,
       "zxAnIgmpLastMemberQryInterval": zxAnIgmpLastMemberQryInterval,
       "zxAnIgmpLastMemberQryCount": zxAnIgmpLastMemberQryCount,
       "zxAnIgmpV1QuerierTimeout": zxAnIgmpV1QuerierTimeout,
       "zxAnIgmpUnsolicitReportInterval": zxAnIgmpUnsolicitReportInterval,
       "zxAnIgmpNetworkSideHostIp": zxAnIgmpNetworkSideHostIp,
       "zxAnIgmpForwCvlanOnOff": zxAnIgmpForwCvlanOnOff,
       "zxAnIgmpHostTrackEnable": zxAnIgmpHostTrackEnable,
       "zxAnIgmpNonMatchGroup": zxAnIgmpNonMatchGroup,
       "zxAnIgmpStartUpQryInterval": zxAnIgmpStartUpQryInterval,
       "zxAnIgmpStartUpQryCount": zxAnIgmpStartUpQryCount,
       "zxAnIgmpRouterAlert": zxAnIgmpRouterAlert,
       "zxAnIgmpGeneralLeaveGrpIp": zxAnIgmpGeneralLeaveGrpIp,
       "zxAnIgmpLogEnable": zxAnIgmpLogEnable,
       "zxAnIgmpGroupThreshold": zxAnIgmpGroupThreshold,
       "zxAnIgmpMVlanIgmpSsmCtrlModel": zxAnIgmpMVlanIgmpSsmCtrlModel,
       "zxAnIgmpCapabilities": zxAnIgmpCapabilities,
       "zxAnIgmpPortTable": zxAnIgmpPortTable,
       "zxAnIgmpPortEntry": zxAnIgmpPortEntry,
       "zxAnIgmpIfIndex": zxAnIgmpIfIndex,
       "zxAnIgmpIfAdminStatus": zxAnIgmpIfAdminStatus,
       "zxAnIgmpIfProtoVersion": zxAnIgmpIfProtoVersion,
       "zxAnIgmpIfFastLeaveEnable": zxAnIgmpIfFastLeaveEnable,
       "zxAnIgmpPortUsage": zxAnIgmpPortUsage,
       "zxAnIgmpDataPort": zxAnIgmpDataPort,
       "zxAnIgmpIfProxyIpAddr": zxAnIgmpIfProxyIpAddr,
       "zxAnIgmpPortPacketLimit": zxAnIgmpPortPacketLimit,
       "zxAnIgmpPortMaxBandwidth": zxAnIgmpPortMaxBandwidth,
       "zxAnIgmpIfMaxConcurrentGroups": zxAnIgmpIfMaxConcurrentGroups,
       "zxAnIgmpIfCurrActGroups": zxAnIgmpIfCurrActGroups,
       "zxAnIgmpIfQryInterval": zxAnIgmpIfQryInterval,
       "zxAnIgmpIfLastMemberQryInterval": zxAnIgmpIfLastMemberQryInterval,
       "zxAnIgmpIfQryResponseInterval": zxAnIgmpIfQryResponseInterval,
       "zxAnIgmpPortEtherPriority": zxAnIgmpPortEtherPriority,
       "zxAnIgmpIfRobustnessVariable": zxAnIgmpIfRobustnessVariable,
       "zxAnIgmpMvlanAutoTranslateEnable": zxAnIgmpMvlanAutoTranslateEnable,
       "zxAnIgmpPortQueryPacketCos": zxAnIgmpPortQueryPacketCos,
       "zxAnIgmpMvlanTable": zxAnIgmpMvlanTable,
       "zxAnIgmpMvlanEntry": zxAnIgmpMvlanEntry,
       "zxAnIgmpMVid": zxAnIgmpMVid,
       "zxAnIgmpMVlanIgmpAdminStatus": zxAnIgmpMVlanIgmpAdminStatus,
       "zxAnIgmpMVlanIgmpWorkMode": zxAnIgmpMVlanIgmpWorkMode,
       "zxAnIgmpMVlanHostIpAddr": zxAnIgmpMVlanHostIpAddr,
       "zxAnIgmpMVlanGroupPreConfEnable": zxAnIgmpMVlanGroupPreConfEnable,
       "zxAnIgmpMVlanMaxConcurrentGroups": zxAnIgmpMVlanMaxConcurrentGroups,
       "zxAnIgmpMVlanCurrActGroups": zxAnIgmpMVlanCurrActGroups,
       "zxAnIgmpMVlanIgmpPacketPriority": zxAnIgmpMVlanIgmpPacketPriority,
       "zxAnIgmpMVlanHostVersion": zxAnIgmpMVlanHostVersion,
       "zxAnMvlanActHosts": zxAnMvlanActHosts,
       "zxAnIgmpMVlanCVid": zxAnIgmpMVlanCVid,
       "zxAnMvlanReportAndLeavePacketCos": zxAnMvlanReportAndLeavePacketCos,
       "zxAnIgmpMVlanIgmpMessageVid": zxAnIgmpMVlanIgmpMessageVid,
       "zxAnIgmpMVlanMaxBandwidth": zxAnIgmpMVlanMaxBandwidth,
       "zxAnIgmpMgmtMVlanRowStatus": zxAnIgmpMgmtMVlanRowStatus,
       "zxAnIgmpMvlanPortListTable": zxAnIgmpMvlanPortListTable,
       "zxAnIgmpMvlanPortListEntry": zxAnIgmpMvlanPortListEntry,
       "zxAnIgmpMVlanPortListShelf": zxAnIgmpMVlanPortListShelf,
       "zxAnIgmpMVlanPortListSlot": zxAnIgmpMVlanPortListSlot,
       "zxAnIgmpMVlanSrcPortList": zxAnIgmpMVlanSrcPortList,
       "zxAnIgmpMVlanRecvPortList": zxAnIgmpMVlanRecvPortList,
       "zxAnIgmpGroupTable": zxAnIgmpGroupTable,
       "zxAnIgmpGroupEntry": zxAnIgmpGroupEntry,
       "zxAnIgmpSourceIpAddr": zxAnIgmpSourceIpAddr,
       "zxAnIgmpGroupIpAddr": zxAnIgmpGroupIpAddr,
       "zxAnIgmpGroupBandwidthCost": zxAnIgmpGroupBandwidthCost,
       "zxAnIgmpGroupPrejoinEnable": zxAnIgmpGroupPrejoinEnable,
       "zxAnIgmpGroupMaxHosts": zxAnIgmpGroupMaxHosts,
       "zxAnIgmpGroupCurrActHosts": zxAnIgmpGroupCurrActHosts,
       "zxAnIgmpGroupV3SrcIp": zxAnIgmpGroupV3SrcIp,
       "zxAnIgmpGroupHostState": zxAnIgmpGroupHostState,
       "zxAnIgmpMgmtGroupRowStatus": zxAnIgmpMgmtGroupRowStatus,
       "zxAnIgmpGroupPortListTable": zxAnIgmpGroupPortListTable,
       "zxAnIgmpGroupPortListEntry": zxAnIgmpGroupPortListEntry,
       "zxAnIgmpGroupStaticPortList": zxAnIgmpGroupStaticPortList,
       "zxAnIgmpGroupDynamicPortList": zxAnIgmpGroupDynamicPortList,
       "zxAnIgmpParamListCmdTable": zxAnIgmpParamListCmdTable,
       "zxAnIgmpParamListCmdEntry": zxAnIgmpParamListCmdEntry,
       "zxAnIgmpParamListCmd": zxAnIgmpParamListCmd,
       "zxAnIgmpParamObject": zxAnIgmpParamObject,
       "zxAnIgmpCounterTable": zxAnIgmpCounterTable,
       "zxAnIgmpCounterEntry": zxAnIgmpCounterEntry,
       "zxAnIgmpCounterReset": zxAnIgmpCounterReset,
       "zxAnIgmpCounterRxCommQuery": zxAnIgmpCounterRxCommQuery,
       "zxAnIgmpCounterRxSpecialQuery": zxAnIgmpCounterRxSpecialQuery,
       "zxAnIgmpCounterRxV1Report": zxAnIgmpCounterRxV1Report,
       "zxAnIgmpCounterRxV2Report": zxAnIgmpCounterRxV2Report,
       "zxAnIgmpCounterRxV3Report": zxAnIgmpCounterRxV3Report,
       "zxAnIgmpCounterRxLeave": zxAnIgmpCounterRxLeave,
       "zxAnIgmpCounterRxError": zxAnIgmpCounterRxError,
       "zxAnIgmpCounterRxUnknown": zxAnIgmpCounterRxUnknown,
       "zxAnIgmpCounterTxCommQuery": zxAnIgmpCounterTxCommQuery,
       "zxAnIgmpCounterTxSpecialQuery": zxAnIgmpCounterTxSpecialQuery,
       "zxAnIgmpCounterTxV1Report": zxAnIgmpCounterTxV1Report,
       "zxAnIgmpCounterTxV2Report": zxAnIgmpCounterTxV2Report,
       "zxAnIgmpCounterTxV3Report": zxAnIgmpCounterTxV3Report,
       "zxAnIgmpCounterTxLeave": zxAnIgmpCounterTxLeave,
       "zxAnIgmpCounterDropRxCommQuery": zxAnIgmpCounterDropRxCommQuery,
       "zxAnIgmpCounterDropRxSpecialQuery": zxAnIgmpCounterDropRxSpecialQuery,
       "zxAnIgmpCounterDropRxV1Report": zxAnIgmpCounterDropRxV1Report,
       "zxAnIgmpCounterDropRxV2Report": zxAnIgmpCounterDropRxV2Report,
       "zxAnIgmpCounterDropRxV3Report": zxAnIgmpCounterDropRxV3Report,
       "zxAnIgmpCounterDropRxLeave": zxAnIgmpCounterDropRxLeave,
       "zxAnIgmpCounterDropRxUnknown": zxAnIgmpCounterDropRxUnknown,
       "zxAnIgmpCounterJoinSuccess": zxAnIgmpCounterJoinSuccess,
       "zxAnIgmpCounterJoinFailure": zxAnIgmpCounterJoinFailure,
       "zxAnMVlanTranslateTable": zxAnMVlanTranslateTable,
       "zxAnMVlanTranslateEntry": zxAnMVlanTranslateEntry,
       "zxAnMVlanTranslatePortIndex": zxAnMVlanTranslatePortIndex,
       "zxAnMVlanTranslateEn": zxAnMVlanTranslateEn,
       "zxAnMVlanTranslateCVlan": zxAnMVlanTranslateCVlan,
       "zxAnIgmpPortActiveGroupTable": zxAnIgmpPortActiveGroupTable,
       "zxAnIgmpPortActiveGroupEntry": zxAnIgmpPortActiveGroupEntry,
       "zxAnIgmpPortTypeInGroup": zxAnIgmpPortTypeInGroup,
       "zxAnIgmpPMGlobal": zxAnIgmpPMGlobal,
       "zxAnIgmpGlobalCounterReset": zxAnIgmpGlobalCounterReset,
       "zxAnMvlanCounterReset": zxAnMvlanCounterReset,
       "zxAnIgmpIfMulticastStatsTable": zxAnIgmpIfMulticastStatsTable,
       "zxAnIgmpIfMulticastStatsEntry": zxAnIgmpIfMulticastStatsEntry,
       "zxAnIgmpIfMulticastTxPktRate": zxAnIgmpIfMulticastTxPktRate,
       "zxAnIgmpMgmtMVlanRecvIfTable": zxAnIgmpMgmtMVlanRecvIfTable,
       "zxAnIgmpMgmtMVlanRecvIfEntry": zxAnIgmpMgmtMVlanRecvIfEntry,
       "zxAnIgmpMgmtMVlanRecvIfRowStatus": zxAnIgmpMgmtMVlanRecvIfRowStatus,
       "zxAnIgmpMgmtGroupUserTable": zxAnIgmpMgmtGroupUserTable,
       "zxAnIgmpMgmtGroupUserEntry": zxAnIgmpMgmtGroupUserEntry,
       "zxAnIgmpUserIpAddr": zxAnIgmpUserIpAddr,
       "zxAnIgmpGrpUserSrcFilterMode": zxAnIgmpGrpUserSrcFilterMode,
       "zxAnIgmpMgmtStaticGroupUserTable": zxAnIgmpMgmtStaticGroupUserTable,
       "zxAnIgmpMgmtStaticGroupUserEntry": zxAnIgmpMgmtStaticGroupUserEntry,
       "zxAnIgmpStaticGrpUserRowStatus": zxAnIgmpStaticGrpUserRowStatus,
       "zxAnIgmpVplsMulticastObjects": zxAnIgmpVplsMulticastObjects,
       "zxAnIgmpVplsMvlanSrcPwTable": zxAnIgmpVplsMvlanSrcPwTable,
       "zxAnIgmpVplsMvlanSrcPwEntry": zxAnIgmpVplsMvlanSrcPwEntry,
       "zxAnIgmpVplsMVlanSrcPwName": zxAnIgmpVplsMVlanSrcPwName,
       "zxAnIgmpVplsMVlanSrcPwRowStatus": zxAnIgmpVplsMVlanSrcPwRowStatus,
       "zxAnMulticastStatsObjects": zxAnMulticastStatsObjects,
       "zxAnMulticastGroupStatsTable": zxAnMulticastGroupStatsTable,
       "zxAnMulticastGroupStatsEntry": zxAnMulticastGroupStatsEntry,
       "zxAnMCastGrpStatsMVid": zxAnMCastGrpStatsMVid,
       "zxAnMCastGrpStatsGroupIpType": zxAnMCastGrpStatsGroupIpType,
       "zxAnMCastGrpStatsGroupIpAddr": zxAnMCastGrpStatsGroupIpAddr,
       "zxAnMCastGrpStatsBandwidth": zxAnMCastGrpStatsBandwidth,
       "zxAnMCastGrpStatsBandwidthUnit": zxAnMCastGrpStatsBandwidthUnit,
       "zxAnMCastGrpStatsRowStatus": zxAnMCastGrpStatsRowStatus,
       "zxAnIgmpTrapObjects": zxAnIgmpTrapObjects,
       "zxAnIgmpGroupThreshExceeded": zxAnIgmpGroupThreshExceeded,
       "zxAnIgmpGroupThreshExceededCleared": zxAnIgmpGroupThreshExceededCleared,
       "zxAnIgmpPktRateLimitExceededAlm": zxAnIgmpPktRateLimitExceededAlm,
       "zxAnIgmpPktRateLimitExceededClr": zxAnIgmpPktRateLimitExceededClr}
)
