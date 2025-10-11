# SNMP MIB module (RUCKUS-WLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-WLINK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:35 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusCommonWLINKModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonWLINKModule")

(RuckusSSID,) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusSSID")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusWLINKMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusWLINKObjects_ObjectIdentity = ObjectIdentity
ruckusWLINKObjects = _RuckusWLINKObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1)
)
_RuckusWLINKInfo_ObjectIdentity = ObjectIdentity
ruckusWLINKInfo = _RuckusWLINKInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1)
)
_RuckusWLINKTable_Object = MibTable
ruckusWLINKTable = _RuckusWLINKTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusWLINKTable.setStatus("current")
_RuckusWLINKEntry_Object = MibTableRow
ruckusWLINKEntry = _RuckusWLINKEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1)
)
ruckusWLINKEntry.setIndexNames(
    (0, "RUCKUS-WLINK-MIB", "ruckusWLINKIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLINKEntry.setStatus("current")
_RuckusWLINKSSID_Type = RuckusSSID
_RuckusWLINKSSID_Object = MibTableColumn
ruckusWLINKSSID = _RuckusWLINKSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 1),
    _RuckusWLINKSSID_Type()
)
ruckusWLINKSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKSSID.setStatus("current")


class _RuckusWLINKRole_Type(Integer32):
    """Custom type ruckusWLINKRole based on Integer32"""
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
        *(("rootBridge", 1),
          ("nonRootBridge", 2),
          ("notDecided", 3),
          ("notAvailable", 4))
    )


_RuckusWLINKRole_Type.__name__ = "Integer32"
_RuckusWLINKRole_Object = MibTableColumn
ruckusWLINKRole = _RuckusWLINKRole_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 2),
    _RuckusWLINKRole_Type()
)
ruckusWLINKRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRole.setStatus("current")
_RuckusWLINKLocalMAC_Type = MacAddress
_RuckusWLINKLocalMAC_Object = MibTableColumn
ruckusWLINKLocalMAC = _RuckusWLINKLocalMAC_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 3),
    _RuckusWLINKLocalMAC_Type()
)
ruckusWLINKLocalMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKLocalMAC.setStatus("current")
_RuckusWLINKRemoteMAC_Type = MacAddress
_RuckusWLINKRemoteMAC_Object = MibTableColumn
ruckusWLINKRemoteMAC = _RuckusWLINKRemoteMAC_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 4),
    _RuckusWLINKRemoteMAC_Type()
)
ruckusWLINKRemoteMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRemoteMAC.setStatus("current")
_RuckusWLINKTxPkts_Type = Counter32
_RuckusWLINKTxPkts_Object = MibTableColumn
ruckusWLINKTxPkts = _RuckusWLINKTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 5),
    _RuckusWLINKTxPkts_Type()
)
ruckusWLINKTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKTxPkts.setStatus("current")
_RuckusWLINKTxBytes_Type = Counter32
_RuckusWLINKTxBytes_Object = MibTableColumn
ruckusWLINKTxBytes = _RuckusWLINKTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 6),
    _RuckusWLINKTxBytes_Type()
)
ruckusWLINKTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKTxBytes.setStatus("current")
_RuckusWLINKRxPkts_Type = Counter32
_RuckusWLINKRxPkts_Object = MibTableColumn
ruckusWLINKRxPkts = _RuckusWLINKRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 7),
    _RuckusWLINKRxPkts_Type()
)
ruckusWLINKRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRxPkts.setStatus("current")
_RuckusWLINKRxBytes_Type = Counter32
_RuckusWLINKRxBytes_Object = MibTableColumn
ruckusWLINKRxBytes = _RuckusWLINKRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 8),
    _RuckusWLINKRxBytes_Type()
)
ruckusWLINKRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRxBytes.setStatus("current")


class _RuckusWLINKEstablishTime_Type(DisplayString):
    """Custom type ruckusWLINKEstablishTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusWLINKEstablishTime_Type.__name__ = "DisplayString"
_RuckusWLINKEstablishTime_Object = MibTableColumn
ruckusWLINKEstablishTime = _RuckusWLINKEstablishTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 9),
    _RuckusWLINKEstablishTime_Type()
)
ruckusWLINKEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKEstablishTime.setStatus("current")
_RuckusWLINKUpTime_Type = Unsigned32
_RuckusWLINKUpTime_Object = MibTableColumn
ruckusWLINKUpTime = _RuckusWLINKUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 10),
    _RuckusWLINKUpTime_Type()
)
ruckusWLINKUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKUpTime.setStatus("current")
_RuckusWLINKRssi_Type = Integer32
_RuckusWLINKRssi_Object = MibTableColumn
ruckusWLINKRssi = _RuckusWLINKRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 11),
    _RuckusWLINKRssi_Type()
)
ruckusWLINKRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRssi.setStatus("current")
_RuckusWLINKUpCount_Type = Integer32
_RuckusWLINKUpCount_Object = MibTableColumn
ruckusWLINKUpCount = _RuckusWLINKUpCount_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 12),
    _RuckusWLINKUpCount_Type()
)
ruckusWLINKUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKUpCount.setStatus("current")
_RuckusWLINKDownCount_Type = Integer32
_RuckusWLINKDownCount_Object = MibTableColumn
ruckusWLINKDownCount = _RuckusWLINKDownCount_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 13),
    _RuckusWLINKDownCount_Type()
)
ruckusWLINKDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKDownCount.setStatus("current")
_RuckusWLINKIndex_Type = InterfaceIndex
_RuckusWLINKIndex_Object = MibTableColumn
ruckusWLINKIndex = _RuckusWLINKIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 200),
    _RuckusWLINKIndex_Type()
)
ruckusWLINKIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIndex.setStatus("current")
_RuckusWLINKIITable_Object = MibTable
ruckusWLINKIITable = _RuckusWLINKIITable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusWLINKIITable.setStatus("current")
_RuckusWLINKIIEntry_Object = MibTableRow
ruckusWLINKIIEntry = _RuckusWLINKIIEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1)
)
ruckusWLINKIIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLINK-MIB", "ruckusWLINKIIStaIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLINKIIEntry.setStatus("current")
_RuckusWLINKIIStaIndex_Type = Integer32
_RuckusWLINKIIStaIndex_Object = MibTableColumn
ruckusWLINKIIStaIndex = _RuckusWLINKIIStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 1),
    _RuckusWLINKIIStaIndex_Type()
)
ruckusWLINKIIStaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIStaIndex.setStatus("current")
_RuckusWLINKIISSID_Type = RuckusSSID
_RuckusWLINKIISSID_Object = MibTableColumn
ruckusWLINKIISSID = _RuckusWLINKIISSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 2),
    _RuckusWLINKIISSID_Type()
)
ruckusWLINKIISSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIISSID.setStatus("current")


class _RuckusWLINKIIRole_Type(Integer32):
    """Custom type ruckusWLINKIIRole based on Integer32"""
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
        *(("rootBridge", 1),
          ("nonRootBridge", 2),
          ("notDecided", 3),
          ("notAvailable", 4))
    )


_RuckusWLINKIIRole_Type.__name__ = "Integer32"
_RuckusWLINKIIRole_Object = MibTableColumn
ruckusWLINKIIRole = _RuckusWLINKIIRole_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 3),
    _RuckusWLINKIIRole_Type()
)
ruckusWLINKIIRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIRole.setStatus("current")
_RuckusWLINKIILocalMAC_Type = MacAddress
_RuckusWLINKIILocalMAC_Object = MibTableColumn
ruckusWLINKIILocalMAC = _RuckusWLINKIILocalMAC_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 4),
    _RuckusWLINKIILocalMAC_Type()
)
ruckusWLINKIILocalMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIILocalMAC.setStatus("current")
_RuckusWLINKIIRemoteMAC_Type = MacAddress
_RuckusWLINKIIRemoteMAC_Object = MibTableColumn
ruckusWLINKIIRemoteMAC = _RuckusWLINKIIRemoteMAC_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 5),
    _RuckusWLINKIIRemoteMAC_Type()
)
ruckusWLINKIIRemoteMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIRemoteMAC.setStatus("current")
_RuckusWLINKIITxPkts_Type = Counter32
_RuckusWLINKIITxPkts_Object = MibTableColumn
ruckusWLINKIITxPkts = _RuckusWLINKIITxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 6),
    _RuckusWLINKIITxPkts_Type()
)
ruckusWLINKIITxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIITxPkts.setStatus("current")
_RuckusWLINKIITxBytes_Type = Counter32
_RuckusWLINKIITxBytes_Object = MibTableColumn
ruckusWLINKIITxBytes = _RuckusWLINKIITxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 7),
    _RuckusWLINKIITxBytes_Type()
)
ruckusWLINKIITxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIITxBytes.setStatus("current")
_RuckusWLINKIIRxPkts_Type = Counter32
_RuckusWLINKIIRxPkts_Object = MibTableColumn
ruckusWLINKIIRxPkts = _RuckusWLINKIIRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 8),
    _RuckusWLINKIIRxPkts_Type()
)
ruckusWLINKIIRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIRxPkts.setStatus("current")
_RuckusWLINKIIRxBytes_Type = Counter32
_RuckusWLINKIIRxBytes_Object = MibTableColumn
ruckusWLINKIIRxBytes = _RuckusWLINKIIRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 9),
    _RuckusWLINKIIRxBytes_Type()
)
ruckusWLINKIIRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIRxBytes.setStatus("current")


class _RuckusWLINKIIEstablishTime_Type(DisplayString):
    """Custom type ruckusWLINKIIEstablishTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusWLINKIIEstablishTime_Type.__name__ = "DisplayString"
_RuckusWLINKIIEstablishTime_Object = MibTableColumn
ruckusWLINKIIEstablishTime = _RuckusWLINKIIEstablishTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 10),
    _RuckusWLINKIIEstablishTime_Type()
)
ruckusWLINKIIEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIEstablishTime.setStatus("current")
_RuckusWLINKIIUpTime_Type = Unsigned32
_RuckusWLINKIIUpTime_Object = MibTableColumn
ruckusWLINKIIUpTime = _RuckusWLINKIIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 11),
    _RuckusWLINKIIUpTime_Type()
)
ruckusWLINKIIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIUpTime.setStatus("current")
_RuckusWLINKIIRssi_Type = Integer32
_RuckusWLINKIIRssi_Object = MibTableColumn
ruckusWLINKIIRssi = _RuckusWLINKIIRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 12),
    _RuckusWLINKIIRssi_Type()
)
ruckusWLINKIIRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIRssi.setStatus("current")
_RuckusWLINKIIUpCount_Type = Integer32
_RuckusWLINKIIUpCount_Object = MibTableColumn
ruckusWLINKIIUpCount = _RuckusWLINKIIUpCount_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 13),
    _RuckusWLINKIIUpCount_Type()
)
ruckusWLINKIIUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIUpCount.setStatus("current")
_RuckusWLINKIIDownCount_Type = Integer32
_RuckusWLINKIIDownCount_Object = MibTableColumn
ruckusWLINKIIDownCount = _RuckusWLINKIIDownCount_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 2, 1, 14),
    _RuckusWLINKIIDownCount_Type()
)
ruckusWLINKIIDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKIIDownCount.setStatus("current")
_RuckusWLINKEvents_ObjectIdentity = ObjectIdentity
ruckusWLINKEvents = _RuckusWLINKEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-WLINK-MIB",
    **{"ruckusWLINKMIB": ruckusWLINKMIB,
       "ruckusWLINKObjects": ruckusWLINKObjects,
       "ruckusWLINKInfo": ruckusWLINKInfo,
       "ruckusWLINKTable": ruckusWLINKTable,
       "ruckusWLINKEntry": ruckusWLINKEntry,
       "ruckusWLINKSSID": ruckusWLINKSSID,
       "ruckusWLINKRole": ruckusWLINKRole,
       "ruckusWLINKLocalMAC": ruckusWLINKLocalMAC,
       "ruckusWLINKRemoteMAC": ruckusWLINKRemoteMAC,
       "ruckusWLINKTxPkts": ruckusWLINKTxPkts,
       "ruckusWLINKTxBytes": ruckusWLINKTxBytes,
       "ruckusWLINKRxPkts": ruckusWLINKRxPkts,
       "ruckusWLINKRxBytes": ruckusWLINKRxBytes,
       "ruckusWLINKEstablishTime": ruckusWLINKEstablishTime,
       "ruckusWLINKUpTime": ruckusWLINKUpTime,
       "ruckusWLINKRssi": ruckusWLINKRssi,
       "ruckusWLINKUpCount": ruckusWLINKUpCount,
       "ruckusWLINKDownCount": ruckusWLINKDownCount,
       "ruckusWLINKIndex": ruckusWLINKIndex,
       "ruckusWLINKIITable": ruckusWLINKIITable,
       "ruckusWLINKIIEntry": ruckusWLINKIIEntry,
       "ruckusWLINKIIStaIndex": ruckusWLINKIIStaIndex,
       "ruckusWLINKIISSID": ruckusWLINKIISSID,
       "ruckusWLINKIIRole": ruckusWLINKIIRole,
       "ruckusWLINKIILocalMAC": ruckusWLINKIILocalMAC,
       "ruckusWLINKIIRemoteMAC": ruckusWLINKIIRemoteMAC,
       "ruckusWLINKIITxPkts": ruckusWLINKIITxPkts,
       "ruckusWLINKIITxBytes": ruckusWLINKIITxBytes,
       "ruckusWLINKIIRxPkts": ruckusWLINKIIRxPkts,
       "ruckusWLINKIIRxBytes": ruckusWLINKIIRxBytes,
       "ruckusWLINKIIEstablishTime": ruckusWLINKIIEstablishTime,
       "ruckusWLINKIIUpTime": ruckusWLINKIIUpTime,
       "ruckusWLINKIIRssi": ruckusWLINKIIRssi,
       "ruckusWLINKIIUpCount": ruckusWLINKIIUpCount,
       "ruckusWLINKIIDownCount": ruckusWLINKIIDownCount,
       "ruckusWLINKEvents": ruckusWLINKEvents}
)
