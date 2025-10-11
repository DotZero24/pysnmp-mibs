# SNMP MIB module (QTECH-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-L2TP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:37 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

qtechVPDNMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112)
)
if mibBuilder.loadTexts:
    qtechVPDNMIB.setRevisions(
        ("2011-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechL2TPSessionObjects_ObjectIdentity = ObjectIdentity
qtechL2TPSessionObjects = _QtechL2TPSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1)
)
_QtechL2TPSessionTable_Object = MibTable
qtechL2TPSessionTable = _QtechL2TPSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1)
)
if mibBuilder.loadTexts:
    qtechL2TPSessionTable.setStatus("current")
_QtechL2TPSessionEntry_Object = MibTableRow
qtechL2TPSessionEntry = _QtechL2TPSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1)
)
qtechL2TPSessionEntry.setIndexNames(
    (0, "QTECH-L2TP-MIB", "l2tpPrivateSessionIfIndex"),
)
if mibBuilder.loadTexts:
    qtechL2TPSessionEntry.setStatus("current")


class _L2tpPrivateSessionIfIndex_Type(Integer32):
    """Custom type l2tpPrivateSessionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2tpPrivateSessionIfIndex_Type.__name__ = "Integer32"
_L2tpPrivateSessionIfIndex_Object = MibTableColumn
l2tpPrivateSessionIfIndex = _L2tpPrivateSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 1),
    _L2tpPrivateSessionIfIndex_Type()
)
l2tpPrivateSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPrivateSessionIfIndex.setStatus("current")


class _L2tpPrivateLocalTunnelID_Type(Integer32):
    """Custom type l2tpPrivateLocalTunnelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2tpPrivateLocalTunnelID_Type.__name__ = "Integer32"
_L2tpPrivateLocalTunnelID_Object = MibTableColumn
l2tpPrivateLocalTunnelID = _L2tpPrivateLocalTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 2),
    _L2tpPrivateLocalTunnelID_Type()
)
l2tpPrivateLocalTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPrivateLocalTunnelID.setStatus("current")
_L2tpPrivateSessionLocalIpAdd_Type = IpAddress
_L2tpPrivateSessionLocalIpAdd_Object = MibTableColumn
l2tpPrivateSessionLocalIpAdd = _L2tpPrivateSessionLocalIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 3),
    _L2tpPrivateSessionLocalIpAdd_Type()
)
l2tpPrivateSessionLocalIpAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPrivateSessionLocalIpAdd.setStatus("current")
_L2tpPrivateSessionRemoteIpAdd_Type = IpAddress
_L2tpPrivateSessionRemoteIpAdd_Object = MibTableColumn
l2tpPrivateSessionRemoteIpAdd = _L2tpPrivateSessionRemoteIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 4),
    _L2tpPrivateSessionRemoteIpAdd_Type()
)
l2tpPrivateSessionRemoteIpAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPrivateSessionRemoteIpAdd.setStatus("current")


class _L2tpPrivateSessionVrfId_Type(Integer32):
    """Custom type l2tpPrivateSessionVrfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2tpPrivateSessionVrfId_Type.__name__ = "Integer32"
_L2tpPrivateSessionVrfId_Object = MibTableColumn
l2tpPrivateSessionVrfId = _L2tpPrivateSessionVrfId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 5),
    _L2tpPrivateSessionVrfId_Type()
)
l2tpPrivateSessionVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPrivateSessionVrfId.setStatus("current")


class _L2tpPrivateSessionExistTime_Type(Integer32):
    """Custom type l2tpPrivateSessionExistTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2tpPrivateSessionExistTime_Type.__name__ = "Integer32"
_L2tpPrivateSessionExistTime_Object = MibTableColumn
l2tpPrivateSessionExistTime = _L2tpPrivateSessionExistTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 6),
    _L2tpPrivateSessionExistTime_Type()
)
l2tpPrivateSessionExistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPrivateSessionExistTime.setStatus("current")


class _L2tpPrivateSessionStatus_Type(Integer32):
    """Custom type l2tpPrivateSessionStatus based on Integer32"""
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
        *(("sessionIdle", 1),
          ("sessionConnecting", 2),
          ("sessionEstablished", 3),
          ("sessionDisconnecting", 4))
    )


_L2tpPrivateSessionStatus_Type.__name__ = "Integer32"
_L2tpPrivateSessionStatus_Object = MibTableColumn
l2tpPrivateSessionStatus = _L2tpPrivateSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 1, 1, 1, 7),
    _L2tpPrivateSessionStatus_Type()
)
l2tpPrivateSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpPrivateSessionStatus.setStatus("current")
_QtechVPDNMonitor_ObjectIdentity = ObjectIdentity
qtechVPDNMonitor = _QtechVPDNMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 2)
)
_QtechVPDNMonitorTRAP_ObjectIdentity = ObjectIdentity
qtechVPDNMonitorTRAP = _QtechVPDNMonitorTRAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 2, 1)
)
_QtechVPDNNotifications_ObjectIdentity = ObjectIdentity
qtechVPDNNotifications = _QtechVPDNNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 2, 1, 1)
)

# Managed Objects groups


# Notification objects

qtechVPDNStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 2, 1, 1, 1)
)
qtechVPDNStart.setObjects(
      *(("QTECH-L2TP-MIB", "l2tpPrivateSessionIfIndex"),
        ("QTECH-L2TP-MIB", "l2tpPrivateLocalTunnelID"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionLocalIpAdd"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionRemoteIpAdd"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionVrfId"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionExistTime"))
)
if mibBuilder.loadTexts:
    qtechVPDNStart.setStatus(
        "current"
    )

qtechVPDNStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 112, 2, 1, 1, 2)
)
qtechVPDNStop.setObjects(
      *(("QTECH-L2TP-MIB", "l2tpPrivateSessionIfIndex"),
        ("QTECH-L2TP-MIB", "l2tpPrivateLocalTunnelID"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionLocalIpAdd"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionRemoteIpAdd"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionVrfId"),
        ("QTECH-L2TP-MIB", "l2tpPrivateSessionExistTime"))
)
if mibBuilder.loadTexts:
    qtechVPDNStop.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-L2TP-MIB",
    **{"qtechVPDNMIB": qtechVPDNMIB,
       "qtechL2TPSessionObjects": qtechL2TPSessionObjects,
       "qtechL2TPSessionTable": qtechL2TPSessionTable,
       "qtechL2TPSessionEntry": qtechL2TPSessionEntry,
       "l2tpPrivateSessionIfIndex": l2tpPrivateSessionIfIndex,
       "l2tpPrivateLocalTunnelID": l2tpPrivateLocalTunnelID,
       "l2tpPrivateSessionLocalIpAdd": l2tpPrivateSessionLocalIpAdd,
       "l2tpPrivateSessionRemoteIpAdd": l2tpPrivateSessionRemoteIpAdd,
       "l2tpPrivateSessionVrfId": l2tpPrivateSessionVrfId,
       "l2tpPrivateSessionExistTime": l2tpPrivateSessionExistTime,
       "l2tpPrivateSessionStatus": l2tpPrivateSessionStatus,
       "qtechVPDNMonitor": qtechVPDNMonitor,
       "qtechVPDNMonitorTRAP": qtechVPDNMonitorTRAP,
       "qtechVPDNNotifications": qtechVPDNNotifications,
       "qtechVPDNStart": qtechVPDNStart,
       "qtechVPDNStop": qtechVPDNStop}
)
