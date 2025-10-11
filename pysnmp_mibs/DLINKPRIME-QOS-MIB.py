# SNMP MIB module (DLINKPRIME-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:10 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

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

dlinkPrimeQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13)
)
if mibBuilder.loadTexts:
    dlinkPrimeQosMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpQosMIBObjects_ObjectIdentity = ObjectIdentity
dpQosMIBObjects = _DpQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1)
)
_DpQosScheduling_ObjectIdentity = ObjectIdentity
dpQosScheduling = _DpQosScheduling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 1)
)
_DpQosSchedulingModeTable_Object = MibTable
dpQosSchedulingModeTable = _DpQosSchedulingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dpQosSchedulingModeTable.setStatus("current")
_DpQosSchedulingModeEntry_Object = MibTableRow
dpQosSchedulingModeEntry = _DpQosSchedulingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 1, 1, 1)
)
dpQosSchedulingModeEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dpQosSchedulingModeEntry.setStatus("current")


class _DpQosSchedulingMode_Type(Integer32):
    """Custom type dpQosSchedulingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2))
    )


_DpQosSchedulingMode_Type.__name__ = "Integer32"
_DpQosSchedulingMode_Object = MibTableColumn
dpQosSchedulingMode = _DpQosSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 1, 1, 1, 1),
    _DpQosSchedulingMode_Type()
)
dpQosSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpQosSchedulingMode.setStatus("current")
_DpQosBandwidthCtrl_ObjectIdentity = ObjectIdentity
dpQosBandwidthCtrl = _DpQosBandwidthCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 2)
)
_DpQosBandwidthCtrlTable_Object = MibTable
dpQosBandwidthCtrlTable = _DpQosBandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dpQosBandwidthCtrlTable.setStatus("current")
_DpQosBandwidthCtrlEntry_Object = MibTableRow
dpQosBandwidthCtrlEntry = _DpQosBandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 2, 1, 1)
)
dpQosBandwidthCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dpQosBandwidthCtrlEntry.setStatus("current")


class _DpQosBandwidthRxRate_Type(Integer32):
    """Custom type dpQosBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("limit_8Kbps", 2),
          ("limit_16Kbps", 3),
          ("limit_32Kbps", 4),
          ("limit_64Kbps", 5),
          ("limit_128Kbps", 6),
          ("limit_256Kbps", 7),
          ("limit_512Kbps", 8),
          ("limit_1Mbps", 9),
          ("limit_2Mbps", 10),
          ("limit_4Mbps", 11),
          ("limit_8Mbps", 12),
          ("limit_16Mbps", 13),
          ("limit_32Mbps", 14),
          ("limit_64Mbps", 15),
          ("limit_128Mbps", 16),
          ("limit_256Mbps", 17),
          ("limit_512Mbps", 18))
    )


_DpQosBandwidthRxRate_Type.__name__ = "Integer32"
_DpQosBandwidthRxRate_Object = MibTableColumn
dpQosBandwidthRxRate = _DpQosBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 2, 1, 1, 1),
    _DpQosBandwidthRxRate_Type()
)
dpQosBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpQosBandwidthRxRate.setStatus("current")


class _DpQosBandwidthTxRate_Type(Integer32):
    """Custom type dpQosBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("limit_16Kbps", 3),
          ("limit_32Kbps", 4),
          ("limit_64Kbps", 5),
          ("limit_128Kbps", 6),
          ("limit_256Kbps", 7),
          ("limit_512Kbps", 8),
          ("limit_1Mbps", 9),
          ("limit_2Mbps", 10),
          ("limit_4Mbps", 11),
          ("limit_8Mbps", 12),
          ("limit_16Mbps", 13),
          ("limit_32Mbps", 14),
          ("limit_64Mbps", 15),
          ("limit_128Mbps", 16),
          ("limit_256Mbps", 17),
          ("limit_512Mbps", 18))
    )


_DpQosBandwidthTxRate_Type.__name__ = "Integer32"
_DpQosBandwidthTxRate_Object = MibTableColumn
dpQosBandwidthTxRate = _DpQosBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 2, 1, 1, 2),
    _DpQosBandwidthTxRate_Type()
)
dpQosBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpQosBandwidthTxRate.setStatus("current")
_DpQosCosCfg_ObjectIdentity = ObjectIdentity
dpQosCosCfg = _DpQosCosCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 3)
)
_DpQosCosCfgTable_Object = MibTable
dpQosCosCfgTable = _DpQosCosCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dpQosCosCfgTable.setStatus("current")
_DpQosCosCfgEntry_Object = MibTableRow
dpQosCosCfgEntry = _DpQosCosCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 3, 1, 1)
)
dpQosCosCfgEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dpQosCosCfgEntry.setStatus("current")


class _DpQosCfgSetCos_Type(Integer32):
    """Custom type dpQosCfgSetCos based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_DpQosCfgSetCos_Type.__name__ = "Integer32"
_DpQosCfgSetCos_Object = MibTableColumn
dpQosCfgSetCos = _DpQosCfgSetCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 1, 3, 1, 1, 1),
    _DpQosCfgSetCos_Type()
)
dpQosCfgSetCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpQosCfgSetCos.setStatus("current")
_DpQosMIBConformance_ObjectIdentity = ObjectIdentity
dpQosMIBConformance = _DpQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2)
)
_DpQosCompliances_ObjectIdentity = ObjectIdentity
dpQosCompliances = _DpQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2, 1)
)
_DpQosGroups_ObjectIdentity = ObjectIdentity
dpQosGroups = _DpQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2, 2)
)

# Managed Objects groups

dpQosSchedulingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2, 2, 1)
)
dpQosSchedulingGroup.setObjects(
    ("DLINKPRIME-QOS-MIB", "dpQosSchedulingMode")
)
if mibBuilder.loadTexts:
    dpQosSchedulingGroup.setStatus("current")

dpQosPortBandwidthCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2, 2, 2)
)
dpQosPortBandwidthCtrlGroup.setObjects(
      *(("DLINKPRIME-QOS-MIB", "dpQosBandwidthRxRate"),
        ("DLINKPRIME-QOS-MIB", "dpQosBandwidthTxRate"))
)
if mibBuilder.loadTexts:
    dpQosPortBandwidthCtrlGroup.setStatus("current")

dpQosCoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2, 2, 3)
)
dpQosCoSGroup.setObjects(
    ("DLINKPRIME-QOS-MIB", "dpQosCfgSetCos")
)
if mibBuilder.loadTexts:
    dpQosCoSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 13, 2, 1, 1)
)
dpQosCompliance.setObjects(
      *(("DLINKPRIME-QOS-MIB", "dpQosSchedulingGroup"),
        ("DLINKPRIME-QOS-MIB", "dpQosPortBandwidthCtrlGroup"),
        ("DLINKPRIME-QOS-MIB", "dpQosCoSGroup"))
)
if mibBuilder.loadTexts:
    dpQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-QOS-MIB",
    **{"dlinkPrimeQosMIB": dlinkPrimeQosMIB,
       "dpQosMIBObjects": dpQosMIBObjects,
       "dpQosScheduling": dpQosScheduling,
       "dpQosSchedulingModeTable": dpQosSchedulingModeTable,
       "dpQosSchedulingModeEntry": dpQosSchedulingModeEntry,
       "dpQosSchedulingMode": dpQosSchedulingMode,
       "dpQosBandwidthCtrl": dpQosBandwidthCtrl,
       "dpQosBandwidthCtrlTable": dpQosBandwidthCtrlTable,
       "dpQosBandwidthCtrlEntry": dpQosBandwidthCtrlEntry,
       "dpQosBandwidthRxRate": dpQosBandwidthRxRate,
       "dpQosBandwidthTxRate": dpQosBandwidthTxRate,
       "dpQosCosCfg": dpQosCosCfg,
       "dpQosCosCfgTable": dpQosCosCfgTable,
       "dpQosCosCfgEntry": dpQosCosCfgEntry,
       "dpQosCfgSetCos": dpQosCfgSetCos,
       "dpQosMIBConformance": dpQosMIBConformance,
       "dpQosCompliances": dpQosCompliances,
       "dpQosCompliance": dpQosCompliance,
       "dpQosGroups": dpQosGroups,
       "dpQosSchedulingGroup": dpQosSchedulingGroup,
       "dpQosPortBandwidthCtrlGroup": dpQosPortBandwidthCtrlGroup,
       "dpQosCoSGroup": dpQosCoSGroup}
)
