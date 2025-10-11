# SNMP MIB module (TPLINK-ACL-RULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-ACL-RULE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:06 2025
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

(tplinkAclMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-ACL-MIB",
    "tplinkAclMIBObjects")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TpAclRuleConfigure_ObjectIdentity = ObjectIdentity
tpAclRuleConfigure = _TpAclRuleConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1)
)
_TpMacRuleTable_Object = MibTable
tpMacRuleTable = _TpMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpMacRuleTable.setStatus("current")
_TpMacRuleEntry_Object = MibTableRow
tpMacRuleEntry = _TpMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1)
)
tpMacRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpMacAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpMacRuleId"),
)
if mibBuilder.loadTexts:
    tpMacRuleEntry.setStatus("current")
_TpMacAclId_Type = Integer32
_TpMacAclId_Object = MibTableColumn
tpMacAclId = _TpMacAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 1),
    _TpMacAclId_Type()
)
tpMacAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMacAclId.setStatus("current")
_TpMacRuleId_Type = Integer32
_TpMacRuleId_Object = MibTableColumn
tpMacRuleId = _TpMacRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 2),
    _TpMacRuleId_Type()
)
tpMacRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMacRuleId.setStatus("current")
_TpMacAclName_Type = OctetString
_TpMacAclName_Object = MibTableColumn
tpMacAclName = _TpMacAclName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 3),
    _TpMacAclName_Type()
)
tpMacAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacAclName.setStatus("current")


class _TpMacSecOperation_Type(Integer32):
    """Custom type tpMacSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_TpMacSecOperation_Type.__name__ = "Integer32"
_TpMacSecOperation_Object = MibTableColumn
tpMacSecOperation = _TpMacSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 4),
    _TpMacSecOperation_Type()
)
tpMacSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacSecOperation.setStatus("current")


class _TpMacCounterLogging_Type(Integer32):
    """Custom type tpMacCounterLogging based on Integer32"""
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


_TpMacCounterLogging_Type.__name__ = "Integer32"
_TpMacCounterLogging_Object = MibTableColumn
tpMacCounterLogging = _TpMacCounterLogging_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 5),
    _TpMacCounterLogging_Type()
)
tpMacCounterLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacCounterLogging.setStatus("current")
_TpMacSmacAddress_Type = OctetString
_TpMacSmacAddress_Object = MibTableColumn
tpMacSmacAddress = _TpMacSmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 6),
    _TpMacSmacAddress_Type()
)
tpMacSmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacSmacAddress.setStatus("current")
_TpMacSmacMask_Type = OctetString
_TpMacSmacMask_Object = MibTableColumn
tpMacSmacMask = _TpMacSmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 7),
    _TpMacSmacMask_Type()
)
tpMacSmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacSmacMask.setStatus("current")
_TpMacDmacAddress_Type = OctetString
_TpMacDmacAddress_Object = MibTableColumn
tpMacDmacAddress = _TpMacDmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 8),
    _TpMacDmacAddress_Type()
)
tpMacDmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacDmacAddress.setStatus("current")
_TpMacDmacMask_Type = OctetString
_TpMacDmacMask_Object = MibTableColumn
tpMacDmacMask = _TpMacDmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 9),
    _TpMacDmacMask_Type()
)
tpMacDmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacDmacMask.setStatus("current")
_TpMacVlanId_Type = Integer32
_TpMacVlanId_Object = MibTableColumn
tpMacVlanId = _TpMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 10),
    _TpMacVlanId_Type()
)
tpMacVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacVlanId.setStatus("current")
_TpMacEtherType_Type = Integer32
_TpMacEtherType_Object = MibTableColumn
tpMacEtherType = _TpMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 11),
    _TpMacEtherType_Type()
)
tpMacEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacEtherType.setStatus("current")
_TpMacPri_Type = Integer32
_TpMacPri_Object = MibTableColumn
tpMacPri = _TpMacPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 12),
    _TpMacPri_Type()
)
tpMacPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacPri.setStatus("current")
_TpMacTimeSegment_Type = OctetString
_TpMacTimeSegment_Object = MibTableColumn
tpMacTimeSegment = _TpMacTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 13),
    _TpMacTimeSegment_Type()
)
tpMacTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacTimeSegment.setStatus("current")
_TpMacRuleStatus_Type = TPRowStatus
_TpMacRuleStatus_Object = MibTableColumn
tpMacRuleStatus = _TpMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 14),
    _TpMacRuleStatus_Type()
)
tpMacRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacRuleStatus.setStatus("current")
_TpIpRuleTable_Object = MibTable
tpIpRuleTable = _TpIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpIpRuleTable.setStatus("current")
_TpIpRuleEntry_Object = MibTableRow
tpIpRuleEntry = _TpIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1)
)
tpIpRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpIpAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpIpRuleId"),
)
if mibBuilder.loadTexts:
    tpIpRuleEntry.setStatus("current")
_TpIpAclId_Type = Integer32
_TpIpAclId_Object = MibTableColumn
tpIpAclId = _TpIpAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 1),
    _TpIpAclId_Type()
)
tpIpAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpAclId.setStatus("current")
_TpIpRuleId_Type = Integer32
_TpIpRuleId_Object = MibTableColumn
tpIpRuleId = _TpIpRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 2),
    _TpIpRuleId_Type()
)
tpIpRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpRuleId.setStatus("current")
_TpIpAclName_Type = OctetString
_TpIpAclName_Object = MibTableColumn
tpIpAclName = _TpIpAclName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 3),
    _TpIpAclName_Type()
)
tpIpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpAclName.setStatus("current")


class _TpIpSecOperation_Type(Integer32):
    """Custom type tpIpSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_TpIpSecOperation_Type.__name__ = "Integer32"
_TpIpSecOperation_Object = MibTableColumn
tpIpSecOperation = _TpIpSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 4),
    _TpIpSecOperation_Type()
)
tpIpSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpSecOperation.setStatus("current")


class _TpIpCounterLogging_Type(Integer32):
    """Custom type tpIpCounterLogging based on Integer32"""
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


_TpIpCounterLogging_Type.__name__ = "Integer32"
_TpIpCounterLogging_Object = MibTableColumn
tpIpCounterLogging = _TpIpCounterLogging_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 5),
    _TpIpCounterLogging_Type()
)
tpIpCounterLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpCounterLogging.setStatus("current")


class _TpIpFragment_Type(Integer32):
    """Custom type tpIpFragment based on Integer32"""
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


_TpIpFragment_Type.__name__ = "Integer32"
_TpIpFragment_Object = MibTableColumn
tpIpFragment = _TpIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 6),
    _TpIpFragment_Type()
)
tpIpFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpFragment.setStatus("current")
_TpIpSipAddress_Type = IpAddress
_TpIpSipAddress_Object = MibTableColumn
tpIpSipAddress = _TpIpSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 7),
    _TpIpSipAddress_Type()
)
tpIpSipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpSipAddress.setStatus("current")
_TpIpSipMask_Type = IpAddress
_TpIpSipMask_Object = MibTableColumn
tpIpSipMask = _TpIpSipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 8),
    _TpIpSipMask_Type()
)
tpIpSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpSipMask.setStatus("current")
_TpIpDipAddress_Type = IpAddress
_TpIpDipAddress_Object = MibTableColumn
tpIpDipAddress = _TpIpDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 9),
    _TpIpDipAddress_Type()
)
tpIpDipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpDipAddress.setStatus("current")
_TpIpDipMask_Type = IpAddress
_TpIpDipMask_Object = MibTableColumn
tpIpDipMask = _TpIpDipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 10),
    _TpIpDipMask_Type()
)
tpIpDipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpDipMask.setStatus("current")
_TpIpProtocol_Type = Integer32
_TpIpProtocol_Object = MibTableColumn
tpIpProtocol = _TpIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 11),
    _TpIpProtocol_Type()
)
tpIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpProtocol.setStatus("current")
_TpIpTcpFlag_Type = Integer32
_TpIpTcpFlag_Object = MibTableColumn
tpIpTcpFlag = _TpIpTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 12),
    _TpIpTcpFlag_Type()
)
tpIpTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpTcpFlag.setStatus("current")
_TpIpSourcePort_Type = Integer32
_TpIpSourcePort_Object = MibTableColumn
tpIpSourcePort = _TpIpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 13),
    _TpIpSourcePort_Type()
)
tpIpSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpSourcePort.setStatus("current")
_TpIpSourcePortMask_Type = OctetString
_TpIpSourcePortMask_Object = MibTableColumn
tpIpSourcePortMask = _TpIpSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 14),
    _TpIpSourcePortMask_Type()
)
tpIpSourcePortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpSourcePortMask.setStatus("current")
_TpIpDestPort_Type = Integer32
_TpIpDestPort_Object = MibTableColumn
tpIpDestPort = _TpIpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 15),
    _TpIpDestPort_Type()
)
tpIpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpDestPort.setStatus("current")
_TpIpDestPortMask_Type = OctetString
_TpIpDestPortMask_Object = MibTableColumn
tpIpDestPortMask = _TpIpDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 16),
    _TpIpDestPortMask_Type()
)
tpIpDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpDestPortMask.setStatus("current")
_TpIpDscp_Type = Integer32
_TpIpDscp_Object = MibTableColumn
tpIpDscp = _TpIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 17),
    _TpIpDscp_Type()
)
tpIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpDscp.setStatus("current")
_TpIpTos_Type = Integer32
_TpIpTos_Object = MibTableColumn
tpIpTos = _TpIpTos_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 18),
    _TpIpTos_Type()
)
tpIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpTos.setStatus("current")
_TpIpPre_Type = Integer32
_TpIpPre_Object = MibTableColumn
tpIpPre = _TpIpPre_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 19),
    _TpIpPre_Type()
)
tpIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpPre.setStatus("current")
_TpIpTimeSegment_Type = OctetString
_TpIpTimeSegment_Object = MibTableColumn
tpIpTimeSegment = _TpIpTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 20),
    _TpIpTimeSegment_Type()
)
tpIpTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpTimeSegment.setStatus("current")
_TpIpRuleStatus_Type = TPRowStatus
_TpIpRuleStatus_Object = MibTableColumn
tpIpRuleStatus = _TpIpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 21),
    _TpIpRuleStatus_Type()
)
tpIpRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpRuleStatus.setStatus("current")
_TpCombRuleTable_Object = MibTable
tpCombRuleTable = _TpCombRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tpCombRuleTable.setStatus("current")
_TpCombRuleEntry_Object = MibTableRow
tpCombRuleEntry = _TpCombRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1)
)
tpCombRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpCombAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpCombRuleId"),
)
if mibBuilder.loadTexts:
    tpCombRuleEntry.setStatus("current")
_TpCombAclId_Type = Integer32
_TpCombAclId_Object = MibTableColumn
tpCombAclId = _TpCombAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 1),
    _TpCombAclId_Type()
)
tpCombAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCombAclId.setStatus("current")
_TpCombRuleId_Type = Integer32
_TpCombRuleId_Object = MibTableColumn
tpCombRuleId = _TpCombRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 2),
    _TpCombRuleId_Type()
)
tpCombRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCombRuleId.setStatus("current")
_TpCombAclName_Type = OctetString
_TpCombAclName_Object = MibTableColumn
tpCombAclName = _TpCombAclName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 3),
    _TpCombAclName_Type()
)
tpCombAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombAclName.setStatus("current")


class _TpCombSecOperation_Type(Integer32):
    """Custom type tpCombSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_TpCombSecOperation_Type.__name__ = "Integer32"
_TpCombSecOperation_Object = MibTableColumn
tpCombSecOperation = _TpCombSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 4),
    _TpCombSecOperation_Type()
)
tpCombSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSecOperation.setStatus("current")


class _TpCombCounterLogging_Type(Integer32):
    """Custom type tpCombCounterLogging based on Integer32"""
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


_TpCombCounterLogging_Type.__name__ = "Integer32"
_TpCombCounterLogging_Object = MibTableColumn
tpCombCounterLogging = _TpCombCounterLogging_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 5),
    _TpCombCounterLogging_Type()
)
tpCombCounterLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombCounterLogging.setStatus("current")
_TpCombSmacAddress_Type = OctetString
_TpCombSmacAddress_Object = MibTableColumn
tpCombSmacAddress = _TpCombSmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 6),
    _TpCombSmacAddress_Type()
)
tpCombSmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSmacAddress.setStatus("current")
_TpCombSmacMask_Type = OctetString
_TpCombSmacMask_Object = MibTableColumn
tpCombSmacMask = _TpCombSmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 7),
    _TpCombSmacMask_Type()
)
tpCombSmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSmacMask.setStatus("current")
_TpCombDmacAddress_Type = OctetString
_TpCombDmacAddress_Object = MibTableColumn
tpCombDmacAddress = _TpCombDmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 8),
    _TpCombDmacAddress_Type()
)
tpCombDmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDmacAddress.setStatus("current")
_TpCombDmacMask_Type = OctetString
_TpCombDmacMask_Object = MibTableColumn
tpCombDmacMask = _TpCombDmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 9),
    _TpCombDmacMask_Type()
)
tpCombDmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDmacMask.setStatus("current")
_TpCombVlanId_Type = Integer32
_TpCombVlanId_Object = MibTableColumn
tpCombVlanId = _TpCombVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 10),
    _TpCombVlanId_Type()
)
tpCombVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombVlanId.setStatus("current")
_TpCombEtherType_Type = Integer32
_TpCombEtherType_Object = MibTableColumn
tpCombEtherType = _TpCombEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 11),
    _TpCombEtherType_Type()
)
tpCombEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombEtherType.setStatus("current")
_TpCombPri_Type = Integer32
_TpCombPri_Object = MibTableColumn
tpCombPri = _TpCombPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 12),
    _TpCombPri_Type()
)
tpCombPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombPri.setStatus("current")
_TpCombSipAddress_Type = IpAddress
_TpCombSipAddress_Object = MibTableColumn
tpCombSipAddress = _TpCombSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 13),
    _TpCombSipAddress_Type()
)
tpCombSipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSipAddress.setStatus("current")
_TpCombSipMask_Type = IpAddress
_TpCombSipMask_Object = MibTableColumn
tpCombSipMask = _TpCombSipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 14),
    _TpCombSipMask_Type()
)
tpCombSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSipMask.setStatus("current")
_TpCombDipAddress_Type = IpAddress
_TpCombDipAddress_Object = MibTableColumn
tpCombDipAddress = _TpCombDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 15),
    _TpCombDipAddress_Type()
)
tpCombDipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDipAddress.setStatus("current")
_TpCombDipMask_Type = IpAddress
_TpCombDipMask_Object = MibTableColumn
tpCombDipMask = _TpCombDipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 16),
    _TpCombDipMask_Type()
)
tpCombDipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDipMask.setStatus("current")
_TpCombDscp_Type = Integer32
_TpCombDscp_Object = MibTableColumn
tpCombDscp = _TpCombDscp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 17),
    _TpCombDscp_Type()
)
tpCombDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDscp.setStatus("current")
_TpCombTos_Type = Integer32
_TpCombTos_Object = MibTableColumn
tpCombTos = _TpCombTos_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 18),
    _TpCombTos_Type()
)
tpCombTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombTos.setStatus("current")
_TpCombPre_Type = Integer32
_TpCombPre_Object = MibTableColumn
tpCombPre = _TpCombPre_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 19),
    _TpCombPre_Type()
)
tpCombPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombPre.setStatus("current")


class _TpCombFragment_Type(Integer32):
    """Custom type tpCombFragment based on Integer32"""
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


_TpCombFragment_Type.__name__ = "Integer32"
_TpCombFragment_Object = MibTableColumn
tpCombFragment = _TpCombFragment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 20),
    _TpCombFragment_Type()
)
tpCombFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombFragment.setStatus("current")
_TpCombProtocol_Type = Integer32
_TpCombProtocol_Object = MibTableColumn
tpCombProtocol = _TpCombProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 21),
    _TpCombProtocol_Type()
)
tpCombProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombProtocol.setStatus("current")
_TpCombSourcePort_Type = Integer32
_TpCombSourcePort_Object = MibTableColumn
tpCombSourcePort = _TpCombSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 22),
    _TpCombSourcePort_Type()
)
tpCombSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSourcePort.setStatus("current")
_TpCombSourcePortMask_Type = OctetString
_TpCombSourcePortMask_Object = MibTableColumn
tpCombSourcePortMask = _TpCombSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 23),
    _TpCombSourcePortMask_Type()
)
tpCombSourcePortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSourcePortMask.setStatus("current")
_TpCombDestPort_Type = Integer32
_TpCombDestPort_Object = MibTableColumn
tpCombDestPort = _TpCombDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 24),
    _TpCombDestPort_Type()
)
tpCombDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDestPort.setStatus("current")
_TpCombDestPortMask_Type = OctetString
_TpCombDestPortMask_Object = MibTableColumn
tpCombDestPortMask = _TpCombDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 25),
    _TpCombDestPortMask_Type()
)
tpCombDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDestPortMask.setStatus("current")
_TpCombTcpFlag_Type = Integer32
_TpCombTcpFlag_Object = MibTableColumn
tpCombTcpFlag = _TpCombTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 26),
    _TpCombTcpFlag_Type()
)
tpCombTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombTcpFlag.setStatus("current")
_TpCombTimeSegment_Type = OctetString
_TpCombTimeSegment_Object = MibTableColumn
tpCombTimeSegment = _TpCombTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 27),
    _TpCombTimeSegment_Type()
)
tpCombTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombTimeSegment.setStatus("current")
_TpCombRuleStatus_Type = TPRowStatus
_TpCombRuleStatus_Object = MibTableColumn
tpCombRuleStatus = _TpCombRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 28),
    _TpCombRuleStatus_Type()
)
tpCombRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombRuleStatus.setStatus("current")
_TpIPv6RuleTable_Object = MibTable
tpIPv6RuleTable = _TpIPv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tpIPv6RuleTable.setStatus("current")
_TpIPv6RuleEntry_Object = MibTableRow
tpIPv6RuleEntry = _TpIPv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1)
)
tpIPv6RuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpIPv6AclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpIPv6RuleId"),
)
if mibBuilder.loadTexts:
    tpIPv6RuleEntry.setStatus("current")
_TpIPv6AclId_Type = Integer32
_TpIPv6AclId_Object = MibTableColumn
tpIPv6AclId = _TpIPv6AclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 1),
    _TpIPv6AclId_Type()
)
tpIPv6AclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6AclId.setStatus("current")
_TpIPv6RuleId_Type = Integer32
_TpIPv6RuleId_Object = MibTableColumn
tpIPv6RuleId = _TpIPv6RuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 2),
    _TpIPv6RuleId_Type()
)
tpIPv6RuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6RuleId.setStatus("current")
_TpIPv6AclName_Type = OctetString
_TpIPv6AclName_Object = MibTableColumn
tpIPv6AclName = _TpIPv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 3),
    _TpIPv6AclName_Type()
)
tpIPv6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6AclName.setStatus("current")


class _TpIPv6SecOperation_Type(Integer32):
    """Custom type tpIPv6SecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_TpIPv6SecOperation_Type.__name__ = "Integer32"
_TpIPv6SecOperation_Object = MibTableColumn
tpIPv6SecOperation = _TpIPv6SecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 4),
    _TpIPv6SecOperation_Type()
)
tpIPv6SecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SecOperation.setStatus("current")


class _TpIPv6CounterLogging_Type(Integer32):
    """Custom type tpIPv6CounterLogging based on Integer32"""
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


_TpIPv6CounterLogging_Type.__name__ = "Integer32"
_TpIPv6CounterLogging_Object = MibTableColumn
tpIPv6CounterLogging = _TpIPv6CounterLogging_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 5),
    _TpIPv6CounterLogging_Type()
)
tpIPv6CounterLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6CounterLogging.setStatus("current")
_TpIPv6TrafficClass_Type = Integer32
_TpIPv6TrafficClass_Object = MibTableColumn
tpIPv6TrafficClass = _TpIPv6TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 6),
    _TpIPv6TrafficClass_Type()
)
tpIPv6TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6TrafficClass.setStatus("current")
_TpIPv6FlowLabel_Type = Integer32
_TpIPv6FlowLabel_Object = MibTableColumn
tpIPv6FlowLabel = _TpIPv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 7),
    _TpIPv6FlowLabel_Type()
)
tpIPv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6FlowLabel.setStatus("current")
_TpIPv6SipAddress_Type = OctetString
_TpIPv6SipAddress_Object = MibTableColumn
tpIPv6SipAddress = _TpIPv6SipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 8),
    _TpIPv6SipAddress_Type()
)
tpIPv6SipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SipAddress.setStatus("current")
_TpIPv6SipMask_Type = OctetString
_TpIPv6SipMask_Object = MibTableColumn
tpIPv6SipMask = _TpIPv6SipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 9),
    _TpIPv6SipMask_Type()
)
tpIPv6SipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SipMask.setStatus("current")
_TpIPv6DipAddress_Type = OctetString
_TpIPv6DipAddress_Object = MibTableColumn
tpIPv6DipAddress = _TpIPv6DipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 10),
    _TpIPv6DipAddress_Type()
)
tpIPv6DipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6DipAddress.setStatus("current")
_TpIPv6DipMask_Type = OctetString
_TpIPv6DipMask_Object = MibTableColumn
tpIPv6DipMask = _TpIPv6DipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 11),
    _TpIPv6DipMask_Type()
)
tpIPv6DipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6DipMask.setStatus("current")
_TpIPv6Protocol_Type = Integer32
_TpIPv6Protocol_Object = MibTableColumn
tpIPv6Protocol = _TpIPv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 12),
    _TpIPv6Protocol_Type()
)
tpIPv6Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6Protocol.setStatus("current")
_TpIPv6SourcePort_Type = Integer32
_TpIPv6SourcePort_Object = MibTableColumn
tpIPv6SourcePort = _TpIPv6SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 13),
    _TpIPv6SourcePort_Type()
)
tpIPv6SourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SourcePort.setStatus("current")
_TpIPv6DestPort_Type = Integer32
_TpIPv6DestPort_Object = MibTableColumn
tpIPv6DestPort = _TpIPv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 14),
    _TpIPv6DestPort_Type()
)
tpIPv6DestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6DestPort.setStatus("current")
_TpIPv6TimeSegment_Type = OctetString
_TpIPv6TimeSegment_Object = MibTableColumn
tpIPv6TimeSegment = _TpIPv6TimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 15),
    _TpIPv6TimeSegment_Type()
)
tpIPv6TimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6TimeSegment.setStatus("current")
_TpIPv6RuleStatus_Type = TPRowStatus
_TpIPv6RuleStatus_Object = MibTableColumn
tpIPv6RuleStatus = _TpIPv6RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 16),
    _TpIPv6RuleStatus_Type()
)
tpIPv6RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6RuleStatus.setStatus("current")
_TpPktCntntOffsetProfile_ObjectIdentity = ObjectIdentity
tpPktCntntOffsetProfile = _TpPktCntntOffsetProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5)
)
_TpPktCntntOffset0_Type = Integer32
_TpPktCntntOffset0_Object = MibScalar
tpPktCntntOffset0 = _TpPktCntntOffset0_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1),
    _TpPktCntntOffset0_Type()
)
tpPktCntntOffset0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntOffset0.setStatus("current")
_TpPktCntntOffset1_Type = Integer32
_TpPktCntntOffset1_Object = MibScalar
tpPktCntntOffset1 = _TpPktCntntOffset1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 2),
    _TpPktCntntOffset1_Type()
)
tpPktCntntOffset1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntOffset1.setStatus("current")
_TpPktCntntOffset2_Type = Integer32
_TpPktCntntOffset2_Object = MibScalar
tpPktCntntOffset2 = _TpPktCntntOffset2_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 3),
    _TpPktCntntOffset2_Type()
)
tpPktCntntOffset2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntOffset2.setStatus("current")
_TpPktCntntOffset3_Type = Integer32
_TpPktCntntOffset3_Object = MibScalar
tpPktCntntOffset3 = _TpPktCntntOffset3_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 4),
    _TpPktCntntOffset3_Type()
)
tpPktCntntOffset3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntOffset3.setStatus("current")
_TpPktCntntRuleTable_Object = MibTable
tpPktCntntRuleTable = _TpPktCntntRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tpPktCntntRuleTable.setStatus("current")
_TpPktCntntRuleEntry_Object = MibTableRow
tpPktCntntRuleEntry = _TpPktCntntRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1)
)
tpPktCntntRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpPktCntntAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpPktCntntRuleId"),
)
if mibBuilder.loadTexts:
    tpPktCntntRuleEntry.setStatus("current")
_TpPktCntntAclId_Type = Integer32
_TpPktCntntAclId_Object = MibTableColumn
tpPktCntntAclId = _TpPktCntntAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 1),
    _TpPktCntntAclId_Type()
)
tpPktCntntAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPktCntntAclId.setStatus("current")
_TpPktCntntRuleId_Type = Integer32
_TpPktCntntRuleId_Object = MibTableColumn
tpPktCntntRuleId = _TpPktCntntRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 2),
    _TpPktCntntRuleId_Type()
)
tpPktCntntRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPktCntntRuleId.setStatus("current")
_TpPktCntntAclName_Type = OctetString
_TpPktCntntAclName_Object = MibTableColumn
tpPktCntntAclName = _TpPktCntntAclName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 3),
    _TpPktCntntAclName_Type()
)
tpPktCntntAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntAclName.setStatus("current")


class _TpPktCntntSecOperation_Type(Integer32):
    """Custom type tpPktCntntSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_TpPktCntntSecOperation_Type.__name__ = "Integer32"
_TpPktCntntSecOperation_Object = MibTableColumn
tpPktCntntSecOperation = _TpPktCntntSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 4),
    _TpPktCntntSecOperation_Type()
)
tpPktCntntSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntSecOperation.setStatus("current")


class _TpPktCntntCounterLogging_Type(Integer32):
    """Custom type tpPktCntntCounterLogging based on Integer32"""
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


_TpPktCntntCounterLogging_Type.__name__ = "Integer32"
_TpPktCntntCounterLogging_Object = MibTableColumn
tpPktCntntCounterLogging = _TpPktCntntCounterLogging_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 5),
    _TpPktCntntCounterLogging_Type()
)
tpPktCntntCounterLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntCounterLogging.setStatus("current")
_TpPktCntntChunkValue0_Type = OctetString
_TpPktCntntChunkValue0_Object = MibTableColumn
tpPktCntntChunkValue0 = _TpPktCntntChunkValue0_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 6),
    _TpPktCntntChunkValue0_Type()
)
tpPktCntntChunkValue0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkValue0.setStatus("current")
_TpPktCntntChunkMask0_Type = OctetString
_TpPktCntntChunkMask0_Object = MibTableColumn
tpPktCntntChunkMask0 = _TpPktCntntChunkMask0_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 7),
    _TpPktCntntChunkMask0_Type()
)
tpPktCntntChunkMask0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkMask0.setStatus("current")
_TpPktCntntChunkValue1_Type = OctetString
_TpPktCntntChunkValue1_Object = MibTableColumn
tpPktCntntChunkValue1 = _TpPktCntntChunkValue1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 8),
    _TpPktCntntChunkValue1_Type()
)
tpPktCntntChunkValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkValue1.setStatus("current")
_TpPktCntntChunkMask1_Type = OctetString
_TpPktCntntChunkMask1_Object = MibTableColumn
tpPktCntntChunkMask1 = _TpPktCntntChunkMask1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 9),
    _TpPktCntntChunkMask1_Type()
)
tpPktCntntChunkMask1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkMask1.setStatus("current")
_TpPktCntntChunkValue2_Type = OctetString
_TpPktCntntChunkValue2_Object = MibTableColumn
tpPktCntntChunkValue2 = _TpPktCntntChunkValue2_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 10),
    _TpPktCntntChunkValue2_Type()
)
tpPktCntntChunkValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkValue2.setStatus("current")
_TpPktCntntChunkMask2_Type = OctetString
_TpPktCntntChunkMask2_Object = MibTableColumn
tpPktCntntChunkMask2 = _TpPktCntntChunkMask2_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 11),
    _TpPktCntntChunkMask2_Type()
)
tpPktCntntChunkMask2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkMask2.setStatus("current")
_TpPktCntntChunkValue3_Type = OctetString
_TpPktCntntChunkValue3_Object = MibTableColumn
tpPktCntntChunkValue3 = _TpPktCntntChunkValue3_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 12),
    _TpPktCntntChunkValue3_Type()
)
tpPktCntntChunkValue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkValue3.setStatus("current")
_TpPktCntntChunkMask3_Type = OctetString
_TpPktCntntChunkMask3_Object = MibTableColumn
tpPktCntntChunkMask3 = _TpPktCntntChunkMask3_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 13),
    _TpPktCntntChunkMask3_Type()
)
tpPktCntntChunkMask3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntChunkMask3.setStatus("current")
_TpPktCntntTimeSegment_Type = OctetString
_TpPktCntntTimeSegment_Object = MibTableColumn
tpPktCntntTimeSegment = _TpPktCntntTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 14),
    _TpPktCntntTimeSegment_Type()
)
tpPktCntntTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntTimeSegment.setStatus("current")
_TpPktCntntRuleStatus_Type = TPRowStatus
_TpPktCntntRuleStatus_Object = MibTableColumn
tpPktCntntRuleStatus = _TpPktCntntRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 6, 1, 15),
    _TpPktCntntRuleStatus_Type()
)
tpPktCntntRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPktCntntRuleStatus.setStatus("current")
_TpAclRuleCounterTable_Object = MibTable
tpAclRuleCounterTable = _TpAclRuleCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tpAclRuleCounterTable.setStatus("current")
_TpAclRuleCounterEntry_Object = MibTableRow
tpAclRuleCounterEntry = _TpAclRuleCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 7, 1)
)
tpAclRuleCounterEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpAclCounterAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpAclCounterRuleId"),
)
if mibBuilder.loadTexts:
    tpAclRuleCounterEntry.setStatus("current")
_TpAclCounterAclId_Type = Integer32
_TpAclCounterAclId_Object = MibTableColumn
tpAclCounterAclId = _TpAclCounterAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 7, 1, 1),
    _TpAclCounterAclId_Type()
)
tpAclCounterAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclCounterAclId.setStatus("current")
_TpAclCounterRuleId_Type = Integer32
_TpAclCounterRuleId_Object = MibTableColumn
tpAclCounterRuleId = _TpAclCounterRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 7, 1, 2),
    _TpAclCounterRuleId_Type()
)
tpAclCounterRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclCounterRuleId.setStatus("current")
_TpAclCounterLoggingEnable_Type = Integer32
_TpAclCounterLoggingEnable_Object = MibTableColumn
tpAclCounterLoggingEnable = _TpAclCounterLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 7, 1, 3),
    _TpAclCounterLoggingEnable_Type()
)
tpAclCounterLoggingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclCounterLoggingEnable.setStatus("current")
_TpAclCounterNum_Type = Integer32
_TpAclCounterNum_Object = MibTableColumn
tpAclCounterNum = _TpAclCounterNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 7, 1, 4),
    _TpAclCounterNum_Type()
)
tpAclCounterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclCounterNum.setStatus("current")
_TplinkAclNotifications_ObjectIdentity = ObjectIdentity
tplinkAclNotifications = _TplinkAclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2)
)

# Managed Objects groups


# Notification objects

tpAclLoggingCounter = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1)
)
tpAclLoggingCounter.setObjects(
      *(("TPLINK-ACL-RULE-MIB", "tpAclCounterAclId"),
        ("TPLINK-ACL-RULE-MIB", "tpAclCounterRuleId"),
        ("TPLINK-ACL-RULE-MIB", "tpAclCounterNum"))
)
if mibBuilder.loadTexts:
    tpAclLoggingCounter.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ACL-RULE-MIB",
    **{"tpAclRuleConfigure": tpAclRuleConfigure,
       "tpMacRuleTable": tpMacRuleTable,
       "tpMacRuleEntry": tpMacRuleEntry,
       "tpMacAclId": tpMacAclId,
       "tpMacRuleId": tpMacRuleId,
       "tpMacAclName": tpMacAclName,
       "tpMacSecOperation": tpMacSecOperation,
       "tpMacCounterLogging": tpMacCounterLogging,
       "tpMacSmacAddress": tpMacSmacAddress,
       "tpMacSmacMask": tpMacSmacMask,
       "tpMacDmacAddress": tpMacDmacAddress,
       "tpMacDmacMask": tpMacDmacMask,
       "tpMacVlanId": tpMacVlanId,
       "tpMacEtherType": tpMacEtherType,
       "tpMacPri": tpMacPri,
       "tpMacTimeSegment": tpMacTimeSegment,
       "tpMacRuleStatus": tpMacRuleStatus,
       "tpIpRuleTable": tpIpRuleTable,
       "tpIpRuleEntry": tpIpRuleEntry,
       "tpIpAclId": tpIpAclId,
       "tpIpRuleId": tpIpRuleId,
       "tpIpAclName": tpIpAclName,
       "tpIpSecOperation": tpIpSecOperation,
       "tpIpCounterLogging": tpIpCounterLogging,
       "tpIpFragment": tpIpFragment,
       "tpIpSipAddress": tpIpSipAddress,
       "tpIpSipMask": tpIpSipMask,
       "tpIpDipAddress": tpIpDipAddress,
       "tpIpDipMask": tpIpDipMask,
       "tpIpProtocol": tpIpProtocol,
       "tpIpTcpFlag": tpIpTcpFlag,
       "tpIpSourcePort": tpIpSourcePort,
       "tpIpSourcePortMask": tpIpSourcePortMask,
       "tpIpDestPort": tpIpDestPort,
       "tpIpDestPortMask": tpIpDestPortMask,
       "tpIpDscp": tpIpDscp,
       "tpIpTos": tpIpTos,
       "tpIpPre": tpIpPre,
       "tpIpTimeSegment": tpIpTimeSegment,
       "tpIpRuleStatus": tpIpRuleStatus,
       "tpCombRuleTable": tpCombRuleTable,
       "tpCombRuleEntry": tpCombRuleEntry,
       "tpCombAclId": tpCombAclId,
       "tpCombRuleId": tpCombRuleId,
       "tpCombAclName": tpCombAclName,
       "tpCombSecOperation": tpCombSecOperation,
       "tpCombCounterLogging": tpCombCounterLogging,
       "tpCombSmacAddress": tpCombSmacAddress,
       "tpCombSmacMask": tpCombSmacMask,
       "tpCombDmacAddress": tpCombDmacAddress,
       "tpCombDmacMask": tpCombDmacMask,
       "tpCombVlanId": tpCombVlanId,
       "tpCombEtherType": tpCombEtherType,
       "tpCombPri": tpCombPri,
       "tpCombSipAddress": tpCombSipAddress,
       "tpCombSipMask": tpCombSipMask,
       "tpCombDipAddress": tpCombDipAddress,
       "tpCombDipMask": tpCombDipMask,
       "tpCombDscp": tpCombDscp,
       "tpCombTos": tpCombTos,
       "tpCombPre": tpCombPre,
       "tpCombFragment": tpCombFragment,
       "tpCombProtocol": tpCombProtocol,
       "tpCombSourcePort": tpCombSourcePort,
       "tpCombSourcePortMask": tpCombSourcePortMask,
       "tpCombDestPort": tpCombDestPort,
       "tpCombDestPortMask": tpCombDestPortMask,
       "tpCombTcpFlag": tpCombTcpFlag,
       "tpCombTimeSegment": tpCombTimeSegment,
       "tpCombRuleStatus": tpCombRuleStatus,
       "tpIPv6RuleTable": tpIPv6RuleTable,
       "tpIPv6RuleEntry": tpIPv6RuleEntry,
       "tpIPv6AclId": tpIPv6AclId,
       "tpIPv6RuleId": tpIPv6RuleId,
       "tpIPv6AclName": tpIPv6AclName,
       "tpIPv6SecOperation": tpIPv6SecOperation,
       "tpIPv6CounterLogging": tpIPv6CounterLogging,
       "tpIPv6TrafficClass": tpIPv6TrafficClass,
       "tpIPv6FlowLabel": tpIPv6FlowLabel,
       "tpIPv6SipAddress": tpIPv6SipAddress,
       "tpIPv6SipMask": tpIPv6SipMask,
       "tpIPv6DipAddress": tpIPv6DipAddress,
       "tpIPv6DipMask": tpIPv6DipMask,
       "tpIPv6Protocol": tpIPv6Protocol,
       "tpIPv6SourcePort": tpIPv6SourcePort,
       "tpIPv6DestPort": tpIPv6DestPort,
       "tpIPv6TimeSegment": tpIPv6TimeSegment,
       "tpIPv6RuleStatus": tpIPv6RuleStatus,
       "tpPktCntntOffsetProfile": tpPktCntntOffsetProfile,
       "tpPktCntntOffset0": tpPktCntntOffset0,
       "tpPktCntntOffset1": tpPktCntntOffset1,
       "tpPktCntntOffset2": tpPktCntntOffset2,
       "tpPktCntntOffset3": tpPktCntntOffset3,
       "tpPktCntntRuleTable": tpPktCntntRuleTable,
       "tpPktCntntRuleEntry": tpPktCntntRuleEntry,
       "tpPktCntntAclId": tpPktCntntAclId,
       "tpPktCntntRuleId": tpPktCntntRuleId,
       "tpPktCntntAclName": tpPktCntntAclName,
       "tpPktCntntSecOperation": tpPktCntntSecOperation,
       "tpPktCntntCounterLogging": tpPktCntntCounterLogging,
       "tpPktCntntChunkValue0": tpPktCntntChunkValue0,
       "tpPktCntntChunkMask0": tpPktCntntChunkMask0,
       "tpPktCntntChunkValue1": tpPktCntntChunkValue1,
       "tpPktCntntChunkMask1": tpPktCntntChunkMask1,
       "tpPktCntntChunkValue2": tpPktCntntChunkValue2,
       "tpPktCntntChunkMask2": tpPktCntntChunkMask2,
       "tpPktCntntChunkValue3": tpPktCntntChunkValue3,
       "tpPktCntntChunkMask3": tpPktCntntChunkMask3,
       "tpPktCntntTimeSegment": tpPktCntntTimeSegment,
       "tpPktCntntRuleStatus": tpPktCntntRuleStatus,
       "tpAclRuleCounterTable": tpAclRuleCounterTable,
       "tpAclRuleCounterEntry": tpAclRuleCounterEntry,
       "tpAclCounterAclId": tpAclCounterAclId,
       "tpAclCounterRuleId": tpAclCounterRuleId,
       "tpAclCounterLoggingEnable": tpAclCounterLoggingEnable,
       "tpAclCounterNum": tpAclCounterNum,
       "tplinkAclNotifications": tplinkAclNotifications,
       "tpAclLoggingCounter": tpAclLoggingCounter}
)
