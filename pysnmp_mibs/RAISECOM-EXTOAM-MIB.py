# SNMP MIB module (RAISECOM-EXTOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-EXTOAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:19 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomExtendOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomOamExtStatsTable_Object = MibTable
raisecomOamExtStatsTable = _RaisecomOamExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1)
)
if mibBuilder.loadTexts:
    raisecomOamExtStatsTable.setStatus("current")
_RaisecomOamExtStatsEntry_Object = MibTableRow
raisecomOamExtStatsEntry = _RaisecomOamExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1)
)
raisecomOamExtStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomOamExtStatsEntry.setStatus("current")
_RaisecomOamExtVariableGetTx_Type = Counter32
_RaisecomOamExtVariableGetTx_Object = MibTableColumn
raisecomOamExtVariableGetTx = _RaisecomOamExtVariableGetTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 1),
    _RaisecomOamExtVariableGetTx_Type()
)
raisecomOamExtVariableGetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableGetTx.setStatus("current")
_RaisecomOamExtVariableGetRx_Type = Counter32
_RaisecomOamExtVariableGetRx_Object = MibTableColumn
raisecomOamExtVariableGetRx = _RaisecomOamExtVariableGetRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 2),
    _RaisecomOamExtVariableGetRx_Type()
)
raisecomOamExtVariableGetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableGetRx.setStatus("current")
_RaisecomOamExtVariableSetTx_Type = Counter32
_RaisecomOamExtVariableSetTx_Object = MibTableColumn
raisecomOamExtVariableSetTx = _RaisecomOamExtVariableSetTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 3),
    _RaisecomOamExtVariableSetTx_Type()
)
raisecomOamExtVariableSetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableSetTx.setStatus("current")
_RaisecomOamExtVariableSetRx_Type = Counter32
_RaisecomOamExtVariableSetRx_Object = MibTableColumn
raisecomOamExtVariableSetRx = _RaisecomOamExtVariableSetRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 4),
    _RaisecomOamExtVariableSetRx_Type()
)
raisecomOamExtVariableSetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableSetRx.setStatus("current")
_RaisecomOamExtVariableGetResponseTx_Type = Counter32
_RaisecomOamExtVariableGetResponseTx_Object = MibTableColumn
raisecomOamExtVariableGetResponseTx = _RaisecomOamExtVariableGetResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 5),
    _RaisecomOamExtVariableGetResponseTx_Type()
)
raisecomOamExtVariableGetResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableGetResponseTx.setStatus("current")
_RaisecomOamExtVariableGetResponseRx_Type = Counter32
_RaisecomOamExtVariableGetResponseRx_Object = MibTableColumn
raisecomOamExtVariableGetResponseRx = _RaisecomOamExtVariableGetResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 6),
    _RaisecomOamExtVariableGetResponseRx_Type()
)
raisecomOamExtVariableGetResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableGetResponseRx.setStatus("current")
_RaisecomOamExtVariableSetResponseTx_Type = Counter32
_RaisecomOamExtVariableSetResponseTx_Object = MibTableColumn
raisecomOamExtVariableSetResponseTx = _RaisecomOamExtVariableSetResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 7),
    _RaisecomOamExtVariableSetResponseTx_Type()
)
raisecomOamExtVariableSetResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableSetResponseTx.setStatus("current")
_RaisecomOamExtVariableSetResponseRx_Type = Counter32
_RaisecomOamExtVariableSetResponseRx_Object = MibTableColumn
raisecomOamExtVariableSetResponseRx = _RaisecomOamExtVariableSetResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 8),
    _RaisecomOamExtVariableSetResponseRx_Type()
)
raisecomOamExtVariableSetResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtVariableSetResponseRx.setStatus("current")
_RaisecomOamExtFileReadTx_Type = Counter32
_RaisecomOamExtFileReadTx_Object = MibTableColumn
raisecomOamExtFileReadTx = _RaisecomOamExtFileReadTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 9),
    _RaisecomOamExtFileReadTx_Type()
)
raisecomOamExtFileReadTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileReadTx.setStatus("current")
_RaisecomOamExtFileReadRx_Type = Counter32
_RaisecomOamExtFileReadRx_Object = MibTableColumn
raisecomOamExtFileReadRx = _RaisecomOamExtFileReadRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 10),
    _RaisecomOamExtFileReadRx_Type()
)
raisecomOamExtFileReadRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileReadRx.setStatus("current")
_RaisecomOamExtFileWriteTx_Type = Counter32
_RaisecomOamExtFileWriteTx_Object = MibTableColumn
raisecomOamExtFileWriteTx = _RaisecomOamExtFileWriteTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 11),
    _RaisecomOamExtFileWriteTx_Type()
)
raisecomOamExtFileWriteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileWriteTx.setStatus("current")
_RaisecomOamExtFileWriteRx_Type = Counter32
_RaisecomOamExtFileWriteRx_Object = MibTableColumn
raisecomOamExtFileWriteRx = _RaisecomOamExtFileWriteRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 12),
    _RaisecomOamExtFileWriteRx_Type()
)
raisecomOamExtFileWriteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileWriteRx.setStatus("current")
_RaisecomOamExtFileTransferDataRx_Type = Counter32
_RaisecomOamExtFileTransferDataRx_Object = MibTableColumn
raisecomOamExtFileTransferDataRx = _RaisecomOamExtFileTransferDataRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 13),
    _RaisecomOamExtFileTransferDataRx_Type()
)
raisecomOamExtFileTransferDataRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileTransferDataRx.setStatus("current")
_RaisecomOamExtFileTransferDataTx_Type = Counter32
_RaisecomOamExtFileTransferDataTx_Object = MibTableColumn
raisecomOamExtFileTransferDataTx = _RaisecomOamExtFileTransferDataTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 14),
    _RaisecomOamExtFileTransferDataTx_Type()
)
raisecomOamExtFileTransferDataTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileTransferDataTx.setStatus("current")
_RaisecomOamExtFileTransferAckTx_Type = Counter32
_RaisecomOamExtFileTransferAckTx_Object = MibTableColumn
raisecomOamExtFileTransferAckTx = _RaisecomOamExtFileTransferAckTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 15),
    _RaisecomOamExtFileTransferAckTx_Type()
)
raisecomOamExtFileTransferAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileTransferAckTx.setStatus("current")
_RaisecomOamExtFileTransferAckRx_Type = Counter32
_RaisecomOamExtFileTransferAckRx_Object = MibTableColumn
raisecomOamExtFileTransferAckRx = _RaisecomOamExtFileTransferAckRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 16),
    _RaisecomOamExtFileTransferAckRx_Type()
)
raisecomOamExtFileTransferAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtFileTransferAckRx.setStatus("current")
_RaisecomOamExtNotificationTx_Type = Counter32
_RaisecomOamExtNotificationTx_Object = MibTableColumn
raisecomOamExtNotificationTx = _RaisecomOamExtNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 17),
    _RaisecomOamExtNotificationTx_Type()
)
raisecomOamExtNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtNotificationTx.setStatus("current")
_RaisecomOamExtNotificationRx_Type = Counter32
_RaisecomOamExtNotificationRx_Object = MibTableColumn
raisecomOamExtNotificationRx = _RaisecomOamExtNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 18),
    _RaisecomOamExtNotificationRx_Type()
)
raisecomOamExtNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtNotificationRx.setStatus("current")
_RaisecomOamExtStaticInfoTx_Type = Counter32
_RaisecomOamExtStaticInfoTx_Object = MibTableColumn
raisecomOamExtStaticInfoTx = _RaisecomOamExtStaticInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 19),
    _RaisecomOamExtStaticInfoTx_Type()
)
raisecomOamExtStaticInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtStaticInfoTx.setStatus("current")
_RaisecomOamExtStaticInfoRx_Type = Counter32
_RaisecomOamExtStaticInfoRx_Object = MibTableColumn
raisecomOamExtStaticInfoRx = _RaisecomOamExtStaticInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 20),
    _RaisecomOamExtStaticInfoRx_Type()
)
raisecomOamExtStaticInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtStaticInfoRx.setStatus("current")
_RaisecomOamExtDynamicInfoTx_Type = Counter32
_RaisecomOamExtDynamicInfoTx_Object = MibTableColumn
raisecomOamExtDynamicInfoTx = _RaisecomOamExtDynamicInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 21),
    _RaisecomOamExtDynamicInfoTx_Type()
)
raisecomOamExtDynamicInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtDynamicInfoTx.setStatus("current")
_RaisecomOamExtDynamicInfoRx_Type = Counter32
_RaisecomOamExtDynamicInfoRx_Object = MibTableColumn
raisecomOamExtDynamicInfoRx = _RaisecomOamExtDynamicInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 22),
    _RaisecomOamExtDynamicInfoRx_Type()
)
raisecomOamExtDynamicInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtDynamicInfoRx.setStatus("current")
_RaisecomOamExtConfTx_Type = Counter32
_RaisecomOamExtConfTx_Object = MibTableColumn
raisecomOamExtConfTx = _RaisecomOamExtConfTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 23),
    _RaisecomOamExtConfTx_Type()
)
raisecomOamExtConfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtConfTx.setStatus("current")
_RaisecomOamExtConfRx_Type = Counter32
_RaisecomOamExtConfRx_Object = MibTableColumn
raisecomOamExtConfRx = _RaisecomOamExtConfRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 24),
    _RaisecomOamExtConfRx_Type()
)
raisecomOamExtConfRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtConfRx.setStatus("current")
_RaisecomOamExtCmdTx_Type = Counter32
_RaisecomOamExtCmdTx_Object = MibTableColumn
raisecomOamExtCmdTx = _RaisecomOamExtCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 25),
    _RaisecomOamExtCmdTx_Type()
)
raisecomOamExtCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtCmdTx.setStatus("current")
_RaisecomOamExtCmdRx_Type = Counter32
_RaisecomOamExtCmdRx_Object = MibTableColumn
raisecomOamExtCmdRx = _RaisecomOamExtCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 26),
    _RaisecomOamExtCmdRx_Type()
)
raisecomOamExtCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtCmdRx.setStatus("current")
_RaisecomOamExtConnectTx_Type = Counter32
_RaisecomOamExtConnectTx_Object = MibTableColumn
raisecomOamExtConnectTx = _RaisecomOamExtConnectTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 27),
    _RaisecomOamExtConnectTx_Type()
)
raisecomOamExtConnectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtConnectTx.setStatus("current")
_RaisecomOamExtConnectRx_Type = Counter32
_RaisecomOamExtConnectRx_Object = MibTableColumn
raisecomOamExtConnectRx = _RaisecomOamExtConnectRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 28),
    _RaisecomOamExtConnectRx_Type()
)
raisecomOamExtConnectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtConnectRx.setStatus("current")
_RaisecomOamExtUnknownRx_Type = Counter32
_RaisecomOamExtUnknownRx_Object = MibTableColumn
raisecomOamExtUnknownRx = _RaisecomOamExtUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 1, 1, 29),
    _RaisecomOamExtUnknownRx_Type()
)
raisecomOamExtUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtUnknownRx.setStatus("current")
_RaisecomOamExtStatusTable_Object = MibTable
raisecomOamExtStatusTable = _RaisecomOamExtStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 2)
)
if mibBuilder.loadTexts:
    raisecomOamExtStatusTable.setStatus("current")
_RaisecomOamExtStatusEntry_Object = MibTableRow
raisecomOamExtStatusEntry = _RaisecomOamExtStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 2, 1)
)
raisecomOamExtStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomOamExtStatusEntry.setStatus("current")


class _RaisecomOamExtStatus_Type(Integer32):
    """Custom type raisecomOamExtStatus based on Integer32"""
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
        *(("nonoperative", 1),
          ("invariableInfoGet", 2),
          ("invariableInfoGetError", 3),
          ("operational", 4),
          ("fileTransfer", 5))
    )


_RaisecomOamExtStatus_Type.__name__ = "Integer32"
_RaisecomOamExtStatus_Object = MibTableColumn
raisecomOamExtStatus = _RaisecomOamExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 2, 1, 1),
    _RaisecomOamExtStatus_Type()
)
raisecomOamExtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamExtStatus.setStatus("current")
_RaisecomOamExtRemoteMibObjects_ObjectIdentity = ObjectIdentity
raisecomOamExtRemoteMibObjects = _RaisecomOamExtRemoteMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 3)
)
_RaisecomOamNotificationEnable_Type = EnableVar
_RaisecomOamNotificationEnable_Object = MibScalar
raisecomOamNotificationEnable = _RaisecomOamNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 3, 1),
    _RaisecomOamNotificationEnable_Type()
)
raisecomOamNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamNotificationEnable.setStatus("current")
_RaisecomOamExtConfigReqEnable_Type = EnableVar
_RaisecomOamExtConfigReqEnable_Object = MibScalar
raisecomOamExtConfigReqEnable = _RaisecomOamExtConfigReqEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 10, 3, 2),
    _RaisecomOamExtConfigReqEnable_Type()
)
raisecomOamExtConfigReqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamExtConfigReqEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-EXTOAM-MIB",
    **{"raisecomExtendOam": raisecomExtendOam,
       "raisecomOamExtStatsTable": raisecomOamExtStatsTable,
       "raisecomOamExtStatsEntry": raisecomOamExtStatsEntry,
       "raisecomOamExtVariableGetTx": raisecomOamExtVariableGetTx,
       "raisecomOamExtVariableGetRx": raisecomOamExtVariableGetRx,
       "raisecomOamExtVariableSetTx": raisecomOamExtVariableSetTx,
       "raisecomOamExtVariableSetRx": raisecomOamExtVariableSetRx,
       "raisecomOamExtVariableGetResponseTx": raisecomOamExtVariableGetResponseTx,
       "raisecomOamExtVariableGetResponseRx": raisecomOamExtVariableGetResponseRx,
       "raisecomOamExtVariableSetResponseTx": raisecomOamExtVariableSetResponseTx,
       "raisecomOamExtVariableSetResponseRx": raisecomOamExtVariableSetResponseRx,
       "raisecomOamExtFileReadTx": raisecomOamExtFileReadTx,
       "raisecomOamExtFileReadRx": raisecomOamExtFileReadRx,
       "raisecomOamExtFileWriteTx": raisecomOamExtFileWriteTx,
       "raisecomOamExtFileWriteRx": raisecomOamExtFileWriteRx,
       "raisecomOamExtFileTransferDataRx": raisecomOamExtFileTransferDataRx,
       "raisecomOamExtFileTransferDataTx": raisecomOamExtFileTransferDataTx,
       "raisecomOamExtFileTransferAckTx": raisecomOamExtFileTransferAckTx,
       "raisecomOamExtFileTransferAckRx": raisecomOamExtFileTransferAckRx,
       "raisecomOamExtNotificationTx": raisecomOamExtNotificationTx,
       "raisecomOamExtNotificationRx": raisecomOamExtNotificationRx,
       "raisecomOamExtStaticInfoTx": raisecomOamExtStaticInfoTx,
       "raisecomOamExtStaticInfoRx": raisecomOamExtStaticInfoRx,
       "raisecomOamExtDynamicInfoTx": raisecomOamExtDynamicInfoTx,
       "raisecomOamExtDynamicInfoRx": raisecomOamExtDynamicInfoRx,
       "raisecomOamExtConfTx": raisecomOamExtConfTx,
       "raisecomOamExtConfRx": raisecomOamExtConfRx,
       "raisecomOamExtCmdTx": raisecomOamExtCmdTx,
       "raisecomOamExtCmdRx": raisecomOamExtCmdRx,
       "raisecomOamExtConnectTx": raisecomOamExtConnectTx,
       "raisecomOamExtConnectRx": raisecomOamExtConnectRx,
       "raisecomOamExtUnknownRx": raisecomOamExtUnknownRx,
       "raisecomOamExtStatusTable": raisecomOamExtStatusTable,
       "raisecomOamExtStatusEntry": raisecomOamExtStatusEntry,
       "raisecomOamExtStatus": raisecomOamExtStatus,
       "raisecomOamExtRemoteMibObjects": raisecomOamExtRemoteMibObjects,
       "raisecomOamNotificationEnable": raisecomOamNotificationEnable,
       "raisecomOamExtConfigReqEnable": raisecomOamExtConfigReqEnable}
)
