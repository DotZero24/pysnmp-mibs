# SNMP MIB module (TRDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/TRDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:25 2025
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


# MODULE-IDENTITY

iec61375p2 = ModuleIdentity(
    (1, 0, 61375, 2)
)
if mibBuilder.loadTexts:
    iec61375p2.setRevisions(
        ("2019-11-27 00:00",
         "2014-05-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Std_ObjectIdentity = ObjectIdentity
std = _Std_ObjectIdentity(
    (1, 0)
)
_Stdx61375_ObjectIdentity = ObjectIdentity
stdx61375 = _Stdx61375_ObjectIdentity(
    (1, 0, 61375)
)
_Trdp_ObjectIdentity = ObjectIdentity
trdp = _Trdp_ObjectIdentity(
    (1, 0, 61375, 2, 1)
)
_TrdpObjects_ObjectIdentity = ObjectIdentity
trdpObjects = _TrdpObjects_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1)
)
_TrdpGenInfo_ObjectIdentity = ObjectIdentity
trdpGenInfo = _TrdpGenInfo_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1, 1)
)
_TrdpGenVers_Type = Unsigned32
_TrdpGenVers_Object = MibScalar
trdpGenVers = _TrdpGenVers_Object(
    (1, 0, 61375, 2, 1, 1, 1, 1),
    _TrdpGenVers_Type()
)
trdpGenVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenVers.setStatus("current")
_TrdpGenUpTime_Type = Unsigned32
_TrdpGenUpTime_Object = MibScalar
trdpGenUpTime = _TrdpGenUpTime_Object(
    (1, 0, 61375, 2, 1, 1, 1, 2),
    _TrdpGenUpTime_Type()
)
trdpGenUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenUpTime.setStatus("current")
_TrdpGenStatTime_Type = Unsigned32
_TrdpGenStatTime_Object = MibScalar
trdpGenStatTime = _TrdpGenStatTime_Object(
    (1, 0, 61375, 2, 1, 1, 1, 3),
    _TrdpGenStatTime_Type()
)
trdpGenStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenStatTime.setStatus("current")


class _TrdpGenHostName_Type(OctetString):
    """Custom type trdpGenHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TrdpGenHostName_Type.__name__ = "OctetString"
_TrdpGenHostName_Object = MibScalar
trdpGenHostName = _TrdpGenHostName_Object(
    (1, 0, 61375, 2, 1, 1, 1, 4),
    _TrdpGenHostName_Type()
)
trdpGenHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenHostName.setStatus("current")


class _TrdpGenLeadName_Type(OctetString):
    """Custom type trdpGenLeadName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TrdpGenLeadName_Type.__name__ = "OctetString"
_TrdpGenLeadName_Object = MibScalar
trdpGenLeadName = _TrdpGenLeadName_Object(
    (1, 0, 61375, 2, 1, 1, 1, 5),
    _TrdpGenLeadName_Type()
)
trdpGenLeadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenLeadName.setStatus("current")
_TrdpGenOwnIp_Type = IpAddress
_TrdpGenOwnIp_Object = MibScalar
trdpGenOwnIp = _TrdpGenOwnIp_Object(
    (1, 0, 61375, 2, 1, 1, 1, 6),
    _TrdpGenOwnIp_Type()
)
trdpGenOwnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenOwnIp.setStatus("current")
_TrdpGenLeadIp_Type = IpAddress
_TrdpGenLeadIp_Object = MibScalar
trdpGenLeadIp = _TrdpGenLeadIp_Object(
    (1, 0, 61375, 2, 1, 1, 1, 7),
    _TrdpGenLeadIp_Type()
)
trdpGenLeadIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenLeadIp.setStatus("current")
_TrdpGenProcPrio_Type = Unsigned32
_TrdpGenProcPrio_Object = MibScalar
trdpGenProcPrio = _TrdpGenProcPrio_Object(
    (1, 0, 61375, 2, 1, 1, 1, 8),
    _TrdpGenProcPrio_Type()
)
trdpGenProcPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenProcPrio.setStatus("current")
_TrdpGenProcCycle_Type = Unsigned32
_TrdpGenProcCycle_Object = MibScalar
trdpGenProcCycle = _TrdpGenProcCycle_Object(
    (1, 0, 61375, 2, 1, 1, 1, 9),
    _TrdpGenProcCycle_Type()
)
trdpGenProcCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenProcCycle.setStatus("current")
_TrdpGenNumJoin_Type = Unsigned32
_TrdpGenNumJoin_Object = MibScalar
trdpGenNumJoin = _TrdpGenNumJoin_Object(
    (1, 0, 61375, 2, 1, 1, 1, 10),
    _TrdpGenNumJoin_Type()
)
trdpGenNumJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenNumJoin.setStatus("current")
_TrdpGenNumRed_Type = Unsigned32
_TrdpGenNumRed_Object = MibScalar
trdpGenNumRed = _TrdpGenNumRed_Object(
    (1, 0, 61375, 2, 1, 1, 1, 11),
    _TrdpGenNumRed_Type()
)
trdpGenNumRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpGenNumRed.setStatus("current")
_TrdpMemStat_ObjectIdentity = ObjectIdentity
trdpMemStat = _TrdpMemStat_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1, 2)
)
_TrdpMemTotal_Type = Unsigned32
_TrdpMemTotal_Object = MibScalar
trdpMemTotal = _TrdpMemTotal_Object(
    (1, 0, 61375, 2, 1, 1, 2, 1),
    _TrdpMemTotal_Type()
)
trdpMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMemTotal.setStatus("current")
_TrdpMemFree_Type = Unsigned32
_TrdpMemFree_Object = MibScalar
trdpMemFree = _TrdpMemFree_Object(
    (1, 0, 61375, 2, 1, 1, 2, 2),
    _TrdpMemFree_Type()
)
trdpMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMemFree.setStatus("current")
_TrdpMemMinFree_Type = Unsigned32
_TrdpMemMinFree_Object = MibScalar
trdpMemMinFree = _TrdpMemMinFree_Object(
    (1, 0, 61375, 2, 1, 1, 2, 3),
    _TrdpMemMinFree_Type()
)
trdpMemMinFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMemMinFree.setStatus("current")
_TrdpMemAllocBlocks_Type = Unsigned32
_TrdpMemAllocBlocks_Object = MibScalar
trdpMemAllocBlocks = _TrdpMemAllocBlocks_Object(
    (1, 0, 61375, 2, 1, 1, 2, 4),
    _TrdpMemAllocBlocks_Type()
)
trdpMemAllocBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMemAllocBlocks.setStatus("current")
_TrdpMemAllocErr_Type = Unsigned32
_TrdpMemAllocErr_Object = MibScalar
trdpMemAllocErr = _TrdpMemAllocErr_Object(
    (1, 0, 61375, 2, 1, 1, 2, 5),
    _TrdpMemAllocErr_Type()
)
trdpMemAllocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMemAllocErr.setStatus("current")
_TrdpMemFreeErr_Type = Unsigned32
_TrdpMemFreeErr_Object = MibScalar
trdpMemFreeErr = _TrdpMemFreeErr_Object(
    (1, 0, 61375, 2, 1, 1, 2, 6),
    _TrdpMemFreeErr_Type()
)
trdpMemFreeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMemFreeErr.setStatus("current")
_TrdpPdStat_ObjectIdentity = ObjectIdentity
trdpPdStat = _TrdpPdStat_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1, 3)
)
_TrdpPdDefQos_Type = Unsigned32
_TrdpPdDefQos_Object = MibScalar
trdpPdDefQos = _TrdpPdDefQos_Object(
    (1, 0, 61375, 2, 1, 1, 3, 1),
    _TrdpPdDefQos_Type()
)
trdpPdDefQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdDefQos.setStatus("current")
_TrdpPdDefTtl_Type = Unsigned32
_TrdpPdDefTtl_Object = MibScalar
trdpPdDefTtl = _TrdpPdDefTtl_Object(
    (1, 0, 61375, 2, 1, 1, 3, 2),
    _TrdpPdDefTtl_Type()
)
trdpPdDefTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdDefTtl.setStatus("current")
_TrdpPdDefTo_Type = Unsigned32
_TrdpPdDefTo_Object = MibScalar
trdpPdDefTo = _TrdpPdDefTo_Object(
    (1, 0, 61375, 2, 1, 1, 3, 3),
    _TrdpPdDefTo_Type()
)
trdpPdDefTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdDefTo.setStatus("current")
_TrdpPdNumSubs_Type = Unsigned32
_TrdpPdNumSubs_Object = MibScalar
trdpPdNumSubs = _TrdpPdNumSubs_Object(
    (1, 0, 61375, 2, 1, 1, 3, 4),
    _TrdpPdNumSubs_Type()
)
trdpPdNumSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumSubs.setStatus("current")
_TrdpPdNumPub_Type = Unsigned32
_TrdpPdNumPub_Object = MibScalar
trdpPdNumPub = _TrdpPdNumPub_Object(
    (1, 0, 61375, 2, 1, 1, 3, 5),
    _TrdpPdNumPub_Type()
)
trdpPdNumPub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumPub.setStatus("current")
_TrdpPdNumRcv_Type = Unsigned32
_TrdpPdNumRcv_Object = MibScalar
trdpPdNumRcv = _TrdpPdNumRcv_Object(
    (1, 0, 61375, 2, 1, 1, 3, 6),
    _TrdpPdNumRcv_Type()
)
trdpPdNumRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumRcv.setStatus("current")
_TrdpPdNumCrcErr_Type = Unsigned32
_TrdpPdNumCrcErr_Object = MibScalar
trdpPdNumCrcErr = _TrdpPdNumCrcErr_Object(
    (1, 0, 61375, 2, 1, 1, 3, 7),
    _TrdpPdNumCrcErr_Type()
)
trdpPdNumCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumCrcErr.setStatus("current")
_TrdpPdNumProtErr_Type = Unsigned32
_TrdpPdNumProtErr_Object = MibScalar
trdpPdNumProtErr = _TrdpPdNumProtErr_Object(
    (1, 0, 61375, 2, 1, 1, 3, 8),
    _TrdpPdNumProtErr_Type()
)
trdpPdNumProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumProtErr.setStatus("current")
_TrdpPdNumTopoErr_Type = Unsigned32
_TrdpPdNumTopoErr_Object = MibScalar
trdpPdNumTopoErr = _TrdpPdNumTopoErr_Object(
    (1, 0, 61375, 2, 1, 1, 3, 9),
    _TrdpPdNumTopoErr_Type()
)
trdpPdNumTopoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumTopoErr.setStatus("current")
_TrdpPdNumNoSubs_Type = Unsigned32
_TrdpPdNumNoSubs_Object = MibScalar
trdpPdNumNoSubs = _TrdpPdNumNoSubs_Object(
    (1, 0, 61375, 2, 1, 1, 3, 10),
    _TrdpPdNumNoSubs_Type()
)
trdpPdNumNoSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumNoSubs.setStatus("current")
_TrdpPdNumNoPub_Type = Unsigned32
_TrdpPdNumNoPub_Object = MibScalar
trdpPdNumNoPub = _TrdpPdNumNoPub_Object(
    (1, 0, 61375, 2, 1, 1, 3, 11),
    _TrdpPdNumNoPub_Type()
)
trdpPdNumNoPub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumNoPub.setStatus("current")
_TrdpPdNumTo_Type = Unsigned32
_TrdpPdNumTo_Object = MibScalar
trdpPdNumTo = _TrdpPdNumTo_Object(
    (1, 0, 61375, 2, 1, 1, 3, 12),
    _TrdpPdNumTo_Type()
)
trdpPdNumTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumTo.setStatus("current")
_TrdpPdNumSend_Type = Unsigned32
_TrdpPdNumSend_Object = MibScalar
trdpPdNumSend = _TrdpPdNumSend_Object(
    (1, 0, 61375, 2, 1, 1, 3, 13),
    _TrdpPdNumSend_Type()
)
trdpPdNumSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpPdNumSend.setStatus("current")
_TrdpMduStat_ObjectIdentity = ObjectIdentity
trdpMduStat = _TrdpMduStat_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1, 4)
)
_TrdpMduDefQos_Type = Unsigned32
_TrdpMduDefQos_Object = MibScalar
trdpMduDefQos = _TrdpMduDefQos_Object(
    (1, 0, 61375, 2, 1, 1, 4, 1),
    _TrdpMduDefQos_Type()
)
trdpMduDefQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduDefQos.setStatus("current")
_TrdpMduDefTtl_Type = Unsigned32
_TrdpMduDefTtl_Object = MibScalar
trdpMduDefTtl = _TrdpMduDefTtl_Object(
    (1, 0, 61375, 2, 1, 1, 4, 2),
    _TrdpMduDefTtl_Type()
)
trdpMduDefTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduDefTtl.setStatus("current")
_TrdpMduDefReplyTo_Type = Unsigned32
_TrdpMduDefReplyTo_Object = MibScalar
trdpMduDefReplyTo = _TrdpMduDefReplyTo_Object(
    (1, 0, 61375, 2, 1, 1, 4, 3),
    _TrdpMduDefReplyTo_Type()
)
trdpMduDefReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduDefReplyTo.setStatus("current")
_TrdpMduDefConfTo_Type = Unsigned32
_TrdpMduDefConfTo_Object = MibScalar
trdpMduDefConfTo = _TrdpMduDefConfTo_Object(
    (1, 0, 61375, 2, 1, 1, 4, 4),
    _TrdpMduDefConfTo_Type()
)
trdpMduDefConfTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduDefConfTo.setStatus("current")
_TrdpMduNumList_Type = Unsigned32
_TrdpMduNumList_Object = MibScalar
trdpMduNumList = _TrdpMduNumList_Object(
    (1, 0, 61375, 2, 1, 1, 4, 5),
    _TrdpMduNumList_Type()
)
trdpMduNumList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumList.setStatus("current")
_TrdpMduNumRcv_Type = Unsigned32
_TrdpMduNumRcv_Object = MibScalar
trdpMduNumRcv = _TrdpMduNumRcv_Object(
    (1, 0, 61375, 2, 1, 1, 4, 6),
    _TrdpMduNumRcv_Type()
)
trdpMduNumRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumRcv.setStatus("current")
_TrdpMduNumCrcErr_Type = Unsigned32
_TrdpMduNumCrcErr_Object = MibScalar
trdpMduNumCrcErr = _TrdpMduNumCrcErr_Object(
    (1, 0, 61375, 2, 1, 1, 4, 7),
    _TrdpMduNumCrcErr_Type()
)
trdpMduNumCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumCrcErr.setStatus("current")
_TrdpMduNumProtErr_Type = Unsigned32
_TrdpMduNumProtErr_Object = MibScalar
trdpMduNumProtErr = _TrdpMduNumProtErr_Object(
    (1, 0, 61375, 2, 1, 1, 4, 8),
    _TrdpMduNumProtErr_Type()
)
trdpMduNumProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumProtErr.setStatus("current")
_TrdpMduNumTopoErr_Type = Unsigned32
_TrdpMduNumTopoErr_Object = MibScalar
trdpMduNumTopoErr = _TrdpMduNumTopoErr_Object(
    (1, 0, 61375, 2, 1, 1, 4, 9),
    _TrdpMduNumTopoErr_Type()
)
trdpMduNumTopoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumTopoErr.setStatus("current")
_TrdpMduNumNoList_Type = Unsigned32
_TrdpMduNumNoList_Object = MibScalar
trdpMduNumNoList = _TrdpMduNumNoList_Object(
    (1, 0, 61375, 2, 1, 1, 4, 10),
    _TrdpMduNumNoList_Type()
)
trdpMduNumNoList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumNoList.setStatus("current")
_TrdpMduNumReplyTo_Type = Unsigned32
_TrdpMduNumReplyTo_Object = MibScalar
trdpMduNumReplyTo = _TrdpMduNumReplyTo_Object(
    (1, 0, 61375, 2, 1, 1, 4, 11),
    _TrdpMduNumReplyTo_Type()
)
trdpMduNumReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumReplyTo.setStatus("current")
_TrdpMduNumConfTo_Type = Unsigned32
_TrdpMduNumConfTo_Object = MibScalar
trdpMduNumConfTo = _TrdpMduNumConfTo_Object(
    (1, 0, 61375, 2, 1, 1, 4, 12),
    _TrdpMduNumConfTo_Type()
)
trdpMduNumConfTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumConfTo.setStatus("current")
_TrdpMduNumSend_Type = Unsigned32
_TrdpMduNumSend_Object = MibScalar
trdpMduNumSend = _TrdpMduNumSend_Object(
    (1, 0, 61375, 2, 1, 1, 4, 13),
    _TrdpMduNumSend_Type()
)
trdpMduNumSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMduNumSend.setStatus("current")
_TrdpMdtStat_ObjectIdentity = ObjectIdentity
trdpMdtStat = _TrdpMdtStat_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1, 5)
)
_TrdpMdtDefQos_Type = Unsigned32
_TrdpMdtDefQos_Object = MibScalar
trdpMdtDefQos = _TrdpMdtDefQos_Object(
    (1, 0, 61375, 2, 1, 1, 5, 1),
    _TrdpMdtDefQos_Type()
)
trdpMdtDefQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtDefQos.setStatus("current")
_TrdpMdtDefTtl_Type = Unsigned32
_TrdpMdtDefTtl_Object = MibScalar
trdpMdtDefTtl = _TrdpMdtDefTtl_Object(
    (1, 0, 61375, 2, 1, 1, 5, 2),
    _TrdpMdtDefTtl_Type()
)
trdpMdtDefTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtDefTtl.setStatus("current")
_TrdpMdtDefReplyTo_Type = Unsigned32
_TrdpMdtDefReplyTo_Object = MibScalar
trdpMdtDefReplyTo = _TrdpMdtDefReplyTo_Object(
    (1, 0, 61375, 2, 1, 1, 5, 3),
    _TrdpMdtDefReplyTo_Type()
)
trdpMdtDefReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtDefReplyTo.setStatus("current")
_TrdpMdtDefConfTo_Type = Unsigned32
_TrdpMdtDefConfTo_Object = MibScalar
trdpMdtDefConfTo = _TrdpMdtDefConfTo_Object(
    (1, 0, 61375, 2, 1, 1, 5, 4),
    _TrdpMdtDefConfTo_Type()
)
trdpMdtDefConfTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtDefConfTo.setStatus("current")
_TrdpMdtNumList_Type = Unsigned32
_TrdpMdtNumList_Object = MibScalar
trdpMdtNumList = _TrdpMdtNumList_Object(
    (1, 0, 61375, 2, 1, 1, 5, 5),
    _TrdpMdtNumList_Type()
)
trdpMdtNumList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumList.setStatus("current")
_TrdpMdtNumRcv_Type = Unsigned32
_TrdpMdtNumRcv_Object = MibScalar
trdpMdtNumRcv = _TrdpMdtNumRcv_Object(
    (1, 0, 61375, 2, 1, 1, 5, 6),
    _TrdpMdtNumRcv_Type()
)
trdpMdtNumRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumRcv.setStatus("current")
_TrdpMdtNumCrcErr_Type = Unsigned32
_TrdpMdtNumCrcErr_Object = MibScalar
trdpMdtNumCrcErr = _TrdpMdtNumCrcErr_Object(
    (1, 0, 61375, 2, 1, 1, 5, 7),
    _TrdpMdtNumCrcErr_Type()
)
trdpMdtNumCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumCrcErr.setStatus("current")
_TrdpMdtNumProtErr_Type = Unsigned32
_TrdpMdtNumProtErr_Object = MibScalar
trdpMdtNumProtErr = _TrdpMdtNumProtErr_Object(
    (1, 0, 61375, 2, 1, 1, 5, 8),
    _TrdpMdtNumProtErr_Type()
)
trdpMdtNumProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumProtErr.setStatus("current")
_TrdpMdtNumTopoErr_Type = Unsigned32
_TrdpMdtNumTopoErr_Object = MibScalar
trdpMdtNumTopoErr = _TrdpMdtNumTopoErr_Object(
    (1, 0, 61375, 2, 1, 1, 5, 9),
    _TrdpMdtNumTopoErr_Type()
)
trdpMdtNumTopoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumTopoErr.setStatus("current")
_TrdpMdtNumNoList_Type = Unsigned32
_TrdpMdtNumNoList_Object = MibScalar
trdpMdtNumNoList = _TrdpMdtNumNoList_Object(
    (1, 0, 61375, 2, 1, 1, 5, 10),
    _TrdpMdtNumNoList_Type()
)
trdpMdtNumNoList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumNoList.setStatus("current")
_TrdpMdtNumReplyTo_Type = Unsigned32
_TrdpMdtNumReplyTo_Object = MibScalar
trdpMdtNumReplyTo = _TrdpMdtNumReplyTo_Object(
    (1, 0, 61375, 2, 1, 1, 5, 11),
    _TrdpMdtNumReplyTo_Type()
)
trdpMdtNumReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumReplyTo.setStatus("current")
_TrdpMdtNumConfTo_Type = Unsigned32
_TrdpMdtNumConfTo_Object = MibScalar
trdpMdtNumConfTo = _TrdpMdtNumConfTo_Object(
    (1, 0, 61375, 2, 1, 1, 5, 12),
    _TrdpMdtNumConfTo_Type()
)
trdpMdtNumConfTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumConfTo.setStatus("current")
_TrdpMdtNumSend_Type = Unsigned32
_TrdpMdtNumSend_Object = MibScalar
trdpMdtNumSend = _TrdpMdtNumSend_Object(
    (1, 0, 61375, 2, 1, 1, 5, 13),
    _TrdpMdtNumSend_Type()
)
trdpMdtNumSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpMdtNumSend.setStatus("current")
_TrdpRedStat_ObjectIdentity = ObjectIdentity
trdpRedStat = _TrdpRedStat_ObjectIdentity(
    (1, 0, 61375, 2, 1, 1, 6)
)
_TrdpRedId_Type = Unsigned32
_TrdpRedId_Object = MibScalar
trdpRedId = _TrdpRedId_Object(
    (1, 0, 61375, 2, 1, 1, 6, 1),
    _TrdpRedId_Type()
)
trdpRedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpRedId.setStatus("current")
_TrdpRedState_Type = Unsigned32
_TrdpRedState_Object = MibScalar
trdpRedState = _TrdpRedState_Object(
    (1, 0, 61375, 2, 1, 1, 6, 2),
    _TrdpRedState_Type()
)
trdpRedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdpRedState.setStatus("current")
_TrdpConformance_ObjectIdentity = ObjectIdentity
trdpConformance = _TrdpConformance_ObjectIdentity(
    (1, 0, 61375, 2, 1, 2)
)

# Managed Objects groups

trdpGenGroup = ObjectGroup(
    (1, 0, 61375, 2, 1, 2, 2)
)
trdpGenGroup.setObjects(
      *(("TRDP-MIB", "trdpGenVers"),
        ("TRDP-MIB", "trdpGenUpTime"),
        ("TRDP-MIB", "trdpGenStatTime"),
        ("TRDP-MIB", "trdpGenHostName"),
        ("TRDP-MIB", "trdpGenLeadName"),
        ("TRDP-MIB", "trdpGenOwnIp"),
        ("TRDP-MIB", "trdpGenLeadIp"),
        ("TRDP-MIB", "trdpGenProcPrio"),
        ("TRDP-MIB", "trdpGenProcCycle"),
        ("TRDP-MIB", "trdpGenNumJoin"),
        ("TRDP-MIB", "trdpGenNumRed"))
)
if mibBuilder.loadTexts:
    trdpGenGroup.setStatus("current")

trdpMemGroup = ObjectGroup(
    (1, 0, 61375, 2, 1, 2, 3)
)
trdpMemGroup.setObjects(
      *(("TRDP-MIB", "trdpMemTotal"),
        ("TRDP-MIB", "trdpMemFree"),
        ("TRDP-MIB", "trdpMemMinFree"),
        ("TRDP-MIB", "trdpMemAllocBlocks"),
        ("TRDP-MIB", "trdpMemAllocErr"),
        ("TRDP-MIB", "trdpMemFreeErr"),
        ("TRDP-MIB", "trdpMemFreeErr"))
)
if mibBuilder.loadTexts:
    trdpMemGroup.setStatus("current")

trdpPdGroup = ObjectGroup(
    (1, 0, 61375, 2, 1, 2, 4)
)
trdpPdGroup.setObjects(
      *(("TRDP-MIB", "trdpPdDefQos"),
        ("TRDP-MIB", "trdpPdDefTtl"),
        ("TRDP-MIB", "trdpPdDefTo"),
        ("TRDP-MIB", "trdpPdNumSubs"),
        ("TRDP-MIB", "trdpPdNumPub"),
        ("TRDP-MIB", "trdpPdNumRcv"),
        ("TRDP-MIB", "trdpPdNumCrcErr"),
        ("TRDP-MIB", "trdpPdNumProtErr"),
        ("TRDP-MIB", "trdpPdNumTopoErr"),
        ("TRDP-MIB", "trdpPdNumNoSubs"),
        ("TRDP-MIB", "trdpPdNumNoPub"),
        ("TRDP-MIB", "trdpPdNumTo"),
        ("TRDP-MIB", "trdpPdNumSend"))
)
if mibBuilder.loadTexts:
    trdpPdGroup.setStatus("current")

trdpMduGroup = ObjectGroup(
    (1, 0, 61375, 2, 1, 2, 5)
)
trdpMduGroup.setObjects(
      *(("TRDP-MIB", "trdpMduDefQos"),
        ("TRDP-MIB", "trdpMduDefTtl"),
        ("TRDP-MIB", "trdpMduDefReplyTo"),
        ("TRDP-MIB", "trdpMduDefConfTo"),
        ("TRDP-MIB", "trdpMduNumList"),
        ("TRDP-MIB", "trdpMduNumRcv"),
        ("TRDP-MIB", "trdpMduNumCrcErr"),
        ("TRDP-MIB", "trdpMduNumProtErr"),
        ("TRDP-MIB", "trdpMduNumTopoErr"),
        ("TRDP-MIB", "trdpMduNumReplyTo"),
        ("TRDP-MIB", "trdpMduNumNoList"),
        ("TRDP-MIB", "trdpMduNumConfTo"),
        ("TRDP-MIB", "trdpMduNumSend"))
)
if mibBuilder.loadTexts:
    trdpMduGroup.setStatus("current")

trdpMdtGroup = ObjectGroup(
    (1, 0, 61375, 2, 1, 2, 6)
)
trdpMdtGroup.setObjects(
      *(("TRDP-MIB", "trdpMdtDefQos"),
        ("TRDP-MIB", "trdpMdtDefTtl"),
        ("TRDP-MIB", "trdpMdtDefReplyTo"),
        ("TRDP-MIB", "trdpMdtDefConfTo"),
        ("TRDP-MIB", "trdpMdtNumList"),
        ("TRDP-MIB", "trdpMdtNumRcv"),
        ("TRDP-MIB", "trdpMdtNumCrcErr"),
        ("TRDP-MIB", "trdpMdtNumProtErr"),
        ("TRDP-MIB", "trdpMdtNumTopoErr"),
        ("TRDP-MIB", "trdpMdtNumReplyTo"),
        ("TRDP-MIB", "trdpMdtNumNoList"),
        ("TRDP-MIB", "trdpMdtNumConfTo"),
        ("TRDP-MIB", "trdpMdtNumSend"))
)
if mibBuilder.loadTexts:
    trdpMdtGroup.setStatus("current")

trdpRedGroup = ObjectGroup(
    (1, 0, 61375, 2, 1, 2, 7)
)
trdpRedGroup.setObjects(
      *(("TRDP-MIB", "trdpRedId"),
        ("TRDP-MIB", "trdpRedState"))
)
if mibBuilder.loadTexts:
    trdpRedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trdpBasicCompliance = ModuleCompliance(
    (1, 0, 61375, 2, 1, 2, 8)
)
trdpBasicCompliance.setObjects(
      *(("TRDP-MIB", "trdpGenGroup"),
        ("TRDP-MIB", "trdpMemGroup"),
        ("TRDP-MIB", "trdpPdGroup"),
        ("TRDP-MIB", "trdpMduGroup"),
        ("TRDP-MIB", "trdpMdtGroup"),
        ("TRDP-MIB", "trdpRedGroup"))
)
if mibBuilder.loadTexts:
    trdpBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRDP-MIB",
    **{"std": std,
       "stdx61375": stdx61375,
       "iec61375p2": iec61375p2,
       "trdp": trdp,
       "trdpObjects": trdpObjects,
       "trdpGenInfo": trdpGenInfo,
       "trdpGenVers": trdpGenVers,
       "trdpGenUpTime": trdpGenUpTime,
       "trdpGenStatTime": trdpGenStatTime,
       "trdpGenHostName": trdpGenHostName,
       "trdpGenLeadName": trdpGenLeadName,
       "trdpGenOwnIp": trdpGenOwnIp,
       "trdpGenLeadIp": trdpGenLeadIp,
       "trdpGenProcPrio": trdpGenProcPrio,
       "trdpGenProcCycle": trdpGenProcCycle,
       "trdpGenNumJoin": trdpGenNumJoin,
       "trdpGenNumRed": trdpGenNumRed,
       "trdpMemStat": trdpMemStat,
       "trdpMemTotal": trdpMemTotal,
       "trdpMemFree": trdpMemFree,
       "trdpMemMinFree": trdpMemMinFree,
       "trdpMemAllocBlocks": trdpMemAllocBlocks,
       "trdpMemAllocErr": trdpMemAllocErr,
       "trdpMemFreeErr": trdpMemFreeErr,
       "trdpPdStat": trdpPdStat,
       "trdpPdDefQos": trdpPdDefQos,
       "trdpPdDefTtl": trdpPdDefTtl,
       "trdpPdDefTo": trdpPdDefTo,
       "trdpPdNumSubs": trdpPdNumSubs,
       "trdpPdNumPub": trdpPdNumPub,
       "trdpPdNumRcv": trdpPdNumRcv,
       "trdpPdNumCrcErr": trdpPdNumCrcErr,
       "trdpPdNumProtErr": trdpPdNumProtErr,
       "trdpPdNumTopoErr": trdpPdNumTopoErr,
       "trdpPdNumNoSubs": trdpPdNumNoSubs,
       "trdpPdNumNoPub": trdpPdNumNoPub,
       "trdpPdNumTo": trdpPdNumTo,
       "trdpPdNumSend": trdpPdNumSend,
       "trdpMduStat": trdpMduStat,
       "trdpMduDefQos": trdpMduDefQos,
       "trdpMduDefTtl": trdpMduDefTtl,
       "trdpMduDefReplyTo": trdpMduDefReplyTo,
       "trdpMduDefConfTo": trdpMduDefConfTo,
       "trdpMduNumList": trdpMduNumList,
       "trdpMduNumRcv": trdpMduNumRcv,
       "trdpMduNumCrcErr": trdpMduNumCrcErr,
       "trdpMduNumProtErr": trdpMduNumProtErr,
       "trdpMduNumTopoErr": trdpMduNumTopoErr,
       "trdpMduNumNoList": trdpMduNumNoList,
       "trdpMduNumReplyTo": trdpMduNumReplyTo,
       "trdpMduNumConfTo": trdpMduNumConfTo,
       "trdpMduNumSend": trdpMduNumSend,
       "trdpMdtStat": trdpMdtStat,
       "trdpMdtDefQos": trdpMdtDefQos,
       "trdpMdtDefTtl": trdpMdtDefTtl,
       "trdpMdtDefReplyTo": trdpMdtDefReplyTo,
       "trdpMdtDefConfTo": trdpMdtDefConfTo,
       "trdpMdtNumList": trdpMdtNumList,
       "trdpMdtNumRcv": trdpMdtNumRcv,
       "trdpMdtNumCrcErr": trdpMdtNumCrcErr,
       "trdpMdtNumProtErr": trdpMdtNumProtErr,
       "trdpMdtNumTopoErr": trdpMdtNumTopoErr,
       "trdpMdtNumNoList": trdpMdtNumNoList,
       "trdpMdtNumReplyTo": trdpMdtNumReplyTo,
       "trdpMdtNumConfTo": trdpMdtNumConfTo,
       "trdpMdtNumSend": trdpMdtNumSend,
       "trdpRedStat": trdpRedStat,
       "trdpRedId": trdpRedId,
       "trdpRedState": trdpRedState,
       "trdpConformance": trdpConformance,
       "trdpGenGroup": trdpGenGroup,
       "trdpMemGroup": trdpMemGroup,
       "trdpPdGroup": trdpPdGroup,
       "trdpMduGroup": trdpMduGroup,
       "trdpMdtGroup": trdpMdtGroup,
       "trdpRedGroup": trdpRedGroup,
       "trdpBasicCompliance": trdpBasicCompliance}
)
