# SNMP MIB module (H3C-WLANMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-WLANMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:09 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cWlanMt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157)
)
if mibBuilder.loadTexts:
    h3cWlanMt.setRevisions(
        ("2014-09-28 17:47",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cWlanMtVCpuInfoGroup_ObjectIdentity = ObjectIdentity
h3cWlanMtVCpuInfoGroup = _H3cWlanMtVCpuInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1)
)
_H3cWlanMtVCpuInfoTable_Object = MibTable
h3cWlanMtVCpuInfoTable = _H3cWlanMtVCpuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1)
)
if mibBuilder.loadTexts:
    h3cWlanMtVCpuInfoTable.setStatus("current")
_H3cWlanMtVCpuInfoEntry_Object = MibTableRow
h3cWlanMtVCpuInfoEntry = _H3cWlanMtVCpuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1, 1)
)
h3cWlanMtVCpuInfoEntry.setIndexNames(
    (0, "H3C-WLANMT-MIB", "h3cWlanMtVcpuID"),
)
if mibBuilder.loadTexts:
    h3cWlanMtVCpuInfoEntry.setStatus("current")


class _H3cWlanMtVcpuID_Type(Unsigned32):
    """Custom type h3cWlanMtVcpuID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cWlanMtVcpuID_Type.__name__ = "Unsigned32"
_H3cWlanMtVcpuID_Object = MibTableColumn
h3cWlanMtVcpuID = _H3cWlanMtVcpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1, 1, 1),
    _H3cWlanMtVcpuID_Type()
)
h3cWlanMtVcpuID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanMtVcpuID.setStatus("current")


class _H3cWlanMtVcpuUsage_Type(Unsigned32):
    """Custom type h3cWlanMtVcpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cWlanMtVcpuUsage_Type.__name__ = "Unsigned32"
_H3cWlanMtVcpuUsage_Object = MibTableColumn
h3cWlanMtVcpuUsage = _H3cWlanMtVcpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1, 1, 2),
    _H3cWlanMtVcpuUsage_Type()
)
h3cWlanMtVcpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWlanMtVcpuUsage.setStatus("current")
_H3cWlanMtVcpuRx_Type = Counter64
_H3cWlanMtVcpuRx_Object = MibTableColumn
h3cWlanMtVcpuRx = _H3cWlanMtVcpuRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1, 1, 3),
    _H3cWlanMtVcpuRx_Type()
)
h3cWlanMtVcpuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWlanMtVcpuRx.setStatus("current")
_H3cWlanMtVcpuTx_Type = Counter64
_H3cWlanMtVcpuTx_Object = MibTableColumn
h3cWlanMtVcpuTx = _H3cWlanMtVcpuTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1, 1, 4),
    _H3cWlanMtVcpuTx_Type()
)
h3cWlanMtVcpuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWlanMtVcpuTx.setStatus("current")
_H3cWlanMtVcpuDrop_Type = Counter64
_H3cWlanMtVcpuDrop_Object = MibTableColumn
h3cWlanMtVcpuDrop = _H3cWlanMtVcpuDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 1, 1, 1, 5),
    _H3cWlanMtVcpuDrop_Type()
)
h3cWlanMtVcpuDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWlanMtVcpuDrop.setStatus("current")
_H3cWlanMtFrameToCpu_ObjectIdentity = ObjectIdentity
h3cWlanMtFrameToCpu = _H3cWlanMtFrameToCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 2)
)
_H3cWlanMtToCpuTxFrameCnt_Type = Counter64
_H3cWlanMtToCpuTxFrameCnt_Object = MibScalar
h3cWlanMtToCpuTxFrameCnt = _H3cWlanMtToCpuTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 2, 1),
    _H3cWlanMtToCpuTxFrameCnt_Type()
)
h3cWlanMtToCpuTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWlanMtToCpuTxFrameCnt.setStatus("current")
_H3cWlanMtToCpuDropFrameCnt_Type = Counter64
_H3cWlanMtToCpuDropFrameCnt_Object = MibScalar
h3cWlanMtToCpuDropFrameCnt = _H3cWlanMtToCpuDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 157, 2, 2),
    _H3cWlanMtToCpuDropFrameCnt_Type()
)
h3cWlanMtToCpuDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWlanMtToCpuDropFrameCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-WLANMT-MIB",
    **{"h3cWlanMt": h3cWlanMt,
       "h3cWlanMtVCpuInfoGroup": h3cWlanMtVCpuInfoGroup,
       "h3cWlanMtVCpuInfoTable": h3cWlanMtVCpuInfoTable,
       "h3cWlanMtVCpuInfoEntry": h3cWlanMtVCpuInfoEntry,
       "h3cWlanMtVcpuID": h3cWlanMtVcpuID,
       "h3cWlanMtVcpuUsage": h3cWlanMtVcpuUsage,
       "h3cWlanMtVcpuRx": h3cWlanMtVcpuRx,
       "h3cWlanMtVcpuTx": h3cWlanMtVcpuTx,
       "h3cWlanMtVcpuDrop": h3cWlanMtVcpuDrop,
       "h3cWlanMtFrameToCpu": h3cWlanMtFrameToCpu,
       "h3cWlanMtToCpuTxFrameCnt": h3cWlanMtToCpuTxFrameCnt,
       "h3cWlanMtToCpuDropFrameCnt": h3cWlanMtToCpuDropFrameCnt}
)
