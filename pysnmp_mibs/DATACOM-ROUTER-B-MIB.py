# SNMP MIB module (DATACOM-ROUTER-B-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DATACOM-ROUTER-B-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:54 2025
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

(datacomAccessDevicesMIBs,
 datacomModules) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomAccessDevicesMIBs",
    "datacomModules")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class DmDevIndex(Integer32):
    """Custom type DmDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )





class DmDevLocalIndex(Integer32):
    """Custom type DmDevLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )





class DmSlotIndex(Integer32):
    """Custom type DmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )





class DmPortIndex(Integer32):
    """Custom type DmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DatacomRouterBMIBModule_ObjectIdentity = ObjectIdentity
datacomRouterBMIBModule = _DatacomRouterBMIBModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 1, 3521)
)
_DmAdRouterBMIB_ObjectIdentity = ObjectIdentity
dmAdRouterBMIB = _DmAdRouterBMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21)
)
_DmAdRtbInf_ObjectIdentity = ObjectIdentity
dmAdRtbInf = _DmAdRtbInf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1)
)
_RtbInfItfGprsTable_Object = MibTable
rtbInfItfGprsTable = _RtbInfItfGprsTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15)
)
if mibBuilder.loadTexts:
    rtbInfItfGprsTable.setStatus("mandatory")
_RtbInfItfGprsEntry_Object = MibTableRow
rtbInfItfGprsEntry = _RtbInfItfGprsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1)
)
rtbInfItfGprsEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbInfItfGprsDevNo"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbInfItfGprsDevLocalId"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbInfItfGprsSlotNo"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbInfItfGprsPortNo"),
)
if mibBuilder.loadTexts:
    rtbInfItfGprsEntry.setStatus("mandatory")
_RtbInfItfGprsDevNo_Type = DmDevIndex
_RtbInfItfGprsDevNo_Object = MibTableColumn
rtbInfItfGprsDevNo = _RtbInfItfGprsDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 1),
    _RtbInfItfGprsDevNo_Type()
)
rtbInfItfGprsDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsDevNo.setStatus("mandatory")
_RtbInfItfGprsDevLocalId_Type = DmDevLocalIndex
_RtbInfItfGprsDevLocalId_Object = MibTableColumn
rtbInfItfGprsDevLocalId = _RtbInfItfGprsDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 2),
    _RtbInfItfGprsDevLocalId_Type()
)
rtbInfItfGprsDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsDevLocalId.setStatus("mandatory")
_RtbInfItfGprsSlotNo_Type = DmSlotIndex
_RtbInfItfGprsSlotNo_Object = MibTableColumn
rtbInfItfGprsSlotNo = _RtbInfItfGprsSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 3),
    _RtbInfItfGprsSlotNo_Type()
)
rtbInfItfGprsSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsSlotNo.setStatus("mandatory")
_RtbInfItfGprsPortNo_Type = DmPortIndex
_RtbInfItfGprsPortNo_Object = MibTableColumn
rtbInfItfGprsPortNo = _RtbInfItfGprsPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 4),
    _RtbInfItfGprsPortNo_Type()
)
rtbInfItfGprsPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsPortNo.setStatus("mandatory")
_RtbInfItfGprsTaInf_Type = DisplayString
_RtbInfItfGprsTaInf_Object = MibTableColumn
rtbInfItfGprsTaInf = _RtbInfItfGprsTaInf_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 5),
    _RtbInfItfGprsTaInf_Type()
)
rtbInfItfGprsTaInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsTaInf.setStatus("mandatory")
_RtbInfItfGprsTaConf_Type = DisplayString
_RtbInfItfGprsTaConf_Object = MibTableColumn
rtbInfItfGprsTaConf = _RtbInfItfGprsTaConf_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 6),
    _RtbInfItfGprsTaConf_Type()
)
rtbInfItfGprsTaConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsTaConf.setStatus("mandatory")
_RtbInfItfGprsTaSerial_Type = DisplayString
_RtbInfItfGprsTaSerial_Object = MibTableColumn
rtbInfItfGprsTaSerial = _RtbInfItfGprsTaSerial_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 7),
    _RtbInfItfGprsTaSerial_Type()
)
rtbInfItfGprsTaSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsTaSerial.setStatus("mandatory")
_RtbInfItfGprsTaRegistry_Type = DisplayString
_RtbInfItfGprsTaRegistry_Object = MibTableColumn
rtbInfItfGprsTaRegistry = _RtbInfItfGprsTaRegistry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 8),
    _RtbInfItfGprsTaRegistry_Type()
)
rtbInfItfGprsTaRegistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsTaRegistry.setStatus("mandatory")
_RtbInfItfGprsSimCardInf_Type = DisplayString
_RtbInfItfGprsSimCardInf_Object = MibTableColumn
rtbInfItfGprsSimCardInf = _RtbInfItfGprsSimCardInf_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 9),
    _RtbInfItfGprsSimCardInf_Type()
)
rtbInfItfGprsSimCardInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsSimCardInf.setStatus("mandatory")
_RtbInfItfGprsCellConn_Type = DisplayString
_RtbInfItfGprsCellConn_Object = MibTableColumn
rtbInfItfGprsCellConn = _RtbInfItfGprsCellConn_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 10),
    _RtbInfItfGprsCellConn_Type()
)
rtbInfItfGprsCellConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsCellConn.setStatus("mandatory")
_RtbInfItfGprsCellsMon_Type = DisplayString
_RtbInfItfGprsCellsMon_Object = MibTableColumn
rtbInfItfGprsCellsMon = _RtbInfItfGprsCellsMon_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 11),
    _RtbInfItfGprsCellsMon_Type()
)
rtbInfItfGprsCellsMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsCellsMon.setStatus("mandatory")
_RtbInfItfGprsNetInf_Type = DisplayString
_RtbInfItfGprsNetInf_Object = MibTableColumn
rtbInfItfGprsNetInf = _RtbInfItfGprsNetInf_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 1, 15, 1, 12),
    _RtbInfItfGprsNetInf_Type()
)
rtbInfItfGprsNetInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbInfItfGprsNetInf.setStatus("mandatory")
_DmAdRtbStatus_ObjectIdentity = ObjectIdentity
dmAdRtbStatus = _DmAdRtbStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2)
)
_RtbStItfGenTable_Object = MibTable
rtbStItfGenTable = _RtbStItfGenTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12)
)
if mibBuilder.loadTexts:
    rtbStItfGenTable.setStatus("mandatory")
_RtbStItfGenEntry_Object = MibTableRow
rtbStItfGenEntry = _RtbStItfGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1)
)
rtbStItfGenEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfGenDevNo"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfGenDevLocalId"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfGenSlotNo"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfGenPortNo"),
)
if mibBuilder.loadTexts:
    rtbStItfGenEntry.setStatus("mandatory")
_RtbStItfGenDevNo_Type = DmDevIndex
_RtbStItfGenDevNo_Object = MibTableColumn
rtbStItfGenDevNo = _RtbStItfGenDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1, 1),
    _RtbStItfGenDevNo_Type()
)
rtbStItfGenDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfGenDevNo.setStatus("mandatory")
_RtbStItfGenDevLocalId_Type = DmDevLocalIndex
_RtbStItfGenDevLocalId_Object = MibTableColumn
rtbStItfGenDevLocalId = _RtbStItfGenDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1, 2),
    _RtbStItfGenDevLocalId_Type()
)
rtbStItfGenDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfGenDevLocalId.setStatus("mandatory")
_RtbStItfGenSlotNo_Type = DmSlotIndex
_RtbStItfGenSlotNo_Object = MibTableColumn
rtbStItfGenSlotNo = _RtbStItfGenSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1, 3),
    _RtbStItfGenSlotNo_Type()
)
rtbStItfGenSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfGenSlotNo.setStatus("mandatory")
_RtbStItfGenPortNo_Type = DmPortIndex
_RtbStItfGenPortNo_Object = MibTableColumn
rtbStItfGenPortNo = _RtbStItfGenPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1, 4),
    _RtbStItfGenPortNo_Type()
)
rtbStItfGenPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfGenPortNo.setStatus("mandatory")


class _RtbStItfGenLink_Type(Integer32):
    """Custom type rtbStItfGenLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("infNotAvailable", 255))
    )


_RtbStItfGenLink_Type.__name__ = "Integer32"
_RtbStItfGenLink_Object = MibTableColumn
rtbStItfGenLink = _RtbStItfGenLink_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1, 5),
    _RtbStItfGenLink_Type()
)
rtbStItfGenLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfGenLink.setStatus("mandatory")


class _RtbStItfGenIndex_Type(Integer32):
    """Custom type rtbStItfGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )


_RtbStItfGenIndex_Type.__name__ = "Integer32"
_RtbStItfGenIndex_Object = MibTableColumn
rtbStItfGenIndex = _RtbStItfGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 12, 1, 6),
    _RtbStItfGenIndex_Type()
)
rtbStItfGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfGenIndex.setStatus("mandatory")
_RtbStItfAddTable_Object = MibTable
rtbStItfAddTable = _RtbStItfAddTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15)
)
if mibBuilder.loadTexts:
    rtbStItfAddTable.setStatus("mandatory")
_RtbStItfAddEntry_Object = MibTableRow
rtbStItfAddEntry = _RtbStItfAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1)
)
rtbStItfAddEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfAddDevNo"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfAddDevLocalId"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfAddSlotNo"),
    (0, "DATACOM-ROUTER-B-MIB", "rtbStItfAddPortNo"),
)
if mibBuilder.loadTexts:
    rtbStItfAddEntry.setStatus("mandatory")
_RtbStItfAddDevNo_Type = DmDevIndex
_RtbStItfAddDevNo_Object = MibTableColumn
rtbStItfAddDevNo = _RtbStItfAddDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1, 1),
    _RtbStItfAddDevNo_Type()
)
rtbStItfAddDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfAddDevNo.setStatus("mandatory")
_RtbStItfAddDevLocalId_Type = DmDevLocalIndex
_RtbStItfAddDevLocalId_Object = MibTableColumn
rtbStItfAddDevLocalId = _RtbStItfAddDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1, 2),
    _RtbStItfAddDevLocalId_Type()
)
rtbStItfAddDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfAddDevLocalId.setStatus("mandatory")
_RtbStItfAddSlotNo_Type = DmSlotIndex
_RtbStItfAddSlotNo_Object = MibTableColumn
rtbStItfAddSlotNo = _RtbStItfAddSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1, 3),
    _RtbStItfAddSlotNo_Type()
)
rtbStItfAddSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfAddSlotNo.setStatus("mandatory")
_RtbStItfAddPortNo_Type = DmPortIndex
_RtbStItfAddPortNo_Object = MibTableColumn
rtbStItfAddPortNo = _RtbStItfAddPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1, 4),
    _RtbStItfAddPortNo_Type()
)
rtbStItfAddPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfAddPortNo.setStatus("mandatory")
_RtbStItfAddLocal_Type = IpAddress
_RtbStItfAddLocal_Object = MibTableColumn
rtbStItfAddLocal = _RtbStItfAddLocal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1, 5),
    _RtbStItfAddLocal_Type()
)
rtbStItfAddLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfAddLocal.setStatus("mandatory")
_RtbStItfAddRemote_Type = IpAddress
_RtbStItfAddRemote_Object = MibTableColumn
rtbStItfAddRemote = _RtbStItfAddRemote_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 2, 15, 1, 6),
    _RtbStItfAddRemote_Type()
)
rtbStItfAddRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbStItfAddRemote.setStatus("mandatory")
_DmAdRtbPerformance_ObjectIdentity = ObjectIdentity
dmAdRtbPerformance = _DmAdRtbPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5)
)


class _RtbPerfHwStCpu_Type(Integer32):
    """Custom type rtbPerfHwStCpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtbPerfHwStCpu_Type.__name__ = "Integer32"
_RtbPerfHwStCpu_Object = MibScalar
rtbPerfHwStCpu = _RtbPerfHwStCpu_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 1),
    _RtbPerfHwStCpu_Type()
)
rtbPerfHwStCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfHwStCpu.setStatus("mandatory")


class _RtbPerfHwStMemory_Type(Integer32):
    """Custom type rtbPerfHwStMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtbPerfHwStMemory_Type.__name__ = "Integer32"
_RtbPerfHwStMemory_Object = MibScalar
rtbPerfHwStMemory = _RtbPerfHwStMemory_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 2),
    _RtbPerfHwStMemory_Type()
)
rtbPerfHwStMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfHwStMemory.setStatus("mandatory")
_RtbPerfItfTable_Object = MibTable
rtbPerfItfTable = _RtbPerfItfTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15)
)
if mibBuilder.loadTexts:
    rtbPerfItfTable.setStatus("mandatory")
_RtbPerfItfEntry_Object = MibTableRow
rtbPerfItfEntry = _RtbPerfItfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1)
)
rtbPerfItfEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbPerfItfIndex"),
)
if mibBuilder.loadTexts:
    rtbPerfItfEntry.setStatus("mandatory")


class _RtbPerfItfIndex_Type(Integer32):
    """Custom type rtbPerfItfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )


_RtbPerfItfIndex_Type.__name__ = "Integer32"
_RtbPerfItfIndex_Object = MibTableColumn
rtbPerfItfIndex = _RtbPerfItfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 1),
    _RtbPerfItfIndex_Type()
)
rtbPerfItfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfIndex.setStatus("mandatory")
_RtbPerfItfDescr_Type = DisplayString
_RtbPerfItfDescr_Object = MibTableColumn
rtbPerfItfDescr = _RtbPerfItfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 2),
    _RtbPerfItfDescr_Type()
)
rtbPerfItfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfDescr.setStatus("mandatory")
_RtbPerfItfOctets_Type = Counter32
_RtbPerfItfOctets_Object = MibTableColumn
rtbPerfItfOctets = _RtbPerfItfOctets_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 3),
    _RtbPerfItfOctets_Type()
)
rtbPerfItfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfOctets.setStatus("mandatory")
_RtbPerfItfPkts_Type = Counter32
_RtbPerfItfPkts_Object = MibTableColumn
rtbPerfItfPkts = _RtbPerfItfPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 4),
    _RtbPerfItfPkts_Type()
)
rtbPerfItfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfPkts.setStatus("mandatory")
_RtbPerfItfCollisions_Type = Counter32
_RtbPerfItfCollisions_Object = MibTableColumn
rtbPerfItfCollisions = _RtbPerfItfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 5),
    _RtbPerfItfCollisions_Type()
)
rtbPerfItfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfCollisions.setStatus("mandatory")
_RtbPerfItfUtilization_Type = Counter32
_RtbPerfItfUtilization_Object = MibTableColumn
rtbPerfItfUtilization = _RtbPerfItfUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 6),
    _RtbPerfItfUtilization_Type()
)
rtbPerfItfUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfUtilization.setStatus("mandatory")
_RtbPerfItfDrop_Type = Counter32
_RtbPerfItfDrop_Object = MibTableColumn
rtbPerfItfDrop = _RtbPerfItfDrop_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 7),
    _RtbPerfItfDrop_Type()
)
rtbPerfItfDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfDrop.setStatus("mandatory")
_RtbPerfItfError_Type = Counter32
_RtbPerfItfError_Object = MibTableColumn
rtbPerfItfError = _RtbPerfItfError_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 8),
    _RtbPerfItfError_Type()
)
rtbPerfItfError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfError.setStatus("mandatory")
_RtbPerfItfRxDataRate_Type = Counter32
_RtbPerfItfRxDataRate_Object = MibTableColumn
rtbPerfItfRxDataRate = _RtbPerfItfRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 9),
    _RtbPerfItfRxDataRate_Type()
)
rtbPerfItfRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfRxDataRate.setStatus("mandatory")
_RtbPerfItfTxDataRate_Type = Counter32
_RtbPerfItfTxDataRate_Object = MibTableColumn
rtbPerfItfTxDataRate = _RtbPerfItfTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 10),
    _RtbPerfItfTxDataRate_Type()
)
rtbPerfItfTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfTxDataRate.setStatus("mandatory")
_RtbPerfItfRxDropRate_Type = Counter32
_RtbPerfItfRxDropRate_Object = MibTableColumn
rtbPerfItfRxDropRate = _RtbPerfItfRxDropRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 11),
    _RtbPerfItfRxDropRate_Type()
)
rtbPerfItfRxDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfRxDropRate.setStatus("mandatory")
_RtbPerfItfTxDropRate_Type = Counter32
_RtbPerfItfTxDropRate_Object = MibTableColumn
rtbPerfItfTxDropRate = _RtbPerfItfTxDropRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 15, 1, 12),
    _RtbPerfItfTxDropRate_Type()
)
rtbPerfItfTxDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfItfTxDropRate.setStatus("mandatory")
_RtbPerfQoSQueueTable_Object = MibTable
rtbPerfQoSQueueTable = _RtbPerfQoSQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20)
)
if mibBuilder.loadTexts:
    rtbPerfQoSQueueTable.setStatus("mandatory")
_RtbPerfQoSQueueEntry_Object = MibTableRow
rtbPerfQoSQueueEntry = _RtbPerfQoSQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1)
)
rtbPerfQoSQueueEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbPerfQoSQueueIndex"),
)
if mibBuilder.loadTexts:
    rtbPerfQoSQueueEntry.setStatus("mandatory")


class _RtbPerfQoSQueueIndex_Type(Integer32):
    """Custom type rtbPerfQoSQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbPerfQoSQueueIndex_Type.__name__ = "Integer32"
_RtbPerfQoSQueueIndex_Object = MibTableColumn
rtbPerfQoSQueueIndex = _RtbPerfQoSQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 1),
    _RtbPerfQoSQueueIndex_Type()
)
rtbPerfQoSQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueIndex.setStatus("mandatory")
_RtbPerfQoSQueueItfDescr_Type = DisplayString
_RtbPerfQoSQueueItfDescr_Object = MibTableColumn
rtbPerfQoSQueueItfDescr = _RtbPerfQoSQueueItfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 2),
    _RtbPerfQoSQueueItfDescr_Type()
)
rtbPerfQoSQueueItfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueItfDescr.setStatus("mandatory")


class _RtbPerfQoSQueueMark_Type(Integer32):
    """Custom type rtbPerfQoSQueueMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbPerfQoSQueueMark_Type.__name__ = "Integer32"
_RtbPerfQoSQueueMark_Object = MibTableColumn
rtbPerfQoSQueueMark = _RtbPerfQoSQueueMark_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 3),
    _RtbPerfQoSQueueMark_Type()
)
rtbPerfQoSQueueMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueMark.setStatus("mandatory")
_RtbPerfQoSQueueTxDataRate_Type = Counter32
_RtbPerfQoSQueueTxDataRate_Object = MibTableColumn
rtbPerfQoSQueueTxDataRate = _RtbPerfQoSQueueTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 4),
    _RtbPerfQoSQueueTxDataRate_Type()
)
rtbPerfQoSQueueTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueTxDataRate.setStatus("mandatory")
_RtbPerfQoSQueueTxPktDropRate_Type = Counter32
_RtbPerfQoSQueueTxPktDropRate_Object = MibTableColumn
rtbPerfQoSQueueTxPktDropRate = _RtbPerfQoSQueueTxPktDropRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 5),
    _RtbPerfQoSQueueTxPktDropRate_Type()
)
rtbPerfQoSQueueTxPktDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueTxPktDropRate.setStatus("mandatory")
_RtbPerfQoSQueueTrafficDescr_Type = DisplayString
_RtbPerfQoSQueueTrafficDescr_Object = MibTableColumn
rtbPerfQoSQueueTrafficDescr = _RtbPerfQoSQueueTrafficDescr_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 6),
    _RtbPerfQoSQueueTrafficDescr_Type()
)
rtbPerfQoSQueueTrafficDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueTrafficDescr.setStatus("mandatory")
_RtbPerfQoSQueueClassName_Type = DisplayString
_RtbPerfQoSQueueClassName_Object = MibTableColumn
rtbPerfQoSQueueClassName = _RtbPerfQoSQueueClassName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 7),
    _RtbPerfQoSQueueClassName_Type()
)
rtbPerfQoSQueueClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueClassName.setStatus("mandatory")


class _RtbPerfQoSQueuePriority_Type(Integer32):
    """Custom type rtbPerfQoSQueuePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_RtbPerfQoSQueuePriority_Type.__name__ = "Integer32"
_RtbPerfQoSQueuePriority_Object = MibTableColumn
rtbPerfQoSQueuePriority = _RtbPerfQoSQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 8),
    _RtbPerfQoSQueuePriority_Type()
)
rtbPerfQoSQueuePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueuePriority.setStatus("mandatory")
_RtbPerfQoSQueueMinRate_Type = Integer32
_RtbPerfQoSQueueMinRate_Object = MibTableColumn
rtbPerfQoSQueueMinRate = _RtbPerfQoSQueueMinRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 9),
    _RtbPerfQoSQueueMinRate_Type()
)
rtbPerfQoSQueueMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueMinRate.setStatus("mandatory")
_RtbPerfQoSQueueMaxRate_Type = Integer32
_RtbPerfQoSQueueMaxRate_Object = MibTableColumn
rtbPerfQoSQueueMaxRate = _RtbPerfQoSQueueMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 10),
    _RtbPerfQoSQueueMaxRate_Type()
)
rtbPerfQoSQueueMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueMaxRate.setStatus("mandatory")
_RtbPerfQoSQueueDroppedBytes_Type = Counter64
_RtbPerfQoSQueueDroppedBytes_Object = MibTableColumn
rtbPerfQoSQueueDroppedBytes = _RtbPerfQoSQueueDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 11),
    _RtbPerfQoSQueueDroppedBytes_Type()
)
rtbPerfQoSQueueDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueDroppedBytes.setStatus("mandatory")
_RtbPerfQoSQueueSentBytes_Type = Counter64
_RtbPerfQoSQueueSentBytes_Object = MibTableColumn
rtbPerfQoSQueueSentBytes = _RtbPerfQoSQueueSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 12),
    _RtbPerfQoSQueueSentBytes_Type()
)
rtbPerfQoSQueueSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueSentBytes.setStatus("mandatory")
_RtbPerfQoSQueueEnqueuedBytes_Type = Counter32
_RtbPerfQoSQueueEnqueuedBytes_Object = MibTableColumn
rtbPerfQoSQueueEnqueuedBytes = _RtbPerfQoSQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 13),
    _RtbPerfQoSQueueEnqueuedBytes_Type()
)
rtbPerfQoSQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueEnqueuedBytes.setStatus("mandatory")
_RtbPerfQoSQueueTxDataRateBits_Type = Counter32
_RtbPerfQoSQueueTxDataRateBits_Object = MibTableColumn
rtbPerfQoSQueueTxDataRateBits = _RtbPerfQoSQueueTxDataRateBits_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 14),
    _RtbPerfQoSQueueTxDataRateBits_Type()
)
rtbPerfQoSQueueTxDataRateBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueTxDataRateBits.setStatus("mandatory")
_RtbPerfQoSQueueDroppedPkts_Type = Counter64
_RtbPerfQoSQueueDroppedPkts_Object = MibTableColumn
rtbPerfQoSQueueDroppedPkts = _RtbPerfQoSQueueDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 15),
    _RtbPerfQoSQueueDroppedPkts_Type()
)
rtbPerfQoSQueueDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueDroppedPkts.setStatus("mandatory")
_RtbPerfQoSQueueSentPkts_Type = Counter64
_RtbPerfQoSQueueSentPkts_Object = MibTableColumn
rtbPerfQoSQueueSentPkts = _RtbPerfQoSQueueSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 5, 20, 1, 16),
    _RtbPerfQoSQueueSentPkts_Type()
)
rtbPerfQoSQueueSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbPerfQoSQueueSentPkts.setStatus("mandatory")
_DmAdRtbConfigCopy_ObjectIdentity = ObjectIdentity
dmAdRtbConfigCopy = _DmAdRtbConfigCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6)
)


class _RtbConfigCopyProtocol_Type(Integer32):
    """Custom type rtbConfigCopyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2),
          ("sftp", 3))
    )


_RtbConfigCopyProtocol_Type.__name__ = "Integer32"
_RtbConfigCopyProtocol_Object = MibScalar
rtbConfigCopyProtocol = _RtbConfigCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 1),
    _RtbConfigCopyProtocol_Type()
)
rtbConfigCopyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyProtocol.setStatus("mandatory")
_RtbConfigCopyServerAddress_Type = IpAddress
_RtbConfigCopyServerAddress_Object = MibScalar
rtbConfigCopyServerAddress = _RtbConfigCopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 2),
    _RtbConfigCopyServerAddress_Type()
)
rtbConfigCopyServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyServerAddress.setStatus("mandatory")


class _RtbConfigCopyFileName_Type(DisplayString):
    """Custom type rtbConfigCopyFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RtbConfigCopyFileName_Type.__name__ = "DisplayString"
_RtbConfigCopyFileName_Object = MibScalar
rtbConfigCopyFileName = _RtbConfigCopyFileName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 3),
    _RtbConfigCopyFileName_Type()
)
rtbConfigCopyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyFileName.setStatus("mandatory")


class _RtbConfigCopyDestFileType_Type(Integer32):
    """Custom type rtbConfigCopyDestFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("runningConfig", 1),
          ("startupConfig", 2))
    )


_RtbConfigCopyDestFileType_Type.__name__ = "Integer32"
_RtbConfigCopyDestFileType_Object = MibScalar
rtbConfigCopyDestFileType = _RtbConfigCopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 4),
    _RtbConfigCopyDestFileType_Type()
)
rtbConfigCopyDestFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyDestFileType.setStatus("mandatory")


class _RtbConfigCopyInitTransfer_Type(Integer32):
    """Custom type rtbConfigCopyInitTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_RtbConfigCopyInitTransfer_Type.__name__ = "Integer32"
_RtbConfigCopyInitTransfer_Object = MibScalar
rtbConfigCopyInitTransfer = _RtbConfigCopyInitTransfer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 5),
    _RtbConfigCopyInitTransfer_Type()
)
rtbConfigCopyInitTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyInitTransfer.setStatus("mandatory")


class _RtbConfigCopyStatus_Type(Integer32):
    """Custom type rtbConfigCopyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("successful", 1),
          ("running", 2),
          ("failed", 3))
    )


_RtbConfigCopyStatus_Type.__name__ = "Integer32"
_RtbConfigCopyStatus_Object = MibScalar
rtbConfigCopyStatus = _RtbConfigCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 6),
    _RtbConfigCopyStatus_Type()
)
rtbConfigCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbConfigCopyStatus.setStatus("mandatory")


class _RtbConfigCopySave_Type(Integer32):
    """Custom type rtbConfigCopySave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_RtbConfigCopySave_Type.__name__ = "Integer32"
_RtbConfigCopySave_Object = MibScalar
rtbConfigCopySave = _RtbConfigCopySave_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 7),
    _RtbConfigCopySave_Type()
)
rtbConfigCopySave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopySave.setStatus("mandatory")


class _RtbConfigCopyApplyType_Type(Integer32):
    """Custom type rtbConfigCopyApplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("merge", 1),
          ("replace", 2))
    )


_RtbConfigCopyApplyType_Type.__name__ = "Integer32"
_RtbConfigCopyApplyType_Object = MibScalar
rtbConfigCopyApplyType = _RtbConfigCopyApplyType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 8),
    _RtbConfigCopyApplyType_Type()
)
rtbConfigCopyApplyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyApplyType.setStatus("mandatory")


class _RtbConfigCopyFileFormat_Type(Integer32):
    """Custom type rtbConfigCopyFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-detect", 1),
          ("file-tree", 2),
          ("cmd-sets", 3))
    )


_RtbConfigCopyFileFormat_Type.__name__ = "Integer32"
_RtbConfigCopyFileFormat_Object = MibScalar
rtbConfigCopyFileFormat = _RtbConfigCopyFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 9),
    _RtbConfigCopyFileFormat_Type()
)
rtbConfigCopyFileFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyFileFormat.setStatus("mandatory")


class _RtbConfigCopyOpType_Type(Integer32):
    """Custom type rtbConfigCopyOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("export", 2))
    )


_RtbConfigCopyOpType_Type.__name__ = "Integer32"
_RtbConfigCopyOpType_Object = MibScalar
rtbConfigCopyOpType = _RtbConfigCopyOpType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 10),
    _RtbConfigCopyOpType_Type()
)
rtbConfigCopyOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyOpType.setStatus("mandatory")


class _RtbConfigCopyUser_Type(DisplayString):
    """Custom type rtbConfigCopyUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RtbConfigCopyUser_Type.__name__ = "DisplayString"
_RtbConfigCopyUser_Object = MibScalar
rtbConfigCopyUser = _RtbConfigCopyUser_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 11),
    _RtbConfigCopyUser_Type()
)
rtbConfigCopyUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyUser.setStatus("mandatory")


class _RtbConfigCopyPassword_Type(DisplayString):
    """Custom type rtbConfigCopyPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RtbConfigCopyPassword_Type.__name__ = "DisplayString"
_RtbConfigCopyPassword_Object = MibScalar
rtbConfigCopyPassword = _RtbConfigCopyPassword_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 6, 12),
    _RtbConfigCopyPassword_Type()
)
rtbConfigCopyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtbConfigCopyPassword.setStatus("mandatory")
_DmAdRtbLTE_ObjectIdentity = ObjectIdentity
dmAdRtbLTE = _DmAdRtbLTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7)
)


class _RtbLTESignalStrength_Type(DisplayString):
    """Custom type rtbLTESignalStrength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RtbLTESignalStrength_Type.__name__ = "DisplayString"
_RtbLTESignalStrength_Object = MibScalar
rtbLTESignalStrength = _RtbLTESignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 1),
    _RtbLTESignalStrength_Type()
)
rtbLTESignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTESignalStrength.setStatus("mandatory")


class _RtbLTEChannel_Type(Integer32):
    """Custom type rtbLTEChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbLTEChannel_Type.__name__ = "Integer32"
_RtbLTEChannel_Object = MibScalar
rtbLTEChannel = _RtbLTEChannel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 2),
    _RtbLTEChannel_Type()
)
rtbLTEChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTEChannel.setStatus("mandatory")
_RtbLTENeighborTable_Object = MibTable
rtbLTENeighborTable = _RtbLTENeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 3)
)
if mibBuilder.loadTexts:
    rtbLTENeighborTable.setStatus("mandatory")
_RtbLTENeighborEntry_Object = MibTableRow
rtbLTENeighborEntry = _RtbLTENeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 3, 1)
)
rtbLTENeighborEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbLTENeighborIndex"),
)
if mibBuilder.loadTexts:
    rtbLTENeighborEntry.setStatus("mandatory")


class _RtbLTENeighborIndex_Type(Integer32):
    """Custom type rtbLTENeighborIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbLTENeighborIndex_Type.__name__ = "Integer32"
_RtbLTENeighborIndex_Object = MibTableColumn
rtbLTENeighborIndex = _RtbLTENeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 3, 1, 1),
    _RtbLTENeighborIndex_Type()
)
rtbLTENeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborIndex.setStatus("mandatory")


class _RtbLTENeighborIndexNeighbor_Type(Integer32):
    """Custom type rtbLTENeighborIndexNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbLTENeighborIndexNeighbor_Type.__name__ = "Integer32"
_RtbLTENeighborIndexNeighbor_Object = MibTableColumn
rtbLTENeighborIndexNeighbor = _RtbLTENeighborIndexNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 3, 1, 2),
    _RtbLTENeighborIndexNeighbor_Type()
)
rtbLTENeighborIndexNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborIndexNeighbor.setStatus("mandatory")
_RtbLTENeighborDescr_Type = DisplayString
_RtbLTENeighborDescr_Object = MibTableColumn
rtbLTENeighborDescr = _RtbLTENeighborDescr_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 3, 1, 3),
    _RtbLTENeighborDescr_Type()
)
rtbLTENeighborDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborDescr.setStatus("mandatory")
_RtbLTENeighborRFChannelNumber_Type = DisplayString
_RtbLTENeighborRFChannelNumber_Object = MibTableColumn
rtbLTENeighborRFChannelNumber = _RtbLTENeighborRFChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 3, 1, 4),
    _RtbLTENeighborRFChannelNumber_Type()
)
rtbLTENeighborRFChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborRFChannelNumber.setStatus("mandatory")
_RtbLTENeighborCellsTable_Object = MibTable
rtbLTENeighborCellsTable = _RtbLTENeighborCellsTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4)
)
if mibBuilder.loadTexts:
    rtbLTENeighborCellsTable.setStatus("mandatory")
_RtbLTENeighborCellsEntry_Object = MibTableRow
rtbLTENeighborCellsEntry = _RtbLTENeighborCellsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1)
)
rtbLTENeighborCellsEntry.setIndexNames(
    (0, "DATACOM-ROUTER-B-MIB", "rtbLTENeighborCellsIndex"),
)
if mibBuilder.loadTexts:
    rtbLTENeighborCellsEntry.setStatus("mandatory")


class _RtbLTENeighborCellsIndex_Type(Integer32):
    """Custom type rtbLTENeighborCellsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbLTENeighborCellsIndex_Type.__name__ = "Integer32"
_RtbLTENeighborCellsIndex_Object = MibTableColumn
rtbLTENeighborCellsIndex = _RtbLTENeighborCellsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1, 1),
    _RtbLTENeighborCellsIndex_Type()
)
rtbLTENeighborCellsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborCellsIndex.setStatus("mandatory")


class _RtbLTENeighborCellsPhysicalCellID_Type(Integer32):
    """Custom type rtbLTENeighborCellsPhysicalCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbLTENeighborCellsPhysicalCellID_Type.__name__ = "Integer32"
_RtbLTENeighborCellsPhysicalCellID_Object = MibTableColumn
rtbLTENeighborCellsPhysicalCellID = _RtbLTENeighborCellsPhysicalCellID_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1, 2),
    _RtbLTENeighborCellsPhysicalCellID_Type()
)
rtbLTENeighborCellsPhysicalCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborCellsPhysicalCellID.setStatus("mandatory")
_RtbLTENeighborCellsRSRQ_Type = DisplayString
_RtbLTENeighborCellsRSRQ_Object = MibTableColumn
rtbLTENeighborCellsRSRQ = _RtbLTENeighborCellsRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1, 3),
    _RtbLTENeighborCellsRSRQ_Type()
)
rtbLTENeighborCellsRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborCellsRSRQ.setStatus("mandatory")
_RtbLTENeighborCellsRSRP_Type = DisplayString
_RtbLTENeighborCellsRSRP_Object = MibTableColumn
rtbLTENeighborCellsRSRP = _RtbLTENeighborCellsRSRP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1, 4),
    _RtbLTENeighborCellsRSRP_Type()
)
rtbLTENeighborCellsRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborCellsRSRP.setStatus("mandatory")
_RtbLTENeighborCellsRSSI_Type = DisplayString
_RtbLTENeighborCellsRSSI_Object = MibTableColumn
rtbLTENeighborCellsRSSI = _RtbLTENeighborCellsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1, 5),
    _RtbLTENeighborCellsRSSI_Type()
)
rtbLTENeighborCellsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborCellsRSSI.setStatus("mandatory")


class _RtbLTENeighborCellsCellSelectionRXLevel_Type(Integer32):
    """Custom type rtbLTENeighborCellsCellSelectionRXLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000253),
    )


_RtbLTENeighborCellsCellSelectionRXLevel_Type.__name__ = "Integer32"
_RtbLTENeighborCellsCellSelectionRXLevel_Object = MibTableColumn
rtbLTENeighborCellsCellSelectionRXLevel = _RtbLTENeighborCellsCellSelectionRXLevel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 4, 1, 6),
    _RtbLTENeighborCellsCellSelectionRXLevel_Type()
)
rtbLTENeighborCellsCellSelectionRXLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTENeighborCellsCellSelectionRXLevel.setStatus("mandatory")


class _RtbLTEConnectionStatus_Type(Integer32):
    """Custom type rtbLTEConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_RtbLTEConnectionStatus_Type.__name__ = "Integer32"
_RtbLTEConnectionStatus_Object = MibScalar
rtbLTEConnectionStatus = _RtbLTEConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 21, 7, 5),
    _RtbLTEConnectionStatus_Type()
)
rtbLTEConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtbLTEConnectionStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATACOM-ROUTER-B-MIB",
    **{"DisplayString": DisplayString,
       "DmDevIndex": DmDevIndex,
       "DmDevLocalIndex": DmDevLocalIndex,
       "DmSlotIndex": DmSlotIndex,
       "DmPortIndex": DmPortIndex,
       "datacomRouterBMIBModule": datacomRouterBMIBModule,
       "dmAdRouterBMIB": dmAdRouterBMIB,
       "dmAdRtbInf": dmAdRtbInf,
       "rtbInfItfGprsTable": rtbInfItfGprsTable,
       "rtbInfItfGprsEntry": rtbInfItfGprsEntry,
       "rtbInfItfGprsDevNo": rtbInfItfGprsDevNo,
       "rtbInfItfGprsDevLocalId": rtbInfItfGprsDevLocalId,
       "rtbInfItfGprsSlotNo": rtbInfItfGprsSlotNo,
       "rtbInfItfGprsPortNo": rtbInfItfGprsPortNo,
       "rtbInfItfGprsTaInf": rtbInfItfGprsTaInf,
       "rtbInfItfGprsTaConf": rtbInfItfGprsTaConf,
       "rtbInfItfGprsTaSerial": rtbInfItfGprsTaSerial,
       "rtbInfItfGprsTaRegistry": rtbInfItfGprsTaRegistry,
       "rtbInfItfGprsSimCardInf": rtbInfItfGprsSimCardInf,
       "rtbInfItfGprsCellConn": rtbInfItfGprsCellConn,
       "rtbInfItfGprsCellsMon": rtbInfItfGprsCellsMon,
       "rtbInfItfGprsNetInf": rtbInfItfGprsNetInf,
       "dmAdRtbStatus": dmAdRtbStatus,
       "rtbStItfGenTable": rtbStItfGenTable,
       "rtbStItfGenEntry": rtbStItfGenEntry,
       "rtbStItfGenDevNo": rtbStItfGenDevNo,
       "rtbStItfGenDevLocalId": rtbStItfGenDevLocalId,
       "rtbStItfGenSlotNo": rtbStItfGenSlotNo,
       "rtbStItfGenPortNo": rtbStItfGenPortNo,
       "rtbStItfGenLink": rtbStItfGenLink,
       "rtbStItfGenIndex": rtbStItfGenIndex,
       "rtbStItfAddTable": rtbStItfAddTable,
       "rtbStItfAddEntry": rtbStItfAddEntry,
       "rtbStItfAddDevNo": rtbStItfAddDevNo,
       "rtbStItfAddDevLocalId": rtbStItfAddDevLocalId,
       "rtbStItfAddSlotNo": rtbStItfAddSlotNo,
       "rtbStItfAddPortNo": rtbStItfAddPortNo,
       "rtbStItfAddLocal": rtbStItfAddLocal,
       "rtbStItfAddRemote": rtbStItfAddRemote,
       "dmAdRtbPerformance": dmAdRtbPerformance,
       "rtbPerfHwStCpu": rtbPerfHwStCpu,
       "rtbPerfHwStMemory": rtbPerfHwStMemory,
       "rtbPerfItfTable": rtbPerfItfTable,
       "rtbPerfItfEntry": rtbPerfItfEntry,
       "rtbPerfItfIndex": rtbPerfItfIndex,
       "rtbPerfItfDescr": rtbPerfItfDescr,
       "rtbPerfItfOctets": rtbPerfItfOctets,
       "rtbPerfItfPkts": rtbPerfItfPkts,
       "rtbPerfItfCollisions": rtbPerfItfCollisions,
       "rtbPerfItfUtilization": rtbPerfItfUtilization,
       "rtbPerfItfDrop": rtbPerfItfDrop,
       "rtbPerfItfError": rtbPerfItfError,
       "rtbPerfItfRxDataRate": rtbPerfItfRxDataRate,
       "rtbPerfItfTxDataRate": rtbPerfItfTxDataRate,
       "rtbPerfItfRxDropRate": rtbPerfItfRxDropRate,
       "rtbPerfItfTxDropRate": rtbPerfItfTxDropRate,
       "rtbPerfQoSQueueTable": rtbPerfQoSQueueTable,
       "rtbPerfQoSQueueEntry": rtbPerfQoSQueueEntry,
       "rtbPerfQoSQueueIndex": rtbPerfQoSQueueIndex,
       "rtbPerfQoSQueueItfDescr": rtbPerfQoSQueueItfDescr,
       "rtbPerfQoSQueueMark": rtbPerfQoSQueueMark,
       "rtbPerfQoSQueueTxDataRate": rtbPerfQoSQueueTxDataRate,
       "rtbPerfQoSQueueTxPktDropRate": rtbPerfQoSQueueTxPktDropRate,
       "rtbPerfQoSQueueTrafficDescr": rtbPerfQoSQueueTrafficDescr,
       "rtbPerfQoSQueueClassName": rtbPerfQoSQueueClassName,
       "rtbPerfQoSQueuePriority": rtbPerfQoSQueuePriority,
       "rtbPerfQoSQueueMinRate": rtbPerfQoSQueueMinRate,
       "rtbPerfQoSQueueMaxRate": rtbPerfQoSQueueMaxRate,
       "rtbPerfQoSQueueDroppedBytes": rtbPerfQoSQueueDroppedBytes,
       "rtbPerfQoSQueueSentBytes": rtbPerfQoSQueueSentBytes,
       "rtbPerfQoSQueueEnqueuedBytes": rtbPerfQoSQueueEnqueuedBytes,
       "rtbPerfQoSQueueTxDataRateBits": rtbPerfQoSQueueTxDataRateBits,
       "rtbPerfQoSQueueDroppedPkts": rtbPerfQoSQueueDroppedPkts,
       "rtbPerfQoSQueueSentPkts": rtbPerfQoSQueueSentPkts,
       "dmAdRtbConfigCopy": dmAdRtbConfigCopy,
       "rtbConfigCopyProtocol": rtbConfigCopyProtocol,
       "rtbConfigCopyServerAddress": rtbConfigCopyServerAddress,
       "rtbConfigCopyFileName": rtbConfigCopyFileName,
       "rtbConfigCopyDestFileType": rtbConfigCopyDestFileType,
       "rtbConfigCopyInitTransfer": rtbConfigCopyInitTransfer,
       "rtbConfigCopyStatus": rtbConfigCopyStatus,
       "rtbConfigCopySave": rtbConfigCopySave,
       "rtbConfigCopyApplyType": rtbConfigCopyApplyType,
       "rtbConfigCopyFileFormat": rtbConfigCopyFileFormat,
       "rtbConfigCopyOpType": rtbConfigCopyOpType,
       "rtbConfigCopyUser": rtbConfigCopyUser,
       "rtbConfigCopyPassword": rtbConfigCopyPassword,
       "dmAdRtbLTE": dmAdRtbLTE,
       "rtbLTESignalStrength": rtbLTESignalStrength,
       "rtbLTEChannel": rtbLTEChannel,
       "rtbLTENeighborTable": rtbLTENeighborTable,
       "rtbLTENeighborEntry": rtbLTENeighborEntry,
       "rtbLTENeighborIndex": rtbLTENeighborIndex,
       "rtbLTENeighborIndexNeighbor": rtbLTENeighborIndexNeighbor,
       "rtbLTENeighborDescr": rtbLTENeighborDescr,
       "rtbLTENeighborRFChannelNumber": rtbLTENeighborRFChannelNumber,
       "rtbLTENeighborCellsTable": rtbLTENeighborCellsTable,
       "rtbLTENeighborCellsEntry": rtbLTENeighborCellsEntry,
       "rtbLTENeighborCellsIndex": rtbLTENeighborCellsIndex,
       "rtbLTENeighborCellsPhysicalCellID": rtbLTENeighborCellsPhysicalCellID,
       "rtbLTENeighborCellsRSRQ": rtbLTENeighborCellsRSRQ,
       "rtbLTENeighborCellsRSRP": rtbLTENeighborCellsRSRP,
       "rtbLTENeighborCellsRSSI": rtbLTENeighborCellsRSSI,
       "rtbLTENeighborCellsCellSelectionRXLevel": rtbLTENeighborCellsCellSelectionRXLevel,
       "rtbLTEConnectionStatus": rtbLTEConnectionStatus}
)
