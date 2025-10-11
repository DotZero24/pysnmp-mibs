# SNMP MIB module (LOCAL-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/LOCAL-LOOPBACK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:03 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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


# MODULE-IDENTITY

swLocalLoopbackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 67)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwLocalLoopbackCtrl_ObjectIdentity = ObjectIdentity
swLocalLoopbackCtrl = _SwLocalLoopbackCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 1)
)
_SwLocalLoopbackInfo_ObjectIdentity = ObjectIdentity
swLocalLoopbackInfo = _SwLocalLoopbackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 2)
)
_SwLocalLoopbackMgmt_ObjectIdentity = ObjectIdentity
swLocalLoopbackMgmt = _SwLocalLoopbackMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3)
)
_SwLocalLoopbackConfigTable_Object = MibTable
swLocalLoopbackConfigTable = _SwLocalLoopbackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 1)
)
if mibBuilder.loadTexts:
    swLocalLoopbackConfigTable.setStatus("current")
_SwLocalLoopbackConfigEntry_Object = MibTableRow
swLocalLoopbackConfigEntry = _SwLocalLoopbackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 1, 1)
)
swLocalLoopbackConfigEntry.setIndexNames(
    (0, "LOCAL-LOOPBACK-MIB", "swLocalLoopbackPort"),
)
if mibBuilder.loadTexts:
    swLocalLoopbackConfigEntry.setStatus("current")
_SwLocalLoopbackPort_Type = Integer32
_SwLocalLoopbackPort_Object = MibTableColumn
swLocalLoopbackPort = _SwLocalLoopbackPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 1, 1, 1),
    _SwLocalLoopbackPort_Type()
)
swLocalLoopbackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopbackPort.setStatus("current")


class _SwLocalLoopbackMethod_Type(Integer32):
    """Custom type swLocalLoopbackMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("internal", 2),
          ("external", 3))
    )


_SwLocalLoopbackMethod_Type.__name__ = "Integer32"
_SwLocalLoopbackMethod_Object = MibTableColumn
swLocalLoopbackMethod = _SwLocalLoopbackMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 1, 1, 2),
    _SwLocalLoopbackMethod_Type()
)
swLocalLoopbackMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLocalLoopbackMethod.setStatus("current")


class _SwLocalLoopbackMode_Type(Integer32):
    """Custom type swLocalLoopbackMode based on Integer32"""
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
        *(("other", 1),
          ("mac", 2),
          ("phy-copper", 3),
          ("phy-fiber", 4))
    )


_SwLocalLoopbackMode_Type.__name__ = "Integer32"
_SwLocalLoopbackMode_Object = MibTableColumn
swLocalLoopbackMode = _SwLocalLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 1, 1, 3),
    _SwLocalLoopbackMode_Type()
)
swLocalLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLocalLoopbackMode.setStatus("current")


class _SwLocalLoopbackState_Type(Integer32):
    """Custom type swLocalLoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwLocalLoopbackState_Type.__name__ = "Integer32"
_SwLocalLoopbackState_Object = MibTableColumn
swLocalLoopbackState = _SwLocalLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 1, 1, 4),
    _SwLocalLoopbackState_Type()
)
swLocalLoopbackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLocalLoopbackState.setStatus("current")
_SwLocalLoopbackResultTable_Object = MibTable
swLocalLoopbackResultTable = _SwLocalLoopbackResultTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2)
)
if mibBuilder.loadTexts:
    swLocalLoopbackResultTable.setStatus("current")
_SwLocalLoopbackResultEntry_Object = MibTableRow
swLocalLoopbackResultEntry = _SwLocalLoopbackResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1)
)
swLocalLoopbackResultEntry.setIndexNames(
    (0, "LOCAL-LOOPBACK-MIB", "swLocalLoopbackPort"),
)
if mibBuilder.loadTexts:
    swLocalLoopbackResultEntry.setStatus("current")
_SwLocalLoopback64Tx_Type = Counter32
_SwLocalLoopback64Tx_Object = MibTableColumn
swLocalLoopback64Tx = _SwLocalLoopback64Tx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 1),
    _SwLocalLoopback64Tx_Type()
)
swLocalLoopback64Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback64Tx.setStatus("current")
_SwLocalLoopback64Rx_Type = Counter32
_SwLocalLoopback64Rx_Object = MibTableColumn
swLocalLoopback64Rx = _SwLocalLoopback64Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 2),
    _SwLocalLoopback64Rx_Type()
)
swLocalLoopback64Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback64Rx.setStatus("current")
_SwLocalLoopback512Tx_Type = Counter32
_SwLocalLoopback512Tx_Object = MibTableColumn
swLocalLoopback512Tx = _SwLocalLoopback512Tx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 3),
    _SwLocalLoopback512Tx_Type()
)
swLocalLoopback512Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback512Tx.setStatus("current")
_SwLocalLoopback512Rx_Type = Counter32
_SwLocalLoopback512Rx_Object = MibTableColumn
swLocalLoopback512Rx = _SwLocalLoopback512Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 4),
    _SwLocalLoopback512Rx_Type()
)
swLocalLoopback512Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback512Rx.setStatus("current")
_SwLocalLoopback1024Tx_Type = Counter32
_SwLocalLoopback1024Tx_Object = MibTableColumn
swLocalLoopback1024Tx = _SwLocalLoopback1024Tx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 5),
    _SwLocalLoopback1024Tx_Type()
)
swLocalLoopback1024Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback1024Tx.setStatus("current")
_SwLocalLoopback1024Rx_Type = Counter32
_SwLocalLoopback1024Rx_Object = MibTableColumn
swLocalLoopback1024Rx = _SwLocalLoopback1024Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 6),
    _SwLocalLoopback1024Rx_Type()
)
swLocalLoopback1024Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback1024Rx.setStatus("current")
_SwLocalLoopback1536Tx_Type = Counter32
_SwLocalLoopback1536Tx_Object = MibTableColumn
swLocalLoopback1536Tx = _SwLocalLoopback1536Tx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 7),
    _SwLocalLoopback1536Tx_Type()
)
swLocalLoopback1536Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback1536Tx.setStatus("current")
_SwLocalLoopback1536Rx_Type = Counter32
_SwLocalLoopback1536Rx_Object = MibTableColumn
swLocalLoopback1536Rx = _SwLocalLoopback1536Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 8),
    _SwLocalLoopback1536Rx_Type()
)
swLocalLoopback1536Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopback1536Rx.setStatus("current")


class _SwLocalLoopbackStatus_Type(Integer32):
    """Custom type swLocalLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("success", 2),
          ("fail", 3))
    )


_SwLocalLoopbackStatus_Type.__name__ = "Integer32"
_SwLocalLoopbackStatus_Object = MibTableColumn
swLocalLoopbackStatus = _SwLocalLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 67, 3, 2, 1, 9),
    _SwLocalLoopbackStatus_Type()
)
swLocalLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLocalLoopbackStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOCAL-LOOPBACK-MIB",
    **{"swLocalLoopbackMIB": swLocalLoopbackMIB,
       "swLocalLoopbackCtrl": swLocalLoopbackCtrl,
       "swLocalLoopbackInfo": swLocalLoopbackInfo,
       "swLocalLoopbackMgmt": swLocalLoopbackMgmt,
       "swLocalLoopbackConfigTable": swLocalLoopbackConfigTable,
       "swLocalLoopbackConfigEntry": swLocalLoopbackConfigEntry,
       "swLocalLoopbackPort": swLocalLoopbackPort,
       "swLocalLoopbackMethod": swLocalLoopbackMethod,
       "swLocalLoopbackMode": swLocalLoopbackMode,
       "swLocalLoopbackState": swLocalLoopbackState,
       "swLocalLoopbackResultTable": swLocalLoopbackResultTable,
       "swLocalLoopbackResultEntry": swLocalLoopbackResultEntry,
       "swLocalLoopback64Tx": swLocalLoopback64Tx,
       "swLocalLoopback64Rx": swLocalLoopback64Rx,
       "swLocalLoopback512Tx": swLocalLoopback512Tx,
       "swLocalLoopback512Rx": swLocalLoopback512Rx,
       "swLocalLoopback1024Tx": swLocalLoopback1024Tx,
       "swLocalLoopback1024Rx": swLocalLoopback1024Rx,
       "swLocalLoopback1536Tx": swLocalLoopback1536Tx,
       "swLocalLoopback1536Rx": swLocalLoopback1536Rx,
       "swLocalLoopbackStatus": swLocalLoopbackStatus}
)
