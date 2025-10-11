# SNMP MIB module (PKT-STORM-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/PKT-STORM-CTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:36 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swPktStormMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 25)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPktStormCtrl_ObjectIdentity = ObjectIdentity
swPktStormCtrl = _SwPktStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 1)
)
_SwPktStormRecover_Type = PortList
_SwPktStormRecover_Object = MibScalar
swPktStormRecover = _SwPktStormRecover_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 1, 1),
    _SwPktStormRecover_Type()
)
swPktStormRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormRecover.setStatus("current")


class _SwPktStormTrapCtrl_Type(Integer32):
    """Custom type swPktStormTrapCtrl based on Integer32"""
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
        *(("none", 1),
          ("stormOccurred", 2),
          ("stormCleared", 3),
          ("both", 4))
    )


_SwPktStormTrapCtrl_Type.__name__ = "Integer32"
_SwPktStormTrapCtrl_Object = MibScalar
swPktStormTrapCtrl = _SwPktStormTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 1, 2),
    _SwPktStormTrapCtrl_Type()
)
swPktStormTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormTrapCtrl.setStatus("current")


class _SwPktStormLogCtrl_Type(Integer32):
    """Custom type swPktStormLogCtrl based on Integer32"""
    defaultValue = 1

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


_SwPktStormLogCtrl_Type.__name__ = "Integer32"
_SwPktStormLogCtrl_Object = MibScalar
swPktStormLogCtrl = _SwPktStormLogCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 1, 3),
    _SwPktStormLogCtrl_Type()
)
swPktStormLogCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormLogCtrl.setStatus("current")


class _SwPktStormAutoRecoverTime_Type(Integer32):
    """Custom type swPktStormAutoRecoverTime based on Integer32"""
    defaultValue = 0


_SwPktStormAutoRecoverTime_Type.__name__ = "Integer32"
_SwPktStormAutoRecoverTime_Object = MibScalar
swPktStormAutoRecoverTime = _SwPktStormAutoRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 1, 4),
    _SwPktStormAutoRecoverTime_Type()
)
swPktStormAutoRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormAutoRecoverTime.setStatus("current")
if mibBuilder.loadTexts:
    swPktStormAutoRecoverTime.setUnits("minutes")
_SwPktStormInfo_ObjectIdentity = ObjectIdentity
swPktStormInfo = _SwPktStormInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 2)
)
_SwPktStormMgmt_ObjectIdentity = ObjectIdentity
swPktStormMgmt = _SwPktStormMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3)
)
_SwPktStormCtrlTable_Object = MibTable
swPktStormCtrlTable = _SwPktStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1)
)
if mibBuilder.loadTexts:
    swPktStormCtrlTable.setStatus("current")
_SwPktStormCtrlEntry_Object = MibTableRow
swPktStormCtrlEntry = _SwPktStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1)
)
swPktStormCtrlEntry.setIndexNames(
    (0, "PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swPktStormCtrlEntry.setStatus("current")


class _SwPktStormCtrlPortIndex_Type(Integer32):
    """Custom type swPktStormCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPktStormCtrlPortIndex_Type.__name__ = "Integer32"
_SwPktStormCtrlPortIndex_Object = MibTableColumn
swPktStormCtrlPortIndex = _SwPktStormCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 1),
    _SwPktStormCtrlPortIndex_Type()
)
swPktStormCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPktStormCtrlPortIndex.setStatus("current")


class _SwPktStormCtrlthreshold_Type(Integer32):
    """Custom type swPktStormCtrlthreshold based on Integer32"""
    defaultValue = 131072


_SwPktStormCtrlthreshold_Type.__name__ = "Integer32"
_SwPktStormCtrlthreshold_Object = MibTableColumn
swPktStormCtrlthreshold = _SwPktStormCtrlthreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 2),
    _SwPktStormCtrlthreshold_Type()
)
swPktStormCtrlthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlthreshold.setStatus("obsolete")


class _SwPktStormCtrlBroadcastStatus_Type(Integer32):
    """Custom type swPktStormCtrlBroadcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SwPktStormCtrlBroadcastStatus_Type.__name__ = "Integer32"
_SwPktStormCtrlBroadcastStatus_Object = MibTableColumn
swPktStormCtrlBroadcastStatus = _SwPktStormCtrlBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 3),
    _SwPktStormCtrlBroadcastStatus_Type()
)
swPktStormCtrlBroadcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlBroadcastStatus.setStatus("current")


class _SwPktStormCtrlMulticastStatus_Type(Integer32):
    """Custom type swPktStormCtrlMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SwPktStormCtrlMulticastStatus_Type.__name__ = "Integer32"
_SwPktStormCtrlMulticastStatus_Object = MibTableColumn
swPktStormCtrlMulticastStatus = _SwPktStormCtrlMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 4),
    _SwPktStormCtrlMulticastStatus_Type()
)
swPktStormCtrlMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlMulticastStatus.setStatus("current")


class _SwPktStormCtrlUnicastStatus_Type(Integer32):
    """Custom type swPktStormCtrlUnicastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SwPktStormCtrlUnicastStatus_Type.__name__ = "Integer32"
_SwPktStormCtrlUnicastStatus_Object = MibTableColumn
swPktStormCtrlUnicastStatus = _SwPktStormCtrlUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 5),
    _SwPktStormCtrlUnicastStatus_Type()
)
swPktStormCtrlUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlUnicastStatus.setStatus("current")


class _SwPktStormCtrlActionStatus_Type(Integer32):
    """Custom type swPktStormCtrlActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("drop", 2))
    )


_SwPktStormCtrlActionStatus_Type.__name__ = "Integer32"
_SwPktStormCtrlActionStatus_Object = MibTableColumn
swPktStormCtrlActionStatus = _SwPktStormCtrlActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 6),
    _SwPktStormCtrlActionStatus_Type()
)
swPktStormCtrlActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlActionStatus.setStatus("current")


class _SwPktStormCtrlCountDown_Type(Integer32):
    """Custom type swPktStormCtrlCountDown based on Integer32"""
    defaultValue = 0


_SwPktStormCtrlCountDown_Type.__name__ = "Integer32"
_SwPktStormCtrlCountDown_Object = MibTableColumn
swPktStormCtrlCountDown = _SwPktStormCtrlCountDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 7),
    _SwPktStormCtrlCountDown_Type()
)
swPktStormCtrlCountDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlCountDown.setStatus("current")
if mibBuilder.loadTexts:
    swPktStormCtrlCountDown.setUnits("minutes")


class _SwPktStormCtrlTimeinterval_Type(Integer32):
    """Custom type swPktStormCtrlTimeinterval based on Integer32"""
    defaultValue = 5


_SwPktStormCtrlTimeinterval_Type.__name__ = "Integer32"
_SwPktStormCtrlTimeinterval_Object = MibTableColumn
swPktStormCtrlTimeinterval = _SwPktStormCtrlTimeinterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 8),
    _SwPktStormCtrlTimeinterval_Type()
)
swPktStormCtrlTimeinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlTimeinterval.setStatus("current")
if mibBuilder.loadTexts:
    swPktStormCtrlTimeinterval.setUnits("seconds")


class _SwPktStormCtrlShutdownForever_Type(Integer32):
    """Custom type swPktStormCtrlShutdownForever based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SwPktStormCtrlShutdownForever_Type.__name__ = "Integer32"
_SwPktStormCtrlShutdownForever_Object = MibTableColumn
swPktStormCtrlShutdownForever = _SwPktStormCtrlShutdownForever_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 9),
    _SwPktStormCtrlShutdownForever_Type()
)
swPktStormCtrlShutdownForever.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPktStormCtrlShutdownForever.setStatus("current")


class _SwPktStormCtrlBCastThreshold_Type(Integer32):
    """Custom type swPktStormCtrlBCastThreshold based on Integer32"""
    defaultValue = 131072


_SwPktStormCtrlBCastThreshold_Type.__name__ = "Integer32"
_SwPktStormCtrlBCastThreshold_Object = MibTableColumn
swPktStormCtrlBCastThreshold = _SwPktStormCtrlBCastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 10),
    _SwPktStormCtrlBCastThreshold_Type()
)
swPktStormCtrlBCastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlBCastThreshold.setStatus("current")


class _SwPktStormCtrlMCastThreshold_Type(Integer32):
    """Custom type swPktStormCtrlMCastThreshold based on Integer32"""
    defaultValue = 131072


_SwPktStormCtrlMCastThreshold_Type.__name__ = "Integer32"
_SwPktStormCtrlMCastThreshold_Object = MibTableColumn
swPktStormCtrlMCastThreshold = _SwPktStormCtrlMCastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 11),
    _SwPktStormCtrlMCastThreshold_Type()
)
swPktStormCtrlMCastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlMCastThreshold.setStatus("current")


class _SwPktStormCtrlUnicastThreshold_Type(Integer32):
    """Custom type swPktStormCtrlUnicastThreshold based on Integer32"""
    defaultValue = 131072


_SwPktStormCtrlUnicastThreshold_Type.__name__ = "Integer32"
_SwPktStormCtrlUnicastThreshold_Object = MibTableColumn
swPktStormCtrlUnicastThreshold = _SwPktStormCtrlUnicastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 12),
    _SwPktStormCtrlUnicastThreshold_Type()
)
swPktStormCtrlUnicastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktStormCtrlUnicastThreshold.setStatus("current")
_SwPktStormNotify_ObjectIdentity = ObjectIdentity
swPktStormNotify = _SwPktStormNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 5)
)
_SwPktStormNotifyPrefix_ObjectIdentity = ObjectIdentity
swPktStormNotifyPrefix = _SwPktStormNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0)
)

# Managed Objects groups


# Notification objects

swPktStormOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0, 1)
)
swPktStormOccurred.setObjects(
    ("PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex")
)
if mibBuilder.loadTexts:
    swPktStormOccurred.setStatus(
        "current"
    )

swPktStormCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0, 2)
)
swPktStormCleared.setObjects(
    ("PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex")
)
if mibBuilder.loadTexts:
    swPktStormCleared.setStatus(
        "current"
    )

swPktStormDisablePort = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0, 3)
)
swPktStormDisablePort.setObjects(
    ("PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex")
)
if mibBuilder.loadTexts:
    swPktStormDisablePort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKT-STORM-CTRL-MIB",
    **{"PortList": PortList,
       "swPktStormMIB": swPktStormMIB,
       "swPktStormCtrl": swPktStormCtrl,
       "swPktStormRecover": swPktStormRecover,
       "swPktStormTrapCtrl": swPktStormTrapCtrl,
       "swPktStormLogCtrl": swPktStormLogCtrl,
       "swPktStormAutoRecoverTime": swPktStormAutoRecoverTime,
       "swPktStormInfo": swPktStormInfo,
       "swPktStormMgmt": swPktStormMgmt,
       "swPktStormCtrlTable": swPktStormCtrlTable,
       "swPktStormCtrlEntry": swPktStormCtrlEntry,
       "swPktStormCtrlPortIndex": swPktStormCtrlPortIndex,
       "swPktStormCtrlthreshold": swPktStormCtrlthreshold,
       "swPktStormCtrlBroadcastStatus": swPktStormCtrlBroadcastStatus,
       "swPktStormCtrlMulticastStatus": swPktStormCtrlMulticastStatus,
       "swPktStormCtrlUnicastStatus": swPktStormCtrlUnicastStatus,
       "swPktStormCtrlActionStatus": swPktStormCtrlActionStatus,
       "swPktStormCtrlCountDown": swPktStormCtrlCountDown,
       "swPktStormCtrlTimeinterval": swPktStormCtrlTimeinterval,
       "swPktStormCtrlShutdownForever": swPktStormCtrlShutdownForever,
       "swPktStormCtrlBCastThreshold": swPktStormCtrlBCastThreshold,
       "swPktStormCtrlMCastThreshold": swPktStormCtrlMCastThreshold,
       "swPktStormCtrlUnicastThreshold": swPktStormCtrlUnicastThreshold,
       "swPktStormNotify": swPktStormNotify,
       "swPktStormNotifyPrefix": swPktStormNotifyPrefix,
       "swPktStormOccurred": swPktStormOccurred,
       "swPktStormCleared": swPktStormCleared,
       "swPktStormDisablePort": swPktStormDisablePort}
)
