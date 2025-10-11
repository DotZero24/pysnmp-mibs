# SNMP MIB module (TPLINK-IGMPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-IGMPSNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:23 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25)
)
if mibBuilder.loadTexts:
    tplinkIgmpSnoopingMIB.setRevisions(
        ("2012-12-14 14:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIgmpSnoopingMIBObjects = _TplinkIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1)
)
_TpIgmpSnooping_ObjectIdentity = ObjectIdentity
tpIgmpSnooping = _TpIgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1)
)
_TpIgmpSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
tpIgmpSnoopingGlobalConfig = _TpIgmpSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1)
)


class _TpIgmpSnoopingEnable_Type(Integer32):
    """Custom type tpIgmpSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpSnoopingEnable_Type.__name__ = "Integer32"
_TpIgmpSnoopingEnable_Object = MibScalar
tpIgmpSnoopingEnable = _TpIgmpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 1),
    _TpIgmpSnoopingEnable_Type()
)
tpIgmpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpSnoopingEnable.setStatus("current")


class _TpIgmpSnoopingVersion_Type(Integer32):
    """Custom type tpIgmpSnoopingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 0),
          ("igmpv2", 1),
          ("igmpv3", 2))
    )


_TpIgmpSnoopingVersion_Type.__name__ = "Integer32"
_TpIgmpSnoopingVersion_Object = MibScalar
tpIgmpSnoopingVersion = _TpIgmpSnoopingVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 2),
    _TpIgmpSnoopingVersion_Type()
)
tpIgmpSnoopingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpSnoopingVersion.setStatus("current")


class _TpUnknownMulticastPacket_Type(Integer32):
    """Custom type tpUnknownMulticastPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("discard", 1))
    )


_TpUnknownMulticastPacket_Type.__name__ = "Integer32"
_TpUnknownMulticastPacket_Object = MibScalar
tpUnknownMulticastPacket = _TpUnknownMulticastPacket_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 3),
    _TpUnknownMulticastPacket_Type()
)
tpUnknownMulticastPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpUnknownMulticastPacket.setStatus("current")


class _TpIgmpHeaderValidation_Type(Integer32):
    """Custom type tpIgmpHeaderValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpHeaderValidation_Type.__name__ = "Integer32"
_TpIgmpHeaderValidation_Object = MibScalar
tpIgmpHeaderValidation = _TpIgmpHeaderValidation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 4),
    _TpIgmpHeaderValidation_Type()
)
tpIgmpHeaderValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpHeaderValidation.setStatus("current")
_TpIgmpPortConfig_ObjectIdentity = ObjectIdentity
tpIgmpPortConfig = _TpIgmpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2)
)
_TpIgmpPortTable_Object = MibTable
tpIgmpPortTable = _TpIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpIgmpPortTable.setStatus("current")
_TpIgmpPortEntry_Object = MibTableRow
tpIgmpPortEntry = _TpIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1)
)
tpIgmpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpPortEntry.setStatus("current")


class _TpIgmpSnoopingPortEnable_Type(Integer32):
    """Custom type tpIgmpSnoopingPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpSnoopingPortEnable_Type.__name__ = "Integer32"
_TpIgmpSnoopingPortEnable_Object = MibTableColumn
tpIgmpSnoopingPortEnable = _TpIgmpSnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 2),
    _TpIgmpSnoopingPortEnable_Type()
)
tpIgmpSnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpSnoopingPortEnable.setStatus("current")


class _TpIgmpFastLeavePortEnable_Type(Integer32):
    """Custom type tpIgmpFastLeavePortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpFastLeavePortEnable_Type.__name__ = "Integer32"
_TpIgmpFastLeavePortEnable_Object = MibTableColumn
tpIgmpFastLeavePortEnable = _TpIgmpFastLeavePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 3),
    _TpIgmpFastLeavePortEnable_Type()
)
tpIgmpFastLeavePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFastLeavePortEnable.setStatus("current")


class _TpIgmpPortLag_Type(OctetString):
    """Custom type tpIgmpPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpPortLag_Type.__name__ = "OctetString"
_TpIgmpPortLag_Object = MibTableColumn
tpIgmpPortLag = _TpIgmpPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 4),
    _TpIgmpPortLag_Type()
)
tpIgmpPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpPortLag.setStatus("current")
_TpIgmpVlanConfig_ObjectIdentity = ObjectIdentity
tpIgmpVlanConfig = _TpIgmpVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3)
)
_TpIgmpVlanTable_Object = MibTable
tpIgmpVlanTable = _TpIgmpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpIgmpVlanTable.setStatus("current")
_TpIgmpVlanEntry_Object = MibTableRow
tpIgmpVlanEntry = _TpIgmpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1)
)
tpIgmpVlanEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpVlanId"),
)
if mibBuilder.loadTexts:
    tpIgmpVlanEntry.setStatus("current")


class _TpIgmpVlanId_Type(Integer32):
    """Custom type tpIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpIgmpVlanId_Type.__name__ = "Integer32"
_TpIgmpVlanId_Object = MibTableColumn
tpIgmpVlanId = _TpIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 1),
    _TpIgmpVlanId_Type()
)
tpIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpVlanId.setStatus("current")


class _TpIgmpVlanEnable_Type(Integer32):
    """Custom type tpIgmpVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpVlanEnable_Type.__name__ = "Integer32"
_TpIgmpVlanEnable_Object = MibTableColumn
tpIgmpVlanEnable = _TpIgmpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 2),
    _TpIgmpVlanEnable_Type()
)
tpIgmpVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpVlanEnable.setStatus("current")


class _TpIgmpVlanFastLeave_Type(Integer32):
    """Custom type tpIgmpVlanFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpVlanFastLeave_Type.__name__ = "Integer32"
_TpIgmpVlanFastLeave_Object = MibTableColumn
tpIgmpVlanFastLeave = _TpIgmpVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 3),
    _TpIgmpVlanFastLeave_Type()
)
tpIgmpVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpVlanFastLeave.setStatus("current")


class _TpIgmpVlanReportSuppression_Type(Integer32):
    """Custom type tpIgmpVlanReportSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpVlanReportSuppression_Type.__name__ = "Integer32"
_TpIgmpVlanReportSuppression_Object = MibTableColumn
tpIgmpVlanReportSuppression = _TpIgmpVlanReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 4),
    _TpIgmpVlanReportSuppression_Type()
)
tpIgmpVlanReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpVlanReportSuppression.setStatus("current")


class _TpIgmpRouterTime_Type(Integer32):
    """Custom type tpIgmpRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpRouterTime_Type.__name__ = "Integer32"
_TpIgmpRouterTime_Object = MibTableColumn
tpIgmpRouterTime = _TpIgmpRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 5),
    _TpIgmpRouterTime_Type()
)
tpIgmpRouterTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpRouterTime.setStatus("current")


class _TpIgmpMemberTime_Type(Integer32):
    """Custom type tpIgmpMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpMemberTime_Type.__name__ = "Integer32"
_TpIgmpMemberTime_Object = MibTableColumn
tpIgmpMemberTime = _TpIgmpMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 6),
    _TpIgmpMemberTime_Type()
)
tpIgmpMemberTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpMemberTime.setStatus("current")


class _TpIgmpLeaveTime_Type(Integer32):
    """Custom type tpIgmpLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TpIgmpLeaveTime_Type.__name__ = "Integer32"
_TpIgmpLeaveTime_Object = MibTableColumn
tpIgmpLeaveTime = _TpIgmpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 7),
    _TpIgmpLeaveTime_Type()
)
tpIgmpLeaveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpLeaveTime.setStatus("current")


class _TpIgmpRouterPort_Type(OctetString):
    """Custom type tpIgmpRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpRouterPort_Type.__name__ = "OctetString"
_TpIgmpRouterPort_Object = MibTableColumn
tpIgmpRouterPort = _TpIgmpRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 8),
    _TpIgmpRouterPort_Type()
)
tpIgmpRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpRouterPort.setStatus("current")


class _TpIgmpForbiddenRouterPort_Type(OctetString):
    """Custom type tpIgmpForbiddenRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpForbiddenRouterPort_Type.__name__ = "OctetString"
_TpIgmpForbiddenRouterPort_Object = MibTableColumn
tpIgmpForbiddenRouterPort = _TpIgmpForbiddenRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 9),
    _TpIgmpForbiddenRouterPort_Type()
)
tpIgmpForbiddenRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpForbiddenRouterPort.setStatus("current")


class _TpIgmpQueryEnable_Type(Integer32):
    """Custom type tpIgmpQueryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpQueryEnable_Type.__name__ = "Integer32"
_TpIgmpQueryEnable_Object = MibTableColumn
tpIgmpQueryEnable = _TpIgmpQueryEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 10),
    _TpIgmpQueryEnable_Type()
)
tpIgmpQueryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpQueryEnable.setStatus("current")


class _TpIgmpQueryInterval_Type(Integer32):
    """Custom type tpIgmpQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TpIgmpQueryInterval_Type.__name__ = "Integer32"
_TpIgmpQueryInterval_Object = MibTableColumn
tpIgmpQueryInterval = _TpIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 11),
    _TpIgmpQueryInterval_Type()
)
tpIgmpQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpQueryInterval.setStatus("current")


class _TpIgmpQueryMaxResponseTime_Type(Integer32):
    """Custom type tpIgmpQueryMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_TpIgmpQueryMaxResponseTime_Type.__name__ = "Integer32"
_TpIgmpQueryMaxResponseTime_Object = MibTableColumn
tpIgmpQueryMaxResponseTime = _TpIgmpQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 12),
    _TpIgmpQueryMaxResponseTime_Type()
)
tpIgmpQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpQueryMaxResponseTime.setStatus("current")
_TpIgmpQueryGeneralSrcIp_Type = IpAddress
_TpIgmpQueryGeneralSrcIp_Object = MibTableColumn
tpIgmpQueryGeneralSrcIp = _TpIgmpQueryGeneralSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 13),
    _TpIgmpQueryGeneralSrcIp_Type()
)
tpIgmpQueryGeneralSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpQueryGeneralSrcIp.setStatus("current")


class _TpIgmpQueryLastMemberCount_Type(Integer32):
    """Custom type tpIgmpQueryLastMemberCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpIgmpQueryLastMemberCount_Type.__name__ = "Integer32"
_TpIgmpQueryLastMemberCount_Object = MibTableColumn
tpIgmpQueryLastMemberCount = _TpIgmpQueryLastMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 14),
    _TpIgmpQueryLastMemberCount_Type()
)
tpIgmpQueryLastMemberCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpQueryLastMemberCount.setStatus("current")


class _TpIgmpQueryLastMemberInterval_Type(Integer32):
    """Custom type tpIgmpQueryLastMemberInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpIgmpQueryLastMemberInterval_Type.__name__ = "Integer32"
_TpIgmpQueryLastMemberInterval_Object = MibTableColumn
tpIgmpQueryLastMemberInterval = _TpIgmpQueryLastMemberInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 15),
    _TpIgmpQueryLastMemberInterval_Type()
)
tpIgmpQueryLastMemberInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpQueryLastMemberInterval.setStatus("current")
_TpIgmpVlanStatus_Type = TPRowStatus
_TpIgmpVlanStatus_Object = MibTableColumn
tpIgmpVlanStatus = _TpIgmpVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 16),
    _TpIgmpVlanStatus_Type()
)
tpIgmpVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpVlanStatus.setStatus("current")
_TpIgmpFilter_ObjectIdentity = ObjectIdentity
tpIgmpFilter = _TpIgmpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2)
)
_TpIgmpPortFilterConfig_ObjectIdentity = ObjectIdentity
tpIgmpPortFilterConfig = _TpIgmpPortFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1)
)
_TpIgmpFilterPortTable_Object = MibTable
tpIgmpFilterPortTable = _TpIgmpFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpFilterPortTable.setStatus("current")
_TpIgmpFilterPortEntry_Object = MibTableRow
tpIgmpFilterPortEntry = _TpIgmpFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1)
)
tpIgmpFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpFilterPortEntry.setStatus("current")


class _TpIgmpFilterMaxGroup_Type(Integer32):
    """Custom type tpIgmpFilterMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TpIgmpFilterMaxGroup_Type.__name__ = "Integer32"
_TpIgmpFilterMaxGroup_Object = MibTableColumn
tpIgmpFilterMaxGroup = _TpIgmpFilterMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 2),
    _TpIgmpFilterMaxGroup_Type()
)
tpIgmpFilterMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFilterMaxGroup.setStatus("current")


class _TpIgmpFilterMaxGroupAction_Type(Integer32):
    """Custom type tpIgmpFilterMaxGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("replace", 1))
    )


_TpIgmpFilterMaxGroupAction_Type.__name__ = "Integer32"
_TpIgmpFilterMaxGroupAction_Object = MibTableColumn
tpIgmpFilterMaxGroupAction = _TpIgmpFilterMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 3),
    _TpIgmpFilterMaxGroupAction_Type()
)
tpIgmpFilterMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFilterMaxGroupAction.setStatus("current")


class _TpIgmpFilterBindAddrId_Type(OctetString):
    """Custom type tpIgmpFilterBindAddrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TpIgmpFilterBindAddrId_Type.__name__ = "OctetString"
_TpIgmpFilterBindAddrId_Object = MibTableColumn
tpIgmpFilterBindAddrId = _TpIgmpFilterBindAddrId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 4),
    _TpIgmpFilterBindAddrId_Type()
)
tpIgmpFilterBindAddrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFilterBindAddrId.setStatus("current")


class _TpIgmpFilterPortLag_Type(OctetString):
    """Custom type tpIgmpFilterPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpFilterPortLag_Type.__name__ = "OctetString"
_TpIgmpFilterPortLag_Object = MibTableColumn
tpIgmpFilterPortLag = _TpIgmpFilterPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 5),
    _TpIgmpFilterPortLag_Type()
)
tpIgmpFilterPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpFilterPortLag.setStatus("current")
_TpIgmpAuth_ObjectIdentity = ObjectIdentity
tpIgmpAuth = _TpIgmpAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3)
)
_TpIgmpPortAuthConfig_ObjectIdentity = ObjectIdentity
tpIgmpPortAuthConfig = _TpIgmpPortAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1)
)
_TpIgmpAuthPortTable_Object = MibTable
tpIgmpAuthPortTable = _TpIgmpAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpAuthPortTable.setStatus("current")
_TpIgmpAuthPortEntry_Object = MibTableRow
tpIgmpAuthPortEntry = _TpIgmpAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1)
)
tpIgmpAuthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpAuthPortEntry.setStatus("current")


class _TpIgmpAuthEnable_Type(Integer32):
    """Custom type tpIgmpAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpAuthEnable_Type.__name__ = "Integer32"
_TpIgmpAuthEnable_Object = MibTableColumn
tpIgmpAuthEnable = _TpIgmpAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1, 2),
    _TpIgmpAuthEnable_Type()
)
tpIgmpAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpAuthEnable.setStatus("current")


class _TpIgmpAuthPortLag_Type(OctetString):
    """Custom type tpIgmpAuthPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpAuthPortLag_Type.__name__ = "OctetString"
_TpIgmpAuthPortLag_Object = MibTableColumn
tpIgmpAuthPortLag = _TpIgmpAuthPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1, 3),
    _TpIgmpAuthPortLag_Type()
)
tpIgmpAuthPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpAuthPortLag.setStatus("current")
_TpIgmpGlobalAuthAccountConfig_ObjectIdentity = ObjectIdentity
tpIgmpGlobalAuthAccountConfig = _TpIgmpGlobalAuthAccountConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 2)
)


class _TpIgmpGlobalAuthAccountConfigEable_Type(Integer32):
    """Custom type tpIgmpGlobalAuthAccountConfigEable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpGlobalAuthAccountConfigEable_Type.__name__ = "Integer32"
_TpIgmpGlobalAuthAccountConfigEable_Object = MibScalar
tpIgmpGlobalAuthAccountConfigEable = _TpIgmpGlobalAuthAccountConfigEable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 2, 1),
    _TpIgmpGlobalAuthAccountConfigEable_Type()
)
tpIgmpGlobalAuthAccountConfigEable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpGlobalAuthAccountConfigEable.setStatus("current")
_TpIgmpPacketStatistic_ObjectIdentity = ObjectIdentity
tpIgmpPacketStatistic = _TpIgmpPacketStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4)
)
_TpIgmpPktStat_ObjectIdentity = ObjectIdentity
tpIgmpPktStat = _TpIgmpPktStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1)
)
_TpIgmpPktStatTable_Object = MibTable
tpIgmpPktStatTable = _TpIgmpPktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpPktStatTable.setStatus("current")
_TpIgmpPktStatEntry_Object = MibTableRow
tpIgmpPktStatEntry = _TpIgmpPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1)
)
tpIgmpPktStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpPktStatEntry.setStatus("current")
_TpIgmpQueryPktStat_Type = Integer32
_TpIgmpQueryPktStat_Object = MibTableColumn
tpIgmpQueryPktStat = _TpIgmpQueryPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 2),
    _TpIgmpQueryPktStat_Type()
)
tpIgmpQueryPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpQueryPktStat.setStatus("current")
_TpIgmpReportV1PktStat_Type = Integer32
_TpIgmpReportV1PktStat_Object = MibTableColumn
tpIgmpReportV1PktStat = _TpIgmpReportV1PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 3),
    _TpIgmpReportV1PktStat_Type()
)
tpIgmpReportV1PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpReportV1PktStat.setStatus("current")
_TpIgmpReportV2PktStat_Type = Integer32
_TpIgmpReportV2PktStat_Object = MibTableColumn
tpIgmpReportV2PktStat = _TpIgmpReportV2PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 4),
    _TpIgmpReportV2PktStat_Type()
)
tpIgmpReportV2PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpReportV2PktStat.setStatus("current")
_TpIgmpReportV3PktStat_Type = Integer32
_TpIgmpReportV3PktStat_Object = MibTableColumn
tpIgmpReportV3PktStat = _TpIgmpReportV3PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 5),
    _TpIgmpReportV3PktStat_Type()
)
tpIgmpReportV3PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpReportV3PktStat.setStatus("current")
_TpIgmpLeavePktStat_Type = Integer32
_TpIgmpLeavePktStat_Object = MibTableColumn
tpIgmpLeavePktStat = _TpIgmpLeavePktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 6),
    _TpIgmpLeavePktStat_Type()
)
tpIgmpLeavePktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpLeavePktStat.setStatus("current")
_TpIgmpErrorPktStat_Type = Integer32
_TpIgmpErrorPktStat_Object = MibTableColumn
tpIgmpErrorPktStat = _TpIgmpErrorPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 7),
    _TpIgmpErrorPktStat_Type()
)
tpIgmpErrorPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpErrorPktStat.setStatus("current")


class _TpIpIgmpPktStatClear_Type(Integer32):
    """Custom type tpIpIgmpPktStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_TpIpIgmpPktStatClear_Type.__name__ = "Integer32"
_TpIpIgmpPktStatClear_Object = MibScalar
tpIpIgmpPktStatClear = _TpIpIgmpPktStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 2),
    _TpIpIgmpPktStatClear_Type()
)
tpIpIgmpPktStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpIgmpPktStatClear.setStatus("current")
_TpIgmpMultigroup_ObjectIdentity = ObjectIdentity
tpIgmpMultigroup = _TpIgmpMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5)
)
_TpIgmpMulticastGroups_ObjectIdentity = ObjectIdentity
tpIgmpMulticastGroups = _TpIgmpMulticastGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1)
)
_TpIgmpMulticastGroupTable_Object = MibTable
tpIgmpMulticastGroupTable = _TpIgmpMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpMulticastGroupTable.setStatus("current")
_TpIgmpMulticastGroupEntry_Object = MibTableRow
tpIgmpMulticastGroupEntry = _TpIgmpMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1)
)
tpIgmpMulticastGroupEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpMulticastIP"),
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpVlanID"),
)
if mibBuilder.loadTexts:
    tpIgmpMulticastGroupEntry.setStatus("current")
_TpIgmpMulticastIP_Type = IpAddress
_TpIgmpMulticastIP_Object = MibTableColumn
tpIgmpMulticastIP = _TpIgmpMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 1),
    _TpIgmpMulticastIP_Type()
)
tpIgmpMulticastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpMulticastIP.setStatus("current")
_TpIgmpVlanID_Type = Integer32
_TpIgmpVlanID_Object = MibTableColumn
tpIgmpVlanID = _TpIgmpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 2),
    _TpIgmpVlanID_Type()
)
tpIgmpVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpVlanID.setStatus("current")


class _TpIgmpForwardPorts_Type(OctetString):
    """Custom type tpIgmpForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpIgmpForwardPorts_Type.__name__ = "OctetString"
_TpIgmpForwardPorts_Object = MibTableColumn
tpIgmpForwardPorts = _TpIgmpForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 3),
    _TpIgmpForwardPorts_Type()
)
tpIgmpForwardPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpForwardPorts.setStatus("current")


class _TpIgmpGrouptype_Type(Integer32):
    """Custom type tpIgmpGrouptype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_TpIgmpGrouptype_Type.__name__ = "Integer32"
_TpIgmpGrouptype_Object = MibTableColumn
tpIgmpGrouptype = _TpIgmpGrouptype_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 4),
    _TpIgmpGrouptype_Type()
)
tpIgmpGrouptype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpGrouptype.setStatus("current")
_TpIgmpStaticMultigroup_ObjectIdentity = ObjectIdentity
tpIgmpStaticMultigroup = _TpIgmpStaticMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6)
)
_TpIgmpMulticastStaticGroups_ObjectIdentity = ObjectIdentity
tpIgmpMulticastStaticGroups = _TpIgmpMulticastStaticGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1)
)
_TpIgmpMulticastStaticGroupTable_Object = MibTable
tpIgmpMulticastStaticGroupTable = _TpIgmpMulticastStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpMulticastStaticGroupTable.setStatus("current")
_TpIgmpMulticastStaticGroupEntry_Object = MibTableRow
tpIgmpMulticastStaticGroupEntry = _TpIgmpMulticastStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1)
)
tpIgmpMulticastStaticGroupEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpStaticMulticastIP"),
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpStaticVlanID"),
)
if mibBuilder.loadTexts:
    tpIgmpMulticastStaticGroupEntry.setStatus("current")
_TpIgmpStaticMulticastIP_Type = IpAddress
_TpIgmpStaticMulticastIP_Object = MibTableColumn
tpIgmpStaticMulticastIP = _TpIgmpStaticMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 1),
    _TpIgmpStaticMulticastIP_Type()
)
tpIgmpStaticMulticastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpStaticMulticastIP.setStatus("current")
_TpIgmpStaticVlanID_Type = Integer32
_TpIgmpStaticVlanID_Object = MibTableColumn
tpIgmpStaticVlanID = _TpIgmpStaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 2),
    _TpIgmpStaticVlanID_Type()
)
tpIgmpStaticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpStaticVlanID.setStatus("current")


class _TpIgmpStaticForwardPorts_Type(OctetString):
    """Custom type tpIgmpStaticForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpIgmpStaticForwardPorts_Type.__name__ = "OctetString"
_TpIgmpStaticForwardPorts_Object = MibTableColumn
tpIgmpStaticForwardPorts = _TpIgmpStaticForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 3),
    _TpIgmpStaticForwardPorts_Type()
)
tpIgmpStaticForwardPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpStaticForwardPorts.setStatus("current")
_TpIgmpStaticGroupStatus_Type = TPRowStatus
_TpIgmpStaticGroupStatus_Object = MibTableColumn
tpIgmpStaticGroupStatus = _TpIgmpStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 4),
    _TpIgmpStaticGroupStatus_Type()
)
tpIgmpStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpStaticGroupStatus.setStatus("current")
_TplinkIgmpSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkIgmpSnoopingNotifications = _TplinkIgmpSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IGMPSNOOPING-MIB",
    **{"tplinkIgmpSnoopingMIB": tplinkIgmpSnoopingMIB,
       "tplinkIgmpSnoopingMIBObjects": tplinkIgmpSnoopingMIBObjects,
       "tpIgmpSnooping": tpIgmpSnooping,
       "tpIgmpSnoopingGlobalConfig": tpIgmpSnoopingGlobalConfig,
       "tpIgmpSnoopingEnable": tpIgmpSnoopingEnable,
       "tpIgmpSnoopingVersion": tpIgmpSnoopingVersion,
       "tpUnknownMulticastPacket": tpUnknownMulticastPacket,
       "tpIgmpHeaderValidation": tpIgmpHeaderValidation,
       "tpIgmpPortConfig": tpIgmpPortConfig,
       "tpIgmpPortTable": tpIgmpPortTable,
       "tpIgmpPortEntry": tpIgmpPortEntry,
       "tpIgmpSnoopingPortEnable": tpIgmpSnoopingPortEnable,
       "tpIgmpFastLeavePortEnable": tpIgmpFastLeavePortEnable,
       "tpIgmpPortLag": tpIgmpPortLag,
       "tpIgmpVlanConfig": tpIgmpVlanConfig,
       "tpIgmpVlanTable": tpIgmpVlanTable,
       "tpIgmpVlanEntry": tpIgmpVlanEntry,
       "tpIgmpVlanId": tpIgmpVlanId,
       "tpIgmpVlanEnable": tpIgmpVlanEnable,
       "tpIgmpVlanFastLeave": tpIgmpVlanFastLeave,
       "tpIgmpVlanReportSuppression": tpIgmpVlanReportSuppression,
       "tpIgmpRouterTime": tpIgmpRouterTime,
       "tpIgmpMemberTime": tpIgmpMemberTime,
       "tpIgmpLeaveTime": tpIgmpLeaveTime,
       "tpIgmpRouterPort": tpIgmpRouterPort,
       "tpIgmpForbiddenRouterPort": tpIgmpForbiddenRouterPort,
       "tpIgmpQueryEnable": tpIgmpQueryEnable,
       "tpIgmpQueryInterval": tpIgmpQueryInterval,
       "tpIgmpQueryMaxResponseTime": tpIgmpQueryMaxResponseTime,
       "tpIgmpQueryGeneralSrcIp": tpIgmpQueryGeneralSrcIp,
       "tpIgmpQueryLastMemberCount": tpIgmpQueryLastMemberCount,
       "tpIgmpQueryLastMemberInterval": tpIgmpQueryLastMemberInterval,
       "tpIgmpVlanStatus": tpIgmpVlanStatus,
       "tpIgmpFilter": tpIgmpFilter,
       "tpIgmpPortFilterConfig": tpIgmpPortFilterConfig,
       "tpIgmpFilterPortTable": tpIgmpFilterPortTable,
       "tpIgmpFilterPortEntry": tpIgmpFilterPortEntry,
       "tpIgmpFilterMaxGroup": tpIgmpFilterMaxGroup,
       "tpIgmpFilterMaxGroupAction": tpIgmpFilterMaxGroupAction,
       "tpIgmpFilterBindAddrId": tpIgmpFilterBindAddrId,
       "tpIgmpFilterPortLag": tpIgmpFilterPortLag,
       "tpIgmpAuth": tpIgmpAuth,
       "tpIgmpPortAuthConfig": tpIgmpPortAuthConfig,
       "tpIgmpAuthPortTable": tpIgmpAuthPortTable,
       "tpIgmpAuthPortEntry": tpIgmpAuthPortEntry,
       "tpIgmpAuthEnable": tpIgmpAuthEnable,
       "tpIgmpAuthPortLag": tpIgmpAuthPortLag,
       "tpIgmpGlobalAuthAccountConfig": tpIgmpGlobalAuthAccountConfig,
       "tpIgmpGlobalAuthAccountConfigEable": tpIgmpGlobalAuthAccountConfigEable,
       "tpIgmpPacketStatistic": tpIgmpPacketStatistic,
       "tpIgmpPktStat": tpIgmpPktStat,
       "tpIgmpPktStatTable": tpIgmpPktStatTable,
       "tpIgmpPktStatEntry": tpIgmpPktStatEntry,
       "tpIgmpQueryPktStat": tpIgmpQueryPktStat,
       "tpIgmpReportV1PktStat": tpIgmpReportV1PktStat,
       "tpIgmpReportV2PktStat": tpIgmpReportV2PktStat,
       "tpIgmpReportV3PktStat": tpIgmpReportV3PktStat,
       "tpIgmpLeavePktStat": tpIgmpLeavePktStat,
       "tpIgmpErrorPktStat": tpIgmpErrorPktStat,
       "tpIpIgmpPktStatClear": tpIpIgmpPktStatClear,
       "tpIgmpMultigroup": tpIgmpMultigroup,
       "tpIgmpMulticastGroups": tpIgmpMulticastGroups,
       "tpIgmpMulticastGroupTable": tpIgmpMulticastGroupTable,
       "tpIgmpMulticastGroupEntry": tpIgmpMulticastGroupEntry,
       "tpIgmpMulticastIP": tpIgmpMulticastIP,
       "tpIgmpVlanID": tpIgmpVlanID,
       "tpIgmpForwardPorts": tpIgmpForwardPorts,
       "tpIgmpGrouptype": tpIgmpGrouptype,
       "tpIgmpStaticMultigroup": tpIgmpStaticMultigroup,
       "tpIgmpMulticastStaticGroups": tpIgmpMulticastStaticGroups,
       "tpIgmpMulticastStaticGroupTable": tpIgmpMulticastStaticGroupTable,
       "tpIgmpMulticastStaticGroupEntry": tpIgmpMulticastStaticGroupEntry,
       "tpIgmpStaticMulticastIP": tpIgmpStaticMulticastIP,
       "tpIgmpStaticVlanID": tpIgmpStaticVlanID,
       "tpIgmpStaticForwardPorts": tpIgmpStaticForwardPorts,
       "tpIgmpStaticGroupStatus": tpIgmpStaticGroupStatus,
       "tplinkIgmpSnoopingNotifications": tplinkIgmpSnoopingNotifications}
)
