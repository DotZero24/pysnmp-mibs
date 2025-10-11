# SNMP MIB module (DLINKPRIME-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-LBD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:50 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeLoopbackDetectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7)
)
if mibBuilder.loadTexts:
    dlinkPrimeLoopbackDetectMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpLbdNotifications_ObjectIdentity = ObjectIdentity
dpLbdNotifications = _DpLbdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 0)
)
_DpLbdObjects_ObjectIdentity = ObjectIdentity
dpLbdObjects = _DpLbdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1)
)
_DpLbdCtrlGlobalEnabled_Type = TruthValue
_DpLbdCtrlGlobalEnabled_Object = MibScalar
dpLbdCtrlGlobalEnabled = _DpLbdCtrlGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 1),
    _DpLbdCtrlGlobalEnabled_Type()
)
dpLbdCtrlGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLbdCtrlGlobalEnabled.setStatus("current")


class _DpLbdCtrlInterval_Type(Integer32):
    """Custom type dpLbdCtrlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_DpLbdCtrlInterval_Type.__name__ = "Integer32"
_DpLbdCtrlInterval_Object = MibScalar
dpLbdCtrlInterval = _DpLbdCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 2),
    _DpLbdCtrlInterval_Type()
)
dpLbdCtrlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLbdCtrlInterval.setStatus("current")
if mibBuilder.loadTexts:
    dpLbdCtrlInterval.setUnits("seconds")


class _DpLbdCtrlRecover_Type(Integer32):
    """Custom type dpLbdCtrlRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_DpLbdCtrlRecover_Type.__name__ = "Integer32"
_DpLbdCtrlRecover_Object = MibScalar
dpLbdCtrlRecover = _DpLbdCtrlRecover_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 3),
    _DpLbdCtrlRecover_Type()
)
dpLbdCtrlRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLbdCtrlRecover.setStatus("current")
if mibBuilder.loadTexts:
    dpLbdCtrlRecover.setUnits("seconds")
_DpLbdNotifyEnabled_Type = TruthValue
_DpLbdNotifyEnabled_Object = MibScalar
dpLbdNotifyEnabled = _DpLbdNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 4),
    _DpLbdNotifyEnabled_Type()
)
dpLbdNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLbdNotifyEnabled.setStatus("current")
_DpLbdIfCfgTable_Object = MibTable
dpLbdIfCfgTable = _DpLbdIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 5)
)
if mibBuilder.loadTexts:
    dpLbdIfCfgTable.setStatus("current")
_DpLbdIfCfgEntry_Object = MibTableRow
dpLbdIfCfgEntry = _DpLbdIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 5, 1)
)
dpLbdIfCfgEntry.setIndexNames(
    (0, "DLINKPRIME-LBD-MIB", "dpLbdIfCfgIndex"),
)
if mibBuilder.loadTexts:
    dpLbdIfCfgEntry.setStatus("current")
_DpLbdIfCfgIndex_Type = InterfaceIndex
_DpLbdIfCfgIndex_Object = MibTableColumn
dpLbdIfCfgIndex = _DpLbdIfCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 5, 1, 1),
    _DpLbdIfCfgIndex_Type()
)
dpLbdIfCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpLbdIfCfgIndex.setStatus("current")
_DpLbdIfCfgEnabled_Type = TruthValue
_DpLbdIfCfgEnabled_Object = MibTableColumn
dpLbdIfCfgEnabled = _DpLbdIfCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 5, 1, 2),
    _DpLbdIfCfgEnabled_Type()
)
dpLbdIfCfgEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLbdIfCfgEnabled.setStatus("current")


class _DpLbdIfLoopStatus_Type(Integer32):
    """Custom type dpLbdIfLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loop", 2))
    )


_DpLbdIfLoopStatus_Type.__name__ = "Integer32"
_DpLbdIfLoopStatus_Object = MibTableColumn
dpLbdIfLoopStatus = _DpLbdIfLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 5, 1, 3),
    _DpLbdIfLoopStatus_Type()
)
dpLbdIfLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpLbdIfLoopStatus.setStatus("current")
_DpLbdNotifyInfo_ObjectIdentity = ObjectIdentity
dpLbdNotifyInfo = _DpLbdNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 8)
)
if mibBuilder.loadTexts:
    dpLbdNotifyInfo.setStatus("current")
_DpLbdNotifyInfoIfIndex_Type = InterfaceIndex
_DpLbdNotifyInfoIfIndex_Object = MibScalar
dpLbdNotifyInfoIfIndex = _DpLbdNotifyInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 1, 8, 1),
    _DpLbdNotifyInfoIfIndex_Type()
)
dpLbdNotifyInfoIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dpLbdNotifyInfoIfIndex.setStatus("current")
_DpLbdConformance_ObjectIdentity = ObjectIdentity
dpLbdConformance = _DpLbdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2)
)
_DpLbdMIBCompliances_ObjectIdentity = ObjectIdentity
dpLbdMIBCompliances = _DpLbdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2, 1)
)
_DpLbdMIBGroups_ObjectIdentity = ObjectIdentity
dpLbdMIBGroups = _DpLbdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2, 2)
)

# Managed Objects groups

dpLbdCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2, 2, 1)
)
dpLbdCfgGroup.setObjects(
      *(("DLINKPRIME-LBD-MIB", "dpLbdCtrlInterval"),
        ("DLINKPRIME-LBD-MIB", "dpLbdCtrlGlobalEnabled"),
        ("DLINKPRIME-LBD-MIB", "dpLbdNotifyEnabled"),
        ("DLINKPRIME-LBD-MIB", "dpLbdNotifyInfoIfIndex"))
)
if mibBuilder.loadTexts:
    dpLbdCfgGroup.setStatus("current")

dpLbdIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2, 2, 2)
)
dpLbdIfCfgGroup.setObjects(
      *(("DLINKPRIME-LBD-MIB", "dpLbdIfCfgEnabled"),
        ("DLINKPRIME-LBD-MIB", "dpLbdIfLoopStatus"))
)
if mibBuilder.loadTexts:
    dpLbdIfCfgGroup.setStatus("current")


# Notification objects

dpLbdLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 0, 1)
)
dpLbdLoopOccurred.setObjects(
    ("DLINKPRIME-LBD-MIB", "dpLbdNotifyInfoIfIndex")
)
if mibBuilder.loadTexts:
    dpLbdLoopOccurred.setStatus(
        "current"
    )

dpLbdLoopRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 0, 2)
)
dpLbdLoopRecovery.setObjects(
    ("DLINKPRIME-LBD-MIB", "dpLbdNotifyInfoIfIndex")
)
if mibBuilder.loadTexts:
    dpLbdLoopRecovery.setStatus(
        "current"
    )


# Notifications groups

dpLbdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2, 2, 3)
)
dpLbdNotificationGroup.setObjects(
      *(("DLINKPRIME-LBD-MIB", "dpLbdLoopOccurred"),
        ("DLINKPRIME-LBD-MIB", "dpLbdLoopRecovery"))
)
if mibBuilder.loadTexts:
    dpLbdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dpLbdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 7, 2, 1, 1)
)
dpLbdMIBCompliance.setObjects(
      *(("DLINKPRIME-LBD-MIB", "dpLbdCfgGroup"),
        ("DLINKPRIME-LBD-MIB", "dpLbdIfCfgGroup"),
        ("DLINKPRIME-LBD-MIB", "dpLbdCtrlModeGroup"),
        ("DLINKPRIME-LBD-MIB", "dpLbdVlanCtrlGroup"))
)
if mibBuilder.loadTexts:
    dpLbdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-LBD-MIB",
    **{"dlinkPrimeLoopbackDetectMIB": dlinkPrimeLoopbackDetectMIB,
       "dpLbdNotifications": dpLbdNotifications,
       "dpLbdLoopOccurred": dpLbdLoopOccurred,
       "dpLbdLoopRecovery": dpLbdLoopRecovery,
       "dpLbdObjects": dpLbdObjects,
       "dpLbdCtrlGlobalEnabled": dpLbdCtrlGlobalEnabled,
       "dpLbdCtrlInterval": dpLbdCtrlInterval,
       "dpLbdCtrlRecover": dpLbdCtrlRecover,
       "dpLbdNotifyEnabled": dpLbdNotifyEnabled,
       "dpLbdIfCfgTable": dpLbdIfCfgTable,
       "dpLbdIfCfgEntry": dpLbdIfCfgEntry,
       "dpLbdIfCfgIndex": dpLbdIfCfgIndex,
       "dpLbdIfCfgEnabled": dpLbdIfCfgEnabled,
       "dpLbdIfLoopStatus": dpLbdIfLoopStatus,
       "dpLbdNotifyInfo": dpLbdNotifyInfo,
       "dpLbdNotifyInfoIfIndex": dpLbdNotifyInfoIfIndex,
       "dpLbdConformance": dpLbdConformance,
       "dpLbdMIBCompliances": dpLbdMIBCompliances,
       "dpLbdMIBCompliance": dpLbdMIBCompliance,
       "dpLbdMIBGroups": dpLbdMIBGroups,
       "dpLbdCfgGroup": dpLbdCfgGroup,
       "dpLbdIfCfgGroup": dpLbdIfCfgGroup,
       "dpLbdNotificationGroup": dpLbdNotificationGroup}
)
