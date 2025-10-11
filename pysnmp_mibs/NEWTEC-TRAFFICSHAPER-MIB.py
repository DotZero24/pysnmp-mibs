# SNMP MIB module (NEWTEC-TRAFFICSHAPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TRAFFICSHAPER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:07 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,
 NtcNetworkAddress) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable",
    "NtcNetworkAddress")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcTrafficShaper = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000)
)
if mibBuilder.loadTexts:
    ntcTrafficShaper.setRevisions(
        ("2017-07-10 12:00",
         "2014-09-09 09:00",
         "2014-09-04 12:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-07-05 06:00",
         "2013-05-22 06:00",
         "2013-01-08 12:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTrfShapeObjects_ObjectIdentity = ObjectIdentity
ntcTrfShapeObjects = _NtcTrfShapeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1)
)
if mibBuilder.loadTexts:
    ntcTrfShapeObjects.setStatus("current")


class _NtcTrfShEnable_Type(NtcEnable):
    """Custom type ntcTrfShEnable based on NtcEnable"""
    defaultValue = 0


_NtcTrfShEnable_Type.__name__ = "NtcEnable"
_NtcTrfShEnable_Object = MibScalar
ntcTrfShEnable = _NtcTrfShEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 1),
    _NtcTrfShEnable_Type()
)
ntcTrfShEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShEnable.setStatus("current")


class _NtcTrfShInputSelection_Type(Integer32):
    """Custom type ntcTrfShInputSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("data1", 1),
          ("data2", 2),
          ("data", 3))
    )


_NtcTrfShInputSelection_Type.__name__ = "Integer32"
_NtcTrfShInputSelection_Object = MibScalar
ntcTrfShInputSelection = _NtcTrfShInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 2),
    _NtcTrfShInputSelection_Type()
)
ntcTrfShInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShInputSelection.setStatus("current")
_NtcTrfShClassificationTable_Object = MibTable
ntcTrfShClassificationTable = _NtcTrfShClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3)
)
if mibBuilder.loadTexts:
    ntcTrfShClassificationTable.setStatus("current")
_NtcTrfShClassificationEntry_Object = MibTableRow
ntcTrfShClassificationEntry = _NtcTrfShClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1)
)
ntcTrfShClassificationEntry.setIndexNames(
    (0, "NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShClassificationInx"),
)
if mibBuilder.loadTexts:
    ntcTrfShClassificationEntry.setStatus("current")
_NtcTrfShClassificationInx_Type = Unsigned32
_NtcTrfShClassificationInx_Object = MibTableColumn
ntcTrfShClassificationInx = _NtcTrfShClassificationInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 1),
    _NtcTrfShClassificationInx_Type()
)
ntcTrfShClassificationInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTrfShClassificationInx.setStatus("current")


class _NtcTrfShapeClassifName_Type(DisplayString):
    """Custom type ntcTrfShapeClassifName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfShapeClassifName_Type.__name__ = "DisplayString"
_NtcTrfShapeClassifName_Object = MibTableColumn
ntcTrfShapeClassifName = _NtcTrfShapeClassifName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 2),
    _NtcTrfShapeClassifName_Type()
)
ntcTrfShapeClassifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeClassifName.setStatus("current")


class _NtcTrfShClassificationEnable_Type(NtcEnable):
    """Custom type ntcTrfShClassificationEnable based on NtcEnable"""
    defaultValue = 0


_NtcTrfShClassificationEnable_Type.__name__ = "NtcEnable"
_NtcTrfShClassificationEnable_Object = MibTableColumn
ntcTrfShClassificationEnable = _NtcTrfShClassificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 3),
    _NtcTrfShClassificationEnable_Type()
)
ntcTrfShClassificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShClassificationEnable.setStatus("current")


class _NtcTrfShapeUseNetwAddress_Type(Integer32):
    """Custom type ntcTrfShapeUseNetwAddress based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NtcTrfShapeUseNetwAddress_Type.__name__ = "Integer32"
_NtcTrfShapeUseNetwAddress_Object = MibTableColumn
ntcTrfShapeUseNetwAddress = _NtcTrfShapeUseNetwAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 4),
    _NtcTrfShapeUseNetwAddress_Type()
)
ntcTrfShapeUseNetwAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeUseNetwAddress.setStatus("current")


class _NtcTrfShapeNetwAddress_Type(NtcNetworkAddress):
    """Custom type ntcTrfShapeNetwAddress based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0/24")


_NtcTrfShapeNetwAddress_Type.__name__ = "NtcNetworkAddress"
_NtcTrfShapeNetwAddress_Object = MibTableColumn
ntcTrfShapeNetwAddress = _NtcTrfShapeNetwAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 5),
    _NtcTrfShapeNetwAddress_Type()
)
ntcTrfShapeNetwAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeNetwAddress.setStatus("current")


class _NtcTrfShapeExpr_Type(DisplayString):
    """Custom type ntcTrfShapeExpr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4000),
    )


_NtcTrfShapeExpr_Type.__name__ = "DisplayString"
_NtcTrfShapeExpr_Object = MibTableColumn
ntcTrfShapeExpr = _NtcTrfShapeExpr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 6),
    _NtcTrfShapeExpr_Type()
)
ntcTrfShapeExpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeExpr.setStatus("current")


class _NtcTrfShapeShapingNode_Type(DisplayString):
    """Custom type ntcTrfShapeShapingNode based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfShapeShapingNode_Type.__name__ = "DisplayString"
_NtcTrfShapeShapingNode_Object = MibTableColumn
ntcTrfShapeShapingNode = _NtcTrfShapeShapingNode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 3, 1, 7),
    _NtcTrfShapeShapingNode_Type()
)
ntcTrfShapeShapingNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeShapingNode.setStatus("current")
_NtcTrfShShapingNodeTable_Object = MibTable
ntcTrfShShapingNodeTable = _NtcTrfShShapingNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4)
)
if mibBuilder.loadTexts:
    ntcTrfShShapingNodeTable.setStatus("current")
_NtcTrfShShapingNodeEntry_Object = MibTableRow
ntcTrfShShapingNodeEntry = _NtcTrfShShapingNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1)
)
ntcTrfShShapingNodeEntry.setIndexNames(
    (0, "NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShShapingNodeInx"),
)
if mibBuilder.loadTexts:
    ntcTrfShShapingNodeEntry.setStatus("current")
_NtcTrfShShapingNodeInx_Type = Unsigned32
_NtcTrfShShapingNodeInx_Object = MibTableColumn
ntcTrfShShapingNodeInx = _NtcTrfShShapingNodeInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 1),
    _NtcTrfShShapingNodeInx_Type()
)
ntcTrfShShapingNodeInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTrfShShapingNodeInx.setStatus("current")


class _NtcTrfShapeNodeName_Type(DisplayString):
    """Custom type ntcTrfShapeNodeName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfShapeNodeName_Type.__name__ = "DisplayString"
_NtcTrfShapeNodeName_Object = MibTableColumn
ntcTrfShapeNodeName = _NtcTrfShapeNodeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 2),
    _NtcTrfShapeNodeName_Type()
)
ntcTrfShapeNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeName.setStatus("current")


class _NtcTrfShShapingNodeEnable_Type(NtcEnable):
    """Custom type ntcTrfShShapingNodeEnable based on NtcEnable"""
    defaultValue = 0


_NtcTrfShShapingNodeEnable_Type.__name__ = "NtcEnable"
_NtcTrfShShapingNodeEnable_Object = MibTableColumn
ntcTrfShShapingNodeEnable = _NtcTrfShShapingNodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 3),
    _NtcTrfShShapingNodeEnable_Type()
)
ntcTrfShShapingNodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShShapingNodeEnable.setStatus("current")


class _NtcTrfShapeParentName_Type(DisplayString):
    """Custom type ntcTrfShapeParentName based on DisplayString"""
    defaultValue = OctetString("Root")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfShapeParentName_Type.__name__ = "DisplayString"
_NtcTrfShapeParentName_Object = MibTableColumn
ntcTrfShapeParentName = _NtcTrfShapeParentName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 4),
    _NtcTrfShapeParentName_Type()
)
ntcTrfShapeParentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeParentName.setStatus("current")


class _NtcTrfShapeCir_Type(Unsigned32):
    """Custom type ntcTrfShapeCir based on Unsigned32"""
    defaultValue = 0


_NtcTrfShapeCir_Type.__name__ = "Unsigned32"
_NtcTrfShapeCir_Object = MibTableColumn
ntcTrfShapeCir = _NtcTrfShapeCir_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 5),
    _NtcTrfShapeCir_Type()
)
ntcTrfShapeCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeCir.setStatus("current")


class _NtcTrfShapePir_Type(Unsigned32):
    """Custom type ntcTrfShapePir based on Unsigned32"""
    defaultValue = 10000000


_NtcTrfShapePir_Type.__name__ = "Unsigned32"
_NtcTrfShapePir_Object = MibTableColumn
ntcTrfShapePir = _NtcTrfShapePir_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 6),
    _NtcTrfShapePir_Type()
)
ntcTrfShapePir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapePir.setStatus("current")


class _NtcTrfShapeDestChannel_Type(DisplayString):
    """Custom type ntcTrfShapeDestChannel based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcTrfShapeDestChannel_Type.__name__ = "DisplayString"
_NtcTrfShapeDestChannel_Object = MibTableColumn
ntcTrfShapeDestChannel = _NtcTrfShapeDestChannel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 7),
    _NtcTrfShapeDestChannel_Type()
)
ntcTrfShapeDestChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapeDestChannel.setStatus("current")


class _NtcTrfShapePrio_Type(Unsigned32):
    """Custom type ntcTrfShapePrio based on Unsigned32"""
    defaultValue = 50


_NtcTrfShapePrio_Type.__name__ = "Unsigned32"
_NtcTrfShapePrio_Object = MibTableColumn
ntcTrfShapePrio = _NtcTrfShapePrio_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 8),
    _NtcTrfShapePrio_Type()
)
ntcTrfShapePrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShapePrio.setStatus("current")


class _NtcTrfMaxQTime_Type(Unsigned32):
    """Custom type ntcTrfMaxQTime based on Unsigned32"""
    defaultValue = 100


_NtcTrfMaxQTime_Type.__name__ = "Unsigned32"
_NtcTrfMaxQTime_Object = MibTableColumn
ntcTrfMaxQTime = _NtcTrfMaxQTime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 4, 1, 9),
    _NtcTrfMaxQTime_Type()
)
ntcTrfMaxQTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfMaxQTime.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfMaxQTime.setUnits("ms")
_NtcTrfShMonitor_ObjectIdentity = ObjectIdentity
ntcTrfShMonitor = _NtcTrfShMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5)
)
if mibBuilder.loadTexts:
    ntcTrfShMonitor.setStatus("current")
_NtcTrfShMonFwdBytes_Type = Counter64
_NtcTrfShMonFwdBytes_Object = MibScalar
ntcTrfShMonFwdBytes = _NtcTrfShMonFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 1),
    _NtcTrfShMonFwdBytes_Type()
)
ntcTrfShMonFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShMonFwdBytes.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShMonFwdBytes.setUnits("bytes")
_NtcTrfShMonFwdPackets_Type = Counter64
_NtcTrfShMonFwdPackets_Object = MibScalar
ntcTrfShMonFwdPackets = _NtcTrfShMonFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 2),
    _NtcTrfShMonFwdPackets_Type()
)
ntcTrfShMonFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShMonFwdPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShMonFwdPackets.setUnits("packets")
_NtcTrfShMonDropBytes_Type = Counter64
_NtcTrfShMonDropBytes_Object = MibScalar
ntcTrfShMonDropBytes = _NtcTrfShMonDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 3),
    _NtcTrfShMonDropBytes_Type()
)
ntcTrfShMonDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShMonDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShMonDropBytes.setUnits("bytes")
_NtcTrfShMonDropPackets_Type = Counter64
_NtcTrfShMonDropPackets_Object = MibScalar
ntcTrfShMonDropPackets = _NtcTrfShMonDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 4),
    _NtcTrfShMonDropPackets_Type()
)
ntcTrfShMonDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShMonDropPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShMonDropPackets.setUnits("packets")
_NtcTrfShMonShapingNodeTable_Object = MibTable
ntcTrfShMonShapingNodeTable = _NtcTrfShMonShapingNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ntcTrfShMonShapingNodeTable.setStatus("current")
_NtcTrfShMonShapingNodeEntry_Object = MibTableRow
ntcTrfShMonShapingNodeEntry = _NtcTrfShMonShapingNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1)
)
ntcTrfShMonShapingNodeEntry.setIndexNames(
    (0, "NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonShapingNodeInx"),
)
if mibBuilder.loadTexts:
    ntcTrfShMonShapingNodeEntry.setStatus("current")
_NtcTrfShMonShapingNodeInx_Type = Unsigned32
_NtcTrfShMonShapingNodeInx_Object = MibTableColumn
ntcTrfShMonShapingNodeInx = _NtcTrfShMonShapingNodeInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 1),
    _NtcTrfShMonShapingNodeInx_Type()
)
ntcTrfShMonShapingNodeInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTrfShMonShapingNodeInx.setStatus("current")


class _NtcTrfMonShNodeName_Type(DisplayString):
    """Custom type ntcTrfMonShNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfMonShNodeName_Type.__name__ = "DisplayString"
_NtcTrfMonShNodeName_Object = MibTableColumn
ntcTrfMonShNodeName = _NtcTrfMonShNodeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 2),
    _NtcTrfMonShNodeName_Type()
)
ntcTrfMonShNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfMonShNodeName.setStatus("current")
_NtcTrfMonShNodeFwdByte_Type = Counter64
_NtcTrfMonShNodeFwdByte_Object = MibTableColumn
ntcTrfMonShNodeFwdByte = _NtcTrfMonShNodeFwdByte_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 3),
    _NtcTrfMonShNodeFwdByte_Type()
)
ntcTrfMonShNodeFwdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfMonShNodeFwdByte.setStatus("current")
_NtcTfrMonShNodeFwdPackets_Type = Counter64
_NtcTfrMonShNodeFwdPackets_Object = MibTableColumn
ntcTfrMonShNodeFwdPackets = _NtcTfrMonShNodeFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 4),
    _NtcTfrMonShNodeFwdPackets_Type()
)
ntcTfrMonShNodeFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTfrMonShNodeFwdPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcTfrMonShNodeFwdPackets.setUnits("packets")
_NtcTrfMonShNodeDropByt_Type = Counter64
_NtcTrfMonShNodeDropByt_Object = MibTableColumn
ntcTrfMonShNodeDropByt = _NtcTrfMonShNodeDropByt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 5),
    _NtcTrfMonShNodeDropByt_Type()
)
ntcTrfMonShNodeDropByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfMonShNodeDropByt.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfMonShNodeDropByt.setUnits("bytes")
_NtcTrfShapeNodeDropPackets_Type = Counter64
_NtcTrfShapeNodeDropPackets_Object = MibTableColumn
ntcTrfShapeNodeDropPackets = _NtcTrfShapeNodeDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 6),
    _NtcTrfShapeNodeDropPackets_Type()
)
ntcTrfShapeNodeDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeDropPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeDropPackets.setUnits("packets")
_NtcTrfShapeNodeAverageDelay_Type = Unsigned32
_NtcTrfShapeNodeAverageDelay_Object = MibTableColumn
ntcTrfShapeNodeAverageDelay = _NtcTrfShapeNodeAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 7),
    _NtcTrfShapeNodeAverageDelay_Type()
)
ntcTrfShapeNodeAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeAverageDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeAverageDelay.setUnits("ms")
_NtcTrfShapeNodeVolRate_Type = Counter64
_NtcTrfShapeNodeVolRate_Object = MibTableColumn
ntcTrfShapeNodeVolRate = _NtcTrfShapeNodeVolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 8),
    _NtcTrfShapeNodeVolRate_Type()
)
ntcTrfShapeNodeVolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeVolRate.setStatus("current")
_NtcTrfShapeNodeDropRate_Type = Counter64
_NtcTrfShapeNodeDropRate_Object = MibTableColumn
ntcTrfShapeNodeDropRate = _NtcTrfShapeNodeDropRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 9),
    _NtcTrfShapeNodeDropRate_Type()
)
ntcTrfShapeNodeDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeDropRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeDropRate.setUnits("bps")


class _NtcTrfShapeNodeVolUnit_Type(Integer32):
    """Custom type ntcTrfShapeNodeVolUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 0),
          ("symbols", 1))
    )


_NtcTrfShapeNodeVolUnit_Type.__name__ = "Integer32"
_NtcTrfShapeNodeVolUnit_Object = MibTableColumn
ntcTrfShapeNodeVolUnit = _NtcTrfShapeNodeVolUnit_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 5, 1, 10),
    _NtcTrfShapeNodeVolUnit_Type()
)
ntcTrfShapeNodeVolUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShapeNodeVolUnit.setStatus("current")


class _NtcTrfShMonReset_Type(Integer32):
    """Custom type ntcTrfShMonReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcTrfShMonReset_Type.__name__ = "Integer32"
_NtcTrfShMonReset_Object = MibScalar
ntcTrfShMonReset = _NtcTrfShMonReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 6),
    _NtcTrfShMonReset_Type()
)
ntcTrfShMonReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTrfShMonReset.setStatus("current")
_NtcTrfShMonFwdBitRate_Type = Counter64
_NtcTrfShMonFwdBitRate_Object = MibScalar
ntcTrfShMonFwdBitRate = _NtcTrfShMonFwdBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 5, 7),
    _NtcTrfShMonFwdBitRate_Type()
)
ntcTrfShMonFwdBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTrfShMonFwdBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfShMonFwdBitRate.setUnits("bps")
_NtcTrfShExtClassifTable_Object = MibTable
ntcTrfShExtClassifTable = _NtcTrfShExtClassifTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6)
)
if mibBuilder.loadTexts:
    ntcTrfShExtClassifTable.setStatus("current")
_NtcTrfShExtClassifEntry_Object = MibTableRow
ntcTrfShExtClassifEntry = _NtcTrfShExtClassifEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1)
)
ntcTrfShExtClassifEntry.setIndexNames(
    (0, "NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShExtClassifName"),
)
if mibBuilder.loadTexts:
    ntcTrfShExtClassifEntry.setStatus("current")


class _NtcTrfShExtClassifName_Type(DisplayString):
    """Custom type ntcTrfShExtClassifName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_NtcTrfShExtClassifName_Type.__name__ = "DisplayString"
_NtcTrfShExtClassifName_Object = MibTableColumn
ntcTrfShExtClassifName = _NtcTrfShExtClassifName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 1),
    _NtcTrfShExtClassifName_Type()
)
ntcTrfShExtClassifName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTrfShExtClassifName.setStatus("current")
_NtcTrfShExtClassifRowStatus_Type = RowStatus
_NtcTrfShExtClassifRowStatus_Object = MibTableColumn
ntcTrfShExtClassifRowStatus = _NtcTrfShExtClassifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 2),
    _NtcTrfShExtClassifRowStatus_Type()
)
ntcTrfShExtClassifRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShExtClassifRowStatus.setStatus("current")
_NtcTrfShExtClassifEnable_Type = NtcEnable
_NtcTrfShExtClassifEnable_Object = MibTableColumn
ntcTrfShExtClassifEnable = _NtcTrfShExtClassifEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 3),
    _NtcTrfShExtClassifEnable_Type()
)
ntcTrfShExtClassifEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShExtClassifEnable.setStatus("current")


class _NtcTrfShapeExtUseNetwAddr_Type(Integer32):
    """Custom type ntcTrfShapeExtUseNetwAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NtcTrfShapeExtUseNetwAddr_Type.__name__ = "Integer32"
_NtcTrfShapeExtUseNetwAddr_Object = MibTableColumn
ntcTrfShapeExtUseNetwAddr = _NtcTrfShapeExtUseNetwAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 4),
    _NtcTrfShapeExtUseNetwAddr_Type()
)
ntcTrfShapeExtUseNetwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtUseNetwAddr.setStatus("current")
_NtcTrfShapeExtNetwAddr_Type = NtcNetworkAddress
_NtcTrfShapeExtNetwAddr_Object = MibTableColumn
ntcTrfShapeExtNetwAddr = _NtcTrfShapeExtNetwAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 5),
    _NtcTrfShapeExtNetwAddr_Type()
)
ntcTrfShapeExtNetwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtNetwAddr.setStatus("current")


class _NtcTrfShapeExtExpr_Type(DisplayString):
    """Custom type ntcTrfShapeExtExpr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4000),
    )


_NtcTrfShapeExtExpr_Type.__name__ = "DisplayString"
_NtcTrfShapeExtExpr_Object = MibTableColumn
ntcTrfShapeExtExpr = _NtcTrfShapeExtExpr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 6),
    _NtcTrfShapeExtExpr_Type()
)
ntcTrfShapeExtExpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtExpr.setStatus("current")


class _NtcTrfShapeExtShapingNode_Type(DisplayString):
    """Custom type ntcTrfShapeExtShapingNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfShapeExtShapingNode_Type.__name__ = "DisplayString"
_NtcTrfShapeExtShapingNode_Object = MibTableColumn
ntcTrfShapeExtShapingNode = _NtcTrfShapeExtShapingNode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 7),
    _NtcTrfShapeExtShapingNode_Type()
)
ntcTrfShapeExtShapingNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtShapingNode.setStatus("current")


class _NtcTrfShapeExtMatchingOrder_Type(Unsigned32):
    """Custom type ntcTrfShapeExtMatchingOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_NtcTrfShapeExtMatchingOrder_Type.__name__ = "Unsigned32"
_NtcTrfShapeExtMatchingOrder_Object = MibTableColumn
ntcTrfShapeExtMatchingOrder = _NtcTrfShapeExtMatchingOrder_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 6, 1, 8),
    _NtcTrfShapeExtMatchingOrder_Type()
)
ntcTrfShapeExtMatchingOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtMatchingOrder.setStatus("current")
_NtcTrfShExtShapingNodeTable_Object = MibTable
ntcTrfShExtShapingNodeTable = _NtcTrfShExtShapingNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7)
)
if mibBuilder.loadTexts:
    ntcTrfShExtShapingNodeTable.setStatus("current")
_NtcTrfShExtShapingNodeEntry_Object = MibTableRow
ntcTrfShExtShapingNodeEntry = _NtcTrfShExtShapingNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1)
)
ntcTrfShExtShapingNodeEntry.setIndexNames(
    (0, "NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShExtShapingNodeName"),
)
if mibBuilder.loadTexts:
    ntcTrfShExtShapingNodeEntry.setStatus("current")


class _NtcTrfShExtShapingNodeName_Type(DisplayString):
    """Custom type ntcTrfShExtShapingNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_NtcTrfShExtShapingNodeName_Type.__name__ = "DisplayString"
_NtcTrfShExtShapingNodeName_Object = MibTableColumn
ntcTrfShExtShapingNodeName = _NtcTrfShExtShapingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 1),
    _NtcTrfShExtShapingNodeName_Type()
)
ntcTrfShExtShapingNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTrfShExtShapingNodeName.setStatus("current")
_NtcTrfShExtShapingNodeRowStatus_Type = RowStatus
_NtcTrfShExtShapingNodeRowStatus_Object = MibTableColumn
ntcTrfShExtShapingNodeRowStatus = _NtcTrfShExtShapingNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 2),
    _NtcTrfShExtShapingNodeRowStatus_Type()
)
ntcTrfShExtShapingNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShExtShapingNodeRowStatus.setStatus("current")
_NtcTrfShExtShapingNodeEnable_Type = NtcEnable
_NtcTrfShExtShapingNodeEnable_Object = MibTableColumn
ntcTrfShExtShapingNodeEnable = _NtcTrfShExtShapingNodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 3),
    _NtcTrfShExtShapingNodeEnable_Type()
)
ntcTrfShExtShapingNodeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShExtShapingNodeEnable.setStatus("current")


class _NtcTrfShapeExtParentNam_Type(DisplayString):
    """Custom type ntcTrfShapeExtParentNam based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTrfShapeExtParentNam_Type.__name__ = "DisplayString"
_NtcTrfShapeExtParentNam_Object = MibTableColumn
ntcTrfShapeExtParentNam = _NtcTrfShapeExtParentNam_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 4),
    _NtcTrfShapeExtParentNam_Type()
)
ntcTrfShapeExtParentNam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtParentNam.setStatus("current")
_NtcTrfShapeExtCir_Type = Unsigned32
_NtcTrfShapeExtCir_Object = MibTableColumn
ntcTrfShapeExtCir = _NtcTrfShapeExtCir_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 5),
    _NtcTrfShapeExtCir_Type()
)
ntcTrfShapeExtCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtCir.setStatus("current")
_NtcTrfShapeExtPir_Type = Unsigned32
_NtcTrfShapeExtPir_Object = MibTableColumn
ntcTrfShapeExtPir = _NtcTrfShapeExtPir_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 6),
    _NtcTrfShapeExtPir_Type()
)
ntcTrfShapeExtPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtPir.setStatus("current")


class _NtcTrfShapeExtDestChan_Type(DisplayString):
    """Custom type ntcTrfShapeExtDestChan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcTrfShapeExtDestChan_Type.__name__ = "DisplayString"
_NtcTrfShapeExtDestChan_Object = MibTableColumn
ntcTrfShapeExtDestChan = _NtcTrfShapeExtDestChan_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 7),
    _NtcTrfShapeExtDestChan_Type()
)
ntcTrfShapeExtDestChan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtDestChan.setStatus("current")
_NtcTrfShapeExtPrio_Type = Unsigned32
_NtcTrfShapeExtPrio_Object = MibTableColumn
ntcTrfShapeExtPrio = _NtcTrfShapeExtPrio_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 8),
    _NtcTrfShapeExtPrio_Type()
)
ntcTrfShapeExtPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeExtPrio.setStatus("current")
_NtcTrfMaxQTExtime_Type = Unsigned32
_NtcTrfMaxQTExtime_Object = MibTableColumn
ntcTrfMaxQTExtime = _NtcTrfMaxQTExtime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 9),
    _NtcTrfMaxQTExtime_Type()
)
ntcTrfMaxQTExtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfMaxQTExtime.setStatus("current")
if mibBuilder.loadTexts:
    ntcTrfMaxQTExtime.setUnits("ms")


class _NtcTrfShapeUnit_Type(Integer32):
    """Custom type ntcTrfShapeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bitrate", 0),
          ("symbolrate", 1))
    )


_NtcTrfShapeUnit_Type.__name__ = "Integer32"
_NtcTrfShapeUnit_Object = MibTableColumn
ntcTrfShapeUnit = _NtcTrfShapeUnit_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 1, 7, 1, 10),
    _NtcTrfShapeUnit_Type()
)
ntcTrfShapeUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTrfShapeUnit.setStatus("current")
_NtcTrfShapeConformance_ObjectIdentity = ObjectIdentity
ntcTrfShapeConformance = _NtcTrfShapeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 2)
)
if mibBuilder.loadTexts:
    ntcTrfShapeConformance.setStatus("current")
_NtcTrfShapeConfCompliance_ObjectIdentity = ObjectIdentity
ntcTrfShapeConfCompliance = _NtcTrfShapeConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTrfShapeConfCompliance.setStatus("current")
_NtcTrfShapeConfGroup_ObjectIdentity = ObjectIdentity
ntcTrfShapeConfGroup = _NtcTrfShapeConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTrfShapeConfGroup.setStatus("current")

# Managed Objects groups

ntcTrfShapeConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 2, 2, 1)
)
ntcTrfShapeConfGrpV1Standard.setObjects(
      *(("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShEnable"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShInputSelection"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeClassifName"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShClassificationEnable"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeUseNetwAddress"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNetwAddress"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExpr"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeShapingNode"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNodeName"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShShapingNodeEnable"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeParentName"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeCir"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapePir"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeDestChannel"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapePrio"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfMaxQTime"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonFwdBytes"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonFwdPackets"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonDropBytes"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonDropPackets"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfMonShNodeName"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfMonShNodeFwdByte"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTfrMonShNodeFwdPackets"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfMonShNodeDropByt"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNodeDropPackets"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNodeAverageDelay"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNodeVolRate"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNodeDropRate"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeNodeVolUnit"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonReset"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShMonFwdBitRate"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShExtClassifRowStatus"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShExtClassifEnable"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtUseNetwAddr"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtNetwAddr"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtExpr"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtShapingNode"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtMatchingOrder"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShExtShapingNodeRowStatus"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShExtShapingNodeEnable"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtParentNam"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtCir"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtPir"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtDestChan"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeExtPrio"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfMaxQTExtime"),
        ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeUnit"))
)
if mibBuilder.loadTexts:
    ntcTrfShapeConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTrfShapeConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2000, 2, 1, 1)
)
ntcTrfShapeConfCompV1Standard.setObjects(
    ("NEWTEC-TRAFFICSHAPER-MIB", "ntcTrfShapeConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTrfShapeConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TRAFFICSHAPER-MIB",
    **{"ntcTrafficShaper": ntcTrafficShaper,
       "ntcTrfShapeObjects": ntcTrfShapeObjects,
       "ntcTrfShEnable": ntcTrfShEnable,
       "ntcTrfShInputSelection": ntcTrfShInputSelection,
       "ntcTrfShClassificationTable": ntcTrfShClassificationTable,
       "ntcTrfShClassificationEntry": ntcTrfShClassificationEntry,
       "ntcTrfShClassificationInx": ntcTrfShClassificationInx,
       "ntcTrfShapeClassifName": ntcTrfShapeClassifName,
       "ntcTrfShClassificationEnable": ntcTrfShClassificationEnable,
       "ntcTrfShapeUseNetwAddress": ntcTrfShapeUseNetwAddress,
       "ntcTrfShapeNetwAddress": ntcTrfShapeNetwAddress,
       "ntcTrfShapeExpr": ntcTrfShapeExpr,
       "ntcTrfShapeShapingNode": ntcTrfShapeShapingNode,
       "ntcTrfShShapingNodeTable": ntcTrfShShapingNodeTable,
       "ntcTrfShShapingNodeEntry": ntcTrfShShapingNodeEntry,
       "ntcTrfShShapingNodeInx": ntcTrfShShapingNodeInx,
       "ntcTrfShapeNodeName": ntcTrfShapeNodeName,
       "ntcTrfShShapingNodeEnable": ntcTrfShShapingNodeEnable,
       "ntcTrfShapeParentName": ntcTrfShapeParentName,
       "ntcTrfShapeCir": ntcTrfShapeCir,
       "ntcTrfShapePir": ntcTrfShapePir,
       "ntcTrfShapeDestChannel": ntcTrfShapeDestChannel,
       "ntcTrfShapePrio": ntcTrfShapePrio,
       "ntcTrfMaxQTime": ntcTrfMaxQTime,
       "ntcTrfShMonitor": ntcTrfShMonitor,
       "ntcTrfShMonFwdBytes": ntcTrfShMonFwdBytes,
       "ntcTrfShMonFwdPackets": ntcTrfShMonFwdPackets,
       "ntcTrfShMonDropBytes": ntcTrfShMonDropBytes,
       "ntcTrfShMonDropPackets": ntcTrfShMonDropPackets,
       "ntcTrfShMonShapingNodeTable": ntcTrfShMonShapingNodeTable,
       "ntcTrfShMonShapingNodeEntry": ntcTrfShMonShapingNodeEntry,
       "ntcTrfShMonShapingNodeInx": ntcTrfShMonShapingNodeInx,
       "ntcTrfMonShNodeName": ntcTrfMonShNodeName,
       "ntcTrfMonShNodeFwdByte": ntcTrfMonShNodeFwdByte,
       "ntcTfrMonShNodeFwdPackets": ntcTfrMonShNodeFwdPackets,
       "ntcTrfMonShNodeDropByt": ntcTrfMonShNodeDropByt,
       "ntcTrfShapeNodeDropPackets": ntcTrfShapeNodeDropPackets,
       "ntcTrfShapeNodeAverageDelay": ntcTrfShapeNodeAverageDelay,
       "ntcTrfShapeNodeVolRate": ntcTrfShapeNodeVolRate,
       "ntcTrfShapeNodeDropRate": ntcTrfShapeNodeDropRate,
       "ntcTrfShapeNodeVolUnit": ntcTrfShapeNodeVolUnit,
       "ntcTrfShMonReset": ntcTrfShMonReset,
       "ntcTrfShMonFwdBitRate": ntcTrfShMonFwdBitRate,
       "ntcTrfShExtClassifTable": ntcTrfShExtClassifTable,
       "ntcTrfShExtClassifEntry": ntcTrfShExtClassifEntry,
       "ntcTrfShExtClassifName": ntcTrfShExtClassifName,
       "ntcTrfShExtClassifRowStatus": ntcTrfShExtClassifRowStatus,
       "ntcTrfShExtClassifEnable": ntcTrfShExtClassifEnable,
       "ntcTrfShapeExtUseNetwAddr": ntcTrfShapeExtUseNetwAddr,
       "ntcTrfShapeExtNetwAddr": ntcTrfShapeExtNetwAddr,
       "ntcTrfShapeExtExpr": ntcTrfShapeExtExpr,
       "ntcTrfShapeExtShapingNode": ntcTrfShapeExtShapingNode,
       "ntcTrfShapeExtMatchingOrder": ntcTrfShapeExtMatchingOrder,
       "ntcTrfShExtShapingNodeTable": ntcTrfShExtShapingNodeTable,
       "ntcTrfShExtShapingNodeEntry": ntcTrfShExtShapingNodeEntry,
       "ntcTrfShExtShapingNodeName": ntcTrfShExtShapingNodeName,
       "ntcTrfShExtShapingNodeRowStatus": ntcTrfShExtShapingNodeRowStatus,
       "ntcTrfShExtShapingNodeEnable": ntcTrfShExtShapingNodeEnable,
       "ntcTrfShapeExtParentNam": ntcTrfShapeExtParentNam,
       "ntcTrfShapeExtCir": ntcTrfShapeExtCir,
       "ntcTrfShapeExtPir": ntcTrfShapeExtPir,
       "ntcTrfShapeExtDestChan": ntcTrfShapeExtDestChan,
       "ntcTrfShapeExtPrio": ntcTrfShapeExtPrio,
       "ntcTrfMaxQTExtime": ntcTrfMaxQTExtime,
       "ntcTrfShapeUnit": ntcTrfShapeUnit,
       "ntcTrfShapeConformance": ntcTrfShapeConformance,
       "ntcTrfShapeConfCompliance": ntcTrfShapeConfCompliance,
       "ntcTrfShapeConfCompV1Standard": ntcTrfShapeConfCompV1Standard,
       "ntcTrfShapeConfGroup": ntcTrfShapeConfGroup,
       "ntcTrfShapeConfGrpV1Standard": ntcTrfShapeConfGrpV1Standard}
)
