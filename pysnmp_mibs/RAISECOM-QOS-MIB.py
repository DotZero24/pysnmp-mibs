# SNMP MIB module (RAISECOM-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:40 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,
 ObjName,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "ObjName",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

raisecomQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33)
)
if mibBuilder.loadTexts:
    raisecomQosMIB.setRevisions(
        ("2009-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomQosCfg_ObjectIdentity = ObjectIdentity
raisecomQosCfg = _RaisecomQosCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1)
)
_RcQosEnable_Type = EnableVar
_RcQosEnable_Object = MibScalar
rcQosEnable = _RcQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 1),
    _RcQosEnable_Type()
)
rcQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosEnable.setStatus("current")


class _RcQosTrust_Type(Integer32):
    """Custom type rcQosTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("port-prio", 1),
          ("cos", 2),
          ("tos", 3),
          ("dscp", 4))
    )


_RcQosTrust_Type.__name__ = "Integer32"
_RcQosTrust_Object = MibScalar
rcQosTrust = _RcQosTrust_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 2),
    _RcQosTrust_Type()
)
rcQosTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTrust.setStatus("current")


class _RcQosQueueScheduler_Type(Integer32):
    """Custom type rcQosQueueScheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2),
          ("drr", 3),
          ("wfq", 4))
    )


_RcQosQueueScheduler_Type.__name__ = "Integer32"
_RcQosQueueScheduler_Object = MibScalar
rcQosQueueScheduler = _RcQosQueueScheduler_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 3),
    _RcQosQueueScheduler_Type()
)
rcQosQueueScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosQueueScheduler.setStatus("current")
_RcQosWredEnable_Type = EnableVar
_RcQosWredEnable_Object = MibScalar
rcQosWredEnable = _RcQosWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 4),
    _RcQosWredEnable_Type()
)
rcQosWredEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredEnable.setStatus("current")
_RcQosCos2PriProfile_Type = Integer32
_RcQosCos2PriProfile_Object = MibScalar
rcQosCos2PriProfile = _RcQosCos2PriProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 5),
    _RcQosCos2PriProfile_Type()
)
rcQosCos2PriProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosCos2PriProfile.setStatus("current")
_RcQosTos2PriProfile_Type = Integer32
_RcQosTos2PriProfile_Object = MibScalar
rcQosTos2PriProfile = _RcQosTos2PriProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 6),
    _RcQosTos2PriProfile_Type()
)
rcQosTos2PriProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTos2PriProfile.setStatus("current")
_RcQosDscp2PriProfile_Type = Integer32
_RcQosDscp2PriProfile_Object = MibScalar
rcQosDscp2PriProfile = _RcQosDscp2PriProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 7),
    _RcQosDscp2PriProfile_Type()
)
rcQosDscp2PriProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosDscp2PriProfile.setStatus("current")
_RcQosDscpMutationProfile_Type = Integer32
_RcQosDscpMutationProfile_Object = MibScalar
rcQosDscpMutationProfile = _RcQosDscpMutationProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 8),
    _RcQosDscpMutationProfile_Type()
)
rcQosDscpMutationProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosDscpMutationProfile.setStatus("current")
_RcQosCosRemarkProfile_Type = Integer32
_RcQosCosRemarkProfile_Object = MibScalar
rcQosCosRemarkProfile = _RcQosCosRemarkProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 9),
    _RcQosCosRemarkProfile_Type()
)
rcQosCosRemarkProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosCosRemarkProfile.setStatus("current")
_RcQosPortCfgTable_Object = MibTable
rcQosPortCfgTable = _RcQosPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10)
)
if mibBuilder.loadTexts:
    rcQosPortCfgTable.setStatus("current")
_RcQosPortCfgEntry_Object = MibTableRow
rcQosPortCfgEntry = _RcQosPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1)
)
rcQosPortCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortCfgPortId"),
)
if mibBuilder.loadTexts:
    rcQosPortCfgEntry.setStatus("current")
_RcQosPortCfgPortId_Type = Integer32
_RcQosPortCfgPortId_Object = MibTableColumn
rcQosPortCfgPortId = _RcQosPortCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 1),
    _RcQosPortCfgPortId_Type()
)
rcQosPortCfgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortCfgPortId.setStatus("current")


class _RcQosPortCfgTrust_Type(Integer32):
    """Custom type rcQosPortCfgTrust based on Integer32"""
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
        *(("port-priority", 1),
          ("cos", 2),
          ("tos", 3),
          ("dscp", 4),
          ("cos-inner", 5))
    )


_RcQosPortCfgTrust_Type.__name__ = "Integer32"
_RcQosPortCfgTrust_Object = MibTableColumn
rcQosPortCfgTrust = _RcQosPortCfgTrust_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 2),
    _RcQosPortCfgTrust_Type()
)
rcQosPortCfgTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgTrust.setStatus("current")
_RcQosPortCfgPriority_Type = Integer32
_RcQosPortCfgPriority_Object = MibTableColumn
rcQosPortCfgPriority = _RcQosPortCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 3),
    _RcQosPortCfgPriority_Type()
)
rcQosPortCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgPriority.setStatus("current")
_RcQosPortCfgPriorityOverride_Type = EnableVar
_RcQosPortCfgPriorityOverride_Object = MibTableColumn
rcQosPortCfgPriorityOverride = _RcQosPortCfgPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 4),
    _RcQosPortCfgPriorityOverride_Type()
)
rcQosPortCfgPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgPriorityOverride.setStatus("current")


class _RcQosPortCfgQueueScheduler_Type(Integer32):
    """Custom type rcQosPortCfgQueueScheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2),
          ("drr", 3),
          ("wfq", 4))
    )


_RcQosPortCfgQueueScheduler_Type.__name__ = "Integer32"
_RcQosPortCfgQueueScheduler_Object = MibTableColumn
rcQosPortCfgQueueScheduler = _RcQosPortCfgQueueScheduler_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 5),
    _RcQosPortCfgQueueScheduler_Type()
)
rcQosPortCfgQueueScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgQueueScheduler.setStatus("current")


class _RcQosPortCfgSmacPriorityOverride_Type(Integer32):
    """Custom type rcQosPortCfgSmacPriorityOverride based on Integer32"""
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
        *(("null", 0),
          ("frame-priority", 1),
          ("queue-priority", 2),
          ("both", 3))
    )


_RcQosPortCfgSmacPriorityOverride_Type.__name__ = "Integer32"
_RcQosPortCfgSmacPriorityOverride_Object = MibTableColumn
rcQosPortCfgSmacPriorityOverride = _RcQosPortCfgSmacPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 6),
    _RcQosPortCfgSmacPriorityOverride_Type()
)
rcQosPortCfgSmacPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgSmacPriorityOverride.setStatus("current")


class _RcQosPortCfgDmacPriorityOverride_Type(Integer32):
    """Custom type rcQosPortCfgDmacPriorityOverride based on Integer32"""
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
        *(("null", 0),
          ("frame-priority", 1),
          ("queue-priority", 2),
          ("both", 3))
    )


_RcQosPortCfgDmacPriorityOverride_Type.__name__ = "Integer32"
_RcQosPortCfgDmacPriorityOverride_Object = MibTableColumn
rcQosPortCfgDmacPriorityOverride = _RcQosPortCfgDmacPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 7),
    _RcQosPortCfgDmacPriorityOverride_Type()
)
rcQosPortCfgDmacPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgDmacPriorityOverride.setStatus("current")


class _RcQosPortCfgVlanPriorityOverride_Type(Integer32):
    """Custom type rcQosPortCfgVlanPriorityOverride based on Integer32"""
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
        *(("null", 0),
          ("frame-priority", 1),
          ("queue-priority", 2),
          ("both", 3))
    )


_RcQosPortCfgVlanPriorityOverride_Type.__name__ = "Integer32"
_RcQosPortCfgVlanPriorityOverride_Object = MibTableColumn
rcQosPortCfgVlanPriorityOverride = _RcQosPortCfgVlanPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 8),
    _RcQosPortCfgVlanPriorityOverride_Type()
)
rcQosPortCfgVlanPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCfgVlanPriorityOverride.setStatus("current")
_RcQosPortCos2PriProfile_Type = Integer32
_RcQosPortCos2PriProfile_Object = MibTableColumn
rcQosPortCos2PriProfile = _RcQosPortCos2PriProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 9),
    _RcQosPortCos2PriProfile_Type()
)
rcQosPortCos2PriProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCos2PriProfile.setStatus("current")
_RcQosPortTos2PriProfile_Type = Integer32
_RcQosPortTos2PriProfile_Object = MibTableColumn
rcQosPortTos2PriProfile = _RcQosPortTos2PriProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 10),
    _RcQosPortTos2PriProfile_Type()
)
rcQosPortTos2PriProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortTos2PriProfile.setStatus("current")
_RcQosPortDscp2PriProfile_Type = Integer32
_RcQosPortDscp2PriProfile_Object = MibTableColumn
rcQosPortDscp2PriProfile = _RcQosPortDscp2PriProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 11),
    _RcQosPortDscp2PriProfile_Type()
)
rcQosPortDscp2PriProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortDscp2PriProfile.setStatus("current")
_RcQosPortDscpMutationProfile_Type = Integer32
_RcQosPortDscpMutationProfile_Object = MibTableColumn
rcQosPortDscpMutationProfile = _RcQosPortDscpMutationProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 12),
    _RcQosPortDscpMutationProfile_Type()
)
rcQosPortDscpMutationProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortDscpMutationProfile.setStatus("current")
_RcQosPortCosRemarkProfile_Type = Integer32
_RcQosPortCosRemarkProfile_Object = MibTableColumn
rcQosPortCosRemarkProfile = _RcQosPortCosRemarkProfile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 10, 1, 13),
    _RcQosPortCosRemarkProfile_Type()
)
rcQosPortCosRemarkProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCosRemarkProfile.setStatus("current")
_RcQosPortSchedulerQueueTable_Object = MibTable
rcQosPortSchedulerQueueTable = _RcQosPortSchedulerQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11)
)
if mibBuilder.loadTexts:
    rcQosPortSchedulerQueueTable.setStatus("current")
_RcQosPortSchedulerQueueEntry_Object = MibTableRow
rcQosPortSchedulerQueueEntry = _RcQosPortSchedulerQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11, 1)
)
rcQosPortSchedulerQueueEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortSchedulerPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortSchedulerQueueId"),
)
if mibBuilder.loadTexts:
    rcQosPortSchedulerQueueEntry.setStatus("current")
_RcQosPortSchedulerPortId_Type = Integer32
_RcQosPortSchedulerPortId_Object = MibTableColumn
rcQosPortSchedulerPortId = _RcQosPortSchedulerPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11, 1, 1),
    _RcQosPortSchedulerPortId_Type()
)
rcQosPortSchedulerPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortSchedulerPortId.setStatus("current")
_RcQosPortSchedulerQueueId_Type = Integer32
_RcQosPortSchedulerQueueId_Object = MibTableColumn
rcQosPortSchedulerQueueId = _RcQosPortSchedulerQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11, 1, 2),
    _RcQosPortSchedulerQueueId_Type()
)
rcQosPortSchedulerQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortSchedulerQueueId.setStatus("current")
_RcQosPortSchedulerWRR_Type = Integer32
_RcQosPortSchedulerWRR_Object = MibTableColumn
rcQosPortSchedulerWRR = _RcQosPortSchedulerWRR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11, 1, 3),
    _RcQosPortSchedulerWRR_Type()
)
rcQosPortSchedulerWRR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortSchedulerWRR.setStatus("current")
_RcQosPortSchedulerDRR_Type = Integer32
_RcQosPortSchedulerDRR_Object = MibTableColumn
rcQosPortSchedulerDRR = _RcQosPortSchedulerDRR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11, 1, 4),
    _RcQosPortSchedulerDRR_Type()
)
rcQosPortSchedulerDRR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortSchedulerDRR.setStatus("current")
_RcQosPortSchedulerWFQ_Type = Integer32
_RcQosPortSchedulerWFQ_Object = MibTableColumn
rcQosPortSchedulerWFQ = _RcQosPortSchedulerWFQ_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 11, 1, 5),
    _RcQosPortSchedulerWFQ_Type()
)
rcQosPortSchedulerWFQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortSchedulerWFQ.setStatus("current")
_RcQosLocalPrioMappingTable_Object = MibTable
rcQosLocalPrioMappingTable = _RcQosLocalPrioMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 12)
)
if mibBuilder.loadTexts:
    rcQosLocalPrioMappingTable.setStatus("current")
_RcQosLocalPrioMappingEntry_Object = MibTableRow
rcQosLocalPrioMappingEntry = _RcQosLocalPrioMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 12, 1)
)
rcQosLocalPrioMappingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosLocalPriority"),
)
if mibBuilder.loadTexts:
    rcQosLocalPrioMappingEntry.setStatus("current")


class _RcQosLocalPriority_Type(Integer32):
    """Custom type rcQosLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosLocalPriority_Type.__name__ = "Integer32"
_RcQosLocalPriority_Object = MibTableColumn
rcQosLocalPriority = _RcQosLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 12, 1, 1),
    _RcQosLocalPriority_Type()
)
rcQosLocalPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosLocalPriority.setStatus("current")


class _RcQosQueueId_Type(Integer32):
    """Custom type rcQosQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosQueueId_Type.__name__ = "Integer32"
_RcQosQueueId_Object = MibTableColumn
rcQosQueueId = _RcQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 12, 1, 2),
    _RcQosQueueId_Type()
)
rcQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosQueueId.setStatus("current")
_RcQosCosMappingTable_Object = MibTable
rcQosCosMappingTable = _RcQosCosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 13)
)
if mibBuilder.loadTexts:
    rcQosCosMappingTable.setStatus("current")
_RcQosCosMappingEntry_Object = MibTableRow
rcQosCosMappingEntry = _RcQosCosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 13, 1)
)
rcQosCosMappingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCosValue"),
)
if mibBuilder.loadTexts:
    rcQosCosMappingEntry.setStatus("current")


class _RcQosCosValue_Type(Integer32):
    """Custom type rcQosCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosValue_Type.__name__ = "Integer32"
_RcQosCosValue_Object = MibTableColumn
rcQosCosValue = _RcQosCosValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 13, 1, 1),
    _RcQosCosValue_Type()
)
rcQosCosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosValue.setStatus("current")


class _RcQosCosLocalPriority_Type(Integer32):
    """Custom type rcQosCosLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosLocalPriority_Type.__name__ = "Integer32"
_RcQosCosLocalPriority_Object = MibTableColumn
rcQosCosLocalPriority = _RcQosCosLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 13, 1, 2),
    _RcQosCosLocalPriority_Type()
)
rcQosCosLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosCosLocalPriority.setStatus("current")


class _RcQosCosColor_Type(Integer32):
    """Custom type rcQosCosColor based on Integer32"""
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
        *(("null", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosCosColor_Type.__name__ = "Integer32"
_RcQosCosColor_Object = MibTableColumn
rcQosCosColor = _RcQosCosColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 13, 1, 3),
    _RcQosCosColor_Type()
)
rcQosCosColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosCosColor.setStatus("current")
_RcQosTosMappingTable_Object = MibTable
rcQosTosMappingTable = _RcQosTosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 14)
)
if mibBuilder.loadTexts:
    rcQosTosMappingTable.setStatus("current")
_RcQosTosMappingEntry_Object = MibTableRow
rcQosTosMappingEntry = _RcQosTosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 14, 1)
)
rcQosTosMappingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosTosValue"),
)
if mibBuilder.loadTexts:
    rcQosTosMappingEntry.setStatus("current")


class _RcQosTosValue_Type(Integer32):
    """Custom type rcQosTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosTosValue_Type.__name__ = "Integer32"
_RcQosTosValue_Object = MibTableColumn
rcQosTosValue = _RcQosTosValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 14, 1, 1),
    _RcQosTosValue_Type()
)
rcQosTosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosTosValue.setStatus("current")


class _RcQosTosLocalPriority_Type(Integer32):
    """Custom type rcQosTosLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosTosLocalPriority_Type.__name__ = "Integer32"
_RcQosTosLocalPriority_Object = MibTableColumn
rcQosTosLocalPriority = _RcQosTosLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 14, 1, 2),
    _RcQosTosLocalPriority_Type()
)
rcQosTosLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTosLocalPriority.setStatus("current")


class _RcQosTosColor_Type(Integer32):
    """Custom type rcQosTosColor based on Integer32"""
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
        *(("null", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosTosColor_Type.__name__ = "Integer32"
_RcQosTosColor_Object = MibTableColumn
rcQosTosColor = _RcQosTosColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 14, 1, 3),
    _RcQosTosColor_Type()
)
rcQosTosColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTosColor.setStatus("current")
_RcQosDscpMapingTable_Object = MibTable
rcQosDscpMapingTable = _RcQosDscpMapingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 15)
)
if mibBuilder.loadTexts:
    rcQosDscpMapingTable.setStatus("current")
_RcQosDscpMapingEntry_Object = MibTableRow
rcQosDscpMapingEntry = _RcQosDscpMapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 15, 1)
)
rcQosDscpMapingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosDscpValue"),
)
if mibBuilder.loadTexts:
    rcQosDscpMapingEntry.setStatus("current")


class _RcQosDscpValue_Type(Integer32):
    """Custom type rcQosDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosDscpValue_Type.__name__ = "Integer32"
_RcQosDscpValue_Object = MibTableColumn
rcQosDscpValue = _RcQosDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 15, 1, 1),
    _RcQosDscpValue_Type()
)
rcQosDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosDscpValue.setStatus("current")


class _RcQosDscpLocalPriority_Type(Integer32):
    """Custom type rcQosDscpLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosDscpLocalPriority_Type.__name__ = "Integer32"
_RcQosDscpLocalPriority_Object = MibTableColumn
rcQosDscpLocalPriority = _RcQosDscpLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 15, 1, 2),
    _RcQosDscpLocalPriority_Type()
)
rcQosDscpLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosDscpLocalPriority.setStatus("current")


class _RcQosDscpColor_Type(Integer32):
    """Custom type rcQosDscpColor based on Integer32"""
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
        *(("null", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosDscpColor_Type.__name__ = "Integer32"
_RcQosDscpColor_Object = MibTableColumn
rcQosDscpColor = _RcQosDscpColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 15, 1, 3),
    _RcQosDscpColor_Type()
)
rcQosDscpColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosDscpColor.setStatus("current")
_RcQosSchedulerQueueTable_Object = MibTable
rcQosSchedulerQueueTable = _RcQosSchedulerQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 16)
)
if mibBuilder.loadTexts:
    rcQosSchedulerQueueTable.setStatus("current")
_RcQosSchedulerQueueEntry_Object = MibTableRow
rcQosSchedulerQueueEntry = _RcQosSchedulerQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 16, 1)
)
rcQosSchedulerQueueEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosSchedulerQueueId"),
)
if mibBuilder.loadTexts:
    rcQosSchedulerQueueEntry.setStatus("current")
_RcQosSchedulerQueueId_Type = Integer32
_RcQosSchedulerQueueId_Object = MibTableColumn
rcQosSchedulerQueueId = _RcQosSchedulerQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 16, 1, 1),
    _RcQosSchedulerQueueId_Type()
)
rcQosSchedulerQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosSchedulerQueueId.setStatus("current")
_RcQosSchedulerWRR_Type = Integer32
_RcQosSchedulerWRR_Object = MibTableColumn
rcQosSchedulerWRR = _RcQosSchedulerWRR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 16, 1, 2),
    _RcQosSchedulerWRR_Type()
)
rcQosSchedulerWRR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosSchedulerWRR.setStatus("current")
_RcQosSchedulerDRR_Type = Integer32
_RcQosSchedulerDRR_Object = MibTableColumn
rcQosSchedulerDRR = _RcQosSchedulerDRR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 16, 1, 3),
    _RcQosSchedulerDRR_Type()
)
rcQosSchedulerDRR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosSchedulerDRR.setStatus("current")
_RcQosSchedulerWFQ_Type = Integer32
_RcQosSchedulerWFQ_Object = MibTableColumn
rcQosSchedulerWFQ = _RcQosSchedulerWFQ_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 16, 1, 4),
    _RcQosSchedulerWFQ_Type()
)
rcQosSchedulerWFQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosSchedulerWFQ.setStatus("current")
_RcQosWredTcpConfigTable_Object = MibTable
rcQosWredTcpConfigTable = _RcQosWredTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17)
)
if mibBuilder.loadTexts:
    rcQosWredTcpConfigTable.setStatus("current")
_RcQosWredTcpConfigEntry_Object = MibTableRow
rcQosWredTcpConfigEntry = _RcQosWredTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1)
)
rcQosWredTcpConfigEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosWredQueueId"),
)
if mibBuilder.loadTexts:
    rcQosWredTcpConfigEntry.setStatus("current")
_RcQosWredQueueId_Type = Integer32
_RcQosWredQueueId_Object = MibTableColumn
rcQosWredQueueId = _RcQosWredQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 1),
    _RcQosWredQueueId_Type()
)
rcQosWredQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosWredQueueId.setStatus("current")
_RcQosWredGreenDropStartPoint_Type = Integer32
_RcQosWredGreenDropStartPoint_Object = MibTableColumn
rcQosWredGreenDropStartPoint = _RcQosWredGreenDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 2),
    _RcQosWredGreenDropStartPoint_Type()
)
rcQosWredGreenDropStartPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredGreenDropStartPoint.setStatus("current")
_RcQosWredGreenDropEndPoint_Type = Integer32
_RcQosWredGreenDropEndPoint_Object = MibTableColumn
rcQosWredGreenDropEndPoint = _RcQosWredGreenDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 3),
    _RcQosWredGreenDropEndPoint_Type()
)
rcQosWredGreenDropEndPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredGreenDropEndPoint.setStatus("current")
_RcQosWredGreenDropProbability_Type = Integer32
_RcQosWredGreenDropProbability_Object = MibTableColumn
rcQosWredGreenDropProbability = _RcQosWredGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 4),
    _RcQosWredGreenDropProbability_Type()
)
rcQosWredGreenDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredGreenDropProbability.setStatus("current")
_RcQosWredYellowDropStartPoint_Type = Integer32
_RcQosWredYellowDropStartPoint_Object = MibTableColumn
rcQosWredYellowDropStartPoint = _RcQosWredYellowDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 5),
    _RcQosWredYellowDropStartPoint_Type()
)
rcQosWredYellowDropStartPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredYellowDropStartPoint.setStatus("current")
_RcQosWredYellowDropEndPoint_Type = Integer32
_RcQosWredYellowDropEndPoint_Object = MibTableColumn
rcQosWredYellowDropEndPoint = _RcQosWredYellowDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 6),
    _RcQosWredYellowDropEndPoint_Type()
)
rcQosWredYellowDropEndPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredYellowDropEndPoint.setStatus("current")
_RcQosWredYellowDropProbability_Type = Integer32
_RcQosWredYellowDropProbability_Object = MibTableColumn
rcQosWredYellowDropProbability = _RcQosWredYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 7),
    _RcQosWredYellowDropProbability_Type()
)
rcQosWredYellowDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredYellowDropProbability.setStatus("current")
_RcQosWredRedDropStartPoint_Type = Integer32
_RcQosWredRedDropStartPoint_Object = MibTableColumn
rcQosWredRedDropStartPoint = _RcQosWredRedDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 8),
    _RcQosWredRedDropStartPoint_Type()
)
rcQosWredRedDropStartPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredRedDropStartPoint.setStatus("current")
_RcQosWredRedDropEndPoint_Type = Integer32
_RcQosWredRedDropEndPoint_Object = MibTableColumn
rcQosWredRedDropEndPoint = _RcQosWredRedDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 9),
    _RcQosWredRedDropEndPoint_Type()
)
rcQosWredRedDropEndPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredRedDropEndPoint.setStatus("current")
_RcQosWredRedDropProbability_Type = Integer32
_RcQosWredRedDropProbability_Object = MibTableColumn
rcQosWredRedDropProbability = _RcQosWredRedDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 10),
    _RcQosWredRedDropProbability_Type()
)
rcQosWredRedDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredRedDropProbability.setStatus("current")


class _RcQosWredStatus_Type(Integer32):
    """Custom type rcQosWredStatus based on Integer32"""
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


_RcQosWredStatus_Type.__name__ = "Integer32"
_RcQosWredStatus_Object = MibTableColumn
rcQosWredStatus = _RcQosWredStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 17, 1, 11),
    _RcQosWredStatus_Type()
)
rcQosWredStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosWredStatus.setStatus("current")
_RcQosPortWredTcpConfigTable_Object = MibTable
rcQosPortWredTcpConfigTable = _RcQosPortWredTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18)
)
if mibBuilder.loadTexts:
    rcQosPortWredTcpConfigTable.setStatus("current")
_RcQosPortWredTcpConfigEntry_Object = MibTableRow
rcQosPortWredTcpConfigEntry = _RcQosPortWredTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1)
)
rcQosPortWredTcpConfigEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortWredPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortWredQueueId"),
)
if mibBuilder.loadTexts:
    rcQosPortWredTcpConfigEntry.setStatus("current")
_RcQosPortWredPortId_Type = Integer32
_RcQosPortWredPortId_Object = MibTableColumn
rcQosPortWredPortId = _RcQosPortWredPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 1),
    _RcQosPortWredPortId_Type()
)
rcQosPortWredPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortWredPortId.setStatus("current")
_RcQosPortWredQueueId_Type = Integer32
_RcQosPortWredQueueId_Object = MibTableColumn
rcQosPortWredQueueId = _RcQosPortWredQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 2),
    _RcQosPortWredQueueId_Type()
)
rcQosPortWredQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortWredQueueId.setStatus("current")
_RcQosPortWredGreenDropStartPoint_Type = Integer32
_RcQosPortWredGreenDropStartPoint_Object = MibTableColumn
rcQosPortWredGreenDropStartPoint = _RcQosPortWredGreenDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 3),
    _RcQosPortWredGreenDropStartPoint_Type()
)
rcQosPortWredGreenDropStartPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredGreenDropStartPoint.setStatus("current")
_RcQosPortWredGreenDropEndPoint_Type = Integer32
_RcQosPortWredGreenDropEndPoint_Object = MibTableColumn
rcQosPortWredGreenDropEndPoint = _RcQosPortWredGreenDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 4),
    _RcQosPortWredGreenDropEndPoint_Type()
)
rcQosPortWredGreenDropEndPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredGreenDropEndPoint.setStatus("current")
_RcQosPortWredGreenDropProbability_Type = Integer32
_RcQosPortWredGreenDropProbability_Object = MibTableColumn
rcQosPortWredGreenDropProbability = _RcQosPortWredGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 5),
    _RcQosPortWredGreenDropProbability_Type()
)
rcQosPortWredGreenDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredGreenDropProbability.setStatus("current")
_RcQosPortWredYellowDropStartPoint_Type = Integer32
_RcQosPortWredYellowDropStartPoint_Object = MibTableColumn
rcQosPortWredYellowDropStartPoint = _RcQosPortWredYellowDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 6),
    _RcQosPortWredYellowDropStartPoint_Type()
)
rcQosPortWredYellowDropStartPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredYellowDropStartPoint.setStatus("current")
_RcQosPortWredYellowDropEndPoint_Type = Integer32
_RcQosPortWredYellowDropEndPoint_Object = MibTableColumn
rcQosPortWredYellowDropEndPoint = _RcQosPortWredYellowDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 7),
    _RcQosPortWredYellowDropEndPoint_Type()
)
rcQosPortWredYellowDropEndPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredYellowDropEndPoint.setStatus("current")
_RcQosPortWredYellowDropProbability_Type = Integer32
_RcQosPortWredYellowDropProbability_Object = MibTableColumn
rcQosPortWredYellowDropProbability = _RcQosPortWredYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 8),
    _RcQosPortWredYellowDropProbability_Type()
)
rcQosPortWredYellowDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredYellowDropProbability.setStatus("current")
_RcQosPortWredRedDropStartPoint_Type = Integer32
_RcQosPortWredRedDropStartPoint_Object = MibTableColumn
rcQosPortWredRedDropStartPoint = _RcQosPortWredRedDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 9),
    _RcQosPortWredRedDropStartPoint_Type()
)
rcQosPortWredRedDropStartPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredRedDropStartPoint.setStatus("current")
_RcQosPortWredRedDropEndPoint_Type = Integer32
_RcQosPortWredRedDropEndPoint_Object = MibTableColumn
rcQosPortWredRedDropEndPoint = _RcQosPortWredRedDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 10),
    _RcQosPortWredRedDropEndPoint_Type()
)
rcQosPortWredRedDropEndPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredRedDropEndPoint.setStatus("current")
_RcQosPortWredRedDropProbability_Type = Integer32
_RcQosPortWredRedDropProbability_Object = MibTableColumn
rcQosPortWredRedDropProbability = _RcQosPortWredRedDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 11),
    _RcQosPortWredRedDropProbability_Type()
)
rcQosPortWredRedDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredRedDropProbability.setStatus("current")


class _RcQosPortWredStatus_Type(Integer32):
    """Custom type rcQosPortWredStatus based on Integer32"""
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


_RcQosPortWredStatus_Type.__name__ = "Integer32"
_RcQosPortWredStatus_Object = MibTableColumn
rcQosPortWredStatus = _RcQosPortWredStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 18, 1, 12),
    _RcQosPortWredStatus_Type()
)
rcQosPortWredStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortWredStatus.setStatus("current")
_RcQosShapingTable_Object = MibTable
rcQosShapingTable = _RcQosShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19)
)
if mibBuilder.loadTexts:
    rcQosShapingTable.setStatus("current")
_RcQosShapingEntry_Object = MibTableRow
rcQosShapingEntry = _RcQosShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1)
)
rcQosShapingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosShapingQueueId"),
)
if mibBuilder.loadTexts:
    rcQosShapingEntry.setStatus("current")
_RcQosShapingQueueId_Type = Integer32
_RcQosShapingQueueId_Object = MibTableColumn
rcQosShapingQueueId = _RcQosShapingQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1, 1),
    _RcQosShapingQueueId_Type()
)
rcQosShapingQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosShapingQueueId.setStatus("current")
_RcQosShapingCir_Type = Integer32
_RcQosShapingCir_Object = MibTableColumn
rcQosShapingCir = _RcQosShapingCir_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1, 2),
    _RcQosShapingCir_Type()
)
rcQosShapingCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosShapingCir.setStatus("current")
_RcQosShapingCbs_Type = Integer32
_RcQosShapingCbs_Object = MibTableColumn
rcQosShapingCbs = _RcQosShapingCbs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1, 3),
    _RcQosShapingCbs_Type()
)
rcQosShapingCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosShapingCbs.setStatus("current")
_RcQosShapingPir_Type = Integer32
_RcQosShapingPir_Object = MibTableColumn
rcQosShapingPir = _RcQosShapingPir_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1, 4),
    _RcQosShapingPir_Type()
)
rcQosShapingPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosShapingPir.setStatus("current")
_RcQosShapingPbs_Type = Integer32
_RcQosShapingPbs_Object = MibTableColumn
rcQosShapingPbs = _RcQosShapingPbs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1, 5),
    _RcQosShapingPbs_Type()
)
rcQosShapingPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosShapingPbs.setStatus("current")


class _RcQosShapingStatus_Type(Integer32):
    """Custom type rcQosShapingStatus based on Integer32"""
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


_RcQosShapingStatus_Type.__name__ = "Integer32"
_RcQosShapingStatus_Object = MibTableColumn
rcQosShapingStatus = _RcQosShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 19, 1, 6),
    _RcQosShapingStatus_Type()
)
rcQosShapingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosShapingStatus.setStatus("current")
_RcQosPortShapingTable_Object = MibTable
rcQosPortShapingTable = _RcQosPortShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20)
)
if mibBuilder.loadTexts:
    rcQosPortShapingTable.setStatus("current")
_RcQosPortShapingEntry_Object = MibTableRow
rcQosPortShapingEntry = _RcQosPortShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1)
)
rcQosPortShapingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortShapingPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortShapingQueueId"),
)
if mibBuilder.loadTexts:
    rcQosPortShapingEntry.setStatus("current")
_RcQosPortShapingPortId_Type = Integer32
_RcQosPortShapingPortId_Object = MibTableColumn
rcQosPortShapingPortId = _RcQosPortShapingPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 1),
    _RcQosPortShapingPortId_Type()
)
rcQosPortShapingPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortShapingPortId.setStatus("current")
_RcQosPortShapingQueueId_Type = Integer32
_RcQosPortShapingQueueId_Object = MibTableColumn
rcQosPortShapingQueueId = _RcQosPortShapingQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 2),
    _RcQosPortShapingQueueId_Type()
)
rcQosPortShapingQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortShapingQueueId.setStatus("current")
_RcQosPortShapingCir_Type = Integer32
_RcQosPortShapingCir_Object = MibTableColumn
rcQosPortShapingCir = _RcQosPortShapingCir_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 3),
    _RcQosPortShapingCir_Type()
)
rcQosPortShapingCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortShapingCir.setStatus("current")
_RcQosPortShapingCbs_Type = Integer32
_RcQosPortShapingCbs_Object = MibTableColumn
rcQosPortShapingCbs = _RcQosPortShapingCbs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 4),
    _RcQosPortShapingCbs_Type()
)
rcQosPortShapingCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortShapingCbs.setStatus("current")
_RcQosPortShapingPir_Type = Integer32
_RcQosPortShapingPir_Object = MibTableColumn
rcQosPortShapingPir = _RcQosPortShapingPir_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 5),
    _RcQosPortShapingPir_Type()
)
rcQosPortShapingPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortShapingPir.setStatus("current")
_RcQosPortShapingPbs_Type = Integer32
_RcQosPortShapingPbs_Object = MibTableColumn
rcQosPortShapingPbs = _RcQosPortShapingPbs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 6),
    _RcQosPortShapingPbs_Type()
)
rcQosPortShapingPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortShapingPbs.setStatus("current")


class _RcQosPortShapingStatus_Type(Integer32):
    """Custom type rcQosPortShapingStatus based on Integer32"""
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


_RcQosPortShapingStatus_Type.__name__ = "Integer32"
_RcQosPortShapingStatus_Object = MibTableColumn
rcQosPortShapingStatus = _RcQosPortShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 20, 1, 7),
    _RcQosPortShapingStatus_Type()
)
rcQosPortShapingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortShapingStatus.setStatus("current")
_RcQosPortCosMappingTable_Object = MibTable
rcQosPortCosMappingTable = _RcQosPortCosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 21)
)
if mibBuilder.loadTexts:
    rcQosPortCosMappingTable.setStatus("current")
_RcQosPortCosMappingEntry_Object = MibTableRow
rcQosPortCosMappingEntry = _RcQosPortCosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 21, 1)
)
rcQosPortCosMappingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortCosPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortCosValue"),
)
if mibBuilder.loadTexts:
    rcQosPortCosMappingEntry.setStatus("current")
_RcQosPortCosPortId_Type = Integer32
_RcQosPortCosPortId_Object = MibTableColumn
rcQosPortCosPortId = _RcQosPortCosPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 21, 1, 1),
    _RcQosPortCosPortId_Type()
)
rcQosPortCosPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortCosPortId.setStatus("current")


class _RcQosPortCosValue_Type(Integer32):
    """Custom type rcQosPortCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPortCosValue_Type.__name__ = "Integer32"
_RcQosPortCosValue_Object = MibTableColumn
rcQosPortCosValue = _RcQosPortCosValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 21, 1, 2),
    _RcQosPortCosValue_Type()
)
rcQosPortCosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortCosValue.setStatus("current")


class _RcQosPortCosLocalPriority_Type(Integer32):
    """Custom type rcQosPortCosLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPortCosLocalPriority_Type.__name__ = "Integer32"
_RcQosPortCosLocalPriority_Object = MibTableColumn
rcQosPortCosLocalPriority = _RcQosPortCosLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 21, 1, 3),
    _RcQosPortCosLocalPriority_Type()
)
rcQosPortCosLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCosLocalPriority.setStatus("current")


class _RcQosPortCosColor_Type(Integer32):
    """Custom type rcQosPortCosColor based on Integer32"""
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
        *(("null", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosPortCosColor_Type.__name__ = "Integer32"
_RcQosPortCosColor_Object = MibTableColumn
rcQosPortCosColor = _RcQosPortCosColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 21, 1, 4),
    _RcQosPortCosColor_Type()
)
rcQosPortCosColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortCosColor.setStatus("current")
_RcQosPortTosMappingTable_Object = MibTable
rcQosPortTosMappingTable = _RcQosPortTosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 22)
)
if mibBuilder.loadTexts:
    rcQosPortTosMappingTable.setStatus("current")
_RcQosPortTosMappingEntry_Object = MibTableRow
rcQosPortTosMappingEntry = _RcQosPortTosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 22, 1)
)
rcQosPortTosMappingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortTosPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortTosValue"),
)
if mibBuilder.loadTexts:
    rcQosPortTosMappingEntry.setStatus("current")
_RcQosPortTosPortId_Type = Integer32
_RcQosPortTosPortId_Object = MibTableColumn
rcQosPortTosPortId = _RcQosPortTosPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 22, 1, 1),
    _RcQosPortTosPortId_Type()
)
rcQosPortTosPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortTosPortId.setStatus("current")


class _RcQosPortTosValue_Type(Integer32):
    """Custom type rcQosPortTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPortTosValue_Type.__name__ = "Integer32"
_RcQosPortTosValue_Object = MibTableColumn
rcQosPortTosValue = _RcQosPortTosValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 22, 1, 2),
    _RcQosPortTosValue_Type()
)
rcQosPortTosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortTosValue.setStatus("current")


class _RcQosPortTosLocalPriority_Type(Integer32):
    """Custom type rcQosPortTosLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPortTosLocalPriority_Type.__name__ = "Integer32"
_RcQosPortTosLocalPriority_Object = MibTableColumn
rcQosPortTosLocalPriority = _RcQosPortTosLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 22, 1, 3),
    _RcQosPortTosLocalPriority_Type()
)
rcQosPortTosLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortTosLocalPriority.setStatus("current")


class _RcQosPortTosColor_Type(Integer32):
    """Custom type rcQosPortTosColor based on Integer32"""
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
        *(("null", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosPortTosColor_Type.__name__ = "Integer32"
_RcQosPortTosColor_Object = MibTableColumn
rcQosPortTosColor = _RcQosPortTosColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 22, 1, 4),
    _RcQosPortTosColor_Type()
)
rcQosPortTosColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortTosColor.setStatus("current")
_RcQosPortDscpMapingTable_Object = MibTable
rcQosPortDscpMapingTable = _RcQosPortDscpMapingTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 23)
)
if mibBuilder.loadTexts:
    rcQosPortDscpMapingTable.setStatus("current")
_RcQosPortDscpMapingEntry_Object = MibTableRow
rcQosPortDscpMapingEntry = _RcQosPortDscpMapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 23, 1)
)
rcQosPortDscpMapingEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortDscpPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortDscpValue"),
)
if mibBuilder.loadTexts:
    rcQosPortDscpMapingEntry.setStatus("current")
_RcQosPortDscpPortId_Type = Integer32
_RcQosPortDscpPortId_Object = MibTableColumn
rcQosPortDscpPortId = _RcQosPortDscpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 23, 1, 1),
    _RcQosPortDscpPortId_Type()
)
rcQosPortDscpPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortDscpPortId.setStatus("current")


class _RcQosPortDscpValue_Type(Integer32):
    """Custom type rcQosPortDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosPortDscpValue_Type.__name__ = "Integer32"
_RcQosPortDscpValue_Object = MibTableColumn
rcQosPortDscpValue = _RcQosPortDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 23, 1, 2),
    _RcQosPortDscpValue_Type()
)
rcQosPortDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortDscpValue.setStatus("current")


class _RcQosPortDscpLocalPriority_Type(Integer32):
    """Custom type rcQosPortDscpLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPortDscpLocalPriority_Type.__name__ = "Integer32"
_RcQosPortDscpLocalPriority_Object = MibTableColumn
rcQosPortDscpLocalPriority = _RcQosPortDscpLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 23, 1, 3),
    _RcQosPortDscpLocalPriority_Type()
)
rcQosPortDscpLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortDscpLocalPriority.setStatus("current")


class _RcQosPortDscpColor_Type(Integer32):
    """Custom type rcQosPortDscpColor based on Integer32"""
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
        *(("null", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosPortDscpColor_Type.__name__ = "Integer32"
_RcQosPortDscpColor_Object = MibTableColumn
rcQosPortDscpColor = _RcQosPortDscpColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 23, 1, 4),
    _RcQosPortDscpColor_Type()
)
rcQosPortDscpColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortDscpColor.setStatus("current")
_RcQosPortDropPktsStatisticTable_Object = MibTable
rcQosPortDropPktsStatisticTable = _RcQosPortDropPktsStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24)
)
if mibBuilder.loadTexts:
    rcQosPortDropPktsStatisticTable.setStatus("current")
_RcQosPortDropPktsStatisticEntry_Object = MibTableRow
rcQosPortDropPktsStatisticEntry = _RcQosPortDropPktsStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1)
)
rcQosPortDropPktsStatisticEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortStatisticsPortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortStatisticsQueueId"),
)
if mibBuilder.loadTexts:
    rcQosPortDropPktsStatisticEntry.setStatus("current")
_RcQosPortStatisticsPortId_Type = Integer32
_RcQosPortStatisticsPortId_Object = MibTableColumn
rcQosPortStatisticsPortId = _RcQosPortStatisticsPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1, 1),
    _RcQosPortStatisticsPortId_Type()
)
rcQosPortStatisticsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortStatisticsPortId.setStatus("current")
_RcQosPortStatisticsQueueId_Type = Integer32
_RcQosPortStatisticsQueueId_Object = MibTableColumn
rcQosPortStatisticsQueueId = _RcQosPortStatisticsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1, 2),
    _RcQosPortStatisticsQueueId_Type()
)
rcQosPortStatisticsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortStatisticsQueueId.setStatus("current")
_RcQosPortStatisticsDropPkts_Type = Counter64
_RcQosPortStatisticsDropPkts_Object = MibTableColumn
rcQosPortStatisticsDropPkts = _RcQosPortStatisticsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1, 3),
    _RcQosPortStatisticsDropPkts_Type()
)
rcQosPortStatisticsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosPortStatisticsDropPkts.setStatus("current")
_RcQosPortStatisticsDropBytes_Type = Counter64
_RcQosPortStatisticsDropBytes_Object = MibTableColumn
rcQosPortStatisticsDropBytes = _RcQosPortStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1, 4),
    _RcQosPortStatisticsDropBytes_Type()
)
rcQosPortStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosPortStatisticsDropBytes.setStatus("current")


class _RcQosPortStatisticsDropUnit_Type(Integer32):
    """Custom type rcQosPortStatisticsDropUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("packets", 0),
          ("bytes", 1))
    )


_RcQosPortStatisticsDropUnit_Type.__name__ = "Integer32"
_RcQosPortStatisticsDropUnit_Object = MibTableColumn
rcQosPortStatisticsDropUnit = _RcQosPortStatisticsDropUnit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1, 5),
    _RcQosPortStatisticsDropUnit_Type()
)
rcQosPortStatisticsDropUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosPortStatisticsDropUnit.setStatus("current")
_RcQosPortStatisticsClear_Type = EnableVar
_RcQosPortStatisticsClear_Object = MibTableColumn
rcQosPortStatisticsClear = _RcQosPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 24, 1, 6),
    _RcQosPortStatisticsClear_Type()
)
rcQosPortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosPortStatisticsClear.setStatus("current")
_RcQosMappingCosToPriTable_Object = MibTable
rcQosMappingCosToPriTable = _RcQosMappingCosToPriTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25)
)
if mibBuilder.loadTexts:
    rcQosMappingCosToPriTable.setStatus("current")
_RcQosMappingCosToPriEntry_Object = MibTableRow
rcQosMappingCosToPriEntry = _RcQosMappingCosToPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1)
)
rcQosMappingCosToPriEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCosToPriIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosToPriCos"),
)
if mibBuilder.loadTexts:
    rcQosMappingCosToPriEntry.setStatus("current")


class _RcQosCosToPriIndex_Type(Integer32):
    """Custom type rcQosCosToPriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosCosToPriIndex_Type.__name__ = "Integer32"
_RcQosCosToPriIndex_Object = MibTableColumn
rcQosCosToPriIndex = _RcQosCosToPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 1),
    _RcQosCosToPriIndex_Type()
)
rcQosCosToPriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosToPriIndex.setStatus("current")


class _RcQosCosToPriCos_Type(Integer32):
    """Custom type rcQosCosToPriCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosToPriCos_Type.__name__ = "Integer32"
_RcQosCosToPriCos_Object = MibTableColumn
rcQosCosToPriCos = _RcQosCosToPriCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 2),
    _RcQosCosToPriCos_Type()
)
rcQosCosToPriCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosToPriCos.setStatus("current")


class _RcQosCosToPriLpri_Type(Integer32):
    """Custom type rcQosCosToPriLpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosToPriLpri_Type.__name__ = "Integer32"
_RcQosCosToPriLpri_Object = MibTableColumn
rcQosCosToPriLpri = _RcQosCosToPriLpri_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 3),
    _RcQosCosToPriLpri_Type()
)
rcQosCosToPriLpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosToPriLpri.setStatus("current")


class _RcQosCosToPriColor_Type(Integer32):
    """Custom type rcQosCosToPriColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosCosToPriColor_Type.__name__ = "Integer32"
_RcQosCosToPriColor_Object = MibTableColumn
rcQosCosToPriColor = _RcQosCosToPriColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 4),
    _RcQosCosToPriColor_Type()
)
rcQosCosToPriColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosToPriColor.setStatus("current")
_RcQosCosToPriDesc_Type = ObjName
_RcQosCosToPriDesc_Object = MibTableColumn
rcQosCosToPriDesc = _RcQosCosToPriDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 5),
    _RcQosCosToPriDesc_Type()
)
rcQosCosToPriDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosToPriDesc.setStatus("current")
_RcQosCosToPriRef_Type = Integer32
_RcQosCosToPriRef_Object = MibTableColumn
rcQosCosToPriRef = _RcQosCosToPriRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 6),
    _RcQosCosToPriRef_Type()
)
rcQosCosToPriRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosToPriRef.setStatus("current")
_RcQosCosToPriStatus_Type = RowStatus
_RcQosCosToPriStatus_Object = MibTableColumn
rcQosCosToPriStatus = _RcQosCosToPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 25, 1, 7),
    _RcQosCosToPriStatus_Type()
)
rcQosCosToPriStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosToPriStatus.setStatus("current")
_RcQosMappingTosToPriTable_Object = MibTable
rcQosMappingTosToPriTable = _RcQosMappingTosToPriTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26)
)
if mibBuilder.loadTexts:
    rcQosMappingTosToPriTable.setStatus("current")
_RcQosMappingTosToPriEntry_Object = MibTableRow
rcQosMappingTosToPriEntry = _RcQosMappingTosToPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1)
)
rcQosMappingTosToPriEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosTosToPriIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosTosToPriTos"),
)
if mibBuilder.loadTexts:
    rcQosMappingTosToPriEntry.setStatus("current")


class _RcQosTosToPriIndex_Type(Integer32):
    """Custom type rcQosTosToPriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosTosToPriIndex_Type.__name__ = "Integer32"
_RcQosTosToPriIndex_Object = MibTableColumn
rcQosTosToPriIndex = _RcQosTosToPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 1),
    _RcQosTosToPriIndex_Type()
)
rcQosTosToPriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosTosToPriIndex.setStatus("current")


class _RcQosTosToPriTos_Type(Integer32):
    """Custom type rcQosTosToPriTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosTosToPriTos_Type.__name__ = "Integer32"
_RcQosTosToPriTos_Object = MibTableColumn
rcQosTosToPriTos = _RcQosTosToPriTos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 2),
    _RcQosTosToPriTos_Type()
)
rcQosTosToPriTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosTosToPriTos.setStatus("current")


class _RcQosTosToPriLpri_Type(Integer32):
    """Custom type rcQosTosToPriLpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosTosToPriLpri_Type.__name__ = "Integer32"
_RcQosTosToPriLpri_Object = MibTableColumn
rcQosTosToPriLpri = _RcQosTosToPriLpri_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 3),
    _RcQosTosToPriLpri_Type()
)
rcQosTosToPriLpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosTosToPriLpri.setStatus("current")


class _RcQosTosToPriColor_Type(Integer32):
    """Custom type rcQosTosToPriColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosTosToPriColor_Type.__name__ = "Integer32"
_RcQosTosToPriColor_Object = MibTableColumn
rcQosTosToPriColor = _RcQosTosToPriColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 4),
    _RcQosTosToPriColor_Type()
)
rcQosTosToPriColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosTosToPriColor.setStatus("current")
_RcQosTosToPriDesc_Type = ObjName
_RcQosTosToPriDesc_Object = MibTableColumn
rcQosTosToPriDesc = _RcQosTosToPriDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 5),
    _RcQosTosToPriDesc_Type()
)
rcQosTosToPriDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosTosToPriDesc.setStatus("current")
_RcQosTosToPriRef_Type = Integer32
_RcQosTosToPriRef_Object = MibTableColumn
rcQosTosToPriRef = _RcQosTosToPriRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 6),
    _RcQosTosToPriRef_Type()
)
rcQosTosToPriRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosTosToPriRef.setStatus("current")
_RcQosTosToPriStatus_Type = RowStatus
_RcQosTosToPriStatus_Object = MibTableColumn
rcQosTosToPriStatus = _RcQosTosToPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 26, 1, 7),
    _RcQosTosToPriStatus_Type()
)
rcQosTosToPriStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosTosToPriStatus.setStatus("current")
_RcQosMappingDscpToPriTable_Object = MibTable
rcQosMappingDscpToPriTable = _RcQosMappingDscpToPriTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27)
)
if mibBuilder.loadTexts:
    rcQosMappingDscpToPriTable.setStatus("current")
_RcQosMappingDscpToPriEntry_Object = MibTableRow
rcQosMappingDscpToPriEntry = _RcQosMappingDscpToPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1)
)
rcQosMappingDscpToPriEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosDscpToPriIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosDscpToPriDscp"),
)
if mibBuilder.loadTexts:
    rcQosMappingDscpToPriEntry.setStatus("current")


class _RcQosDscpToPriIndex_Type(Integer32):
    """Custom type rcQosDscpToPriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosDscpToPriIndex_Type.__name__ = "Integer32"
_RcQosDscpToPriIndex_Object = MibTableColumn
rcQosDscpToPriIndex = _RcQosDscpToPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 1),
    _RcQosDscpToPriIndex_Type()
)
rcQosDscpToPriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosDscpToPriIndex.setStatus("current")


class _RcQosDscpToPriDscp_Type(Integer32):
    """Custom type rcQosDscpToPriDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosDscpToPriDscp_Type.__name__ = "Integer32"
_RcQosDscpToPriDscp_Object = MibTableColumn
rcQosDscpToPriDscp = _RcQosDscpToPriDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 2),
    _RcQosDscpToPriDscp_Type()
)
rcQosDscpToPriDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosDscpToPriDscp.setStatus("current")


class _RcQosDscpToPriLpri_Type(Integer32):
    """Custom type rcQosDscpToPriLpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosDscpToPriLpri_Type.__name__ = "Integer32"
_RcQosDscpToPriLpri_Object = MibTableColumn
rcQosDscpToPriLpri = _RcQosDscpToPriLpri_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 3),
    _RcQosDscpToPriLpri_Type()
)
rcQosDscpToPriLpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpToPriLpri.setStatus("current")


class _RcQosDscpToPriColor_Type(Integer32):
    """Custom type rcQosDscpToPriColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RcQosDscpToPriColor_Type.__name__ = "Integer32"
_RcQosDscpToPriColor_Object = MibTableColumn
rcQosDscpToPriColor = _RcQosDscpToPriColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 4),
    _RcQosDscpToPriColor_Type()
)
rcQosDscpToPriColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpToPriColor.setStatus("current")
_RcQosDscpToPriDesc_Type = ObjName
_RcQosDscpToPriDesc_Object = MibTableColumn
rcQosDscpToPriDesc = _RcQosDscpToPriDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 5),
    _RcQosDscpToPriDesc_Type()
)
rcQosDscpToPriDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpToPriDesc.setStatus("current")
_RcQosDscpToPriRef_Type = Integer32
_RcQosDscpToPriRef_Object = MibTableColumn
rcQosDscpToPriRef = _RcQosDscpToPriRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 6),
    _RcQosDscpToPriRef_Type()
)
rcQosDscpToPriRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpToPriRef.setStatus("current")
_RcQosDscpToPriStatus_Type = RowStatus
_RcQosDscpToPriStatus_Object = MibTableColumn
rcQosDscpToPriStatus = _RcQosDscpToPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 27, 1, 7),
    _RcQosDscpToPriStatus_Type()
)
rcQosDscpToPriStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpToPriStatus.setStatus("current")
_RcQosMappingDscpMutationTable_Object = MibTable
rcQosMappingDscpMutationTable = _RcQosMappingDscpMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28)
)
if mibBuilder.loadTexts:
    rcQosMappingDscpMutationTable.setStatus("current")
_RcQosMappingDscpMutationEntry_Object = MibTableRow
rcQosMappingDscpMutationEntry = _RcQosMappingDscpMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1)
)
rcQosMappingDscpMutationEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosDscpMutationIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosDscpMutationDscp"),
)
if mibBuilder.loadTexts:
    rcQosMappingDscpMutationEntry.setStatus("current")


class _RcQosDscpMutationIndex_Type(Integer32):
    """Custom type rcQosDscpMutationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosDscpMutationIndex_Type.__name__ = "Integer32"
_RcQosDscpMutationIndex_Object = MibTableColumn
rcQosDscpMutationIndex = _RcQosDscpMutationIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1, 1),
    _RcQosDscpMutationIndex_Type()
)
rcQosDscpMutationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosDscpMutationIndex.setStatus("current")


class _RcQosDscpMutationDscp_Type(Integer32):
    """Custom type rcQosDscpMutationDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosDscpMutationDscp_Type.__name__ = "Integer32"
_RcQosDscpMutationDscp_Object = MibTableColumn
rcQosDscpMutationDscp = _RcQosDscpMutationDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1, 2),
    _RcQosDscpMutationDscp_Type()
)
rcQosDscpMutationDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosDscpMutationDscp.setStatus("current")


class _RcQosDscpMutationNewDscp_Type(Integer32):
    """Custom type rcQosDscpMutationNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosDscpMutationNewDscp_Type.__name__ = "Integer32"
_RcQosDscpMutationNewDscp_Object = MibTableColumn
rcQosDscpMutationNewDscp = _RcQosDscpMutationNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1, 3),
    _RcQosDscpMutationNewDscp_Type()
)
rcQosDscpMutationNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpMutationNewDscp.setStatus("current")
_RcQosDscpMutationDesc_Type = ObjName
_RcQosDscpMutationDesc_Object = MibTableColumn
rcQosDscpMutationDesc = _RcQosDscpMutationDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1, 4),
    _RcQosDscpMutationDesc_Type()
)
rcQosDscpMutationDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpMutationDesc.setStatus("current")
_RcQosDscpMutationRef_Type = Integer32
_RcQosDscpMutationRef_Object = MibTableColumn
rcQosDscpMutationRef = _RcQosDscpMutationRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1, 5),
    _RcQosDscpMutationRef_Type()
)
rcQosDscpMutationRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpMutationRef.setStatus("current")
_RcQosDscpMutationStatus_Type = RowStatus
_RcQosDscpMutationStatus_Object = MibTableColumn
rcQosDscpMutationStatus = _RcQosDscpMutationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 28, 1, 6),
    _RcQosDscpMutationStatus_Type()
)
rcQosDscpMutationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosDscpMutationStatus.setStatus("current")
_RcQosMappingCosRemarkTable_Object = MibTable
rcQosMappingCosRemarkTable = _RcQosMappingCosRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29)
)
if mibBuilder.loadTexts:
    rcQosMappingCosRemarkTable.setStatus("current")
_RcQosMappingCosRemarkEntry_Object = MibTableRow
rcQosMappingCosRemarkEntry = _RcQosMappingCosRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1)
)
rcQosMappingCosRemarkEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCosRemarkIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosRemarkLpri"),
)
if mibBuilder.loadTexts:
    rcQosMappingCosRemarkEntry.setStatus("current")


class _RcQosCosRemarkIndex_Type(Integer32):
    """Custom type rcQosCosRemarkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosCosRemarkIndex_Type.__name__ = "Integer32"
_RcQosCosRemarkIndex_Object = MibTableColumn
rcQosCosRemarkIndex = _RcQosCosRemarkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1, 1),
    _RcQosCosRemarkIndex_Type()
)
rcQosCosRemarkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosRemarkIndex.setStatus("current")


class _RcQosCosRemarkLpri_Type(Integer32):
    """Custom type rcQosCosRemarkLpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosRemarkLpri_Type.__name__ = "Integer32"
_RcQosCosRemarkLpri_Object = MibTableColumn
rcQosCosRemarkLpri = _RcQosCosRemarkLpri_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1, 2),
    _RcQosCosRemarkLpri_Type()
)
rcQosCosRemarkLpri.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosRemarkLpri.setStatus("current")


class _RcQosCosRemarkCos_Type(Integer32):
    """Custom type rcQosCosRemarkCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosRemarkCos_Type.__name__ = "Integer32"
_RcQosCosRemarkCos_Object = MibTableColumn
rcQosCosRemarkCos = _RcQosCosRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1, 3),
    _RcQosCosRemarkCos_Type()
)
rcQosCosRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosRemarkCos.setStatus("current")
_RcQosCosRemarkDesc_Type = ObjName
_RcQosCosRemarkDesc_Object = MibTableColumn
rcQosCosRemarkDesc = _RcQosCosRemarkDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1, 4),
    _RcQosCosRemarkDesc_Type()
)
rcQosCosRemarkDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosRemarkDesc.setStatus("current")
_RcQosCosRemarkRef_Type = Integer32
_RcQosCosRemarkRef_Object = MibTableColumn
rcQosCosRemarkRef = _RcQosCosRemarkRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1, 5),
    _RcQosCosRemarkRef_Type()
)
rcQosCosRemarkRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosRemarkRef.setStatus("current")
_RcQosCosRemarkStatus_Type = RowStatus
_RcQosCosRemarkStatus_Object = MibTableColumn
rcQosCosRemarkStatus = _RcQosCosRemarkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 29, 1, 6),
    _RcQosCosRemarkStatus_Type()
)
rcQosCosRemarkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosRemarkStatus.setStatus("current")
_RcQosWredProfileTable_Object = MibTable
rcQosWredProfileTable = _RcQosWredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30)
)
if mibBuilder.loadTexts:
    rcQosWredProfileTable.setStatus("current")
_RcQosWredProfileEntry_Object = MibTableRow
rcQosWredProfileEntry = _RcQosWredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1)
)
rcQosWredProfileEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosWredProfileIndex"),
)
if mibBuilder.loadTexts:
    rcQosWredProfileEntry.setStatus("current")


class _RcQosWredProfileIndex_Type(Integer32):
    """Custom type rcQosWredProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosWredProfileIndex_Type.__name__ = "Integer32"
_RcQosWredProfileIndex_Object = MibTableColumn
rcQosWredProfileIndex = _RcQosWredProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 1),
    _RcQosWredProfileIndex_Type()
)
rcQosWredProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosWredProfileIndex.setStatus("current")
_RcQosWredProfileGreenDropStartPoint_Type = Integer32
_RcQosWredProfileGreenDropStartPoint_Object = MibTableColumn
rcQosWredProfileGreenDropStartPoint = _RcQosWredProfileGreenDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 2),
    _RcQosWredProfileGreenDropStartPoint_Type()
)
rcQosWredProfileGreenDropStartPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileGreenDropStartPoint.setStatus("current")
_RcQosWredProfileGreenDropEndPoint_Type = Integer32
_RcQosWredProfileGreenDropEndPoint_Object = MibTableColumn
rcQosWredProfileGreenDropEndPoint = _RcQosWredProfileGreenDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 3),
    _RcQosWredProfileGreenDropEndPoint_Type()
)
rcQosWredProfileGreenDropEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileGreenDropEndPoint.setStatus("current")
_RcQosWredProfileGreenDropProbability_Type = Integer32
_RcQosWredProfileGreenDropProbability_Object = MibTableColumn
rcQosWredProfileGreenDropProbability = _RcQosWredProfileGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 4),
    _RcQosWredProfileGreenDropProbability_Type()
)
rcQosWredProfileGreenDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileGreenDropProbability.setStatus("current")
_RcQosWredProfileYellowDropStartPoint_Type = Integer32
_RcQosWredProfileYellowDropStartPoint_Object = MibTableColumn
rcQosWredProfileYellowDropStartPoint = _RcQosWredProfileYellowDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 5),
    _RcQosWredProfileYellowDropStartPoint_Type()
)
rcQosWredProfileYellowDropStartPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileYellowDropStartPoint.setStatus("current")
_RcQosWredProfileYellowDropEndPoint_Type = Integer32
_RcQosWredProfileYellowDropEndPoint_Object = MibTableColumn
rcQosWredProfileYellowDropEndPoint = _RcQosWredProfileYellowDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 6),
    _RcQosWredProfileYellowDropEndPoint_Type()
)
rcQosWredProfileYellowDropEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileYellowDropEndPoint.setStatus("current")
_RcQosWredProfileYellowDropProbability_Type = Integer32
_RcQosWredProfileYellowDropProbability_Object = MibTableColumn
rcQosWredProfileYellowDropProbability = _RcQosWredProfileYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 7),
    _RcQosWredProfileYellowDropProbability_Type()
)
rcQosWredProfileYellowDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileYellowDropProbability.setStatus("current")
_RcQosWredProfileRedDropStartPoint_Type = Integer32
_RcQosWredProfileRedDropStartPoint_Object = MibTableColumn
rcQosWredProfileRedDropStartPoint = _RcQosWredProfileRedDropStartPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 8),
    _RcQosWredProfileRedDropStartPoint_Type()
)
rcQosWredProfileRedDropStartPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileRedDropStartPoint.setStatus("current")
_RcQosWredProfileRedDropEndPoint_Type = Integer32
_RcQosWredProfileRedDropEndPoint_Object = MibTableColumn
rcQosWredProfileRedDropEndPoint = _RcQosWredProfileRedDropEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 9),
    _RcQosWredProfileRedDropEndPoint_Type()
)
rcQosWredProfileRedDropEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileRedDropEndPoint.setStatus("current")
_RcQosWredProfileRedDropProbability_Type = Integer32
_RcQosWredProfileRedDropProbability_Object = MibTableColumn
rcQosWredProfileRedDropProbability = _RcQosWredProfileRedDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 10),
    _RcQosWredProfileRedDropProbability_Type()
)
rcQosWredProfileRedDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileRedDropProbability.setStatus("current")
_RcQosWredProfileDesc_Type = ObjName
_RcQosWredProfileDesc_Object = MibTableColumn
rcQosWredProfileDesc = _RcQosWredProfileDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 11),
    _RcQosWredProfileDesc_Type()
)
rcQosWredProfileDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileDesc.setStatus("current")
_RcQosWredProfileRef_Type = Integer32
_RcQosWredProfileRef_Object = MibTableColumn
rcQosWredProfileRef = _RcQosWredProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 12),
    _RcQosWredProfileRef_Type()
)
rcQosWredProfileRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileRef.setStatus("current")
_RcQosWredProfileStatus_Type = RowStatus
_RcQosWredProfileStatus_Object = MibTableColumn
rcQosWredProfileStatus = _RcQosWredProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 30, 1, 13),
    _RcQosWredProfileStatus_Type()
)
rcQosWredProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosWredProfileStatus.setStatus("current")
_RcQosGloWredProfileTable_Object = MibTable
rcQosGloWredProfileTable = _RcQosGloWredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 31)
)
if mibBuilder.loadTexts:
    rcQosGloWredProfileTable.setStatus("current")
_RcQosGloWredProfileEntry_Object = MibTableRow
rcQosGloWredProfileEntry = _RcQosGloWredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 31, 1)
)
rcQosGloWredProfileEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosGloWredProfileQueueId"),
)
if mibBuilder.loadTexts:
    rcQosGloWredProfileEntry.setStatus("current")
_RcQosGloWredProfileQueueId_Type = Integer32
_RcQosGloWredProfileQueueId_Object = MibTableColumn
rcQosGloWredProfileQueueId = _RcQosGloWredProfileQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 31, 1, 1),
    _RcQosGloWredProfileQueueId_Type()
)
rcQosGloWredProfileQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosGloWredProfileQueueId.setStatus("current")


class _RcQosGloWredProfileIndex_Type(Integer32):
    """Custom type rcQosGloWredProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosGloWredProfileIndex_Type.__name__ = "Integer32"
_RcQosGloWredProfileIndex_Object = MibTableColumn
rcQosGloWredProfileIndex = _RcQosGloWredProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 31, 1, 2),
    _RcQosGloWredProfileIndex_Type()
)
rcQosGloWredProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosGloWredProfileIndex.setStatus("current")
_RcQosGloWredProfileStatus_Type = RowStatus
_RcQosGloWredProfileStatus_Object = MibTableColumn
rcQosGloWredProfileStatus = _RcQosGloWredProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 31, 1, 3),
    _RcQosGloWredProfileStatus_Type()
)
rcQosGloWredProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosGloWredProfileStatus.setStatus("current")
_RcQosPortWredProfileTable_Object = MibTable
rcQosPortWredProfileTable = _RcQosPortWredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 32)
)
if mibBuilder.loadTexts:
    rcQosPortWredProfileTable.setStatus("current")
_RcQosPortWredProfileEntry_Object = MibTableRow
rcQosPortWredProfileEntry = _RcQosPortWredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 32, 1)
)
rcQosPortWredProfileEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPortWredProfilePortId"),
    (0, "RAISECOM-QOS-MIB", "rcQosPortWredProfileQueueId"),
)
if mibBuilder.loadTexts:
    rcQosPortWredProfileEntry.setStatus("current")
_RcQosPortWredProfilePortId_Type = Integer32
_RcQosPortWredProfilePortId_Object = MibTableColumn
rcQosPortWredProfilePortId = _RcQosPortWredProfilePortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 32, 1, 1),
    _RcQosPortWredProfilePortId_Type()
)
rcQosPortWredProfilePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortWredProfilePortId.setStatus("current")
_RcQosPortWredProfileQueueId_Type = Integer32
_RcQosPortWredProfileQueueId_Object = MibTableColumn
rcQosPortWredProfileQueueId = _RcQosPortWredProfileQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 32, 1, 2),
    _RcQosPortWredProfileQueueId_Type()
)
rcQosPortWredProfileQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPortWredProfileQueueId.setStatus("current")


class _RcQosPortWredProfileIndex_Type(Integer32):
    """Custom type rcQosPortWredProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcQosPortWredProfileIndex_Type.__name__ = "Integer32"
_RcQosPortWredProfileIndex_Object = MibTableColumn
rcQosPortWredProfileIndex = _RcQosPortWredProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 32, 1, 3),
    _RcQosPortWredProfileIndex_Type()
)
rcQosPortWredProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPortWredProfileIndex.setStatus("current")
_RcQosPortWredProfileStatus_Type = RowStatus
_RcQosPortWredProfileStatus_Object = MibTableColumn
rcQosPortWredProfileStatus = _RcQosPortWredProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 1, 32, 1, 4),
    _RcQosPortWredProfileStatus_Type()
)
rcQosPortWredProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPortWredProfileStatus.setStatus("current")
_RaisecomQosTrafficClass_ObjectIdentity = ObjectIdentity
raisecomQosTrafficClass = _RaisecomQosTrafficClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2)
)
_RcPolicyEnable_Type = EnableVar
_RcPolicyEnable_Object = MibScalar
rcPolicyEnable = _RcPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 1),
    _RcPolicyEnable_Type()
)
rcPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPolicyEnable.setStatus("current")
_RcQosServicePolicyTable_Object = MibTable
rcQosServicePolicyTable = _RcQosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 2)
)
if mibBuilder.loadTexts:
    rcQosServicePolicyTable.setStatus("current")
_RcQosServicePolicyEntry_Object = MibTableRow
rcQosServicePolicyEntry = _RcQosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 2, 1)
)
rcQosServicePolicyEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosServicePolicyIngress"),
)
if mibBuilder.loadTexts:
    rcQosServicePolicyEntry.setStatus("current")
_RcQosServicePolicyIngress_Type = Integer32
_RcQosServicePolicyIngress_Object = MibTableColumn
rcQosServicePolicyIngress = _RcQosServicePolicyIngress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 2, 1, 1),
    _RcQosServicePolicyIngress_Type()
)
rcQosServicePolicyIngress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosServicePolicyIngress.setStatus("current")
_RcQosServicePolicyEgress_Type = PortList
_RcQosServicePolicyEgress_Object = MibTableColumn
rcQosServicePolicyEgress = _RcQosServicePolicyEgress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 2, 1, 2),
    _RcQosServicePolicyEgress_Type()
)
rcQosServicePolicyEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosServicePolicyEgress.setStatus("current")
_RcQosServicePolicyMapName_Type = ObjName
_RcQosServicePolicyMapName_Object = MibTableColumn
rcQosServicePolicyMapName = _RcQosServicePolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 2, 1, 3),
    _RcQosServicePolicyMapName_Type()
)
rcQosServicePolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosServicePolicyMapName.setStatus("current")
_RcQosServicePolicyStatus_Type = RowStatus
_RcQosServicePolicyStatus_Object = MibTableColumn
rcQosServicePolicyStatus = _RcQosServicePolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 2, 1, 4),
    _RcQosServicePolicyStatus_Type()
)
rcQosServicePolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosServicePolicyStatus.setStatus("current")
_RcQosPolicyMapCfgTable_Object = MibTable
rcQosPolicyMapCfgTable = _RcQosPolicyMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 3)
)
if mibBuilder.loadTexts:
    rcQosPolicyMapCfgTable.setStatus("current")
_RcQosPolicyMapCfgEntry_Object = MibTableRow
rcQosPolicyMapCfgEntry = _RcQosPolicyMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 3, 1)
)
rcQosPolicyMapCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPolicyMapName"),
)
if mibBuilder.loadTexts:
    rcQosPolicyMapCfgEntry.setStatus("current")
_RcQosPolicyMapName_Type = ObjName
_RcQosPolicyMapName_Object = MibTableColumn
rcQosPolicyMapName = _RcQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 3, 1, 1),
    _RcQosPolicyMapName_Type()
)
rcQosPolicyMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPolicyMapName.setStatus("current")


class _RcQosPolicyMapDesc_Type(OctetString):
    """Custom type rcQosPolicyMapDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RcQosPolicyMapDesc_Type.__name__ = "OctetString"
_RcQosPolicyMapDesc_Object = MibTableColumn
rcQosPolicyMapDesc = _RcQosPolicyMapDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 3, 1, 2),
    _RcQosPolicyMapDesc_Type()
)
rcQosPolicyMapDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicyMapDesc.setStatus("current")
_RcQosPolicyMapCfgStatus_Type = RowStatus
_RcQosPolicyMapCfgStatus_Object = MibTableColumn
rcQosPolicyMapCfgStatus = _RcQosPolicyMapCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 3, 1, 3),
    _RcQosPolicyMapCfgStatus_Type()
)
rcQosPolicyMapCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicyMapCfgStatus.setStatus("current")


class _RcQosPolicyMapType_Type(Integer32):
    """Custom type rcQosPolicyMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("policy-map", 1),
          ("vlan-policy-map", 2),
          ("cos-policy-map", 3),
          ("pw-policy-map", 4))
    )


_RcQosPolicyMapType_Type.__name__ = "Integer32"
_RcQosPolicyMapType_Object = MibTableColumn
rcQosPolicyMapType = _RcQosPolicyMapType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 3, 1, 4),
    _RcQosPolicyMapType_Type()
)
rcQosPolicyMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicyMapType.setStatus("current")
_RcQosCMCfgTable_Object = MibTable
rcQosCMCfgTable = _RcQosCMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4)
)
if mibBuilder.loadTexts:
    rcQosCMCfgTable.setStatus("current")
_RcQosCMCfgEntry_Object = MibTableRow
rcQosCMCfgEntry = _RcQosCMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1)
)
rcQosCMCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCMName"),
)
if mibBuilder.loadTexts:
    rcQosCMCfgEntry.setStatus("current")
_RcQosCMName_Type = ObjName
_RcQosCMName_Object = MibTableColumn
rcQosCMName = _RcQosCMName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1, 1),
    _RcQosCMName_Type()
)
rcQosCMName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCMName.setStatus("current")


class _RcQosCMDesc_Type(OctetString):
    """Custom type rcQosCMDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RcQosCMDesc_Type.__name__ = "OctetString"
_RcQosCMDesc_Object = MibTableColumn
rcQosCMDesc = _RcQosCMDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1, 2),
    _RcQosCMDesc_Type()
)
rcQosCMDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCMDesc.setStatus("current")


class _RcQosCMMatchType_Type(Integer32):
    """Custom type rcQosCMMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 1),
          ("matchAny", 2))
    )


_RcQosCMMatchType_Type.__name__ = "Integer32"
_RcQosCMMatchType_Object = MibTableColumn
rcQosCMMatchType = _RcQosCMMatchType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1, 3),
    _RcQosCMMatchType_Type()
)
rcQosCMMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCMMatchType.setStatus("current")
_RcQosCMClassID_Type = Integer32
_RcQosCMClassID_Object = MibTableColumn
rcQosCMClassID = _RcQosCMClassID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1, 4),
    _RcQosCMClassID_Type()
)
rcQosCMClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosCMClassID.setStatus("current")
_RcQosCMStatus_Type = RowStatus
_RcQosCMStatus_Object = MibTableColumn
rcQosCMStatus = _RcQosCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1, 5),
    _RcQosCMStatus_Type()
)
rcQosCMStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCMStatus.setStatus("current")
_RcQosCMDoubleTagging_Type = TruthValue
_RcQosCMDoubleTagging_Object = MibTableColumn
rcQosCMDoubleTagging = _RcQosCMDoubleTagging_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 4, 1, 6),
    _RcQosCMDoubleTagging_Type()
)
rcQosCMDoubleTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCMDoubleTagging.setStatus("deprecated")
_RcQosMatchStmtTable_Object = MibTable
rcQosMatchStmtTable = _RcQosMatchStmtTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5)
)
if mibBuilder.loadTexts:
    rcQosMatchStmtTable.setStatus("current")
_RcQosMatchStmtEntry_Object = MibTableRow
rcQosMatchStmtEntry = _RcQosMatchStmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5, 1)
)
rcQosMatchStmtEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosMatchStmtClassName"),
    (0, "RAISECOM-QOS-MIB", "rcQosMatchStmtType"),
    (0, "RAISECOM-QOS-MIB", "rcQosMatchStmtValue"),
)
if mibBuilder.loadTexts:
    rcQosMatchStmtEntry.setStatus("current")
_RcQosMatchStmtClassName_Type = ObjName
_RcQosMatchStmtClassName_Object = MibTableColumn
rcQosMatchStmtClassName = _RcQosMatchStmtClassName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5, 1, 1),
    _RcQosMatchStmtClassName_Type()
)
rcQosMatchStmtClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosMatchStmtClassName.setStatus("current")


class _RcQosMatchStmtType_Type(Integer32):
    """Custom type rcQosMatchStmtType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ip-acl", 1),
          ("mac-acl", 2),
          ("user-acl", 3),
          ("dscp", 4),
          ("ipprecedence", 5),
          ("class", 6),
          ("vlan", 7),
          ("vlan-inner", 8),
          ("cos", 9),
          ("ipv6-acl", 10),
          ("traffic-class", 11),
          ("inner-outer-vlan", 12),
          ("tunnel-label", 13),
          ("tunnel-exp", 14),
          ("vc-label", 15),
          ("vc-exp", 16),
          ("flow-label", 17))
    )


_RcQosMatchStmtType_Type.__name__ = "Integer32"
_RcQosMatchStmtType_Object = MibTableColumn
rcQosMatchStmtType = _RcQosMatchStmtType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5, 1, 2),
    _RcQosMatchStmtType_Type()
)
rcQosMatchStmtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosMatchStmtType.setStatus("current")


class _RcQosMatchStmtValue_Type(Integer32):
    """Custom type rcQosMatchStmtValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosMatchStmtValue_Type.__name__ = "Integer32"
_RcQosMatchStmtValue_Object = MibTableColumn
rcQosMatchStmtValue = _RcQosMatchStmtValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5, 1, 3),
    _RcQosMatchStmtValue_Type()
)
rcQosMatchStmtValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosMatchStmtValue.setStatus("current")
_RcQosMatchStmtSubName_Type = ObjName
_RcQosMatchStmtSubName_Object = MibTableColumn
rcQosMatchStmtSubName = _RcQosMatchStmtSubName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5, 1, 4),
    _RcQosMatchStmtSubName_Type()
)
rcQosMatchStmtSubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosMatchStmtSubName.setStatus("current")
_RcQosMatchStmtStatus_Type = RowStatus
_RcQosMatchStmtStatus_Object = MibTableColumn
rcQosMatchStmtStatus = _RcQosMatchStmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 5, 1, 5),
    _RcQosMatchStmtStatus_Type()
)
rcQosMatchStmtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosMatchStmtStatus.setStatus("current")
_RcQosPolicerCfgTable_Object = MibTable
rcQosPolicerCfgTable = _RcQosPolicerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6)
)
if mibBuilder.loadTexts:
    rcQosPolicerCfgTable.setStatus("current")
_RcQosPolicerCfgEntry_Object = MibTableRow
rcQosPolicerCfgEntry = _RcQosPolicerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1)
)
rcQosPolicerCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosPolicerCfgName"),
)
if mibBuilder.loadTexts:
    rcQosPolicerCfgEntry.setStatus("current")
_RcQosPolicerCfgName_Type = ObjName
_RcQosPolicerCfgName_Object = MibTableColumn
rcQosPolicerCfgName = _RcQosPolicerCfgName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 1),
    _RcQosPolicerCfgName_Type()
)
rcQosPolicerCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosPolicerCfgName.setStatus("current")


class _RcQosPolicerCfgType_Type(Integer32):
    """Custom type rcQosPolicerCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("single-policer", 1),
          ("class-policer", 2),
          ("aggregate-policer", 3),
          ("hierarchy-policer", 4))
    )


_RcQosPolicerCfgType_Type.__name__ = "Integer32"
_RcQosPolicerCfgType_Object = MibTableColumn
rcQosPolicerCfgType = _RcQosPolicerCfgType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 2),
    _RcQosPolicerCfgType_Type()
)
rcQosPolicerCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerCfgType.setStatus("current")


class _RcQosPolicerCfgMode_Type(Integer32):
    """Custom type rcQosPolicerCfgMode based on Integer32"""
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
        *(("flow", 1),
          ("rfc2697", 2),
          ("rfc2698", 3),
          ("rfc4115", 4),
          ("mef", 5),
          ("single", 6),
          ("double", 7))
    )


_RcQosPolicerCfgMode_Type.__name__ = "Integer32"
_RcQosPolicerCfgMode_Object = MibTableColumn
rcQosPolicerCfgMode = _RcQosPolicerCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 3),
    _RcQosPolicerCfgMode_Type()
)
rcQosPolicerCfgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerCfgMode.setStatus("current")


class _RcQosPolicerCfgCIR_Type(Integer32):
    """Custom type rcQosPolicerCfgCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RcQosPolicerCfgCIR_Type.__name__ = "Integer32"
_RcQosPolicerCfgCIR_Object = MibTableColumn
rcQosPolicerCfgCIR = _RcQosPolicerCfgCIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 4),
    _RcQosPolicerCfgCIR_Type()
)
rcQosPolicerCfgCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerCfgCIR.setStatus("current")


class _RcQosPolicerCfgEIR_Type(Integer32):
    """Custom type rcQosPolicerCfgEIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RcQosPolicerCfgEIR_Type.__name__ = "Integer32"
_RcQosPolicerCfgEIR_Object = MibTableColumn
rcQosPolicerCfgEIR = _RcQosPolicerCfgEIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 5),
    _RcQosPolicerCfgEIR_Type()
)
rcQosPolicerCfgEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerCfgEIR.setStatus("current")
_RcQosPolicerCfgCBS_Type = Integer32
_RcQosPolicerCfgCBS_Object = MibTableColumn
rcQosPolicerCfgCBS = _RcQosPolicerCfgCBS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 6),
    _RcQosPolicerCfgCBS_Type()
)
rcQosPolicerCfgCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerCfgCBS.setStatus("current")
_RcQosPolicerCfgEBS_Type = Integer32
_RcQosPolicerCfgEBS_Object = MibTableColumn
rcQosPolicerCfgEBS = _RcQosPolicerCfgEBS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 7),
    _RcQosPolicerCfgEBS_Type()
)
rcQosPolicerCfgEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerCfgEBS.setStatus("current")
_RcQosPolicerGreenActType_Type = Integer32
_RcQosPolicerGreenActType_Object = MibTableColumn
rcQosPolicerGreenActType = _RcQosPolicerGreenActType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 8),
    _RcQosPolicerGreenActType_Type()
)
rcQosPolicerGreenActType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerGreenActType.setStatus("current")


class _RcQosPolicerGreenActDscp_Type(Integer32):
    """Custom type rcQosPolicerGreenActDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosPolicerGreenActDscp_Type.__name__ = "Integer32"
_RcQosPolicerGreenActDscp_Object = MibTableColumn
rcQosPolicerGreenActDscp = _RcQosPolicerGreenActDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 9),
    _RcQosPolicerGreenActDscp_Type()
)
rcQosPolicerGreenActDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerGreenActDscp.setStatus("current")


class _RcQosPolicerGreenActCos_Type(Integer32):
    """Custom type rcQosPolicerGreenActCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPolicerGreenActCos_Type.__name__ = "Integer32"
_RcQosPolicerGreenActCos_Object = MibTableColumn
rcQosPolicerGreenActCos = _RcQosPolicerGreenActCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 10),
    _RcQosPolicerGreenActCos_Type()
)
rcQosPolicerGreenActCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerGreenActCos.setStatus("current")


class _RcQosPolicerGreenActLocalPrio_Type(Integer32):
    """Custom type rcQosPolicerGreenActLocalPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPolicerGreenActLocalPrio_Type.__name__ = "Integer32"
_RcQosPolicerGreenActLocalPrio_Object = MibTableColumn
rcQosPolicerGreenActLocalPrio = _RcQosPolicerGreenActLocalPrio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 11),
    _RcQosPolicerGreenActLocalPrio_Type()
)
rcQosPolicerGreenActLocalPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerGreenActLocalPrio.setStatus("current")


class _RcQosPolicerGreenActColor_Type(Integer32):
    """Custom type rcQosPolicerGreenActColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("yellow", 1),
          ("red", 2))
    )


_RcQosPolicerGreenActColor_Type.__name__ = "Integer32"
_RcQosPolicerGreenActColor_Object = MibTableColumn
rcQosPolicerGreenActColor = _RcQosPolicerGreenActColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 12),
    _RcQosPolicerGreenActColor_Type()
)
rcQosPolicerGreenActColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerGreenActColor.setStatus("current")
_RcQosPolicerGreenActCopytoCpu_Type = TruthValue
_RcQosPolicerGreenActCopytoCpu_Object = MibTableColumn
rcQosPolicerGreenActCopytoCpu = _RcQosPolicerGreenActCopytoCpu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 13),
    _RcQosPolicerGreenActCopytoCpu_Type()
)
rcQosPolicerGreenActCopytoCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerGreenActCopytoCpu.setStatus("current")
_RcQosPolicerYellowActType_Type = Integer32
_RcQosPolicerYellowActType_Object = MibTableColumn
rcQosPolicerYellowActType = _RcQosPolicerYellowActType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 14),
    _RcQosPolicerYellowActType_Type()
)
rcQosPolicerYellowActType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerYellowActType.setStatus("current")


class _RcQosPolicerYellowActDscp_Type(Integer32):
    """Custom type rcQosPolicerYellowActDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosPolicerYellowActDscp_Type.__name__ = "Integer32"
_RcQosPolicerYellowActDscp_Object = MibTableColumn
rcQosPolicerYellowActDscp = _RcQosPolicerYellowActDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 15),
    _RcQosPolicerYellowActDscp_Type()
)
rcQosPolicerYellowActDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerYellowActDscp.setStatus("current")


class _RcQosPolicerYellowActCos_Type(Integer32):
    """Custom type rcQosPolicerYellowActCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPolicerYellowActCos_Type.__name__ = "Integer32"
_RcQosPolicerYellowActCos_Object = MibTableColumn
rcQosPolicerYellowActCos = _RcQosPolicerYellowActCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 16),
    _RcQosPolicerYellowActCos_Type()
)
rcQosPolicerYellowActCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerYellowActCos.setStatus("current")


class _RcQosPolicerYellowActLocalPrio_Type(Integer32):
    """Custom type rcQosPolicerYellowActLocalPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPolicerYellowActLocalPrio_Type.__name__ = "Integer32"
_RcQosPolicerYellowActLocalPrio_Object = MibTableColumn
rcQosPolicerYellowActLocalPrio = _RcQosPolicerYellowActLocalPrio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 17),
    _RcQosPolicerYellowActLocalPrio_Type()
)
rcQosPolicerYellowActLocalPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerYellowActLocalPrio.setStatus("current")


class _RcQosPolicerYellowActColor_Type(Integer32):
    """Custom type rcQosPolicerYellowActColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("green", 1),
          ("red", 2))
    )


_RcQosPolicerYellowActColor_Type.__name__ = "Integer32"
_RcQosPolicerYellowActColor_Object = MibTableColumn
rcQosPolicerYellowActColor = _RcQosPolicerYellowActColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 18),
    _RcQosPolicerYellowActColor_Type()
)
rcQosPolicerYellowActColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerYellowActColor.setStatus("current")
_RcQosPolicerYellowActCopytoCpu_Type = TruthValue
_RcQosPolicerYellowActCopytoCpu_Object = MibTableColumn
rcQosPolicerYellowActCopytoCpu = _RcQosPolicerYellowActCopytoCpu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 19),
    _RcQosPolicerYellowActCopytoCpu_Type()
)
rcQosPolicerYellowActCopytoCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerYellowActCopytoCpu.setStatus("current")
_RcQosPolicerRedActType_Type = Integer32
_RcQosPolicerRedActType_Object = MibTableColumn
rcQosPolicerRedActType = _RcQosPolicerRedActType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 20),
    _RcQosPolicerRedActType_Type()
)
rcQosPolicerRedActType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerRedActType.setStatus("current")


class _RcQosPolicerRedActDscp_Type(Integer32):
    """Custom type rcQosPolicerRedActDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosPolicerRedActDscp_Type.__name__ = "Integer32"
_RcQosPolicerRedActDscp_Object = MibTableColumn
rcQosPolicerRedActDscp = _RcQosPolicerRedActDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 21),
    _RcQosPolicerRedActDscp_Type()
)
rcQosPolicerRedActDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerRedActDscp.setStatus("current")


class _RcQosPolicerRedActCos_Type(Integer32):
    """Custom type rcQosPolicerRedActCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPolicerRedActCos_Type.__name__ = "Integer32"
_RcQosPolicerRedActCos_Object = MibTableColumn
rcQosPolicerRedActCos = _RcQosPolicerRedActCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 22),
    _RcQosPolicerRedActCos_Type()
)
rcQosPolicerRedActCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerRedActCos.setStatus("current")


class _RcQosPolicerRedActLocalPrio_Type(Integer32):
    """Custom type rcQosPolicerRedActLocalPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosPolicerRedActLocalPrio_Type.__name__ = "Integer32"
_RcQosPolicerRedActLocalPrio_Object = MibTableColumn
rcQosPolicerRedActLocalPrio = _RcQosPolicerRedActLocalPrio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 23),
    _RcQosPolicerRedActLocalPrio_Type()
)
rcQosPolicerRedActLocalPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerRedActLocalPrio.setStatus("current")


class _RcQosPolicerRedActColor_Type(Integer32):
    """Custom type rcQosPolicerRedActColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("green", 1),
          ("yellow", 2))
    )


_RcQosPolicerRedActColor_Type.__name__ = "Integer32"
_RcQosPolicerRedActColor_Object = MibTableColumn
rcQosPolicerRedActColor = _RcQosPolicerRedActColor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 24),
    _RcQosPolicerRedActColor_Type()
)
rcQosPolicerRedActColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerRedActColor.setStatus("current")
_RcQosPolicerRedActCopytoCpu_Type = TruthValue
_RcQosPolicerRedActCopytoCpu_Object = MibTableColumn
rcQosPolicerRedActCopytoCpu = _RcQosPolicerRedActCopytoCpu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 25),
    _RcQosPolicerRedActCopytoCpu_Type()
)
rcQosPolicerRedActCopytoCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerRedActCopytoCpu.setStatus("current")


class _RcQosPolicerColorMode_Type(Integer32):
    """Custom type rcQosPolicerColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("color-blind", 0),
          ("color-aware", 1))
    )


_RcQosPolicerColorMode_Type.__name__ = "Integer32"
_RcQosPolicerColorMode_Object = MibTableColumn
rcQosPolicerColorMode = _RcQosPolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 26),
    _RcQosPolicerColorMode_Type()
)
rcQosPolicerColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerColorMode.setStatus("current")
_RcQoSPolicerRef_Type = Integer32
_RcQoSPolicerRef_Object = MibTableColumn
rcQoSPolicerRef = _RcQoSPolicerRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 27),
    _RcQoSPolicerRef_Type()
)
rcQoSPolicerRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQoSPolicerRef.setStatus("current")
_RcQosPolicerStatus_Type = RowStatus
_RcQosPolicerStatus_Object = MibTableColumn
rcQosPolicerStatus = _RcQosPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 6, 1, 28),
    _RcQosPolicerStatus_Type()
)
rcQosPolicerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosPolicerStatus.setStatus("current")
_RcQosActionCfgTable_Object = MibTable
rcQosActionCfgTable = _RcQosActionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7)
)
if mibBuilder.loadTexts:
    rcQosActionCfgTable.setStatus("current")
_RcQosActionCfgEntry_Object = MibTableRow
rcQosActionCfgEntry = _RcQosActionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1)
)
rcQosActionCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosActionPmapName"),
    (0, "RAISECOM-QOS-MIB", "rcQosActionCmapName"),
)
if mibBuilder.loadTexts:
    rcQosActionCfgEntry.setStatus("current")
_RcQosActionPmapName_Type = ObjName
_RcQosActionPmapName_Object = MibTableColumn
rcQosActionPmapName = _RcQosActionPmapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 1),
    _RcQosActionPmapName_Type()
)
rcQosActionPmapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosActionPmapName.setStatus("current")
_RcQosActionCmapName_Type = ObjName
_RcQosActionCmapName_Object = MibTableColumn
rcQosActionCmapName = _RcQosActionCmapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 2),
    _RcQosActionCmapName_Type()
)
rcQosActionCmapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosActionCmapName.setStatus("current")


class _RcQosActionType_Type(Integer32):
    """Custom type rcQosActionType based on Integer32"""
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
        *(("none", 0),
          ("set-dscp", 1),
          ("set-cos", 2),
          ("set-ipprec", 3))
    )


_RcQosActionType_Type.__name__ = "Integer32"
_RcQosActionType_Object = MibTableColumn
rcQosActionType = _RcQosActionType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 3),
    _RcQosActionType_Type()
)
rcQosActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionType.setStatus("current")


class _RcQosActionSetValue_Type(Integer32):
    """Custom type rcQosActionSetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQosActionSetValue_Type.__name__ = "Integer32"
_RcQosActionSetValue_Object = MibTableColumn
rcQosActionSetValue = _RcQosActionSetValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 4),
    _RcQosActionSetValue_Type()
)
rcQosActionSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetValue.setStatus("current")
_RcQosActionPoliceName_Type = ObjName
_RcQosActionPoliceName_Object = MibTableColumn
rcQosActionPoliceName = _RcQosActionPoliceName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 5),
    _RcQosActionPoliceName_Type()
)
rcQosActionPoliceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionPoliceName.setStatus("current")
_RcQosActionStatsEnable_Type = EnableVar
_RcQosActionStatsEnable_Object = MibTableColumn
rcQosActionStatsEnable = _RcQosActionStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 6),
    _RcQosActionStatsEnable_Type()
)
rcQosActionStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionStatsEnable.setStatus("current")
_RcQosActionStatus_Type = RowStatus
_RcQosActionStatus_Object = MibTableColumn
rcQosActionStatus = _RcQosActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 7),
    _RcQosActionStatus_Type()
)
rcQosActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionStatus.setStatus("current")
_RcQosActionRedirectPort_Type = Integer32
_RcQosActionRedirectPort_Object = MibTableColumn
rcQosActionRedirectPort = _RcQosActionRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 8),
    _RcQosActionRedirectPort_Type()
)
rcQosActionRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionRedirectPort.setStatus("current")


class _RcQosActionSetVlan_Type(Integer32):
    """Custom type rcQosActionSetVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosActionSetVlan_Type.__name__ = "Integer32"
_RcQosActionSetVlan_Object = MibTableColumn
rcQosActionSetVlan = _RcQosActionSetVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 9),
    _RcQosActionSetVlan_Type()
)
rcQosActionSetVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetVlan.setStatus("current")


class _RcQosActionSetInnerVlan_Type(Integer32):
    """Custom type rcQosActionSetInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosActionSetInnerVlan_Type.__name__ = "Integer32"
_RcQosActionSetInnerVlan_Object = MibTableColumn
rcQosActionSetInnerVlan = _RcQosActionSetInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 10),
    _RcQosActionSetInnerVlan_Type()
)
rcQosActionSetInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetInnerVlan.setStatus("current")


class _RcQosActionAddOuterVlan_Type(Integer32):
    """Custom type rcQosActionAddOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosActionAddOuterVlan_Type.__name__ = "Integer32"
_RcQosActionAddOuterVlan_Object = MibTableColumn
rcQosActionAddOuterVlan = _RcQosActionAddOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 11),
    _RcQosActionAddOuterVlan_Type()
)
rcQosActionAddOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionAddOuterVlan.setStatus("current")
_RcQosActionCopyToMirror_Type = EnableVar
_RcQosActionCopyToMirror_Object = MibTableColumn
rcQosActionCopyToMirror = _RcQosActionCopyToMirror_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 12),
    _RcQosActionCopyToMirror_Type()
)
rcQosActionCopyToMirror.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionCopyToMirror.setStatus("current")
_RcQosActionMirrorToPort_Type = Integer32
_RcQosActionMirrorToPort_Object = MibTableColumn
rcQosActionMirrorToPort = _RcQosActionMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 13),
    _RcQosActionMirrorToPort_Type()
)
rcQosActionMirrorToPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionMirrorToPort.setStatus("current")


class _RcQosActionSetLocalPriority_Type(Integer32):
    """Custom type rcQosActionSetLocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcQosActionSetLocalPriority_Type.__name__ = "Integer32"
_RcQosActionSetLocalPriority_Object = MibTableColumn
rcQosActionSetLocalPriority = _RcQosActionSetLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 14),
    _RcQosActionSetLocalPriority_Type()
)
rcQosActionSetLocalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetLocalPriority.setStatus("current")
_RcQosActionHierarchyPoliceName_Type = ObjName
_RcQosActionHierarchyPoliceName_Object = MibTableColumn
rcQosActionHierarchyPoliceName = _RcQosActionHierarchyPoliceName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 15),
    _RcQosActionHierarchyPoliceName_Type()
)
rcQosActionHierarchyPoliceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionHierarchyPoliceName.setStatus("current")


class _RcQosActionSetIpPrece_Type(Integer32):
    """Custom type rcQosActionSetIpPrece based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcQosActionSetIpPrece_Type.__name__ = "Integer32"
_RcQosActionSetIpPrece_Object = MibTableColumn
rcQosActionSetIpPrece = _RcQosActionSetIpPrece_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 16),
    _RcQosActionSetIpPrece_Type()
)
rcQosActionSetIpPrece.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetIpPrece.setStatus("current")


class _RcQosActionSetIpDscp_Type(Integer32):
    """Custom type rcQosActionSetIpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RcQosActionSetIpDscp_Type.__name__ = "Integer32"
_RcQosActionSetIpDscp_Object = MibTableColumn
rcQosActionSetIpDscp = _RcQosActionSetIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 17),
    _RcQosActionSetIpDscp_Type()
)
rcQosActionSetIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetIpDscp.setStatus("current")


class _RcQosActionSetCos_Type(Integer32):
    """Custom type rcQosActionSetCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcQosActionSetCos_Type.__name__ = "Integer32"
_RcQosActionSetCos_Object = MibTableColumn
rcQosActionSetCos = _RcQosActionSetCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 18),
    _RcQosActionSetCos_Type()
)
rcQosActionSetCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetCos.setStatus("current")


class _RcQosActionSetIPAddressType_Type(Integer32):
    """Custom type rcQosActionSetIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RcQosActionSetIPAddressType_Type.__name__ = "Integer32"
_RcQosActionSetIPAddressType_Object = MibTableColumn
rcQosActionSetIPAddressType = _RcQosActionSetIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 19),
    _RcQosActionSetIPAddressType_Type()
)
rcQosActionSetIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetIPAddressType.setStatus("current")
_RcQosActionSetIPAddress_Type = InetAddress
_RcQosActionSetIPAddress_Object = MibTableColumn
rcQosActionSetIPAddress = _RcQosActionSetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 20),
    _RcQosActionSetIPAddress_Type()
)
rcQosActionSetIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionSetIPAddress.setStatus("current")


class _RcQosActionCopyToMirrorSession_Type(Integer32):
    """Custom type rcQosActionCopyToMirrorSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RcQosActionCopyToMirrorSession_Type.__name__ = "Integer32"
_RcQosActionCopyToMirrorSession_Object = MibTableColumn
rcQosActionCopyToMirrorSession = _RcQosActionCopyToMirrorSession_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 7, 1, 21),
    _RcQosActionCopyToMirrorSession_Type()
)
rcQosActionCopyToMirrorSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosActionCopyToMirrorSession.setStatus("current")
_RcQosServicePolicyEgressTable_Object = MibTable
rcQosServicePolicyEgressTable = _RcQosServicePolicyEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 8)
)
if mibBuilder.loadTexts:
    rcQosServicePolicyEgressTable.setStatus("current")
_RcQosServicePolicyEgressEntry_Object = MibTableRow
rcQosServicePolicyEgressEntry = _RcQosServicePolicyEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 8, 1)
)
rcQosServicePolicyEgressEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosServicePolicyEgressIndex"),
)
if mibBuilder.loadTexts:
    rcQosServicePolicyEgressEntry.setStatus("current")
_RcQosServicePolicyEgressIndex_Type = Integer32
_RcQosServicePolicyEgressIndex_Object = MibTableColumn
rcQosServicePolicyEgressIndex = _RcQosServicePolicyEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 8, 1, 1),
    _RcQosServicePolicyEgressIndex_Type()
)
rcQosServicePolicyEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosServicePolicyEgressIndex.setStatus("current")
_RcQosServicePolicyEgressMapName_Type = ObjName
_RcQosServicePolicyEgressMapName_Object = MibTableColumn
rcQosServicePolicyEgressMapName = _RcQosServicePolicyEgressMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 8, 1, 2),
    _RcQosServicePolicyEgressMapName_Type()
)
rcQosServicePolicyEgressMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosServicePolicyEgressMapName.setStatus("current")
_RcQosServicePolicyEgressStatus_Type = RowStatus
_RcQosServicePolicyEgressStatus_Object = MibTableColumn
rcQosServicePolicyEgressStatus = _RcQosServicePolicyEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 8, 1, 3),
    _RcQosServicePolicyEgressStatus_Type()
)
rcQosServicePolicyEgressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosServicePolicyEgressStatus.setStatus("current")
_RcQosCosServicePolicyTable_Object = MibTable
rcQosCosServicePolicyTable = _RcQosCosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 9)
)
if mibBuilder.loadTexts:
    rcQosCosServicePolicyTable.setStatus("current")
_RcQosCosServicePolicyEntry_Object = MibTableRow
rcQosCosServicePolicyEntry = _RcQosCosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 9, 1)
)
rcQosCosServicePolicyEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCosServicePolicyPort"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosServicePolicyVlan"),
)
if mibBuilder.loadTexts:
    rcQosCosServicePolicyEntry.setStatus("current")
_RcQosCosServicePolicyPort_Type = Integer32
_RcQosCosServicePolicyPort_Object = MibTableColumn
rcQosCosServicePolicyPort = _RcQosCosServicePolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 9, 1, 1),
    _RcQosCosServicePolicyPort_Type()
)
rcQosCosServicePolicyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosServicePolicyPort.setStatus("current")
_RcQosCosServicePolicyVlan_Type = Integer32
_RcQosCosServicePolicyVlan_Object = MibTableColumn
rcQosCosServicePolicyVlan = _RcQosCosServicePolicyVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 9, 1, 2),
    _RcQosCosServicePolicyVlan_Type()
)
rcQosCosServicePolicyVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosServicePolicyVlan.setStatus("current")


class _RcQosCosServicePolicyMapName_Type(OctetString):
    """Custom type rcQosCosServicePolicyMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcQosCosServicePolicyMapName_Type.__name__ = "OctetString"
_RcQosCosServicePolicyMapName_Object = MibTableColumn
rcQosCosServicePolicyMapName = _RcQosCosServicePolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 9, 1, 3),
    _RcQosCosServicePolicyMapName_Type()
)
rcQosCosServicePolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosServicePolicyMapName.setStatus("current")
_RcQosCosServicePolicyRowStatus_Type = RowStatus
_RcQosCosServicePolicyRowStatus_Object = MibTableColumn
rcQosCosServicePolicyRowStatus = _RcQosCosServicePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 9, 1, 4),
    _RcQosCosServicePolicyRowStatus_Type()
)
rcQosCosServicePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosServicePolicyRowStatus.setStatus("current")
_RcQosVlanPolicyTable_Object = MibTable
rcQosVlanPolicyTable = _RcQosVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 10)
)
if mibBuilder.loadTexts:
    rcQosVlanPolicyTable.setStatus("current")
_RcQosVlanPolicyEntry_Object = MibTableRow
rcQosVlanPolicyEntry = _RcQosVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 10, 1)
)
rcQosVlanPolicyEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosVlanPolicyPmapName"),
    (0, "RAISECOM-QOS-MIB", "rcQosVlanPolicyVlan"),
)
if mibBuilder.loadTexts:
    rcQosVlanPolicyEntry.setStatus("current")


class _RcQosVlanPolicyPmapName_Type(OctetString):
    """Custom type rcQosVlanPolicyPmapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcQosVlanPolicyPmapName_Type.__name__ = "OctetString"
_RcQosVlanPolicyPmapName_Object = MibTableColumn
rcQosVlanPolicyPmapName = _RcQosVlanPolicyPmapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 10, 1, 1),
    _RcQosVlanPolicyPmapName_Type()
)
rcQosVlanPolicyPmapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosVlanPolicyPmapName.setStatus("current")


class _RcQosVlanPolicyVlan_Type(Integer32):
    """Custom type rcQosVlanPolicyVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosVlanPolicyVlan_Type.__name__ = "Integer32"
_RcQosVlanPolicyVlan_Object = MibTableColumn
rcQosVlanPolicyVlan = _RcQosVlanPolicyVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 10, 1, 2),
    _RcQosVlanPolicyVlan_Type()
)
rcQosVlanPolicyVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosVlanPolicyVlan.setStatus("current")


class _RcQosVlanPolicyPolicerName_Type(OctetString):
    """Custom type rcQosVlanPolicyPolicerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcQosVlanPolicyPolicerName_Type.__name__ = "OctetString"
_RcQosVlanPolicyPolicerName_Object = MibTableColumn
rcQosVlanPolicyPolicerName = _RcQosVlanPolicyPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 10, 1, 3),
    _RcQosVlanPolicyPolicerName_Type()
)
rcQosVlanPolicyPolicerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosVlanPolicyPolicerName.setStatus("current")
_RcQosVlanPolicyRowStatus_Type = RowStatus
_RcQosVlanPolicyRowStatus_Object = MibTableColumn
rcQosVlanPolicyRowStatus = _RcQosVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 10, 1, 4),
    _RcQosVlanPolicyRowStatus_Type()
)
rcQosVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosVlanPolicyRowStatus.setStatus("current")
_RcQosCosPolicyTable_Object = MibTable
rcQosCosPolicyTable = _RcQosCosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 11)
)
if mibBuilder.loadTexts:
    rcQosCosPolicyTable.setStatus("current")
_RcQosCosPolicyEntry_Object = MibTableRow
rcQosCosPolicyEntry = _RcQosCosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 11, 1)
)
rcQosCosPolicyEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCosPolicyPmapName"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosPolicyCos"),
)
if mibBuilder.loadTexts:
    rcQosCosPolicyEntry.setStatus("current")


class _RcQosCosPolicyPmapName_Type(OctetString):
    """Custom type rcQosCosPolicyPmapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcQosCosPolicyPmapName_Type.__name__ = "OctetString"
_RcQosCosPolicyPmapName_Object = MibTableColumn
rcQosCosPolicyPmapName = _RcQosCosPolicyPmapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 11, 1, 1),
    _RcQosCosPolicyPmapName_Type()
)
rcQosCosPolicyPmapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosPolicyPmapName.setStatus("current")


class _RcQosCosPolicyCos_Type(Integer32):
    """Custom type rcQosCosPolicyCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcQosCosPolicyCos_Type.__name__ = "Integer32"
_RcQosCosPolicyCos_Object = MibTableColumn
rcQosCosPolicyCos = _RcQosCosPolicyCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 11, 1, 2),
    _RcQosCosPolicyCos_Type()
)
rcQosCosPolicyCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosPolicyCos.setStatus("current")


class _RcQosCosPolicyPolicerName_Type(OctetString):
    """Custom type rcQosCosPolicyPolicerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcQosCosPolicyPolicerName_Type.__name__ = "OctetString"
_RcQosCosPolicyPolicerName_Object = MibTableColumn
rcQosCosPolicyPolicerName = _RcQosCosPolicyPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 11, 1, 3),
    _RcQosCosPolicyPolicerName_Type()
)
rcQosCosPolicyPolicerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosPolicyPolicerName.setStatus("current")
_RcQosCosPolicyRowStatus_Type = RowStatus
_RcQosCosPolicyRowStatus_Object = MibTableColumn
rcQosCosPolicyRowStatus = _RcQosCosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 11, 1, 4),
    _RcQosCosPolicyRowStatus_Type()
)
rcQosCosPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosPolicyRowStatus.setStatus("current")
_RcQosBandwidthProfileCfgTable_Object = MibTable
rcQosBandwidthProfileCfgTable = _RcQosBandwidthProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12)
)
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgTable.setStatus("current")
_RcQosBandwidthProfileCfgEntry_Object = MibTableRow
rcQosBandwidthProfileCfgEntry = _RcQosBandwidthProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1)
)
rcQosBandwidthProfileCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthProfileCfgIndex"),
)
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgEntry.setStatus("current")
_RcQosBandwidthProfileCfgIndex_Type = Integer32
_RcQosBandwidthProfileCfgIndex_Object = MibTableColumn
rcQosBandwidthProfileCfgIndex = _RcQosBandwidthProfileCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 1),
    _RcQosBandwidthProfileCfgIndex_Type()
)
rcQosBandwidthProfileCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgIndex.setStatus("current")


class _RcQosBandwidthProfileCfgCIR_Type(Integer32):
    """Custom type rcQosBandwidthProfileCfgCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RcQosBandwidthProfileCfgCIR_Type.__name__ = "Integer32"
_RcQosBandwidthProfileCfgCIR_Object = MibTableColumn
rcQosBandwidthProfileCfgCIR = _RcQosBandwidthProfileCfgCIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 2),
    _RcQosBandwidthProfileCfgCIR_Type()
)
rcQosBandwidthProfileCfgCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgCIR.setStatus("current")


class _RcQosBandwidthProfileCfgEIR_Type(Integer32):
    """Custom type rcQosBandwidthProfileCfgEIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RcQosBandwidthProfileCfgEIR_Type.__name__ = "Integer32"
_RcQosBandwidthProfileCfgEIR_Object = MibTableColumn
rcQosBandwidthProfileCfgEIR = _RcQosBandwidthProfileCfgEIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 3),
    _RcQosBandwidthProfileCfgEIR_Type()
)
rcQosBandwidthProfileCfgEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgEIR.setStatus("current")
_RcQosBandwidthProfileCfgCBS_Type = Integer32
_RcQosBandwidthProfileCfgCBS_Object = MibTableColumn
rcQosBandwidthProfileCfgCBS = _RcQosBandwidthProfileCfgCBS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 4),
    _RcQosBandwidthProfileCfgCBS_Type()
)
rcQosBandwidthProfileCfgCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgCBS.setStatus("current")
_RcQosBandwidthProfileCfgEBS_Type = Integer32
_RcQosBandwidthProfileCfgEBS_Object = MibTableColumn
rcQosBandwidthProfileCfgEBS = _RcQosBandwidthProfileCfgEBS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 5),
    _RcQosBandwidthProfileCfgEBS_Type()
)
rcQosBandwidthProfileCfgEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCfgEBS.setStatus("current")


class _RcQosBandwidthProfileColorMode_Type(Integer32):
    """Custom type rcQosBandwidthProfileColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("color-blind", 0),
          ("color-aware", 1))
    )


_RcQosBandwidthProfileColorMode_Type.__name__ = "Integer32"
_RcQosBandwidthProfileColorMode_Object = MibTableColumn
rcQosBandwidthProfileColorMode = _RcQosBandwidthProfileColorMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 6),
    _RcQosBandwidthProfileColorMode_Type()
)
rcQosBandwidthProfileColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileColorMode.setStatus("current")


class _RcQosBandwidthProfileCoupling_Type(Integer32):
    """Custom type rcQosBandwidthProfileCoupling based on Integer32"""
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


_RcQosBandwidthProfileCoupling_Type.__name__ = "Integer32"
_RcQosBandwidthProfileCoupling_Object = MibTableColumn
rcQosBandwidthProfileCoupling = _RcQosBandwidthProfileCoupling_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 7),
    _RcQosBandwidthProfileCoupling_Type()
)
rcQosBandwidthProfileCoupling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileCoupling.setStatus("current")
_RcQoSBandwidthProfileRef_Type = Integer32
_RcQoSBandwidthProfileRef_Object = MibTableColumn
rcQoSBandwidthProfileRef = _RcQoSBandwidthProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 8),
    _RcQoSBandwidthProfileRef_Type()
)
rcQoSBandwidthProfileRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQoSBandwidthProfileRef.setStatus("current")
_RcQosBandwidthProfileStatus_Type = RowStatus
_RcQosBandwidthProfileStatus_Object = MibTableColumn
rcQosBandwidthProfileStatus = _RcQosBandwidthProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 9),
    _RcQosBandwidthProfileStatus_Type()
)
rcQosBandwidthProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileStatus.setStatus("current")


class _RcQosBandwidthProfileDesc_Type(OctetString):
    """Custom type rcQosBandwidthProfileDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcQosBandwidthProfileDesc_Type.__name__ = "OctetString"
_RcQosBandwidthProfileDesc_Object = MibTableColumn
rcQosBandwidthProfileDesc = _RcQosBandwidthProfileDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 12, 1, 10),
    _RcQosBandwidthProfileDesc_Type()
)
rcQosBandwidthProfileDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthProfileDesc.setStatus("current")
_RcQosHierarchyCosIndexCfgTable_Object = MibTable
rcQosHierarchyCosIndexCfgTable = _RcQosHierarchyCosIndexCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 13)
)
if mibBuilder.loadTexts:
    rcQosHierarchyCosIndexCfgTable.setStatus("current")
_RcQosHierarchyCosIndexCfgEntry_Object = MibTableRow
rcQosHierarchyCosIndexCfgEntry = _RcQosHierarchyCosIndexCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 13, 1)
)
rcQosHierarchyCosIndexCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosHierarchyCosIndex"),
)
if mibBuilder.loadTexts:
    rcQosHierarchyCosIndexCfgEntry.setStatus("current")
_RcQosHierarchyCosIndex_Type = Integer32
_RcQosHierarchyCosIndex_Object = MibTableColumn
rcQosHierarchyCosIndex = _RcQosHierarchyCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 13, 1, 1),
    _RcQosHierarchyCosIndex_Type()
)
rcQosHierarchyCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosHierarchyCosIndex.setStatus("current")
_RcQosHierarchyCosRef_Type = Integer32
_RcQosHierarchyCosRef_Object = MibTableColumn
rcQosHierarchyCosRef = _RcQosHierarchyCosRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 13, 1, 2),
    _RcQosHierarchyCosRef_Type()
)
rcQosHierarchyCosRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosHierarchyCosRef.setStatus("current")
_RcQosHierarchyCosCfgStatus_Type = RowStatus
_RcQosHierarchyCosCfgStatus_Object = MibTableColumn
rcQosHierarchyCosCfgStatus = _RcQosHierarchyCosCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 13, 1, 3),
    _RcQosHierarchyCosCfgStatus_Type()
)
rcQosHierarchyCosCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHierarchyCosCfgStatus.setStatus("current")


class _RcQosHierarchyCosCfgDesc_Type(OctetString):
    """Custom type rcQosHierarchyCosCfgDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcQosHierarchyCosCfgDesc_Type.__name__ = "OctetString"
_RcQosHierarchyCosCfgDesc_Object = MibTableColumn
rcQosHierarchyCosCfgDesc = _RcQosHierarchyCosCfgDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 13, 1, 4),
    _RcQosHierarchyCosCfgDesc_Type()
)
rcQosHierarchyCosCfgDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHierarchyCosCfgDesc.setStatus("current")
_RcQosHCosBandwidthProfileTable_Object = MibTable
rcQosHCosBandwidthProfileTable = _RcQosHCosBandwidthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14)
)
if mibBuilder.loadTexts:
    rcQosHCosBandwidthProfileTable.setStatus("current")
_RcQosHCosBandwidthProfileEntry_Object = MibTableRow
rcQosHCosBandwidthProfileEntry = _RcQosHCosBandwidthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14, 1)
)
rcQosHCosBandwidthProfileEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosHCosBandwidthProfileIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosHCosBandwidthProfileCos"),
)
if mibBuilder.loadTexts:
    rcQosHCosBandwidthProfileEntry.setStatus("current")
_RcQosHCosBandwidthProfileIndex_Type = Integer32
_RcQosHCosBandwidthProfileIndex_Object = MibTableColumn
rcQosHCosBandwidthProfileIndex = _RcQosHCosBandwidthProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14, 1, 1),
    _RcQosHCosBandwidthProfileIndex_Type()
)
rcQosHCosBandwidthProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosHCosBandwidthProfileIndex.setStatus("current")


class _RcQosHCosBandwidthProfileCos_Type(Integer32):
    """Custom type rcQosHCosBandwidthProfileCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcQosHCosBandwidthProfileCos_Type.__name__ = "Integer32"
_RcQosHCosBandwidthProfileCos_Object = MibTableColumn
rcQosHCosBandwidthProfileCos = _RcQosHCosBandwidthProfileCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14, 1, 2),
    _RcQosHCosBandwidthProfileCos_Type()
)
rcQosHCosBandwidthProfileCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosHCosBandwidthProfileCos.setStatus("current")
_RcQosHCosBandwidthProfileBwpIndex_Type = Integer32
_RcQosHCosBandwidthProfileBwpIndex_Object = MibTableColumn
rcQosHCosBandwidthProfileBwpIndex = _RcQosHCosBandwidthProfileBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14, 1, 3),
    _RcQosHCosBandwidthProfileBwpIndex_Type()
)
rcQosHCosBandwidthProfileBwpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHCosBandwidthProfileBwpIndex.setStatus("current")
_RcQoSHCosBandwidthProfileRef_Type = Integer32
_RcQoSHCosBandwidthProfileRef_Object = MibTableColumn
rcQoSHCosBandwidthProfileRef = _RcQoSHCosBandwidthProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14, 1, 4),
    _RcQoSHCosBandwidthProfileRef_Type()
)
rcQoSHCosBandwidthProfileRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQoSHCosBandwidthProfileRef.setStatus("current")
_RcQosHCosBandwidthProfileRowStatus_Type = RowStatus
_RcQosHCosBandwidthProfileRowStatus_Object = MibTableColumn
rcQosHCosBandwidthProfileRowStatus = _RcQosHCosBandwidthProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 14, 1, 5),
    _RcQosHCosBandwidthProfileRowStatus_Type()
)
rcQosHCosBandwidthProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHCosBandwidthProfileRowStatus.setStatus("current")
_RcQosHierarchyVlanIndexCfgTable_Object = MibTable
rcQosHierarchyVlanIndexCfgTable = _RcQosHierarchyVlanIndexCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 15)
)
if mibBuilder.loadTexts:
    rcQosHierarchyVlanIndexCfgTable.setStatus("current")
_RcQosHierarchyVlanIndexCfgEntry_Object = MibTableRow
rcQosHierarchyVlanIndexCfgEntry = _RcQosHierarchyVlanIndexCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 15, 1)
)
rcQosHierarchyVlanIndexCfgEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosHierarchyVlanIndex"),
)
if mibBuilder.loadTexts:
    rcQosHierarchyVlanIndexCfgEntry.setStatus("current")
_RcQosHierarchyVlanIndex_Type = Integer32
_RcQosHierarchyVlanIndex_Object = MibTableColumn
rcQosHierarchyVlanIndex = _RcQosHierarchyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 15, 1, 1),
    _RcQosHierarchyVlanIndex_Type()
)
rcQosHierarchyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosHierarchyVlanIndex.setStatus("current")
_RcQosHierarchyVlanRef_Type = Integer32
_RcQosHierarchyVlanRef_Object = MibTableColumn
rcQosHierarchyVlanRef = _RcQosHierarchyVlanRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 15, 1, 2),
    _RcQosHierarchyVlanRef_Type()
)
rcQosHierarchyVlanRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosHierarchyVlanRef.setStatus("current")
_RcQosHierarchyVlanCfgStatus_Type = RowStatus
_RcQosHierarchyVlanCfgStatus_Object = MibTableColumn
rcQosHierarchyVlanCfgStatus = _RcQosHierarchyVlanCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 15, 1, 3),
    _RcQosHierarchyVlanCfgStatus_Type()
)
rcQosHierarchyVlanCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHierarchyVlanCfgStatus.setStatus("current")


class _RcQosHierarchyVlanCfgDesc_Type(OctetString):
    """Custom type rcQosHierarchyVlanCfgDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcQosHierarchyVlanCfgDesc_Type.__name__ = "OctetString"
_RcQosHierarchyVlanCfgDesc_Object = MibTableColumn
rcQosHierarchyVlanCfgDesc = _RcQosHierarchyVlanCfgDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 15, 1, 4),
    _RcQosHierarchyVlanCfgDesc_Type()
)
rcQosHierarchyVlanCfgDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHierarchyVlanCfgDesc.setStatus("current")
_RcQosHVlanBandwidthProfileTable_Object = MibTable
rcQosHVlanBandwidthProfileTable = _RcQosHVlanBandwidthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16)
)
if mibBuilder.loadTexts:
    rcQosHVlanBandwidthProfileTable.setStatus("current")
_RcQosHVlanBandwidthProfileEntry_Object = MibTableRow
rcQosHVlanBandwidthProfileEntry = _RcQosHVlanBandwidthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16, 1)
)
rcQosHVlanBandwidthProfileEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosHVlanBandwidthProfileIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosHVlanBandwidthProfileVlan"),
)
if mibBuilder.loadTexts:
    rcQosHVlanBandwidthProfileEntry.setStatus("current")
_RcQosHVlanBandwidthProfileIndex_Type = Integer32
_RcQosHVlanBandwidthProfileIndex_Object = MibTableColumn
rcQosHVlanBandwidthProfileIndex = _RcQosHVlanBandwidthProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16, 1, 1),
    _RcQosHVlanBandwidthProfileIndex_Type()
)
rcQosHVlanBandwidthProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosHVlanBandwidthProfileIndex.setStatus("current")


class _RcQosHVlanBandwidthProfileVlan_Type(Integer32):
    """Custom type rcQosHVlanBandwidthProfileVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosHVlanBandwidthProfileVlan_Type.__name__ = "Integer32"
_RcQosHVlanBandwidthProfileVlan_Object = MibTableColumn
rcQosHVlanBandwidthProfileVlan = _RcQosHVlanBandwidthProfileVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16, 1, 2),
    _RcQosHVlanBandwidthProfileVlan_Type()
)
rcQosHVlanBandwidthProfileVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosHVlanBandwidthProfileVlan.setStatus("current")
_RcQosHVlanBandwidthProfileBwpIndex_Type = Integer32
_RcQosHVlanBandwidthProfileBwpIndex_Object = MibTableColumn
rcQosHVlanBandwidthProfileBwpIndex = _RcQosHVlanBandwidthProfileBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16, 1, 3),
    _RcQosHVlanBandwidthProfileBwpIndex_Type()
)
rcQosHVlanBandwidthProfileBwpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHVlanBandwidthProfileBwpIndex.setStatus("current")
_RcQoSHVlanBandwidthProfileRef_Type = Integer32
_RcQoSHVlanBandwidthProfileRef_Object = MibTableColumn
rcQoSHVlanBandwidthProfileRef = _RcQoSHVlanBandwidthProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16, 1, 4),
    _RcQoSHVlanBandwidthProfileRef_Type()
)
rcQoSHVlanBandwidthProfileRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQoSHVlanBandwidthProfileRef.setStatus("current")
_RcQosHVlanBandwidthProfileRowStatus_Type = RowStatus
_RcQosHVlanBandwidthProfileRowStatus_Object = MibTableColumn
rcQosHVlanBandwidthProfileRowStatus = _RcQosHVlanBandwidthProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 16, 1, 5),
    _RcQosHVlanBandwidthProfileRowStatus_Type()
)
rcQosHVlanBandwidthProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosHVlanBandwidthProfileRowStatus.setStatus("current")
_RcQosBandwidthPortTable_Object = MibTable
rcQosBandwidthPortTable = _RcQosBandwidthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17)
)
if mibBuilder.loadTexts:
    rcQosBandwidthPortTable.setStatus("current")
_RcQosBandwidthPortEntry_Object = MibTableRow
rcQosBandwidthPortEntry = _RcQosBandwidthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1)
)
rcQosBandwidthPortEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    rcQosBandwidthPortEntry.setStatus("current")
_RcQosBandwidthPortIndex_Type = Integer32
_RcQosBandwidthPortIndex_Object = MibTableColumn
rcQosBandwidthPortIndex = _RcQosBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 1),
    _RcQosBandwidthPortIndex_Type()
)
rcQosBandwidthPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosBandwidthPortIndex.setStatus("current")
_RcQosBandwidthPortBwpIndex_Type = Integer32
_RcQosBandwidthPortBwpIndex_Object = MibTableColumn
rcQosBandwidthPortBwpIndex = _RcQosBandwidthPortBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 2),
    _RcQosBandwidthPortBwpIndex_Type()
)
rcQosBandwidthPortBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthPortBwpIndex.setStatus("current")
_RcQosBandwidthPortEgrBwpIndex_Type = Integer32
_RcQosBandwidthPortEgrBwpIndex_Object = MibTableColumn
rcQosBandwidthPortEgrBwpIndex = _RcQosBandwidthPortEgrBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 3),
    _RcQosBandwidthPortEgrBwpIndex_Type()
)
rcQosBandwidthPortEgrBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthPortEgrBwpIndex.setStatus("current")
_RcQosBandwidthPortHBwEnable_Type = EnableVar
_RcQosBandwidthPortHBwEnable_Object = MibTableColumn
rcQosBandwidthPortHBwEnable = _RcQosBandwidthPortHBwEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 4),
    _RcQosBandwidthPortHBwEnable_Type()
)
rcQosBandwidthPortHBwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthPortHBwEnable.setStatus("current")
_RcQosBandwidthPortHvBwpIndex_Type = Integer32
_RcQosBandwidthPortHvBwpIndex_Object = MibTableColumn
rcQosBandwidthPortHvBwpIndex = _RcQosBandwidthPortHvBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 5),
    _RcQosBandwidthPortHvBwpIndex_Type()
)
rcQosBandwidthPortHvBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthPortHvBwpIndex.setStatus("current")
_RcQosBandwidthPortDeiRemarkEnable_Type = EnableVar
_RcQosBandwidthPortDeiRemarkEnable_Object = MibTableColumn
rcQosBandwidthPortDeiRemarkEnable = _RcQosBandwidthPortDeiRemarkEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 6),
    _RcQosBandwidthPortDeiRemarkEnable_Type()
)
rcQosBandwidthPortDeiRemarkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthPortDeiRemarkEnable.setStatus("current")
_RcQosBandwidthPortColorAwareEnable_Type = EnableVar
_RcQosBandwidthPortColorAwareEnable_Object = MibTableColumn
rcQosBandwidthPortColorAwareEnable = _RcQosBandwidthPortColorAwareEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 17, 1, 7),
    _RcQosBandwidthPortColorAwareEnable_Type()
)
rcQosBandwidthPortColorAwareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthPortColorAwareEnable.setStatus("current")
_RcQosBandwidthVlanTable_Object = MibTable
rcQosBandwidthVlanTable = _RcQosBandwidthVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18)
)
if mibBuilder.loadTexts:
    rcQosBandwidthVlanTable.setStatus("current")
_RcQosBandwidthVlanEntry_Object = MibTableRow
rcQosBandwidthVlanEntry = _RcQosBandwidthVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1)
)
rcQosBandwidthVlanEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthVlanPort"),
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthVlanIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthVlanPortType"),
)
if mibBuilder.loadTexts:
    rcQosBandwidthVlanEntry.setStatus("current")


class _RcQosBandwidthVlanIndex_Type(Integer32):
    """Custom type rcQosBandwidthVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosBandwidthVlanIndex_Type.__name__ = "Integer32"
_RcQosBandwidthVlanIndex_Object = MibTableColumn
rcQosBandwidthVlanIndex = _RcQosBandwidthVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 1),
    _RcQosBandwidthVlanIndex_Type()
)
rcQosBandwidthVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanIndex.setStatus("current")
_RcQosBandwidthVlanPort_Type = Integer32
_RcQosBandwidthVlanPort_Object = MibTableColumn
rcQosBandwidthVlanPort = _RcQosBandwidthVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 2),
    _RcQosBandwidthVlanPort_Type()
)
rcQosBandwidthVlanPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanPort.setStatus("current")


class _RcQosBandwidthVlanPortType_Type(Integer32):
    """Custom type rcQosBandwidthVlanPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_RcQosBandwidthVlanPortType_Type.__name__ = "Integer32"
_RcQosBandwidthVlanPortType_Object = MibTableColumn
rcQosBandwidthVlanPortType = _RcQosBandwidthVlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 3),
    _RcQosBandwidthVlanPortType_Type()
)
rcQosBandwidthVlanPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanPortType.setStatus("current")
_RcQosBandwidthVlanBwpIndex_Type = Integer32
_RcQosBandwidthVlanBwpIndex_Object = MibTableColumn
rcQosBandwidthVlanBwpIndex = _RcQosBandwidthVlanBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 4),
    _RcQosBandwidthVlanBwpIndex_Type()
)
rcQosBandwidthVlanBwpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanBwpIndex.setStatus("current")
_RcQosBandwidthVlanHBwEnable_Type = EnableVar
_RcQosBandwidthVlanHBwEnable_Object = MibTableColumn
rcQosBandwidthVlanHBwEnable = _RcQosBandwidthVlanHBwEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 5),
    _RcQosBandwidthVlanHBwEnable_Type()
)
rcQosBandwidthVlanHBwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanHBwEnable.setStatus("current")
_RcQosBandwidthVlanHcBwpIndex_Type = Integer32
_RcQosBandwidthVlanHcBwpIndex_Object = MibTableColumn
rcQosBandwidthVlanHcBwpIndex = _RcQosBandwidthVlanHcBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 6),
    _RcQosBandwidthVlanHcBwpIndex_Type()
)
rcQosBandwidthVlanHcBwpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanHcBwpIndex.setStatus("current")
_RcQosBandwidthVlanRowStatus_Type = RowStatus
_RcQosBandwidthVlanRowStatus_Object = MibTableColumn
rcQosBandwidthVlanRowStatus = _RcQosBandwidthVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 18, 1, 7),
    _RcQosBandwidthVlanRowStatus_Type()
)
rcQosBandwidthVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthVlanRowStatus.setStatus("current")
_RcQosBandwidthCosTable_Object = MibTable
rcQosBandwidthCosTable = _RcQosBandwidthCosTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19)
)
if mibBuilder.loadTexts:
    rcQosBandwidthCosTable.setStatus("current")
_RcQosBandwidthCosEntry_Object = MibTableRow
rcQosBandwidthCosEntry = _RcQosBandwidthCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1)
)
rcQosBandwidthCosEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthCosPort"),
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthCosVlan"),
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthCosIndex"),
    (0, "RAISECOM-QOS-MIB", "rcQosBandwidthCosPortType"),
)
if mibBuilder.loadTexts:
    rcQosBandwidthCosEntry.setStatus("current")


class _RcQosBandwidthCosIndex_Type(Integer32):
    """Custom type rcQosBandwidthCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosBandwidthCosIndex_Type.__name__ = "Integer32"
_RcQosBandwidthCosIndex_Object = MibTableColumn
rcQosBandwidthCosIndex = _RcQosBandwidthCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1, 1),
    _RcQosBandwidthCosIndex_Type()
)
rcQosBandwidthCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosBandwidthCosIndex.setStatus("current")


class _RcQosBandwidthCosVlan_Type(Integer32):
    """Custom type rcQosBandwidthCosVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcQosBandwidthCosVlan_Type.__name__ = "Integer32"
_RcQosBandwidthCosVlan_Object = MibTableColumn
rcQosBandwidthCosVlan = _RcQosBandwidthCosVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1, 2),
    _RcQosBandwidthCosVlan_Type()
)
rcQosBandwidthCosVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosBandwidthCosVlan.setStatus("current")
_RcQosBandwidthCosPort_Type = Integer32
_RcQosBandwidthCosPort_Object = MibTableColumn
rcQosBandwidthCosPort = _RcQosBandwidthCosPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1, 3),
    _RcQosBandwidthCosPort_Type()
)
rcQosBandwidthCosPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosBandwidthCosPort.setStatus("current")


class _RcQosBandwidthCosPortType_Type(Integer32):
    """Custom type rcQosBandwidthCosPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_RcQosBandwidthCosPortType_Type.__name__ = "Integer32"
_RcQosBandwidthCosPortType_Object = MibTableColumn
rcQosBandwidthCosPortType = _RcQosBandwidthCosPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1, 4),
    _RcQosBandwidthCosPortType_Type()
)
rcQosBandwidthCosPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosBandwidthCosPortType.setStatus("current")
_RcQosBandwidthCosBwpIndex_Type = Integer32
_RcQosBandwidthCosBwpIndex_Object = MibTableColumn
rcQosBandwidthCosBwpIndex = _RcQosBandwidthCosBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1, 5),
    _RcQosBandwidthCosBwpIndex_Type()
)
rcQosBandwidthCosBwpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthCosBwpIndex.setStatus("current")
_RcQosBandwidthCosRowStatus_Type = RowStatus
_RcQosBandwidthCosRowStatus_Object = MibTableColumn
rcQosBandwidthCosRowStatus = _RcQosBandwidthCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 19, 1, 6),
    _RcQosBandwidthCosRowStatus_Type()
)
rcQosBandwidthCosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosBandwidthCosRowStatus.setStatus("current")
_RcQosBandwidthGlobalEnable_Type = EnableVar
_RcQosBandwidthGlobalEnable_Object = MibScalar
rcQosBandwidthGlobalEnable = _RcQosBandwidthGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 20),
    _RcQosBandwidthGlobalEnable_Type()
)
rcQosBandwidthGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosBandwidthGlobalEnable.setStatus("current")
_RcQosBandwidthNotificationGroup_ObjectIdentity = ObjectIdentity
rcQosBandwidthNotificationGroup = _RcQosBandwidthNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 21)
)
_RaisecomQosStatistics_ObjectIdentity = ObjectIdentity
raisecomQosStatistics = _RaisecomQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3)
)
_RcQosTrafficStatsTable_Object = MibTable
rcQosTrafficStatsTable = _RcQosTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1)
)
if mibBuilder.loadTexts:
    rcQosTrafficStatsTable.setStatus("current")
_RcQosTrafficStatsEntry_Object = MibTableRow
rcQosTrafficStatsEntry = _RcQosTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1)
)
rcQosTrafficStatsEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosTrafficStatsPort"),
    (0, "RAISECOM-QOS-MIB", "rcQosTrafficStatsDirection"),
    (0, "RAISECOM-QOS-MIB", "rcQosTrafficStatsCmapName"),
)
if mibBuilder.loadTexts:
    rcQosTrafficStatsEntry.setStatus("current")
_RcQosTrafficStatsPort_Type = Integer32
_RcQosTrafficStatsPort_Object = MibTableColumn
rcQosTrafficStatsPort = _RcQosTrafficStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 1),
    _RcQosTrafficStatsPort_Type()
)
rcQosTrafficStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosTrafficStatsPort.setStatus("current")


class _RcQosTrafficStatsDirection_Type(Integer32):
    """Custom type rcQosTrafficStatsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_RcQosTrafficStatsDirection_Type.__name__ = "Integer32"
_RcQosTrafficStatsDirection_Object = MibTableColumn
rcQosTrafficStatsDirection = _RcQosTrafficStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 2),
    _RcQosTrafficStatsDirection_Type()
)
rcQosTrafficStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosTrafficStatsDirection.setStatus("current")
_RcQosTrafficStatsCmapName_Type = ObjName
_RcQosTrafficStatsCmapName_Object = MibTableColumn
rcQosTrafficStatsCmapName = _RcQosTrafficStatsCmapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 3),
    _RcQosTrafficStatsCmapName_Type()
)
rcQosTrafficStatsCmapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosTrafficStatsCmapName.setStatus("current")


class _RcQosTrafficStatsPolicerType_Type(Integer32):
    """Custom type rcQosTrafficStatsPolicerType based on Integer32"""
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
        *(("none", 0),
          ("singleflow", 1),
          ("classflow", 2),
          ("aggregate", 3))
    )


_RcQosTrafficStatsPolicerType_Type.__name__ = "Integer32"
_RcQosTrafficStatsPolicerType_Object = MibTableColumn
rcQosTrafficStatsPolicerType = _RcQosTrafficStatsPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 4),
    _RcQosTrafficStatsPolicerType_Type()
)
rcQosTrafficStatsPolicerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosTrafficStatsPolicerType.setStatus("current")
_RcQosTrafficCounterReset_Type = EnableVar
_RcQosTrafficCounterReset_Object = MibTableColumn
rcQosTrafficCounterReset = _RcQosTrafficCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 5),
    _RcQosTrafficCounterReset_Type()
)
rcQosTrafficCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTrafficCounterReset.setStatus("current")
_RcQosTrafficPolicyName_Type = ObjName
_RcQosTrafficPolicyName_Object = MibTableColumn
rcQosTrafficPolicyName = _RcQosTrafficPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 6),
    _RcQosTrafficPolicyName_Type()
)
rcQosTrafficPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTrafficPolicyName.setStatus("current")
_RcQosTrafficPolicerName_Type = ObjName
_RcQosTrafficPolicerName_Object = MibTableColumn
rcQosTrafficPolicerName = _RcQosTrafficPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 7),
    _RcQosTrafficPolicerName_Type()
)
rcQosTrafficPolicerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTrafficPolicerName.setStatus("current")
_RcQosTrafficCounterHwStatus_Type = TruthValue
_RcQosTrafficCounterHwStatus_Object = MibTableColumn
rcQosTrafficCounterHwStatus = _RcQosTrafficCounterHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 8),
    _RcQosTrafficCounterHwStatus_Type()
)
rcQosTrafficCounterHwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTrafficCounterHwStatus.setStatus("current")


class _RcQosTrafficStatisticsUnit_Type(Integer32):
    """Custom type rcQosTrafficStatisticsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 1),
          ("pkts", 2))
    )


_RcQosTrafficStatisticsUnit_Type.__name__ = "Integer32"
_RcQosTrafficStatisticsUnit_Object = MibTableColumn
rcQosTrafficStatisticsUnit = _RcQosTrafficStatisticsUnit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 9),
    _RcQosTrafficStatisticsUnit_Type()
)
rcQosTrafficStatisticsUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQosTrafficStatisticsUnit.setStatus("current")
_RcQosTrafficCounterInprofilePkt64_Type = Counter64
_RcQosTrafficCounterInprofilePkt64_Object = MibTableColumn
rcQosTrafficCounterInprofilePkt64 = _RcQosTrafficCounterInprofilePkt64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 10),
    _RcQosTrafficCounterInprofilePkt64_Type()
)
rcQosTrafficCounterInprofilePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosTrafficCounterInprofilePkt64.setStatus("current")
_RcQosTrafficCounterInprofileByte64_Type = Counter64
_RcQosTrafficCounterInprofileByte64_Object = MibTableColumn
rcQosTrafficCounterInprofileByte64 = _RcQosTrafficCounterInprofileByte64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 11),
    _RcQosTrafficCounterInprofileByte64_Type()
)
rcQosTrafficCounterInprofileByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosTrafficCounterInprofileByte64.setStatus("current")
_RcQosTrafficCounterOutprofilePkt64_Type = Counter64
_RcQosTrafficCounterOutprofilePkt64_Object = MibTableColumn
rcQosTrafficCounterOutprofilePkt64 = _RcQosTrafficCounterOutprofilePkt64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 12),
    _RcQosTrafficCounterOutprofilePkt64_Type()
)
rcQosTrafficCounterOutprofilePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosTrafficCounterOutprofilePkt64.setStatus("current")
_RcQosTrafficCounterOutprofileByte64_Type = Counter64
_RcQosTrafficCounterOutprofileByte64_Object = MibTableColumn
rcQosTrafficCounterOutprofileByte64 = _RcQosTrafficCounterOutprofileByte64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 13),
    _RcQosTrafficCounterOutprofileByte64_Type()
)
rcQosTrafficCounterOutprofileByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosTrafficCounterOutprofileByte64.setStatus("current")
_RcQosTrafficbStatistics_Type = EnableVar
_RcQosTrafficbStatistics_Object = MibTableColumn
rcQosTrafficbStatistics = _RcQosTrafficbStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 1, 1, 14),
    _RcQosTrafficbStatistics_Type()
)
rcQosTrafficbStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosTrafficbStatistics.setStatus("current")
_RcQosVlanStatisticsTable_Object = MibTable
rcQosVlanStatisticsTable = _RcQosVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2)
)
if mibBuilder.loadTexts:
    rcQosVlanStatisticsTable.setStatus("current")
_RcQosVlanStatisticsEntry_Object = MibTableRow
rcQosVlanStatisticsEntry = _RcQosVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1)
)
rcQosVlanStatisticsEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosVlanStatisticsPort"),
    (0, "RAISECOM-QOS-MIB", "rcQosVlanStatisticsVlan"),
    (0, "RAISECOM-QOS-MIB", "rcQosVlanStatisticsDirection"),
)
if mibBuilder.loadTexts:
    rcQosVlanStatisticsEntry.setStatus("current")
_RcQosVlanStatisticsPort_Type = Integer32
_RcQosVlanStatisticsPort_Object = MibTableColumn
rcQosVlanStatisticsPort = _RcQosVlanStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 1),
    _RcQosVlanStatisticsPort_Type()
)
rcQosVlanStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsPort.setStatus("current")
_RcQosVlanStatisticsVlan_Type = Integer32
_RcQosVlanStatisticsVlan_Object = MibTableColumn
rcQosVlanStatisticsVlan = _RcQosVlanStatisticsVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 2),
    _RcQosVlanStatisticsVlan_Type()
)
rcQosVlanStatisticsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsVlan.setStatus("current")


class _RcQosVlanStatisticsDirection_Type(Integer32):
    """Custom type rcQosVlanStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_RcQosVlanStatisticsDirection_Type.__name__ = "Integer32"
_RcQosVlanStatisticsDirection_Object = MibTableColumn
rcQosVlanStatisticsDirection = _RcQosVlanStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 3),
    _RcQosVlanStatisticsDirection_Type()
)
rcQosVlanStatisticsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsDirection.setStatus("current")


class _RcQosVlanStatisticsUnit_Type(Integer32):
    """Custom type rcQosVlanStatisticsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pkts", 1),
          ("bytes", 2),
          ("both", 3))
    )


_RcQosVlanStatisticsUnit_Type.__name__ = "Integer32"
_RcQosVlanStatisticsUnit_Object = MibTableColumn
rcQosVlanStatisticsUnit = _RcQosVlanStatisticsUnit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 4),
    _RcQosVlanStatisticsUnit_Type()
)
rcQosVlanStatisticsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsUnit.setStatus("current")
_RcQosVlanStatisticsReset_Type = Integer32
_RcQosVlanStatisticsReset_Object = MibTableColumn
rcQosVlanStatisticsReset = _RcQosVlanStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 5),
    _RcQosVlanStatisticsReset_Type()
)
rcQosVlanStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsReset.setStatus("current")
_RcQosVlanStatisticsPkt_Type = Counter64
_RcQosVlanStatisticsPkt_Object = MibTableColumn
rcQosVlanStatisticsPkt = _RcQosVlanStatisticsPkt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 6),
    _RcQosVlanStatisticsPkt_Type()
)
rcQosVlanStatisticsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsPkt.setStatus("current")
_RcQosVlanStatisticsByte_Type = Counter64
_RcQosVlanStatisticsByte_Object = MibTableColumn
rcQosVlanStatisticsByte = _RcQosVlanStatisticsByte_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 7),
    _RcQosVlanStatisticsByte_Type()
)
rcQosVlanStatisticsByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsByte.setStatus("current")
_RcQosVlanStatisticsRowStatus_Type = RowStatus
_RcQosVlanStatisticsRowStatus_Object = MibTableColumn
rcQosVlanStatisticsRowStatus = _RcQosVlanStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 2, 1, 8),
    _RcQosVlanStatisticsRowStatus_Type()
)
rcQosVlanStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosVlanStatisticsRowStatus.setStatus("current")
_RcQosCosStatisticsTable_Object = MibTable
rcQosCosStatisticsTable = _RcQosCosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3)
)
if mibBuilder.loadTexts:
    rcQosCosStatisticsTable.setStatus("current")
_RcQosCosStatisticsEntry_Object = MibTableRow
rcQosCosStatisticsEntry = _RcQosCosStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1)
)
rcQosCosStatisticsEntry.setIndexNames(
    (0, "RAISECOM-QOS-MIB", "rcQosCosStatisticsPort"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosStatisticsVlan"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosStatisticsCos"),
    (0, "RAISECOM-QOS-MIB", "rcQosCosStatisticsDirection"),
)
if mibBuilder.loadTexts:
    rcQosCosStatisticsEntry.setStatus("current")
_RcQosCosStatisticsPort_Type = Integer32
_RcQosCosStatisticsPort_Object = MibTableColumn
rcQosCosStatisticsPort = _RcQosCosStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 1),
    _RcQosCosStatisticsPort_Type()
)
rcQosCosStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosStatisticsPort.setStatus("current")
_RcQosCosStatisticsVlan_Type = Integer32
_RcQosCosStatisticsVlan_Object = MibTableColumn
rcQosCosStatisticsVlan = _RcQosCosStatisticsVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 2),
    _RcQosCosStatisticsVlan_Type()
)
rcQosCosStatisticsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosStatisticsVlan.setStatus("current")


class _RcQosCosStatisticsCos_Type(Integer32):
    """Custom type rcQosCosStatisticsCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcQosCosStatisticsCos_Type.__name__ = "Integer32"
_RcQosCosStatisticsCos_Object = MibTableColumn
rcQosCosStatisticsCos = _RcQosCosStatisticsCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 3),
    _RcQosCosStatisticsCos_Type()
)
rcQosCosStatisticsCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosStatisticsCos.setStatus("current")


class _RcQosCosStatisticsDirection_Type(Integer32):
    """Custom type rcQosCosStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_RcQosCosStatisticsDirection_Type.__name__ = "Integer32"
_RcQosCosStatisticsDirection_Object = MibTableColumn
rcQosCosStatisticsDirection = _RcQosCosStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 4),
    _RcQosCosStatisticsDirection_Type()
)
rcQosCosStatisticsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQosCosStatisticsDirection.setStatus("current")


class _RcQosCosStatisticsUnit_Type(Integer32):
    """Custom type rcQosCosStatisticsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pkts", 1),
          ("bytes", 2),
          ("both", 3))
    )


_RcQosCosStatisticsUnit_Type.__name__ = "Integer32"
_RcQosCosStatisticsUnit_Object = MibTableColumn
rcQosCosStatisticsUnit = _RcQosCosStatisticsUnit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 5),
    _RcQosCosStatisticsUnit_Type()
)
rcQosCosStatisticsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosCosStatisticsUnit.setStatus("current")
_RcQosCosStatisticsReset_Type = Integer32
_RcQosCosStatisticsReset_Object = MibTableColumn
rcQosCosStatisticsReset = _RcQosCosStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 6),
    _RcQosCosStatisticsReset_Type()
)
rcQosCosStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosStatisticsReset.setStatus("current")
_RcQosCosStatisticsPkt_Type = Counter64
_RcQosCosStatisticsPkt_Object = MibTableColumn
rcQosCosStatisticsPkt = _RcQosCosStatisticsPkt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 7),
    _RcQosCosStatisticsPkt_Type()
)
rcQosCosStatisticsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosCosStatisticsPkt.setStatus("current")
_RcQosCosStatisticsByte_Type = Counter64
_RcQosCosStatisticsByte_Object = MibTableColumn
rcQosCosStatisticsByte = _RcQosCosStatisticsByte_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 8),
    _RcQosCosStatisticsByte_Type()
)
rcQosCosStatisticsByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcQosCosStatisticsByte.setStatus("current")
_RcQosCosStatisticsRowStatus_Type = RowStatus
_RcQosCosStatisticsRowStatus_Object = MibTableColumn
rcQosCosStatisticsRowStatus = _RcQosCosStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 3, 3, 1, 9),
    _RcQosCosStatisticsRowStatus_Type()
)
rcQosCosStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQosCosStatisticsRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

rcQosBandwidthPortModification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 21, 1)
)
rcQosBandwidthPortModification.setObjects(
      *(("RAISECOM-QOS-MIB", "rcQosBandwidthPortIndex"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthPortBwpIndex"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthPortEgrBwpIndex"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthPortHBwEnable"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthPortHvBwpIndex"))
)
if mibBuilder.loadTexts:
    rcQosBandwidthPortModification.setStatus(
        "current"
    )

rcQosBandwidthVlanModification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 21, 2)
)
rcQosBandwidthVlanModification.setObjects(
      *(("RAISECOM-QOS-MIB", "rcQosBandwidthVlanIndex"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthVlanPort"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthVlanPortType"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthVlanBwpIndex"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthVlanHBwEnable"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthVlanHcBwpIndex"))
)
if mibBuilder.loadTexts:
    rcQosBandwidthVlanModification.setStatus(
        "current"
    )

rcQosBandwidthCosModification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 33, 2, 21, 3)
)
rcQosBandwidthCosModification.setObjects(
      *(("RAISECOM-QOS-MIB", "rcQosBandwidthCosVlan"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthCosIndex"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthCosPort"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthCosPortType"),
        ("RAISECOM-QOS-MIB", "rcQosBandwidthCosBwpIndex"))
)
if mibBuilder.loadTexts:
    rcQosBandwidthCosModification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-QOS-MIB",
    **{"raisecomQosMIB": raisecomQosMIB,
       "raisecomQosCfg": raisecomQosCfg,
       "rcQosEnable": rcQosEnable,
       "rcQosTrust": rcQosTrust,
       "rcQosQueueScheduler": rcQosQueueScheduler,
       "rcQosWredEnable": rcQosWredEnable,
       "rcQosCos2PriProfile": rcQosCos2PriProfile,
       "rcQosTos2PriProfile": rcQosTos2PriProfile,
       "rcQosDscp2PriProfile": rcQosDscp2PriProfile,
       "rcQosDscpMutationProfile": rcQosDscpMutationProfile,
       "rcQosCosRemarkProfile": rcQosCosRemarkProfile,
       "rcQosPortCfgTable": rcQosPortCfgTable,
       "rcQosPortCfgEntry": rcQosPortCfgEntry,
       "rcQosPortCfgPortId": rcQosPortCfgPortId,
       "rcQosPortCfgTrust": rcQosPortCfgTrust,
       "rcQosPortCfgPriority": rcQosPortCfgPriority,
       "rcQosPortCfgPriorityOverride": rcQosPortCfgPriorityOverride,
       "rcQosPortCfgQueueScheduler": rcQosPortCfgQueueScheduler,
       "rcQosPortCfgSmacPriorityOverride": rcQosPortCfgSmacPriorityOverride,
       "rcQosPortCfgDmacPriorityOverride": rcQosPortCfgDmacPriorityOverride,
       "rcQosPortCfgVlanPriorityOverride": rcQosPortCfgVlanPriorityOverride,
       "rcQosPortCos2PriProfile": rcQosPortCos2PriProfile,
       "rcQosPortTos2PriProfile": rcQosPortTos2PriProfile,
       "rcQosPortDscp2PriProfile": rcQosPortDscp2PriProfile,
       "rcQosPortDscpMutationProfile": rcQosPortDscpMutationProfile,
       "rcQosPortCosRemarkProfile": rcQosPortCosRemarkProfile,
       "rcQosPortSchedulerQueueTable": rcQosPortSchedulerQueueTable,
       "rcQosPortSchedulerQueueEntry": rcQosPortSchedulerQueueEntry,
       "rcQosPortSchedulerPortId": rcQosPortSchedulerPortId,
       "rcQosPortSchedulerQueueId": rcQosPortSchedulerQueueId,
       "rcQosPortSchedulerWRR": rcQosPortSchedulerWRR,
       "rcQosPortSchedulerDRR": rcQosPortSchedulerDRR,
       "rcQosPortSchedulerWFQ": rcQosPortSchedulerWFQ,
       "rcQosLocalPrioMappingTable": rcQosLocalPrioMappingTable,
       "rcQosLocalPrioMappingEntry": rcQosLocalPrioMappingEntry,
       "rcQosLocalPriority": rcQosLocalPriority,
       "rcQosQueueId": rcQosQueueId,
       "rcQosCosMappingTable": rcQosCosMappingTable,
       "rcQosCosMappingEntry": rcQosCosMappingEntry,
       "rcQosCosValue": rcQosCosValue,
       "rcQosCosLocalPriority": rcQosCosLocalPriority,
       "rcQosCosColor": rcQosCosColor,
       "rcQosTosMappingTable": rcQosTosMappingTable,
       "rcQosTosMappingEntry": rcQosTosMappingEntry,
       "rcQosTosValue": rcQosTosValue,
       "rcQosTosLocalPriority": rcQosTosLocalPriority,
       "rcQosTosColor": rcQosTosColor,
       "rcQosDscpMapingTable": rcQosDscpMapingTable,
       "rcQosDscpMapingEntry": rcQosDscpMapingEntry,
       "rcQosDscpValue": rcQosDscpValue,
       "rcQosDscpLocalPriority": rcQosDscpLocalPriority,
       "rcQosDscpColor": rcQosDscpColor,
       "rcQosSchedulerQueueTable": rcQosSchedulerQueueTable,
       "rcQosSchedulerQueueEntry": rcQosSchedulerQueueEntry,
       "rcQosSchedulerQueueId": rcQosSchedulerQueueId,
       "rcQosSchedulerWRR": rcQosSchedulerWRR,
       "rcQosSchedulerDRR": rcQosSchedulerDRR,
       "rcQosSchedulerWFQ": rcQosSchedulerWFQ,
       "rcQosWredTcpConfigTable": rcQosWredTcpConfigTable,
       "rcQosWredTcpConfigEntry": rcQosWredTcpConfigEntry,
       "rcQosWredQueueId": rcQosWredQueueId,
       "rcQosWredGreenDropStartPoint": rcQosWredGreenDropStartPoint,
       "rcQosWredGreenDropEndPoint": rcQosWredGreenDropEndPoint,
       "rcQosWredGreenDropProbability": rcQosWredGreenDropProbability,
       "rcQosWredYellowDropStartPoint": rcQosWredYellowDropStartPoint,
       "rcQosWredYellowDropEndPoint": rcQosWredYellowDropEndPoint,
       "rcQosWredYellowDropProbability": rcQosWredYellowDropProbability,
       "rcQosWredRedDropStartPoint": rcQosWredRedDropStartPoint,
       "rcQosWredRedDropEndPoint": rcQosWredRedDropEndPoint,
       "rcQosWredRedDropProbability": rcQosWredRedDropProbability,
       "rcQosWredStatus": rcQosWredStatus,
       "rcQosPortWredTcpConfigTable": rcQosPortWredTcpConfigTable,
       "rcQosPortWredTcpConfigEntry": rcQosPortWredTcpConfigEntry,
       "rcQosPortWredPortId": rcQosPortWredPortId,
       "rcQosPortWredQueueId": rcQosPortWredQueueId,
       "rcQosPortWredGreenDropStartPoint": rcQosPortWredGreenDropStartPoint,
       "rcQosPortWredGreenDropEndPoint": rcQosPortWredGreenDropEndPoint,
       "rcQosPortWredGreenDropProbability": rcQosPortWredGreenDropProbability,
       "rcQosPortWredYellowDropStartPoint": rcQosPortWredYellowDropStartPoint,
       "rcQosPortWredYellowDropEndPoint": rcQosPortWredYellowDropEndPoint,
       "rcQosPortWredYellowDropProbability": rcQosPortWredYellowDropProbability,
       "rcQosPortWredRedDropStartPoint": rcQosPortWredRedDropStartPoint,
       "rcQosPortWredRedDropEndPoint": rcQosPortWredRedDropEndPoint,
       "rcQosPortWredRedDropProbability": rcQosPortWredRedDropProbability,
       "rcQosPortWredStatus": rcQosPortWredStatus,
       "rcQosShapingTable": rcQosShapingTable,
       "rcQosShapingEntry": rcQosShapingEntry,
       "rcQosShapingQueueId": rcQosShapingQueueId,
       "rcQosShapingCir": rcQosShapingCir,
       "rcQosShapingCbs": rcQosShapingCbs,
       "rcQosShapingPir": rcQosShapingPir,
       "rcQosShapingPbs": rcQosShapingPbs,
       "rcQosShapingStatus": rcQosShapingStatus,
       "rcQosPortShapingTable": rcQosPortShapingTable,
       "rcQosPortShapingEntry": rcQosPortShapingEntry,
       "rcQosPortShapingPortId": rcQosPortShapingPortId,
       "rcQosPortShapingQueueId": rcQosPortShapingQueueId,
       "rcQosPortShapingCir": rcQosPortShapingCir,
       "rcQosPortShapingCbs": rcQosPortShapingCbs,
       "rcQosPortShapingPir": rcQosPortShapingPir,
       "rcQosPortShapingPbs": rcQosPortShapingPbs,
       "rcQosPortShapingStatus": rcQosPortShapingStatus,
       "rcQosPortCosMappingTable": rcQosPortCosMappingTable,
       "rcQosPortCosMappingEntry": rcQosPortCosMappingEntry,
       "rcQosPortCosPortId": rcQosPortCosPortId,
       "rcQosPortCosValue": rcQosPortCosValue,
       "rcQosPortCosLocalPriority": rcQosPortCosLocalPriority,
       "rcQosPortCosColor": rcQosPortCosColor,
       "rcQosPortTosMappingTable": rcQosPortTosMappingTable,
       "rcQosPortTosMappingEntry": rcQosPortTosMappingEntry,
       "rcQosPortTosPortId": rcQosPortTosPortId,
       "rcQosPortTosValue": rcQosPortTosValue,
       "rcQosPortTosLocalPriority": rcQosPortTosLocalPriority,
       "rcQosPortTosColor": rcQosPortTosColor,
       "rcQosPortDscpMapingTable": rcQosPortDscpMapingTable,
       "rcQosPortDscpMapingEntry": rcQosPortDscpMapingEntry,
       "rcQosPortDscpPortId": rcQosPortDscpPortId,
       "rcQosPortDscpValue": rcQosPortDscpValue,
       "rcQosPortDscpLocalPriority": rcQosPortDscpLocalPriority,
       "rcQosPortDscpColor": rcQosPortDscpColor,
       "rcQosPortDropPktsStatisticTable": rcQosPortDropPktsStatisticTable,
       "rcQosPortDropPktsStatisticEntry": rcQosPortDropPktsStatisticEntry,
       "rcQosPortStatisticsPortId": rcQosPortStatisticsPortId,
       "rcQosPortStatisticsQueueId": rcQosPortStatisticsQueueId,
       "rcQosPortStatisticsDropPkts": rcQosPortStatisticsDropPkts,
       "rcQosPortStatisticsDropBytes": rcQosPortStatisticsDropBytes,
       "rcQosPortStatisticsDropUnit": rcQosPortStatisticsDropUnit,
       "rcQosPortStatisticsClear": rcQosPortStatisticsClear,
       "rcQosMappingCosToPriTable": rcQosMappingCosToPriTable,
       "rcQosMappingCosToPriEntry": rcQosMappingCosToPriEntry,
       "rcQosCosToPriIndex": rcQosCosToPriIndex,
       "rcQosCosToPriCos": rcQosCosToPriCos,
       "rcQosCosToPriLpri": rcQosCosToPriLpri,
       "rcQosCosToPriColor": rcQosCosToPriColor,
       "rcQosCosToPriDesc": rcQosCosToPriDesc,
       "rcQosCosToPriRef": rcQosCosToPriRef,
       "rcQosCosToPriStatus": rcQosCosToPriStatus,
       "rcQosMappingTosToPriTable": rcQosMappingTosToPriTable,
       "rcQosMappingTosToPriEntry": rcQosMappingTosToPriEntry,
       "rcQosTosToPriIndex": rcQosTosToPriIndex,
       "rcQosTosToPriTos": rcQosTosToPriTos,
       "rcQosTosToPriLpri": rcQosTosToPriLpri,
       "rcQosTosToPriColor": rcQosTosToPriColor,
       "rcQosTosToPriDesc": rcQosTosToPriDesc,
       "rcQosTosToPriRef": rcQosTosToPriRef,
       "rcQosTosToPriStatus": rcQosTosToPriStatus,
       "rcQosMappingDscpToPriTable": rcQosMappingDscpToPriTable,
       "rcQosMappingDscpToPriEntry": rcQosMappingDscpToPriEntry,
       "rcQosDscpToPriIndex": rcQosDscpToPriIndex,
       "rcQosDscpToPriDscp": rcQosDscpToPriDscp,
       "rcQosDscpToPriLpri": rcQosDscpToPriLpri,
       "rcQosDscpToPriColor": rcQosDscpToPriColor,
       "rcQosDscpToPriDesc": rcQosDscpToPriDesc,
       "rcQosDscpToPriRef": rcQosDscpToPriRef,
       "rcQosDscpToPriStatus": rcQosDscpToPriStatus,
       "rcQosMappingDscpMutationTable": rcQosMappingDscpMutationTable,
       "rcQosMappingDscpMutationEntry": rcQosMappingDscpMutationEntry,
       "rcQosDscpMutationIndex": rcQosDscpMutationIndex,
       "rcQosDscpMutationDscp": rcQosDscpMutationDscp,
       "rcQosDscpMutationNewDscp": rcQosDscpMutationNewDscp,
       "rcQosDscpMutationDesc": rcQosDscpMutationDesc,
       "rcQosDscpMutationRef": rcQosDscpMutationRef,
       "rcQosDscpMutationStatus": rcQosDscpMutationStatus,
       "rcQosMappingCosRemarkTable": rcQosMappingCosRemarkTable,
       "rcQosMappingCosRemarkEntry": rcQosMappingCosRemarkEntry,
       "rcQosCosRemarkIndex": rcQosCosRemarkIndex,
       "rcQosCosRemarkLpri": rcQosCosRemarkLpri,
       "rcQosCosRemarkCos": rcQosCosRemarkCos,
       "rcQosCosRemarkDesc": rcQosCosRemarkDesc,
       "rcQosCosRemarkRef": rcQosCosRemarkRef,
       "rcQosCosRemarkStatus": rcQosCosRemarkStatus,
       "rcQosWredProfileTable": rcQosWredProfileTable,
       "rcQosWredProfileEntry": rcQosWredProfileEntry,
       "rcQosWredProfileIndex": rcQosWredProfileIndex,
       "rcQosWredProfileGreenDropStartPoint": rcQosWredProfileGreenDropStartPoint,
       "rcQosWredProfileGreenDropEndPoint": rcQosWredProfileGreenDropEndPoint,
       "rcQosWredProfileGreenDropProbability": rcQosWredProfileGreenDropProbability,
       "rcQosWredProfileYellowDropStartPoint": rcQosWredProfileYellowDropStartPoint,
       "rcQosWredProfileYellowDropEndPoint": rcQosWredProfileYellowDropEndPoint,
       "rcQosWredProfileYellowDropProbability": rcQosWredProfileYellowDropProbability,
       "rcQosWredProfileRedDropStartPoint": rcQosWredProfileRedDropStartPoint,
       "rcQosWredProfileRedDropEndPoint": rcQosWredProfileRedDropEndPoint,
       "rcQosWredProfileRedDropProbability": rcQosWredProfileRedDropProbability,
       "rcQosWredProfileDesc": rcQosWredProfileDesc,
       "rcQosWredProfileRef": rcQosWredProfileRef,
       "rcQosWredProfileStatus": rcQosWredProfileStatus,
       "rcQosGloWredProfileTable": rcQosGloWredProfileTable,
       "rcQosGloWredProfileEntry": rcQosGloWredProfileEntry,
       "rcQosGloWredProfileQueueId": rcQosGloWredProfileQueueId,
       "rcQosGloWredProfileIndex": rcQosGloWredProfileIndex,
       "rcQosGloWredProfileStatus": rcQosGloWredProfileStatus,
       "rcQosPortWredProfileTable": rcQosPortWredProfileTable,
       "rcQosPortWredProfileEntry": rcQosPortWredProfileEntry,
       "rcQosPortWredProfilePortId": rcQosPortWredProfilePortId,
       "rcQosPortWredProfileQueueId": rcQosPortWredProfileQueueId,
       "rcQosPortWredProfileIndex": rcQosPortWredProfileIndex,
       "rcQosPortWredProfileStatus": rcQosPortWredProfileStatus,
       "raisecomQosTrafficClass": raisecomQosTrafficClass,
       "rcPolicyEnable": rcPolicyEnable,
       "rcQosServicePolicyTable": rcQosServicePolicyTable,
       "rcQosServicePolicyEntry": rcQosServicePolicyEntry,
       "rcQosServicePolicyIngress": rcQosServicePolicyIngress,
       "rcQosServicePolicyEgress": rcQosServicePolicyEgress,
       "rcQosServicePolicyMapName": rcQosServicePolicyMapName,
       "rcQosServicePolicyStatus": rcQosServicePolicyStatus,
       "rcQosPolicyMapCfgTable": rcQosPolicyMapCfgTable,
       "rcQosPolicyMapCfgEntry": rcQosPolicyMapCfgEntry,
       "rcQosPolicyMapName": rcQosPolicyMapName,
       "rcQosPolicyMapDesc": rcQosPolicyMapDesc,
       "rcQosPolicyMapCfgStatus": rcQosPolicyMapCfgStatus,
       "rcQosPolicyMapType": rcQosPolicyMapType,
       "rcQosCMCfgTable": rcQosCMCfgTable,
       "rcQosCMCfgEntry": rcQosCMCfgEntry,
       "rcQosCMName": rcQosCMName,
       "rcQosCMDesc": rcQosCMDesc,
       "rcQosCMMatchType": rcQosCMMatchType,
       "rcQosCMClassID": rcQosCMClassID,
       "rcQosCMStatus": rcQosCMStatus,
       "rcQosCMDoubleTagging": rcQosCMDoubleTagging,
       "rcQosMatchStmtTable": rcQosMatchStmtTable,
       "rcQosMatchStmtEntry": rcQosMatchStmtEntry,
       "rcQosMatchStmtClassName": rcQosMatchStmtClassName,
       "rcQosMatchStmtType": rcQosMatchStmtType,
       "rcQosMatchStmtValue": rcQosMatchStmtValue,
       "rcQosMatchStmtSubName": rcQosMatchStmtSubName,
       "rcQosMatchStmtStatus": rcQosMatchStmtStatus,
       "rcQosPolicerCfgTable": rcQosPolicerCfgTable,
       "rcQosPolicerCfgEntry": rcQosPolicerCfgEntry,
       "rcQosPolicerCfgName": rcQosPolicerCfgName,
       "rcQosPolicerCfgType": rcQosPolicerCfgType,
       "rcQosPolicerCfgMode": rcQosPolicerCfgMode,
       "rcQosPolicerCfgCIR": rcQosPolicerCfgCIR,
       "rcQosPolicerCfgEIR": rcQosPolicerCfgEIR,
       "rcQosPolicerCfgCBS": rcQosPolicerCfgCBS,
       "rcQosPolicerCfgEBS": rcQosPolicerCfgEBS,
       "rcQosPolicerGreenActType": rcQosPolicerGreenActType,
       "rcQosPolicerGreenActDscp": rcQosPolicerGreenActDscp,
       "rcQosPolicerGreenActCos": rcQosPolicerGreenActCos,
       "rcQosPolicerGreenActLocalPrio": rcQosPolicerGreenActLocalPrio,
       "rcQosPolicerGreenActColor": rcQosPolicerGreenActColor,
       "rcQosPolicerGreenActCopytoCpu": rcQosPolicerGreenActCopytoCpu,
       "rcQosPolicerYellowActType": rcQosPolicerYellowActType,
       "rcQosPolicerYellowActDscp": rcQosPolicerYellowActDscp,
       "rcQosPolicerYellowActCos": rcQosPolicerYellowActCos,
       "rcQosPolicerYellowActLocalPrio": rcQosPolicerYellowActLocalPrio,
       "rcQosPolicerYellowActColor": rcQosPolicerYellowActColor,
       "rcQosPolicerYellowActCopytoCpu": rcQosPolicerYellowActCopytoCpu,
       "rcQosPolicerRedActType": rcQosPolicerRedActType,
       "rcQosPolicerRedActDscp": rcQosPolicerRedActDscp,
       "rcQosPolicerRedActCos": rcQosPolicerRedActCos,
       "rcQosPolicerRedActLocalPrio": rcQosPolicerRedActLocalPrio,
       "rcQosPolicerRedActColor": rcQosPolicerRedActColor,
       "rcQosPolicerRedActCopytoCpu": rcQosPolicerRedActCopytoCpu,
       "rcQosPolicerColorMode": rcQosPolicerColorMode,
       "rcQoSPolicerRef": rcQoSPolicerRef,
       "rcQosPolicerStatus": rcQosPolicerStatus,
       "rcQosActionCfgTable": rcQosActionCfgTable,
       "rcQosActionCfgEntry": rcQosActionCfgEntry,
       "rcQosActionPmapName": rcQosActionPmapName,
       "rcQosActionCmapName": rcQosActionCmapName,
       "rcQosActionType": rcQosActionType,
       "rcQosActionSetValue": rcQosActionSetValue,
       "rcQosActionPoliceName": rcQosActionPoliceName,
       "rcQosActionStatsEnable": rcQosActionStatsEnable,
       "rcQosActionStatus": rcQosActionStatus,
       "rcQosActionRedirectPort": rcQosActionRedirectPort,
       "rcQosActionSetVlan": rcQosActionSetVlan,
       "rcQosActionSetInnerVlan": rcQosActionSetInnerVlan,
       "rcQosActionAddOuterVlan": rcQosActionAddOuterVlan,
       "rcQosActionCopyToMirror": rcQosActionCopyToMirror,
       "rcQosActionMirrorToPort": rcQosActionMirrorToPort,
       "rcQosActionSetLocalPriority": rcQosActionSetLocalPriority,
       "rcQosActionHierarchyPoliceName": rcQosActionHierarchyPoliceName,
       "rcQosActionSetIpPrece": rcQosActionSetIpPrece,
       "rcQosActionSetIpDscp": rcQosActionSetIpDscp,
       "rcQosActionSetCos": rcQosActionSetCos,
       "rcQosActionSetIPAddressType": rcQosActionSetIPAddressType,
       "rcQosActionSetIPAddress": rcQosActionSetIPAddress,
       "rcQosActionCopyToMirrorSession": rcQosActionCopyToMirrorSession,
       "rcQosServicePolicyEgressTable": rcQosServicePolicyEgressTable,
       "rcQosServicePolicyEgressEntry": rcQosServicePolicyEgressEntry,
       "rcQosServicePolicyEgressIndex": rcQosServicePolicyEgressIndex,
       "rcQosServicePolicyEgressMapName": rcQosServicePolicyEgressMapName,
       "rcQosServicePolicyEgressStatus": rcQosServicePolicyEgressStatus,
       "rcQosCosServicePolicyTable": rcQosCosServicePolicyTable,
       "rcQosCosServicePolicyEntry": rcQosCosServicePolicyEntry,
       "rcQosCosServicePolicyPort": rcQosCosServicePolicyPort,
       "rcQosCosServicePolicyVlan": rcQosCosServicePolicyVlan,
       "rcQosCosServicePolicyMapName": rcQosCosServicePolicyMapName,
       "rcQosCosServicePolicyRowStatus": rcQosCosServicePolicyRowStatus,
       "rcQosVlanPolicyTable": rcQosVlanPolicyTable,
       "rcQosVlanPolicyEntry": rcQosVlanPolicyEntry,
       "rcQosVlanPolicyPmapName": rcQosVlanPolicyPmapName,
       "rcQosVlanPolicyVlan": rcQosVlanPolicyVlan,
       "rcQosVlanPolicyPolicerName": rcQosVlanPolicyPolicerName,
       "rcQosVlanPolicyRowStatus": rcQosVlanPolicyRowStatus,
       "rcQosCosPolicyTable": rcQosCosPolicyTable,
       "rcQosCosPolicyEntry": rcQosCosPolicyEntry,
       "rcQosCosPolicyPmapName": rcQosCosPolicyPmapName,
       "rcQosCosPolicyCos": rcQosCosPolicyCos,
       "rcQosCosPolicyPolicerName": rcQosCosPolicyPolicerName,
       "rcQosCosPolicyRowStatus": rcQosCosPolicyRowStatus,
       "rcQosBandwidthProfileCfgTable": rcQosBandwidthProfileCfgTable,
       "rcQosBandwidthProfileCfgEntry": rcQosBandwidthProfileCfgEntry,
       "rcQosBandwidthProfileCfgIndex": rcQosBandwidthProfileCfgIndex,
       "rcQosBandwidthProfileCfgCIR": rcQosBandwidthProfileCfgCIR,
       "rcQosBandwidthProfileCfgEIR": rcQosBandwidthProfileCfgEIR,
       "rcQosBandwidthProfileCfgCBS": rcQosBandwidthProfileCfgCBS,
       "rcQosBandwidthProfileCfgEBS": rcQosBandwidthProfileCfgEBS,
       "rcQosBandwidthProfileColorMode": rcQosBandwidthProfileColorMode,
       "rcQosBandwidthProfileCoupling": rcQosBandwidthProfileCoupling,
       "rcQoSBandwidthProfileRef": rcQoSBandwidthProfileRef,
       "rcQosBandwidthProfileStatus": rcQosBandwidthProfileStatus,
       "rcQosBandwidthProfileDesc": rcQosBandwidthProfileDesc,
       "rcQosHierarchyCosIndexCfgTable": rcQosHierarchyCosIndexCfgTable,
       "rcQosHierarchyCosIndexCfgEntry": rcQosHierarchyCosIndexCfgEntry,
       "rcQosHierarchyCosIndex": rcQosHierarchyCosIndex,
       "rcQosHierarchyCosRef": rcQosHierarchyCosRef,
       "rcQosHierarchyCosCfgStatus": rcQosHierarchyCosCfgStatus,
       "rcQosHierarchyCosCfgDesc": rcQosHierarchyCosCfgDesc,
       "rcQosHCosBandwidthProfileTable": rcQosHCosBandwidthProfileTable,
       "rcQosHCosBandwidthProfileEntry": rcQosHCosBandwidthProfileEntry,
       "rcQosHCosBandwidthProfileIndex": rcQosHCosBandwidthProfileIndex,
       "rcQosHCosBandwidthProfileCos": rcQosHCosBandwidthProfileCos,
       "rcQosHCosBandwidthProfileBwpIndex": rcQosHCosBandwidthProfileBwpIndex,
       "rcQoSHCosBandwidthProfileRef": rcQoSHCosBandwidthProfileRef,
       "rcQosHCosBandwidthProfileRowStatus": rcQosHCosBandwidthProfileRowStatus,
       "rcQosHierarchyVlanIndexCfgTable": rcQosHierarchyVlanIndexCfgTable,
       "rcQosHierarchyVlanIndexCfgEntry": rcQosHierarchyVlanIndexCfgEntry,
       "rcQosHierarchyVlanIndex": rcQosHierarchyVlanIndex,
       "rcQosHierarchyVlanRef": rcQosHierarchyVlanRef,
       "rcQosHierarchyVlanCfgStatus": rcQosHierarchyVlanCfgStatus,
       "rcQosHierarchyVlanCfgDesc": rcQosHierarchyVlanCfgDesc,
       "rcQosHVlanBandwidthProfileTable": rcQosHVlanBandwidthProfileTable,
       "rcQosHVlanBandwidthProfileEntry": rcQosHVlanBandwidthProfileEntry,
       "rcQosHVlanBandwidthProfileIndex": rcQosHVlanBandwidthProfileIndex,
       "rcQosHVlanBandwidthProfileVlan": rcQosHVlanBandwidthProfileVlan,
       "rcQosHVlanBandwidthProfileBwpIndex": rcQosHVlanBandwidthProfileBwpIndex,
       "rcQoSHVlanBandwidthProfileRef": rcQoSHVlanBandwidthProfileRef,
       "rcQosHVlanBandwidthProfileRowStatus": rcQosHVlanBandwidthProfileRowStatus,
       "rcQosBandwidthPortTable": rcQosBandwidthPortTable,
       "rcQosBandwidthPortEntry": rcQosBandwidthPortEntry,
       "rcQosBandwidthPortIndex": rcQosBandwidthPortIndex,
       "rcQosBandwidthPortBwpIndex": rcQosBandwidthPortBwpIndex,
       "rcQosBandwidthPortEgrBwpIndex": rcQosBandwidthPortEgrBwpIndex,
       "rcQosBandwidthPortHBwEnable": rcQosBandwidthPortHBwEnable,
       "rcQosBandwidthPortHvBwpIndex": rcQosBandwidthPortHvBwpIndex,
       "rcQosBandwidthPortDeiRemarkEnable": rcQosBandwidthPortDeiRemarkEnable,
       "rcQosBandwidthPortColorAwareEnable": rcQosBandwidthPortColorAwareEnable,
       "rcQosBandwidthVlanTable": rcQosBandwidthVlanTable,
       "rcQosBandwidthVlanEntry": rcQosBandwidthVlanEntry,
       "rcQosBandwidthVlanIndex": rcQosBandwidthVlanIndex,
       "rcQosBandwidthVlanPort": rcQosBandwidthVlanPort,
       "rcQosBandwidthVlanPortType": rcQosBandwidthVlanPortType,
       "rcQosBandwidthVlanBwpIndex": rcQosBandwidthVlanBwpIndex,
       "rcQosBandwidthVlanHBwEnable": rcQosBandwidthVlanHBwEnable,
       "rcQosBandwidthVlanHcBwpIndex": rcQosBandwidthVlanHcBwpIndex,
       "rcQosBandwidthVlanRowStatus": rcQosBandwidthVlanRowStatus,
       "rcQosBandwidthCosTable": rcQosBandwidthCosTable,
       "rcQosBandwidthCosEntry": rcQosBandwidthCosEntry,
       "rcQosBandwidthCosIndex": rcQosBandwidthCosIndex,
       "rcQosBandwidthCosVlan": rcQosBandwidthCosVlan,
       "rcQosBandwidthCosPort": rcQosBandwidthCosPort,
       "rcQosBandwidthCosPortType": rcQosBandwidthCosPortType,
       "rcQosBandwidthCosBwpIndex": rcQosBandwidthCosBwpIndex,
       "rcQosBandwidthCosRowStatus": rcQosBandwidthCosRowStatus,
       "rcQosBandwidthGlobalEnable": rcQosBandwidthGlobalEnable,
       "rcQosBandwidthNotificationGroup": rcQosBandwidthNotificationGroup,
       "rcQosBandwidthPortModification": rcQosBandwidthPortModification,
       "rcQosBandwidthVlanModification": rcQosBandwidthVlanModification,
       "rcQosBandwidthCosModification": rcQosBandwidthCosModification,
       "raisecomQosStatistics": raisecomQosStatistics,
       "rcQosTrafficStatsTable": rcQosTrafficStatsTable,
       "rcQosTrafficStatsEntry": rcQosTrafficStatsEntry,
       "rcQosTrafficStatsPort": rcQosTrafficStatsPort,
       "rcQosTrafficStatsDirection": rcQosTrafficStatsDirection,
       "rcQosTrafficStatsCmapName": rcQosTrafficStatsCmapName,
       "rcQosTrafficStatsPolicerType": rcQosTrafficStatsPolicerType,
       "rcQosTrafficCounterReset": rcQosTrafficCounterReset,
       "rcQosTrafficPolicyName": rcQosTrafficPolicyName,
       "rcQosTrafficPolicerName": rcQosTrafficPolicerName,
       "rcQosTrafficCounterHwStatus": rcQosTrafficCounterHwStatus,
       "rcQosTrafficStatisticsUnit": rcQosTrafficStatisticsUnit,
       "rcQosTrafficCounterInprofilePkt64": rcQosTrafficCounterInprofilePkt64,
       "rcQosTrafficCounterInprofileByte64": rcQosTrafficCounterInprofileByte64,
       "rcQosTrafficCounterOutprofilePkt64": rcQosTrafficCounterOutprofilePkt64,
       "rcQosTrafficCounterOutprofileByte64": rcQosTrafficCounterOutprofileByte64,
       "rcQosTrafficbStatistics": rcQosTrafficbStatistics,
       "rcQosVlanStatisticsTable": rcQosVlanStatisticsTable,
       "rcQosVlanStatisticsEntry": rcQosVlanStatisticsEntry,
       "rcQosVlanStatisticsPort": rcQosVlanStatisticsPort,
       "rcQosVlanStatisticsVlan": rcQosVlanStatisticsVlan,
       "rcQosVlanStatisticsDirection": rcQosVlanStatisticsDirection,
       "rcQosVlanStatisticsUnit": rcQosVlanStatisticsUnit,
       "rcQosVlanStatisticsReset": rcQosVlanStatisticsReset,
       "rcQosVlanStatisticsPkt": rcQosVlanStatisticsPkt,
       "rcQosVlanStatisticsByte": rcQosVlanStatisticsByte,
       "rcQosVlanStatisticsRowStatus": rcQosVlanStatisticsRowStatus,
       "rcQosCosStatisticsTable": rcQosCosStatisticsTable,
       "rcQosCosStatisticsEntry": rcQosCosStatisticsEntry,
       "rcQosCosStatisticsPort": rcQosCosStatisticsPort,
       "rcQosCosStatisticsVlan": rcQosCosStatisticsVlan,
       "rcQosCosStatisticsCos": rcQosCosStatisticsCos,
       "rcQosCosStatisticsDirection": rcQosCosStatisticsDirection,
       "rcQosCosStatisticsUnit": rcQosCosStatisticsUnit,
       "rcQosCosStatisticsReset": rcQosCosStatisticsReset,
       "rcQosCosStatisticsPkt": rcQosCosStatisticsPkt,
       "rcQosCosStatisticsByte": rcQosCosStatisticsByte,
       "rcQosCosStatisticsRowStatus": rcQosCosStatisticsRowStatus}
)
