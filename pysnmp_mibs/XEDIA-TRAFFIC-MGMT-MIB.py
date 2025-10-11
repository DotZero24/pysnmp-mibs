# SNMP MIB module (XEDIA-TRAFFIC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/extreme/XEDIA-TRAFFIC-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:25 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaTrafficMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XtmIpAddress(TextualConvention, IpAddress):
    status = "current"
    displayHint = "1d."


class XtmProtocol(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )



class XtmPort(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              20,
              21,
              23,
              25,
              53,
              67,
              68,
              69,
              70,
              79,
              80,
              119,
              123,
              161,
              162,
              179)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ftpData", 20),
          ("ftp", 21),
          ("telnet", 23),
          ("smtp", 25),
          ("domain", 53),
          ("bootps", 67),
          ("bootpc", 68),
          ("tftp", 69),
          ("gopher", 70),
          ("finger", 79),
          ("wwwHttp", 80),
          ("nntp", 119),
          ("ntp", 123),
          ("snmp", 161),
          ("snmpTrap", 162),
          ("bgp", 179))
    )



class XtmBitRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XtmTosOctet(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1



class XtmRange(DisplayString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_XtmObjects_ObjectIdentity = ObjectIdentity
xtmObjects = _XtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1)
)
_XtmClassTable_Object = MibTable
xtmClassTable = _XtmClassTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xtmClassTable.setStatus("current")
_XtmClassEntry_Object = MibTableRow
xtmClassEntry = _XtmClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1)
)
xtmClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XEDIA-TRAFFIC-MGMT-MIB", "xtmClassName"),
)
if mibBuilder.loadTexts:
    xtmClassEntry.setStatus("current")


class _XtmClassName_Type(DisplayString):
    """Custom type xtmClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XtmClassName_Type.__name__ = "DisplayString"
_XtmClassName_Object = MibTableColumn
xtmClassName = _XtmClassName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 1),
    _XtmClassName_Type()
)
xtmClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xtmClassName.setStatus("current")


class _XtmClassParent_Type(DisplayString):
    """Custom type xtmClassParent based on DisplayString"""
    defaultValue = OctetString("interface")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XtmClassParent_Type.__name__ = "DisplayString"
_XtmClassParent_Object = MibTableColumn
xtmClassParent = _XtmClassParent_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 2),
    _XtmClassParent_Type()
)
xtmClassParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassParent.setStatus("current")


class _XtmClassRate_Type(XtmBitRate):
    """Custom type xtmClassRate based on XtmBitRate"""
    defaultValue = 0


_XtmClassRate_Type.__name__ = "XtmBitRate"
_XtmClassRate_Object = MibTableColumn
xtmClassRate = _XtmClassRate_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 13),
    _XtmClassRate_Type()
)
xtmClassRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassRate.setStatus("current")
if mibBuilder.loadTexts:
    xtmClassRate.setUnits("bits per second")


class _XtmClassBounded_Type(TruthValue):
    """Custom type xtmClassBounded based on TruthValue"""
    defaultValue = 2


_XtmClassBounded_Type.__name__ = "TruthValue"
_XtmClassBounded_Object = MibTableColumn
xtmClassBounded = _XtmClassBounded_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 14),
    _XtmClassBounded_Type()
)
xtmClassBounded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassBounded.setStatus("current")


class _XtmClassPriority_Type(Integer32):
    """Custom type xtmClassPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_XtmClassPriority_Type.__name__ = "Integer32"
_XtmClassPriority_Object = MibTableColumn
xtmClassPriority = _XtmClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 15),
    _XtmClassPriority_Type()
)
xtmClassPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassPriority.setStatus("current")


class _XtmClassOperStatus_Type(Integer32):
    """Custom type xtmClassOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("downConflict", 3),
          ("autoClassActive", 4))
    )


_XtmClassOperStatus_Type.__name__ = "Integer32"
_XtmClassOperStatus_Object = MibTableColumn
xtmClassOperStatus = _XtmClassOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 22),
    _XtmClassOperStatus_Type()
)
xtmClassOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtmClassOperStatus.setStatus("current")
_XtmClassOperMsg_Type = DisplayString
_XtmClassOperMsg_Object = MibTableColumn
xtmClassOperMsg = _XtmClassOperMsg_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 23),
    _XtmClassOperMsg_Type()
)
xtmClassOperMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtmClassOperMsg.setStatus("current")


class _XtmClassBwUse_Type(Integer32):
    """Custom type xtmClassBwUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atLimit", 1),
          ("underLimit", 2),
          ("overLimit", 3))
    )


_XtmClassBwUse_Type.__name__ = "Integer32"
_XtmClassBwUse_Object = MibTableColumn
xtmClassBwUse = _XtmClassBwUse_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 24),
    _XtmClassBwUse_Type()
)
xtmClassBwUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtmClassBwUse.setStatus("current")
_XtmClassUnsatisfied_Type = TruthValue
_XtmClassUnsatisfied_Object = MibTableColumn
xtmClassUnsatisfied = _XtmClassUnsatisfied_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 25),
    _XtmClassUnsatisfied_Type()
)
xtmClassUnsatisfied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtmClassUnsatisfied.setStatus("current")


class _XtmClassQueueSize_Type(Gauge32):
    """Custom type xtmClassQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_XtmClassQueueSize_Type.__name__ = "Gauge32"
_XtmClassQueueSize_Object = MibTableColumn
xtmClassQueueSize = _XtmClassQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 26),
    _XtmClassQueueSize_Type()
)
xtmClassQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtmClassQueueSize.setStatus("current")
_XtmClassRowStatus_Type = RowStatus
_XtmClassRowStatus_Object = MibTableColumn
xtmClassRowStatus = _XtmClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 27),
    _XtmClassRowStatus_Type()
)
xtmClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassRowStatus.setStatus("current")


class _XtmClassMaxRate_Type(XtmBitRate):
    """Custom type xtmClassMaxRate based on XtmBitRate"""
    defaultValue = 0


_XtmClassMaxRate_Type.__name__ = "XtmBitRate"
_XtmClassMaxRate_Object = MibTableColumn
xtmClassMaxRate = _XtmClassMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 28),
    _XtmClassMaxRate_Type()
)
xtmClassMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    xtmClassMaxRate.setUnits("bits per second")


class _XtmClassPeerClassificationOrder_Type(Integer32):
    """Custom type xtmClassPeerClassificationOrder based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XtmClassPeerClassificationOrder_Type.__name__ = "Integer32"
_XtmClassPeerClassificationOrder_Object = MibTableColumn
xtmClassPeerClassificationOrder = _XtmClassPeerClassificationOrder_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 44),
    _XtmClassPeerClassificationOrder_Type()
)
xtmClassPeerClassificationOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassPeerClassificationOrder.setStatus("current")
_XtmClassSrcIpAddresses_Type = XtmRange
_XtmClassSrcIpAddresses_Object = MibTableColumn
xtmClassSrcIpAddresses = _XtmClassSrcIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 45),
    _XtmClassSrcIpAddresses_Type()
)
xtmClassSrcIpAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassSrcIpAddresses.setStatus("current")
_XtmClassDestIpAddresses_Type = XtmRange
_XtmClassDestIpAddresses_Object = MibTableColumn
xtmClassDestIpAddresses = _XtmClassDestIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 46),
    _XtmClassDestIpAddresses_Type()
)
xtmClassDestIpAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassDestIpAddresses.setStatus("current")
_XtmClassProtocols_Type = XtmRange
_XtmClassProtocols_Object = MibTableColumn
xtmClassProtocols = _XtmClassProtocols_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 47),
    _XtmClassProtocols_Type()
)
xtmClassProtocols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassProtocols.setStatus("current")
_XtmClassSrcPorts_Type = XtmRange
_XtmClassSrcPorts_Object = MibTableColumn
xtmClassSrcPorts = _XtmClassSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 48),
    _XtmClassSrcPorts_Type()
)
xtmClassSrcPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassSrcPorts.setStatus("current")
_XtmClassDestPorts_Type = XtmRange
_XtmClassDestPorts_Object = MibTableColumn
xtmClassDestPorts = _XtmClassDestPorts_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 49),
    _XtmClassDestPorts_Type()
)
xtmClassDestPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassDestPorts.setStatus("current")
_XtmClassApplications_Type = XtmRange
_XtmClassApplications_Object = MibTableColumn
xtmClassApplications = _XtmClassApplications_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 50),
    _XtmClassApplications_Type()
)
xtmClassApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassApplications.setStatus("current")
_XtmClassClassificationTos_Type = XtmRange
_XtmClassClassificationTos_Object = MibTableColumn
xtmClassClassificationTos = _XtmClassClassificationTos_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 51),
    _XtmClassClassificationTos_Type()
)
xtmClassClassificationTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassClassificationTos.setStatus("current")
_XtmClassSrcDomainNames_Type = XtmRange
_XtmClassSrcDomainNames_Object = MibTableColumn
xtmClassSrcDomainNames = _XtmClassSrcDomainNames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 52),
    _XtmClassSrcDomainNames_Type()
)
xtmClassSrcDomainNames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassSrcDomainNames.setStatus("current")
_XtmClassDestDomainNames_Type = XtmRange
_XtmClassDestDomainNames_Object = MibTableColumn
xtmClassDestDomainNames = _XtmClassDestDomainNames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 53),
    _XtmClassDestDomainNames_Type()
)
xtmClassDestDomainNames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassDestDomainNames.setStatus("current")


class _XtmClassOperator_Type(Integer32):
    """Custom type xtmClassOperator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2))
    )


_XtmClassOperator_Type.__name__ = "Integer32"
_XtmClassOperator_Object = MibTableColumn
xtmClassOperator = _XtmClassOperator_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 54),
    _XtmClassOperator_Type()
)
xtmClassOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmClassOperator.setStatus("current")
_XtmNotifications_ObjectIdentity = ObjectIdentity
xtmNotifications = _XtmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 2)
)
_XtmConformance_ObjectIdentity = ObjectIdentity
xtmConformance = _XtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-TRAFFIC-MGMT-MIB",
    **{"XtmIpAddress": XtmIpAddress,
       "XtmProtocol": XtmProtocol,
       "XtmPort": XtmPort,
       "XtmBitRate": XtmBitRate,
       "XtmTosOctet": XtmTosOctet,
       "XtmRange": XtmRange,
       "xediaTrafficMgmtMIB": xediaTrafficMgmtMIB,
       "xtmObjects": xtmObjects,
       "xtmClassTable": xtmClassTable,
       "xtmClassEntry": xtmClassEntry,
       "xtmClassName": xtmClassName,
       "xtmClassParent": xtmClassParent,
       "xtmClassRate": xtmClassRate,
       "xtmClassBounded": xtmClassBounded,
       "xtmClassPriority": xtmClassPriority,
       "xtmClassOperStatus": xtmClassOperStatus,
       "xtmClassOperMsg": xtmClassOperMsg,
       "xtmClassBwUse": xtmClassBwUse,
       "xtmClassUnsatisfied": xtmClassUnsatisfied,
       "xtmClassQueueSize": xtmClassQueueSize,
       "xtmClassRowStatus": xtmClassRowStatus,
       "xtmClassMaxRate": xtmClassMaxRate,
       "xtmClassPeerClassificationOrder": xtmClassPeerClassificationOrder,
       "xtmClassSrcIpAddresses": xtmClassSrcIpAddresses,
       "xtmClassDestIpAddresses": xtmClassDestIpAddresses,
       "xtmClassProtocols": xtmClassProtocols,
       "xtmClassSrcPorts": xtmClassSrcPorts,
       "xtmClassDestPorts": xtmClassDestPorts,
       "xtmClassApplications": xtmClassApplications,
       "xtmClassClassificationTos": xtmClassClassificationTos,
       "xtmClassSrcDomainNames": xtmClassSrcDomainNames,
       "xtmClassDestDomainNames": xtmClassDestDomainNames,
       "xtmClassOperator": xtmClassOperator,
       "xtmNotifications": xtmNotifications,
       "xtmConformance": xtmConformance}
)
