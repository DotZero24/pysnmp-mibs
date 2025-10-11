# SNMP MIB module (MY-AUTH-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-AUTH-GATEWAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:31 2025
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

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "MY-TC",
    "IfIndex")

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


# MODULE-IDENTITY

myAuthGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40)
)
if mibBuilder.loadTexts:
    myAuthGatewayMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyAuthGatewayMIBObjects_ObjectIdentity = ObjectIdentity
myAuthGatewayMIBObjects = _MyAuthGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1)
)
_MyAuthGatewayUserTable_Object = MibTable
myAuthGatewayUserTable = _MyAuthGatewayUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    myAuthGatewayUserTable.setStatus("current")
_MyAuthGatewayUserEntry_Object = MibTableRow
myAuthGatewayUserEntry = _MyAuthGatewayUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1)
)
myAuthGatewayUserEntry.setIndexNames(
    (0, "MY-AUTH-GATEWAY-MIB", "userIpaddr"),
)
if mibBuilder.loadTexts:
    myAuthGatewayUserEntry.setStatus("current")
_UserIpaddr_Type = IpAddress
_UserIpaddr_Object = MibTableColumn
userIpaddr = _UserIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 1),
    _UserIpaddr_Type()
)
userIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userIpaddr.setStatus("current")
_OnlineFlag_Type = Gauge32
_OnlineFlag_Object = MibTableColumn
onlineFlag = _OnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 2),
    _OnlineFlag_Type()
)
onlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onlineFlag.setStatus("current")
_TimeLimit_Type = Gauge32
_TimeLimit_Object = MibTableColumn
timeLimit = _TimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 3),
    _TimeLimit_Type()
)
timeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeLimit.setStatus("current")
_TimeUsed_Type = Gauge32
_TimeUsed_Object = MibTableColumn
timeUsed = _TimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 4),
    _TimeUsed_Type()
)
timeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeUsed.setStatus("current")
_BandwidthLimitUplink_Type = Gauge32
_BandwidthLimitUplink_Object = MibTableColumn
bandwidthLimitUplink = _BandwidthLimitUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 5),
    _BandwidthLimitUplink_Type()
)
bandwidthLimitUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthLimitUplink.setStatus("current")
_BandwidthLimitDownlink_Type = Gauge32
_BandwidthLimitDownlink_Object = MibTableColumn
bandwidthLimitDownlink = _BandwidthLimitDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 6),
    _BandwidthLimitDownlink_Type()
)
bandwidthLimitDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthLimitDownlink.setStatus("current")
_IntramuralFluxLimitUplink_Type = Gauge32
_IntramuralFluxLimitUplink_Object = MibTableColumn
intramuralFluxLimitUplink = _IntramuralFluxLimitUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 7),
    _IntramuralFluxLimitUplink_Type()
)
intramuralFluxLimitUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intramuralFluxLimitUplink.setStatus("current")
_IntramuralFluxLimitDownlink_Type = Gauge32
_IntramuralFluxLimitDownlink_Object = MibTableColumn
intramuralFluxLimitDownlink = _IntramuralFluxLimitDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 8),
    _IntramuralFluxLimitDownlink_Type()
)
intramuralFluxLimitDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intramuralFluxLimitDownlink.setStatus("current")
_InlandFluxLimitUplink_Type = Gauge32
_InlandFluxLimitUplink_Object = MibTableColumn
inlandFluxLimitUplink = _InlandFluxLimitUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 9),
    _InlandFluxLimitUplink_Type()
)
inlandFluxLimitUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlandFluxLimitUplink.setStatus("current")
_InlandFluxLimitDownlink_Type = Gauge32
_InlandFluxLimitDownlink_Object = MibTableColumn
inlandFluxLimitDownlink = _InlandFluxLimitDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 10),
    _InlandFluxLimitDownlink_Type()
)
inlandFluxLimitDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlandFluxLimitDownlink.setStatus("current")
_OverseasFluxLimitUplink_Type = Gauge32
_OverseasFluxLimitUplink_Object = MibTableColumn
overseasFluxLimitUplink = _OverseasFluxLimitUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 11),
    _OverseasFluxLimitUplink_Type()
)
overseasFluxLimitUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overseasFluxLimitUplink.setStatus("current")
_OverseasFluxLimitDownlink_Type = Gauge32
_OverseasFluxLimitDownlink_Object = MibTableColumn
overseasFluxLimitDownlink = _OverseasFluxLimitDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 12),
    _OverseasFluxLimitDownlink_Type()
)
overseasFluxLimitDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overseasFluxLimitDownlink.setStatus("current")
_IntramuralFluxCountUplink_Type = Counter32
_IntramuralFluxCountUplink_Object = MibTableColumn
intramuralFluxCountUplink = _IntramuralFluxCountUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 13),
    _IntramuralFluxCountUplink_Type()
)
intramuralFluxCountUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intramuralFluxCountUplink.setStatus("current")
_IntramuralFluxCountDownlink_Type = Counter32
_IntramuralFluxCountDownlink_Object = MibTableColumn
intramuralFluxCountDownlink = _IntramuralFluxCountDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 14),
    _IntramuralFluxCountDownlink_Type()
)
intramuralFluxCountDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intramuralFluxCountDownlink.setStatus("current")
_InlandFluxCountUplink_Type = Counter32
_InlandFluxCountUplink_Object = MibTableColumn
inlandFluxCountUplink = _InlandFluxCountUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 15),
    _InlandFluxCountUplink_Type()
)
inlandFluxCountUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlandFluxCountUplink.setStatus("current")
_InlandFluxCountDownlink_Type = Counter32
_InlandFluxCountDownlink_Object = MibTableColumn
inlandFluxCountDownlink = _InlandFluxCountDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 16),
    _InlandFluxCountDownlink_Type()
)
inlandFluxCountDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlandFluxCountDownlink.setStatus("current")
_OverseasFluxCountUplink_Type = Counter32
_OverseasFluxCountUplink_Object = MibTableColumn
overseasFluxCountUplink = _OverseasFluxCountUplink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 17),
    _OverseasFluxCountUplink_Type()
)
overseasFluxCountUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overseasFluxCountUplink.setStatus("current")
_OverseasFluxCountDownlink_Type = Counter32
_OverseasFluxCountDownlink_Object = MibTableColumn
overseasFluxCountDownlink = _OverseasFluxCountDownlink_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 18),
    _OverseasFluxCountDownlink_Type()
)
overseasFluxCountDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overseasFluxCountDownlink.setStatus("current")
_UserStatus_Type = RowStatus
_UserStatus_Object = MibTableColumn
userStatus = _UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 19),
    _UserStatus_Type()
)
userStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userStatus.setStatus("current")
_MyAuthGatewayMIBTraps_ObjectIdentity = ObjectIdentity
myAuthGatewayMIBTraps = _MyAuthGatewayMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2)
)
_MyAuthGatewayMIBConformance_ObjectIdentity = ObjectIdentity
myAuthGatewayMIBConformance = _MyAuthGatewayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3)
)
_MyAuthGatewayMIBCompliances_ObjectIdentity = ObjectIdentity
myAuthGatewayMIBCompliances = _MyAuthGatewayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 1)
)
_MyAuthGatewayMIBGroups_ObjectIdentity = ObjectIdentity
myAuthGatewayMIBGroups = _MyAuthGatewayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 2)
)

# Managed Objects groups

myAuthGatewayMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 2, 1)
)
myAuthGatewayMIBGroup.setObjects(
      *(("MY-AUTH-GATEWAY-MIB", "userIpaddr"),
        ("MY-AUTH-GATEWAY-MIB", "onlineFlag"),
        ("MY-AUTH-GATEWAY-MIB", "timeLimit"),
        ("MY-AUTH-GATEWAY-MIB", "timeUsed"),
        ("MY-AUTH-GATEWAY-MIB", "bandwidthLimitUplink"),
        ("MY-AUTH-GATEWAY-MIB", "bandwidthLimitDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "intramuralFluxLimitUplink"),
        ("MY-AUTH-GATEWAY-MIB", "intramuralFluxLimitDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "inlandFluxLimitUplink"),
        ("MY-AUTH-GATEWAY-MIB", "inlandFluxLimitDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "overseasFluxLimitUplink"),
        ("MY-AUTH-GATEWAY-MIB", "overseasFluxLimitDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "intramuralFluxCountUplink"),
        ("MY-AUTH-GATEWAY-MIB", "intramuralFluxCountDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "inlandFluxCountUplink"),
        ("MY-AUTH-GATEWAY-MIB", "inlandFluxCountDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "overseasFluxCountUplink"),
        ("MY-AUTH-GATEWAY-MIB", "overseasFluxCountDownlink"),
        ("MY-AUTH-GATEWAY-MIB", "userStatus"))
)
if mibBuilder.loadTexts:
    myAuthGatewayMIBGroup.setStatus("current")


# Notification objects

myAuthGatewayUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 1)
)
myAuthGatewayUserLeave.setObjects(
    ("MY-AUTH-GATEWAY-MIB", "userIpaddr")
)
if mibBuilder.loadTexts:
    myAuthGatewayUserLeave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myAuthGatewayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 1, 1)
)
myAuthGatewayMIBCompliance.setObjects(
    ("MY-AUTH-GATEWAY-MIB", "myAuthGatewayMIBGroup")
)
if mibBuilder.loadTexts:
    myAuthGatewayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-AUTH-GATEWAY-MIB",
    **{"myAuthGatewayMIB": myAuthGatewayMIB,
       "myAuthGatewayMIBObjects": myAuthGatewayMIBObjects,
       "myAuthGatewayUserTable": myAuthGatewayUserTable,
       "myAuthGatewayUserEntry": myAuthGatewayUserEntry,
       "userIpaddr": userIpaddr,
       "onlineFlag": onlineFlag,
       "timeLimit": timeLimit,
       "timeUsed": timeUsed,
       "bandwidthLimitUplink": bandwidthLimitUplink,
       "bandwidthLimitDownlink": bandwidthLimitDownlink,
       "intramuralFluxLimitUplink": intramuralFluxLimitUplink,
       "intramuralFluxLimitDownlink": intramuralFluxLimitDownlink,
       "inlandFluxLimitUplink": inlandFluxLimitUplink,
       "inlandFluxLimitDownlink": inlandFluxLimitDownlink,
       "overseasFluxLimitUplink": overseasFluxLimitUplink,
       "overseasFluxLimitDownlink": overseasFluxLimitDownlink,
       "intramuralFluxCountUplink": intramuralFluxCountUplink,
       "intramuralFluxCountDownlink": intramuralFluxCountDownlink,
       "inlandFluxCountUplink": inlandFluxCountUplink,
       "inlandFluxCountDownlink": inlandFluxCountDownlink,
       "overseasFluxCountUplink": overseasFluxCountUplink,
       "overseasFluxCountDownlink": overseasFluxCountDownlink,
       "userStatus": userStatus,
       "myAuthGatewayMIBTraps": myAuthGatewayMIBTraps,
       "myAuthGatewayUserLeave": myAuthGatewayUserLeave,
       "myAuthGatewayMIBConformance": myAuthGatewayMIBConformance,
       "myAuthGatewayMIBCompliances": myAuthGatewayMIBCompliances,
       "myAuthGatewayMIBCompliance": myAuthGatewayMIBCompliance,
       "myAuthGatewayMIBGroups": myAuthGatewayMIBGroups,
       "myAuthGatewayMIBGroup": myAuthGatewayMIBGroup}
)
