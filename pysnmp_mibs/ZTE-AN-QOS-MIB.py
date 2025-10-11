# SNMP MIB module (ZTE-AN-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:19 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnQosObjects_ObjectIdentity = ObjectIdentity
zxAnQosObjects = _ZxAnQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1)
)
_ZxAnQosGlobal_ObjectIdentity = ObjectIdentity
zxAnQosGlobal = _ZxAnQosGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 1)
)
_ZxAnInterfaceQosConfTable_Object = MibTable
zxAnInterfaceQosConfTable = _ZxAnInterfaceQosConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnInterfaceQosConfTable.setStatus("current")
_ZxAnInterfaceQosConfEntry_Object = MibTableRow
zxAnInterfaceQosConfEntry = _ZxAnInterfaceQosConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 2, 1)
)
zxAnInterfaceQosConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnInterfaceQosConfEntry.setStatus("current")


class _ZxAnIfQosConfProfileName_Type(DisplayString):
    """Custom type zxAnIfQosConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnIfQosConfProfileName_Type.__name__ = "DisplayString"
_ZxAnIfQosConfProfileName_Object = MibTableColumn
zxAnIfQosConfProfileName = _ZxAnIfQosConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 2, 1, 1),
    _ZxAnIfQosConfProfileName_Type()
)
zxAnIfQosConfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIfQosConfProfileName.setStatus("current")
_ZxAnPortQosConfProfileTable_Object = MibTable
zxAnPortQosConfProfileTable = _ZxAnPortQosConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnPortQosConfProfileTable.setStatus("current")
_ZxAnPortQosConfProfileEntry_Object = MibTableRow
zxAnPortQosConfProfileEntry = _ZxAnPortQosConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1)
)
zxAnPortQosConfProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS-MIB", "zxAnQosConfProfileName"),
)
if mibBuilder.loadTexts:
    zxAnPortQosConfProfileEntry.setStatus("current")


class _ZxAnQosConfProfileName_Type(DisplayString):
    """Custom type zxAnQosConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosConfProfileName_Type.__name__ = "DisplayString"
_ZxAnQosConfProfileName_Object = MibTableColumn
zxAnQosConfProfileName = _ZxAnQosConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 1),
    _ZxAnQosConfProfileName_Type()
)
zxAnQosConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosConfProfileName.setStatus("current")


class _ZxAnQosQueuesNumber_Type(Integer32):
    """Custom type zxAnQosQueuesNumber based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_ZxAnQosQueuesNumber_Type.__name__ = "Integer32"
_ZxAnQosQueuesNumber_Object = MibTableColumn
zxAnQosQueuesNumber = _ZxAnQosQueuesNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 2),
    _ZxAnQosQueuesNumber_Type()
)
zxAnQosQueuesNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueuesNumber.setStatus("current")
_ZxAnQosQueuesMaxSize_Type = ObjectIdentifier
_ZxAnQosQueuesMaxSize_Object = MibTableColumn
zxAnQosQueuesMaxSize = _ZxAnQosQueuesMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 3),
    _ZxAnQosQueuesMaxSize_Type()
)
zxAnQosQueuesMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueuesMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosQueuesMaxSize.setUnits("bytes")


class _ZxAnQosQueueSchedAlgorithm_Type(Integer32):
    """Custom type zxAnQosQueueSchedAlgorithm based on Integer32"""
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
        *(("sp", 1),
          ("wrr", 2),
          ("spAndWrr", 3))
    )


_ZxAnQosQueueSchedAlgorithm_Type.__name__ = "Integer32"
_ZxAnQosQueueSchedAlgorithm_Object = MibTableColumn
zxAnQosQueueSchedAlgorithm = _ZxAnQosQueueSchedAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 4),
    _ZxAnQosQueueSchedAlgorithm_Type()
)
zxAnQosQueueSchedAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueSchedAlgorithm.setStatus("current")
_ZxAnQosQueuesWeight_Type = ObjectIdentifier
_ZxAnQosQueuesWeight_Object = MibTableColumn
zxAnQosQueuesWeight = _ZxAnQosQueuesWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 5),
    _ZxAnQosQueuesWeight_Type()
)
zxAnQosQueuesWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueuesWeight.setStatus("current")
_ZxAnQosPriority2queue_Type = ObjectIdentifier
_ZxAnQosPriority2queue_Object = MibTableColumn
zxAnQosPriority2queue = _ZxAnQosPriority2queue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 6),
    _ZxAnQosPriority2queue_Type()
)
zxAnQosPriority2queue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPriority2queue.setStatus("current")
_ZxAnQosPvc2Priority_Type = ObjectIdentifier
_ZxAnQosPvc2Priority_Object = MibTableColumn
zxAnQosPvc2Priority = _ZxAnQosPvc2Priority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 7),
    _ZxAnQosPvc2Priority_Type()
)
zxAnQosPvc2Priority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPvc2Priority.setStatus("current")
_ZxAnQosPriorityRemarking_Type = ObjectIdentifier
_ZxAnQosPriorityRemarking_Object = MibTableColumn
zxAnQosPriorityRemarking = _ZxAnQosPriorityRemarking_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 8),
    _ZxAnQosPriorityRemarking_Type()
)
zxAnQosPriorityRemarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPriorityRemarking.setStatus("current")
_ZxAnQosConfPrfRowStatus_Type = RowStatus
_ZxAnQosConfPrfRowStatus_Object = MibTableColumn
zxAnQosConfPrfRowStatus = _ZxAnQosConfPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 3, 1, 9),
    _ZxAnQosConfPrfRowStatus_Type()
)
zxAnQosConfPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosConfPrfRowStatus.setStatus("current")
_ZxAnBridgePortConfTable_Object = MibTable
zxAnBridgePortConfTable = _ZxAnBridgePortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnBridgePortConfTable.setStatus("current")
_ZxAnBridgePortConfEntry_Object = MibTableRow
zxAnBridgePortConfEntry = _ZxAnBridgePortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 4, 1)
)
zxAnBridgePortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnBridgePortConfEntry.setStatus("current")


class _ZxAnBridgePortConfProfileName_Type(DisplayString):
    """Custom type zxAnBridgePortConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnBridgePortConfProfileName_Type.__name__ = "DisplayString"
_ZxAnBridgePortConfProfileName_Object = MibTableColumn
zxAnBridgePortConfProfileName = _ZxAnBridgePortConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 4, 1, 1),
    _ZxAnBridgePortConfProfileName_Type()
)
zxAnBridgePortConfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBridgePortConfProfileName.setStatus("current")
_ZxAnBridgePortConfProfileTable_Object = MibTable
zxAnBridgePortConfProfileTable = _ZxAnBridgePortConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnBridgePortConfProfileTable.setStatus("current")
_ZxAnBridgePortConfProfileEntry_Object = MibTableRow
zxAnBridgePortConfProfileEntry = _ZxAnBridgePortConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1)
)
zxAnBridgePortConfProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS-MIB", "zxAnBrgPortConfProfileName"),
)
if mibBuilder.loadTexts:
    zxAnBridgePortConfProfileEntry.setStatus("current")


class _ZxAnBrgPortConfProfileName_Type(DisplayString):
    """Custom type zxAnBrgPortConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnBrgPortConfProfileName_Type.__name__ = "DisplayString"
_ZxAnBrgPortConfProfileName_Object = MibTableColumn
zxAnBrgPortConfProfileName = _ZxAnBrgPortConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 1),
    _ZxAnBrgPortConfProfileName_Type()
)
zxAnBrgPortConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgPortConfProfileName.setStatus("current")


class _ZxAnBrgPortDefaultPriorityCvlan_Type(Integer32):
    """Custom type zxAnBrgPortDefaultPriorityCvlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnBrgPortDefaultPriorityCvlan_Type.__name__ = "Integer32"
_ZxAnBrgPortDefaultPriorityCvlan_Object = MibTableColumn
zxAnBrgPortDefaultPriorityCvlan = _ZxAnBrgPortDefaultPriorityCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 2),
    _ZxAnBrgPortDefaultPriorityCvlan_Type()
)
zxAnBrgPortDefaultPriorityCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortDefaultPriorityCvlan.setStatus("current")


class _ZxAnBrgPortPriorityOvrideCvlan_Type(Integer32):
    """Custom type zxAnBrgPortPriorityOvrideCvlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnBrgPortPriorityOvrideCvlan_Type.__name__ = "Integer32"
_ZxAnBrgPortPriorityOvrideCvlan_Object = MibTableColumn
zxAnBrgPortPriorityOvrideCvlan = _ZxAnBrgPortPriorityOvrideCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 3),
    _ZxAnBrgPortPriorityOvrideCvlan_Type()
)
zxAnBrgPortPriorityOvrideCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPriorityOvrideCvlan.setStatus("current")


class _ZxAnBrgPortPriorityOvrideSvlan_Type(Integer32):
    """Custom type zxAnBrgPortPriorityOvrideSvlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnBrgPortPriorityOvrideSvlan_Type.__name__ = "Integer32"
_ZxAnBrgPortPriorityOvrideSvlan_Object = MibTableColumn
zxAnBrgPortPriorityOvrideSvlan = _ZxAnBrgPortPriorityOvrideSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 4),
    _ZxAnBrgPortPriorityOvrideSvlan_Type()
)
zxAnBrgPortPriorityOvrideSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPriorityOvrideSvlan.setStatus("current")


class _ZxAnBrgPortPriorityTrustCvlan_Type(Integer32):
    """Custom type zxAnBrgPortPriorityTrustCvlan based on Integer32"""
    defaultValue = 1

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
        *(("trust", 1),
          ("mapToDscp", 2),
          ("override", 3),
          ("mapFromDscp", 4))
    )


_ZxAnBrgPortPriorityTrustCvlan_Type.__name__ = "Integer32"
_ZxAnBrgPortPriorityTrustCvlan_Object = MibTableColumn
zxAnBrgPortPriorityTrustCvlan = _ZxAnBrgPortPriorityTrustCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 5),
    _ZxAnBrgPortPriorityTrustCvlan_Type()
)
zxAnBrgPortPriorityTrustCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPriorityTrustCvlan.setStatus("current")


class _ZxAnBrgPortPriorityTrustSvlan_Type(Integer32):
    """Custom type zxAnBrgPortPriorityTrustSvlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("override", 1),
          ("copyFromCvlan", 2))
    )


_ZxAnBrgPortPriorityTrustSvlan_Type.__name__ = "Integer32"
_ZxAnBrgPortPriorityTrustSvlan_Object = MibTableColumn
zxAnBrgPortPriorityTrustSvlan = _ZxAnBrgPortPriorityTrustSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 6),
    _ZxAnBrgPortPriorityTrustSvlan_Type()
)
zxAnBrgPortPriorityTrustSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPriorityTrustSvlan.setStatus("current")


class _ZxAnBrgPortPriorityRemarkEnable_Type(Integer32):
    """Custom type zxAnBrgPortPriorityRemarkEnable based on Integer32"""
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


_ZxAnBrgPortPriorityRemarkEnable_Type.__name__ = "Integer32"
_ZxAnBrgPortPriorityRemarkEnable_Object = MibTableColumn
zxAnBrgPortPriorityRemarkEnable = _ZxAnBrgPortPriorityRemarkEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 7),
    _ZxAnBrgPortPriorityRemarkEnable_Type()
)
zxAnBrgPortPriorityRemarkEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPriorityRemarkEnable.setStatus("current")


class _ZxAnBrgPortPriorityFilterEnable_Type(Integer32):
    """Custom type zxAnBrgPortPriorityFilterEnable based on Integer32"""
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


_ZxAnBrgPortPriorityFilterEnable_Type.__name__ = "Integer32"
_ZxAnBrgPortPriorityFilterEnable_Object = MibTableColumn
zxAnBrgPortPriorityFilterEnable = _ZxAnBrgPortPriorityFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 8),
    _ZxAnBrgPortPriorityFilterEnable_Type()
)
zxAnBrgPortPriorityFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPriorityFilterEnable.setStatus("current")


class _ZxAnBrgPortRateLimitUp_Type(Integer32):
    """Custom type zxAnBrgPortRateLimitUp based on Integer32"""
    defaultValue = 12200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12200),
    )


_ZxAnBrgPortRateLimitUp_Type.__name__ = "Integer32"
_ZxAnBrgPortRateLimitUp_Object = MibTableColumn
zxAnBrgPortRateLimitUp = _ZxAnBrgPortRateLimitUp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 9),
    _ZxAnBrgPortRateLimitUp_Type()
)
zxAnBrgPortRateLimitUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortRateLimitUp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgPortRateLimitUp.setUnits("kbps")


class _ZxAnBrgPortRateLimitDown_Type(Integer32):
    """Custom type zxAnBrgPortRateLimitDown based on Integer32"""
    defaultValue = 32640

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32640),
    )


_ZxAnBrgPortRateLimitDown_Type.__name__ = "Integer32"
_ZxAnBrgPortRateLimitDown_Object = MibTableColumn
zxAnBrgPortRateLimitDown = _ZxAnBrgPortRateLimitDown_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 10),
    _ZxAnBrgPortRateLimitDown_Type()
)
zxAnBrgPortRateLimitDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortRateLimitDown.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgPortRateLimitDown.setUnits("kbps")
_ZxAnBrgPortConfPrfRowStatus_Type = RowStatus
_ZxAnBrgPortConfPrfRowStatus_Object = MibTableColumn
zxAnBrgPortConfPrfRowStatus = _ZxAnBrgPortConfPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 11),
    _ZxAnBrgPortConfPrfRowStatus_Type()
)
zxAnBrgPortConfPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortConfPrfRowStatus.setStatus("current")


class _ZxAnBrgPortDefaultPriority_Type(Integer32):
    """Custom type zxAnBrgPortDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnBrgPortDefaultPriority_Type.__name__ = "Integer32"
_ZxAnBrgPortDefaultPriority_Object = MibTableColumn
zxAnBrgPortDefaultPriority = _ZxAnBrgPortDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 12),
    _ZxAnBrgPortDefaultPriority_Type()
)
zxAnBrgPortDefaultPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortDefaultPriority.setStatus("current")


class _ZxAnBrgPortPrioritySetMode_Type(Integer32):
    """Custom type zxAnBrgPortPrioritySetMode based on Integer32"""
    defaultValue = 1

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
        *(("trust", 1),
          ("override", 2),
          ("remark", 3),
          ("trustDscpMap", 4))
    )


_ZxAnBrgPortPrioritySetMode_Type.__name__ = "Integer32"
_ZxAnBrgPortPrioritySetMode_Object = MibTableColumn
zxAnBrgPortPrioritySetMode = _ZxAnBrgPortPrioritySetMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 13),
    _ZxAnBrgPortPrioritySetMode_Type()
)
zxAnBrgPortPrioritySetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPrioritySetMode.setStatus("current")


class _ZxAnBrgPortPrioritySetModeCvlan_Type(Integer32):
    """Custom type zxAnBrgPortPrioritySetModeCvlan based on Integer32"""
    defaultValue = 1

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
        *(("trust", 1),
          ("override", 2),
          ("remark", 3),
          ("trustDscpMap", 4))
    )


_ZxAnBrgPortPrioritySetModeCvlan_Type.__name__ = "Integer32"
_ZxAnBrgPortPrioritySetModeCvlan_Object = MibTableColumn
zxAnBrgPortPrioritySetModeCvlan = _ZxAnBrgPortPrioritySetModeCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 14),
    _ZxAnBrgPortPrioritySetModeCvlan_Type()
)
zxAnBrgPortPrioritySetModeCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortPrioritySetModeCvlan.setStatus("current")


class _ZxAnBrgPortDSCPSetMode_Type(Integer32):
    """Custom type zxAnBrgPortDSCPSetMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("trustQosMap", 2))
    )


_ZxAnBrgPortDSCPSetMode_Type.__name__ = "Integer32"
_ZxAnBrgPortDSCPSetMode_Object = MibTableColumn
zxAnBrgPortDSCPSetMode = _ZxAnBrgPortDSCPSetMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 5, 1, 15),
    _ZxAnBrgPortDSCPSetMode_Type()
)
zxAnBrgPortDSCPSetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortDSCPSetMode.setStatus("current")
_ZxAnQosCos2DscpMappingTable_Object = MibTable
zxAnQosCos2DscpMappingTable = _ZxAnQosCos2DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnQosCos2DscpMappingTable.setStatus("current")
_ZxAnQosCos2DscpMappingEntry_Object = MibTableRow
zxAnQosCos2DscpMappingEntry = _ZxAnQosCos2DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 6, 1)
)
zxAnQosCos2DscpMappingEntry.setIndexNames(
    (0, "ZTE-AN-QOS-MIB", "zxAnQosCos2DscpMappingCos"),
)
if mibBuilder.loadTexts:
    zxAnQosCos2DscpMappingEntry.setStatus("current")


class _ZxAnQosCos2DscpMappingCos_Type(Integer32):
    """Custom type zxAnQosCos2DscpMappingCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosCos2DscpMappingCos_Type.__name__ = "Integer32"
_ZxAnQosCos2DscpMappingCos_Object = MibTableColumn
zxAnQosCos2DscpMappingCos = _ZxAnQosCos2DscpMappingCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 6, 1, 1),
    _ZxAnQosCos2DscpMappingCos_Type()
)
zxAnQosCos2DscpMappingCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosCos2DscpMappingCos.setStatus("current")


class _ZxAnQosCos2DscpMappingDscp_Type(Integer32):
    """Custom type zxAnQosCos2DscpMappingDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosCos2DscpMappingDscp_Type.__name__ = "Integer32"
_ZxAnQosCos2DscpMappingDscp_Object = MibTableColumn
zxAnQosCos2DscpMappingDscp = _ZxAnQosCos2DscpMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 6, 1, 2),
    _ZxAnQosCos2DscpMappingDscp_Type()
)
zxAnQosCos2DscpMappingDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosCos2DscpMappingDscp.setStatus("current")
_ZxAnQosDscp2CosMappingTable_Object = MibTable
zxAnQosDscp2CosMappingTable = _ZxAnQosDscp2CosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnQosDscp2CosMappingTable.setStatus("current")
_ZxAnQosDscp2CosMappingEntry_Object = MibTableRow
zxAnQosDscp2CosMappingEntry = _ZxAnQosDscp2CosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 7, 1)
)
zxAnQosDscp2CosMappingEntry.setIndexNames(
    (0, "ZTE-AN-QOS-MIB", "zxAnQosDscp2CosMappingDscp"),
)
if mibBuilder.loadTexts:
    zxAnQosDscp2CosMappingEntry.setStatus("current")


class _ZxAnQosDscp2CosMappingDscp_Type(Integer32):
    """Custom type zxAnQosDscp2CosMappingDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosDscp2CosMappingDscp_Type.__name__ = "Integer32"
_ZxAnQosDscp2CosMappingDscp_Object = MibTableColumn
zxAnQosDscp2CosMappingDscp = _ZxAnQosDscp2CosMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 7, 1, 1),
    _ZxAnQosDscp2CosMappingDscp_Type()
)
zxAnQosDscp2CosMappingDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosDscp2CosMappingDscp.setStatus("current")


class _ZxAnQosDscp2CosMappingCos_Type(Integer32):
    """Custom type zxAnQosDscp2CosMappingCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosDscp2CosMappingCos_Type.__name__ = "Integer32"
_ZxAnQosDscp2CosMappingCos_Object = MibTableColumn
zxAnQosDscp2CosMappingCos = _ZxAnQosDscp2CosMappingCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 1, 7, 1, 2),
    _ZxAnQosDscp2CosMappingCos_Type()
)
zxAnQosDscp2CosMappingCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosDscp2CosMappingCos.setStatus("current")
_ZxAnQosTrapObjects_ObjectIdentity = ObjectIdentity
zxAnQosTrapObjects = _ZxAnQosTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-QOS-MIB",
    **{"zxAnQosMib": zxAnQosMib,
       "zxAnQosObjects": zxAnQosObjects,
       "zxAnQosGlobal": zxAnQosGlobal,
       "zxAnInterfaceQosConfTable": zxAnInterfaceQosConfTable,
       "zxAnInterfaceQosConfEntry": zxAnInterfaceQosConfEntry,
       "zxAnIfQosConfProfileName": zxAnIfQosConfProfileName,
       "zxAnPortQosConfProfileTable": zxAnPortQosConfProfileTable,
       "zxAnPortQosConfProfileEntry": zxAnPortQosConfProfileEntry,
       "zxAnQosConfProfileName": zxAnQosConfProfileName,
       "zxAnQosQueuesNumber": zxAnQosQueuesNumber,
       "zxAnQosQueuesMaxSize": zxAnQosQueuesMaxSize,
       "zxAnQosQueueSchedAlgorithm": zxAnQosQueueSchedAlgorithm,
       "zxAnQosQueuesWeight": zxAnQosQueuesWeight,
       "zxAnQosPriority2queue": zxAnQosPriority2queue,
       "zxAnQosPvc2Priority": zxAnQosPvc2Priority,
       "zxAnQosPriorityRemarking": zxAnQosPriorityRemarking,
       "zxAnQosConfPrfRowStatus": zxAnQosConfPrfRowStatus,
       "zxAnBridgePortConfTable": zxAnBridgePortConfTable,
       "zxAnBridgePortConfEntry": zxAnBridgePortConfEntry,
       "zxAnBridgePortConfProfileName": zxAnBridgePortConfProfileName,
       "zxAnBridgePortConfProfileTable": zxAnBridgePortConfProfileTable,
       "zxAnBridgePortConfProfileEntry": zxAnBridgePortConfProfileEntry,
       "zxAnBrgPortConfProfileName": zxAnBrgPortConfProfileName,
       "zxAnBrgPortDefaultPriorityCvlan": zxAnBrgPortDefaultPriorityCvlan,
       "zxAnBrgPortPriorityOvrideCvlan": zxAnBrgPortPriorityOvrideCvlan,
       "zxAnBrgPortPriorityOvrideSvlan": zxAnBrgPortPriorityOvrideSvlan,
       "zxAnBrgPortPriorityTrustCvlan": zxAnBrgPortPriorityTrustCvlan,
       "zxAnBrgPortPriorityTrustSvlan": zxAnBrgPortPriorityTrustSvlan,
       "zxAnBrgPortPriorityRemarkEnable": zxAnBrgPortPriorityRemarkEnable,
       "zxAnBrgPortPriorityFilterEnable": zxAnBrgPortPriorityFilterEnable,
       "zxAnBrgPortRateLimitUp": zxAnBrgPortRateLimitUp,
       "zxAnBrgPortRateLimitDown": zxAnBrgPortRateLimitDown,
       "zxAnBrgPortConfPrfRowStatus": zxAnBrgPortConfPrfRowStatus,
       "zxAnBrgPortDefaultPriority": zxAnBrgPortDefaultPriority,
       "zxAnBrgPortPrioritySetMode": zxAnBrgPortPrioritySetMode,
       "zxAnBrgPortPrioritySetModeCvlan": zxAnBrgPortPrioritySetModeCvlan,
       "zxAnBrgPortDSCPSetMode": zxAnBrgPortDSCPSetMode,
       "zxAnQosCos2DscpMappingTable": zxAnQosCos2DscpMappingTable,
       "zxAnQosCos2DscpMappingEntry": zxAnQosCos2DscpMappingEntry,
       "zxAnQosCos2DscpMappingCos": zxAnQosCos2DscpMappingCos,
       "zxAnQosCos2DscpMappingDscp": zxAnQosCos2DscpMappingDscp,
       "zxAnQosDscp2CosMappingTable": zxAnQosDscp2CosMappingTable,
       "zxAnQosDscp2CosMappingEntry": zxAnQosDscp2CosMappingEntry,
       "zxAnQosDscp2CosMappingDscp": zxAnQosDscp2CosMappingDscp,
       "zxAnQosDscp2CosMappingCos": zxAnQosDscp2CosMappingCos,
       "zxAnQosTrapObjects": zxAnQosTrapObjects}
)
