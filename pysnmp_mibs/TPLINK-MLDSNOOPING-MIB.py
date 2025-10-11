# SNMP MIB module (TPLINK-MLDSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-MLDSNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:32 2025
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

tplinkMldSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43)
)
if mibBuilder.loadTexts:
    tplinkMldSnoopingMIB.setRevisions(
        ("2012-12-14 14:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkMldSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkMldSnoopingMIBObjects = _TplinkMldSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1)
)
_TpMldSnooping_ObjectIdentity = ObjectIdentity
tpMldSnooping = _TpMldSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1)
)
_TpMldSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
tpMldSnoopingGlobalConfig = _TpMldSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1)
)


class _TpMldSnoopingEnable_Type(Integer32):
    """Custom type tpMldSnoopingEnable based on Integer32"""
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


_TpMldSnoopingEnable_Type.__name__ = "Integer32"
_TpMldSnoopingEnable_Object = MibScalar
tpMldSnoopingEnable = _TpMldSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 1),
    _TpMldSnoopingEnable_Type()
)
tpMldSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldSnoopingEnable.setStatus("current")


class _TpMldUnknownMulticastPacket_Type(Integer32):
    """Custom type tpMldUnknownMulticastPacket based on Integer32"""
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


_TpMldUnknownMulticastPacket_Type.__name__ = "Integer32"
_TpMldUnknownMulticastPacket_Object = MibScalar
tpMldUnknownMulticastPacket = _TpMldUnknownMulticastPacket_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 2),
    _TpMldUnknownMulticastPacket_Type()
)
tpMldUnknownMulticastPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldUnknownMulticastPacket.setStatus("current")
_TpMldPortConfig_ObjectIdentity = ObjectIdentity
tpMldPortConfig = _TpMldPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2)
)
_TpMldPortTable_Object = MibTable
tpMldPortTable = _TpMldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpMldPortTable.setStatus("current")
_TpMldPortEntry_Object = MibTableRow
tpMldPortEntry = _TpMldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1)
)
tpMldPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMldPortEntry.setStatus("current")


class _TpMldSnoopingPortEnable_Type(Integer32):
    """Custom type tpMldSnoopingPortEnable based on Integer32"""
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


_TpMldSnoopingPortEnable_Type.__name__ = "Integer32"
_TpMldSnoopingPortEnable_Object = MibTableColumn
tpMldSnoopingPortEnable = _TpMldSnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1, 2),
    _TpMldSnoopingPortEnable_Type()
)
tpMldSnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldSnoopingPortEnable.setStatus("current")


class _TpMldFastLeavePortEnable_Type(Integer32):
    """Custom type tpMldFastLeavePortEnable based on Integer32"""
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


_TpMldFastLeavePortEnable_Type.__name__ = "Integer32"
_TpMldFastLeavePortEnable_Object = MibTableColumn
tpMldFastLeavePortEnable = _TpMldFastLeavePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1, 3),
    _TpMldFastLeavePortEnable_Type()
)
tpMldFastLeavePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFastLeavePortEnable.setStatus("current")


class _TpMldPortLag_Type(OctetString):
    """Custom type tpMldPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldPortLag_Type.__name__ = "OctetString"
_TpMldPortLag_Object = MibTableColumn
tpMldPortLag = _TpMldPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1, 4),
    _TpMldPortLag_Type()
)
tpMldPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldPortLag.setStatus("current")
_TpMldVlanConfig_ObjectIdentity = ObjectIdentity
tpMldVlanConfig = _TpMldVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3)
)
_TpMldVlanTable_Object = MibTable
tpMldVlanTable = _TpMldVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpMldVlanTable.setStatus("current")
_TpMldVlanEntry_Object = MibTableRow
tpMldVlanEntry = _TpMldVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1)
)
tpMldVlanEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldVlanId"),
)
if mibBuilder.loadTexts:
    tpMldVlanEntry.setStatus("current")


class _TpMldVlanId_Type(Integer32):
    """Custom type tpMldVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpMldVlanId_Type.__name__ = "Integer32"
_TpMldVlanId_Object = MibTableColumn
tpMldVlanId = _TpMldVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 1),
    _TpMldVlanId_Type()
)
tpMldVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldVlanId.setStatus("current")


class _TpMldVlanEnable_Type(Integer32):
    """Custom type tpMldVlanEnable based on Integer32"""
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


_TpMldVlanEnable_Type.__name__ = "Integer32"
_TpMldVlanEnable_Object = MibTableColumn
tpMldVlanEnable = _TpMldVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 2),
    _TpMldVlanEnable_Type()
)
tpMldVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldVlanEnable.setStatus("current")


class _TpMldVlanFastLeave_Type(Integer32):
    """Custom type tpMldVlanFastLeave based on Integer32"""
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


_TpMldVlanFastLeave_Type.__name__ = "Integer32"
_TpMldVlanFastLeave_Object = MibTableColumn
tpMldVlanFastLeave = _TpMldVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 3),
    _TpMldVlanFastLeave_Type()
)
tpMldVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldVlanFastLeave.setStatus("current")


class _TpMldVlanReportSuppression_Type(Integer32):
    """Custom type tpMldVlanReportSuppression based on Integer32"""
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


_TpMldVlanReportSuppression_Type.__name__ = "Integer32"
_TpMldVlanReportSuppression_Object = MibTableColumn
tpMldVlanReportSuppression = _TpMldVlanReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 4),
    _TpMldVlanReportSuppression_Type()
)
tpMldVlanReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldVlanReportSuppression.setStatus("current")


class _TpMldRouterTime_Type(Integer32):
    """Custom type tpMldRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldRouterTime_Type.__name__ = "Integer32"
_TpMldRouterTime_Object = MibTableColumn
tpMldRouterTime = _TpMldRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 5),
    _TpMldRouterTime_Type()
)
tpMldRouterTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldRouterTime.setStatus("current")


class _TpMldMemberTime_Type(Integer32):
    """Custom type tpMldMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldMemberTime_Type.__name__ = "Integer32"
_TpMldMemberTime_Object = MibTableColumn
tpMldMemberTime = _TpMldMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 6),
    _TpMldMemberTime_Type()
)
tpMldMemberTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldMemberTime.setStatus("current")


class _TpMldLeaveTime_Type(Integer32):
    """Custom type tpMldLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TpMldLeaveTime_Type.__name__ = "Integer32"
_TpMldLeaveTime_Object = MibTableColumn
tpMldLeaveTime = _TpMldLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 7),
    _TpMldLeaveTime_Type()
)
tpMldLeaveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldLeaveTime.setStatus("current")


class _TpMldRouterPort_Type(OctetString):
    """Custom type tpMldRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldRouterPort_Type.__name__ = "OctetString"
_TpMldRouterPort_Object = MibTableColumn
tpMldRouterPort = _TpMldRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 8),
    _TpMldRouterPort_Type()
)
tpMldRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldRouterPort.setStatus("current")


class _TpMldForbiddenRouterPort_Type(OctetString):
    """Custom type tpMldForbiddenRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldForbiddenRouterPort_Type.__name__ = "OctetString"
_TpMldForbiddenRouterPort_Object = MibTableColumn
tpMldForbiddenRouterPort = _TpMldForbiddenRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 9),
    _TpMldForbiddenRouterPort_Type()
)
tpMldForbiddenRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldForbiddenRouterPort.setStatus("current")


class _TpMldQueryEnable_Type(Integer32):
    """Custom type tpMldQueryEnable based on Integer32"""
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


_TpMldQueryEnable_Type.__name__ = "Integer32"
_TpMldQueryEnable_Object = MibTableColumn
tpMldQueryEnable = _TpMldQueryEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 10),
    _TpMldQueryEnable_Type()
)
tpMldQueryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldQueryEnable.setStatus("current")


class _TpMldQueryInterval_Type(Integer32):
    """Custom type tpMldQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TpMldQueryInterval_Type.__name__ = "Integer32"
_TpMldQueryInterval_Object = MibTableColumn
tpMldQueryInterval = _TpMldQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 11),
    _TpMldQueryInterval_Type()
)
tpMldQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldQueryInterval.setStatus("current")


class _TpMldQueryMaxResponseTime_Type(Integer32):
    """Custom type tpMldQueryMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_TpMldQueryMaxResponseTime_Type.__name__ = "Integer32"
_TpMldQueryMaxResponseTime_Object = MibTableColumn
tpMldQueryMaxResponseTime = _TpMldQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 12),
    _TpMldQueryMaxResponseTime_Type()
)
tpMldQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldQueryMaxResponseTime.setStatus("current")
_TpMldQueryGeneralSrcIp_Type = OctetString
_TpMldQueryGeneralSrcIp_Object = MibTableColumn
tpMldQueryGeneralSrcIp = _TpMldQueryGeneralSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 13),
    _TpMldQueryGeneralSrcIp_Type()
)
tpMldQueryGeneralSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldQueryGeneralSrcIp.setStatus("current")


class _TpMldQueryLastMemberCount_Type(Integer32):
    """Custom type tpMldQueryLastMemberCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpMldQueryLastMemberCount_Type.__name__ = "Integer32"
_TpMldQueryLastMemberCount_Object = MibTableColumn
tpMldQueryLastMemberCount = _TpMldQueryLastMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 14),
    _TpMldQueryLastMemberCount_Type()
)
tpMldQueryLastMemberCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldQueryLastMemberCount.setStatus("current")


class _TpMldQueryLastMemberInterval_Type(Integer32):
    """Custom type tpMldQueryLastMemberInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpMldQueryLastMemberInterval_Type.__name__ = "Integer32"
_TpMldQueryLastMemberInterval_Object = MibTableColumn
tpMldQueryLastMemberInterval = _TpMldQueryLastMemberInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 15),
    _TpMldQueryLastMemberInterval_Type()
)
tpMldQueryLastMemberInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldQueryLastMemberInterval.setStatus("current")
_TpMldVlanStatus_Type = TPRowStatus
_TpMldVlanStatus_Object = MibTableColumn
tpMldVlanStatus = _TpMldVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 16),
    _TpMldVlanStatus_Type()
)
tpMldVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldVlanStatus.setStatus("current")
_TpMldFilter_ObjectIdentity = ObjectIdentity
tpMldFilter = _TpMldFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2)
)
_TpMldPortFilterConfig_ObjectIdentity = ObjectIdentity
tpMldPortFilterConfig = _TpMldPortFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1)
)
_TpMldFilterPortTable_Object = MibTable
tpMldFilterPortTable = _TpMldFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldFilterPortTable.setStatus("current")
_TpMldFilterPortEntry_Object = MibTableRow
tpMldFilterPortEntry = _TpMldFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1)
)
tpMldFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMldFilterPortEntry.setStatus("current")


class _TpMldFilterMaxGroup_Type(Integer32):
    """Custom type tpMldFilterMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TpMldFilterMaxGroup_Type.__name__ = "Integer32"
_TpMldFilterMaxGroup_Object = MibTableColumn
tpMldFilterMaxGroup = _TpMldFilterMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 2),
    _TpMldFilterMaxGroup_Type()
)
tpMldFilterMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFilterMaxGroup.setStatus("current")


class _TpMldFilterMaxGroupAction_Type(Integer32):
    """Custom type tpMldFilterMaxGroupAction based on Integer32"""
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


_TpMldFilterMaxGroupAction_Type.__name__ = "Integer32"
_TpMldFilterMaxGroupAction_Object = MibTableColumn
tpMldFilterMaxGroupAction = _TpMldFilterMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 3),
    _TpMldFilterMaxGroupAction_Type()
)
tpMldFilterMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFilterMaxGroupAction.setStatus("current")


class _TpMldFilterBindAddrId_Type(OctetString):
    """Custom type tpMldFilterBindAddrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TpMldFilterBindAddrId_Type.__name__ = "OctetString"
_TpMldFilterBindAddrId_Object = MibTableColumn
tpMldFilterBindAddrId = _TpMldFilterBindAddrId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 4),
    _TpMldFilterBindAddrId_Type()
)
tpMldFilterBindAddrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFilterBindAddrId.setStatus("current")


class _TpMldFilterPortLag_Type(OctetString):
    """Custom type tpMldFilterPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldFilterPortLag_Type.__name__ = "OctetString"
_TpMldFilterPortLag_Object = MibTableColumn
tpMldFilterPortLag = _TpMldFilterPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 5),
    _TpMldFilterPortLag_Type()
)
tpMldFilterPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldFilterPortLag.setStatus("current")
_TpMldPacketStatistic_ObjectIdentity = ObjectIdentity
tpMldPacketStatistic = _TpMldPacketStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3)
)
_TpMldPktStat_ObjectIdentity = ObjectIdentity
tpMldPktStat = _TpMldPktStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1)
)
_TpMldPktStatTable_Object = MibTable
tpMldPktStatTable = _TpMldPktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldPktStatTable.setStatus("current")
_TpMldPktStatEntry_Object = MibTableRow
tpMldPktStatEntry = _TpMldPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1)
)
tpMldPktStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMldPktStatEntry.setStatus("current")
_TpMldQueryPktStat_Type = Integer32
_TpMldQueryPktStat_Object = MibTableColumn
tpMldQueryPktStat = _TpMldQueryPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 2),
    _TpMldQueryPktStat_Type()
)
tpMldQueryPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldQueryPktStat.setStatus("current")
_TpMldReportV1PktStat_Type = Integer32
_TpMldReportV1PktStat_Object = MibTableColumn
tpMldReportV1PktStat = _TpMldReportV1PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 3),
    _TpMldReportV1PktStat_Type()
)
tpMldReportV1PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldReportV1PktStat.setStatus("current")
_TpMldReportV2PktStat_Type = Integer32
_TpMldReportV2PktStat_Object = MibTableColumn
tpMldReportV2PktStat = _TpMldReportV2PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 4),
    _TpMldReportV2PktStat_Type()
)
tpMldReportV2PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldReportV2PktStat.setStatus("current")
_TpMldDonePktStat_Type = Integer32
_TpMldDonePktStat_Object = MibTableColumn
tpMldDonePktStat = _TpMldDonePktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 6),
    _TpMldDonePktStat_Type()
)
tpMldDonePktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldDonePktStat.setStatus("current")
_TpMldErrorPktStat_Type = Integer32
_TpMldErrorPktStat_Object = MibTableColumn
tpMldErrorPktStat = _TpMldErrorPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 7),
    _TpMldErrorPktStat_Type()
)
tpMldErrorPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldErrorPktStat.setStatus("current")


class _TpIpMldPktStatClear_Type(Integer32):
    """Custom type tpIpMldPktStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_TpIpMldPktStatClear_Type.__name__ = "Integer32"
_TpIpMldPktStatClear_Object = MibScalar
tpIpMldPktStatClear = _TpIpMldPktStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 2),
    _TpIpMldPktStatClear_Type()
)
tpIpMldPktStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpMldPktStatClear.setStatus("current")
_TpMldMultigroup_ObjectIdentity = ObjectIdentity
tpMldMultigroup = _TpMldMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4)
)
_TpMldMulticastGroups_ObjectIdentity = ObjectIdentity
tpMldMulticastGroups = _TpMldMulticastGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1)
)
_TpMldMulticastGroupTable_Object = MibTable
tpMldMulticastGroupTable = _TpMldMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldMulticastGroupTable.setStatus("current")
_TpMldMulticastGroupEntry_Object = MibTableRow
tpMldMulticastGroupEntry = _TpMldMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1)
)
tpMldMulticastGroupEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldMulticastIP"),
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldVlanID"),
)
if mibBuilder.loadTexts:
    tpMldMulticastGroupEntry.setStatus("current")
_TpMldMulticastIP_Type = OctetString
_TpMldMulticastIP_Object = MibTableColumn
tpMldMulticastIP = _TpMldMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 1),
    _TpMldMulticastIP_Type()
)
tpMldMulticastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldMulticastIP.setStatus("current")
_TpMldVlanID_Type = Integer32
_TpMldVlanID_Object = MibTableColumn
tpMldVlanID = _TpMldVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 2),
    _TpMldVlanID_Type()
)
tpMldVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldVlanID.setStatus("current")


class _TpMldForwardPorts_Type(OctetString):
    """Custom type tpMldForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpMldForwardPorts_Type.__name__ = "OctetString"
_TpMldForwardPorts_Object = MibTableColumn
tpMldForwardPorts = _TpMldForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 3),
    _TpMldForwardPorts_Type()
)
tpMldForwardPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldForwardPorts.setStatus("current")


class _TpMldGrouptype_Type(Integer32):
    """Custom type tpMldGrouptype based on Integer32"""
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


_TpMldGrouptype_Type.__name__ = "Integer32"
_TpMldGrouptype_Object = MibTableColumn
tpMldGrouptype = _TpMldGrouptype_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 4),
    _TpMldGrouptype_Type()
)
tpMldGrouptype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldGrouptype.setStatus("current")
_TpMldStaticMultigroup_ObjectIdentity = ObjectIdentity
tpMldStaticMultigroup = _TpMldStaticMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5)
)
_TpMldMulticastStaticGroups_ObjectIdentity = ObjectIdentity
tpMldMulticastStaticGroups = _TpMldMulticastStaticGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1)
)
_TpMldMulticastStaticGroupTable_Object = MibTable
tpMldMulticastStaticGroupTable = _TpMldMulticastStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldMulticastStaticGroupTable.setStatus("current")
_TpMldMulticastStaticGroupEntry_Object = MibTableRow
tpMldMulticastStaticGroupEntry = _TpMldMulticastStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1)
)
tpMldMulticastStaticGroupEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldStaticMulticastIP"),
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldStaticVlanID"),
)
if mibBuilder.loadTexts:
    tpMldMulticastStaticGroupEntry.setStatus("current")
_TpMldStaticMulticastIP_Type = OctetString
_TpMldStaticMulticastIP_Object = MibTableColumn
tpMldStaticMulticastIP = _TpMldStaticMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 1),
    _TpMldStaticMulticastIP_Type()
)
tpMldStaticMulticastIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticMulticastIP.setStatus("current")
_TpMldStaticVlanID_Type = Integer32
_TpMldStaticVlanID_Object = MibTableColumn
tpMldStaticVlanID = _TpMldStaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 2),
    _TpMldStaticVlanID_Type()
)
tpMldStaticVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticVlanID.setStatus("current")


class _TpMldStaticForwardPorts_Type(OctetString):
    """Custom type tpMldStaticForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpMldStaticForwardPorts_Type.__name__ = "OctetString"
_TpMldStaticForwardPorts_Object = MibTableColumn
tpMldStaticForwardPorts = _TpMldStaticForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 3),
    _TpMldStaticForwardPorts_Type()
)
tpMldStaticForwardPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticForwardPorts.setStatus("current")
_TpMldStaticGroupStatus_Type = TPRowStatus
_TpMldStaticGroupStatus_Object = MibTableColumn
tpMldStaticGroupStatus = _TpMldStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 4),
    _TpMldStaticGroupStatus_Type()
)
tpMldStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticGroupStatus.setStatus("current")
_TplinkMldSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkMldSnoopingNotifications = _TplinkMldSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-MLDSNOOPING-MIB",
    **{"tplinkMldSnoopingMIB": tplinkMldSnoopingMIB,
       "tplinkMldSnoopingMIBObjects": tplinkMldSnoopingMIBObjects,
       "tpMldSnooping": tpMldSnooping,
       "tpMldSnoopingGlobalConfig": tpMldSnoopingGlobalConfig,
       "tpMldSnoopingEnable": tpMldSnoopingEnable,
       "tpMldUnknownMulticastPacket": tpMldUnknownMulticastPacket,
       "tpMldPortConfig": tpMldPortConfig,
       "tpMldPortTable": tpMldPortTable,
       "tpMldPortEntry": tpMldPortEntry,
       "tpMldSnoopingPortEnable": tpMldSnoopingPortEnable,
       "tpMldFastLeavePortEnable": tpMldFastLeavePortEnable,
       "tpMldPortLag": tpMldPortLag,
       "tpMldVlanConfig": tpMldVlanConfig,
       "tpMldVlanTable": tpMldVlanTable,
       "tpMldVlanEntry": tpMldVlanEntry,
       "tpMldVlanId": tpMldVlanId,
       "tpMldVlanEnable": tpMldVlanEnable,
       "tpMldVlanFastLeave": tpMldVlanFastLeave,
       "tpMldVlanReportSuppression": tpMldVlanReportSuppression,
       "tpMldRouterTime": tpMldRouterTime,
       "tpMldMemberTime": tpMldMemberTime,
       "tpMldLeaveTime": tpMldLeaveTime,
       "tpMldRouterPort": tpMldRouterPort,
       "tpMldForbiddenRouterPort": tpMldForbiddenRouterPort,
       "tpMldQueryEnable": tpMldQueryEnable,
       "tpMldQueryInterval": tpMldQueryInterval,
       "tpMldQueryMaxResponseTime": tpMldQueryMaxResponseTime,
       "tpMldQueryGeneralSrcIp": tpMldQueryGeneralSrcIp,
       "tpMldQueryLastMemberCount": tpMldQueryLastMemberCount,
       "tpMldQueryLastMemberInterval": tpMldQueryLastMemberInterval,
       "tpMldVlanStatus": tpMldVlanStatus,
       "tpMldFilter": tpMldFilter,
       "tpMldPortFilterConfig": tpMldPortFilterConfig,
       "tpMldFilterPortTable": tpMldFilterPortTable,
       "tpMldFilterPortEntry": tpMldFilterPortEntry,
       "tpMldFilterMaxGroup": tpMldFilterMaxGroup,
       "tpMldFilterMaxGroupAction": tpMldFilterMaxGroupAction,
       "tpMldFilterBindAddrId": tpMldFilterBindAddrId,
       "tpMldFilterPortLag": tpMldFilterPortLag,
       "tpMldPacketStatistic": tpMldPacketStatistic,
       "tpMldPktStat": tpMldPktStat,
       "tpMldPktStatTable": tpMldPktStatTable,
       "tpMldPktStatEntry": tpMldPktStatEntry,
       "tpMldQueryPktStat": tpMldQueryPktStat,
       "tpMldReportV1PktStat": tpMldReportV1PktStat,
       "tpMldReportV2PktStat": tpMldReportV2PktStat,
       "tpMldDonePktStat": tpMldDonePktStat,
       "tpMldErrorPktStat": tpMldErrorPktStat,
       "tpIpMldPktStatClear": tpIpMldPktStatClear,
       "tpMldMultigroup": tpMldMultigroup,
       "tpMldMulticastGroups": tpMldMulticastGroups,
       "tpMldMulticastGroupTable": tpMldMulticastGroupTable,
       "tpMldMulticastGroupEntry": tpMldMulticastGroupEntry,
       "tpMldMulticastIP": tpMldMulticastIP,
       "tpMldVlanID": tpMldVlanID,
       "tpMldForwardPorts": tpMldForwardPorts,
       "tpMldGrouptype": tpMldGrouptype,
       "tpMldStaticMultigroup": tpMldStaticMultigroup,
       "tpMldMulticastStaticGroups": tpMldMulticastStaticGroups,
       "tpMldMulticastStaticGroupTable": tpMldMulticastStaticGroupTable,
       "tpMldMulticastStaticGroupEntry": tpMldMulticastStaticGroupEntry,
       "tpMldStaticMulticastIP": tpMldStaticMulticastIP,
       "tpMldStaticVlanID": tpMldStaticVlanID,
       "tpMldStaticForwardPorts": tpMldStaticForwardPorts,
       "tpMldStaticGroupStatus": tpMldStaticGroupStatus,
       "tplinkMldSnoopingNotifications": tplinkMldSnoopingNotifications}
)
