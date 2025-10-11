# SNMP MIB module (QTECH-WLAN-QOS-EXTRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-WLAN-QOS-EXTRA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:20 2025
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

(qtechApCfgRadioId,
 qtechApMacAddr,
 qtechApgWlanId,
 qtechStaMacAddr) = mibBuilder.importSymbols(
    "QTECH-AC-MGMT-MIB",
    "qtechApCfgRadioId",
    "qtechApMacAddr",
    "qtechApgWlanId",
    "qtechStaMacAddr")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechWlanQosExtraMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60)
)
if mibBuilder.loadTexts:
    qtechWlanQosExtraMib.setRevisions(
        ("2009-09-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWlanDeviceWMMObjects_ObjectIdentity = ObjectIdentity
qtechWlanDeviceWMMObjects = _QtechWlanDeviceWMMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 1)
)
_QtechWMMStatusTable_Object = MibTable
qtechWMMStatusTable = _QtechWMMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWMMStatusTable.setStatus("current")
_QtechWMMStatusEntry_Object = MibTableRow
qtechWMMStatusEntry = _QtechWMMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 1, 1, 1)
)
qtechWMMStatusEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
)
if mibBuilder.loadTexts:
    qtechWMMStatusEntry.setStatus("current")


class _QtechWMMStatus_Type(TruthValue):
    """Custom type qtechWMMStatus based on TruthValue"""
    defaultValue = 1


_QtechWMMStatus_Type.__name__ = "TruthValue"
_QtechWMMStatus_Object = MibTableColumn
qtechWMMStatus = _QtechWMMStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 1, 1, 1, 1),
    _QtechWMMStatus_Type()
)
qtechWMMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWMMStatus.setStatus("current")


class _QtechAPSDStatus_Type(TruthValue):
    """Custom type qtechAPSDStatus based on TruthValue"""
    defaultValue = 1


_QtechAPSDStatus_Type.__name__ = "TruthValue"
_QtechAPSDStatus_Object = MibTableColumn
qtechAPSDStatus = _QtechAPSDStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 1, 1, 1, 2),
    _QtechAPSDStatus_Type()
)
qtechAPSDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPSDStatus.setStatus("current")


class _QtechSMPSStatus_Type(TruthValue):
    """Custom type qtechSMPSStatus based on TruthValue"""
    defaultValue = 1


_QtechSMPSStatus_Type.__name__ = "TruthValue"
_QtechSMPSStatus_Object = MibTableColumn
qtechSMPSStatus = _QtechSMPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 1, 1, 1, 3),
    _QtechSMPSStatus_Type()
)
qtechSMPSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPSStatus.setStatus("current")
_QtechWlanDeviceEDCAObjects_ObjectIdentity = ObjectIdentity
qtechWlanDeviceEDCAObjects = _QtechWlanDeviceEDCAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2)
)
_Qtechdot11EDCATable_Object = MibTable
qtechdot11EDCATable = _Qtechdot11EDCATable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1)
)
if mibBuilder.loadTexts:
    qtechdot11EDCATable.setStatus("current")
_Qtechdot11EDCAEntry_Object = MibTableRow
qtechdot11EDCAEntry = _Qtechdot11EDCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1)
)
qtechdot11EDCAEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApCfgRadioId"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableIndex"),
)
if mibBuilder.loadTexts:
    qtechdot11EDCAEntry.setStatus("current")


class _Qtechdot11EDCATableIndex_Type(Integer32):
    """Custom type qtechdot11EDCATableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Qtechdot11EDCATableIndex_Type.__name__ = "Integer32"
_Qtechdot11EDCATableIndex_Object = MibTableColumn
qtechdot11EDCATableIndex = _Qtechdot11EDCATableIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 1),
    _Qtechdot11EDCATableIndex_Type()
)
qtechdot11EDCATableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechdot11EDCATableIndex.setStatus("current")


class _Qtechdot11EDCATableCWmin_Type(Integer32):
    """Custom type qtechdot11EDCATableCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Qtechdot11EDCATableCWmin_Type.__name__ = "Integer32"
_Qtechdot11EDCATableCWmin_Object = MibTableColumn
qtechdot11EDCATableCWmin = _Qtechdot11EDCATableCWmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 2),
    _Qtechdot11EDCATableCWmin_Type()
)
qtechdot11EDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11EDCATableCWmin.setStatus("current")


class _Qtechdot11EDCATableCWmax_Type(Integer32):
    """Custom type qtechdot11EDCATableCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Qtechdot11EDCATableCWmax_Type.__name__ = "Integer32"
_Qtechdot11EDCATableCWmax_Object = MibTableColumn
qtechdot11EDCATableCWmax = _Qtechdot11EDCATableCWmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 3),
    _Qtechdot11EDCATableCWmax_Type()
)
qtechdot11EDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11EDCATableCWmax.setStatus("current")


class _Qtechdot11EDCATableAIFSN_Type(Integer32):
    """Custom type qtechdot11EDCATableAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Qtechdot11EDCATableAIFSN_Type.__name__ = "Integer32"
_Qtechdot11EDCATableAIFSN_Object = MibTableColumn
qtechdot11EDCATableAIFSN = _Qtechdot11EDCATableAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 4),
    _Qtechdot11EDCATableAIFSN_Type()
)
qtechdot11EDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11EDCATableAIFSN.setStatus("current")


class _Qtechdot11EDCATableTXOPLimit_Type(Integer32):
    """Custom type qtechdot11EDCATableTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Qtechdot11EDCATableTXOPLimit_Type.__name__ = "Integer32"
_Qtechdot11EDCATableTXOPLimit_Object = MibTableColumn
qtechdot11EDCATableTXOPLimit = _Qtechdot11EDCATableTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 5),
    _Qtechdot11EDCATableTXOPLimit_Type()
)
qtechdot11EDCATableTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11EDCATableTXOPLimit.setStatus("current")


class _Qtechdot11EDCATableMSDULifetime_Type(Integer32):
    """Custom type qtechdot11EDCATableMSDULifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Qtechdot11EDCATableMSDULifetime_Type.__name__ = "Integer32"
_Qtechdot11EDCATableMSDULifetime_Object = MibTableColumn
qtechdot11EDCATableMSDULifetime = _Qtechdot11EDCATableMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 6),
    _Qtechdot11EDCATableMSDULifetime_Type()
)
qtechdot11EDCATableMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11EDCATableMSDULifetime.setStatus("current")
_Qtechdot11EDCATableMandatory_Type = TruthValue
_Qtechdot11EDCATableMandatory_Object = MibTableColumn
qtechdot11EDCATableMandatory = _Qtechdot11EDCATableMandatory_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 1, 1, 7),
    _Qtechdot11EDCATableMandatory_Type()
)
qtechdot11EDCATableMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11EDCATableMandatory.setStatus("current")
_Qtechdot11QAPEDCATable_Object = MibTable
qtechdot11QAPEDCATable = _Qtechdot11QAPEDCATable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2)
)
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATable.setStatus("current")
_Qtechdot11QAPEDCAEntry_Object = MibTableRow
qtechdot11QAPEDCAEntry = _Qtechdot11QAPEDCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1)
)
qtechdot11QAPEDCAEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApCfgRadioId"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    qtechdot11QAPEDCAEntry.setStatus("current")


class _Qtechdot11QAPEDCATableIndex_Type(Integer32):
    """Custom type qtechdot11QAPEDCATableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Qtechdot11QAPEDCATableIndex_Type.__name__ = "Integer32"
_Qtechdot11QAPEDCATableIndex_Object = MibTableColumn
qtechdot11QAPEDCATableIndex = _Qtechdot11QAPEDCATableIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 1),
    _Qtechdot11QAPEDCATableIndex_Type()
)
qtechdot11QAPEDCATableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableIndex.setStatus("current")


class _Qtechdot11QAPEDCATableCWmin_Type(Integer32):
    """Custom type qtechdot11QAPEDCATableCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Qtechdot11QAPEDCATableCWmin_Type.__name__ = "Integer32"
_Qtechdot11QAPEDCATableCWmin_Object = MibTableColumn
qtechdot11QAPEDCATableCWmin = _Qtechdot11QAPEDCATableCWmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 2),
    _Qtechdot11QAPEDCATableCWmin_Type()
)
qtechdot11QAPEDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableCWmin.setStatus("current")


class _Qtechdot11QAPEDCATableCWmax_Type(Integer32):
    """Custom type qtechdot11QAPEDCATableCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Qtechdot11QAPEDCATableCWmax_Type.__name__ = "Integer32"
_Qtechdot11QAPEDCATableCWmax_Object = MibTableColumn
qtechdot11QAPEDCATableCWmax = _Qtechdot11QAPEDCATableCWmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 3),
    _Qtechdot11QAPEDCATableCWmax_Type()
)
qtechdot11QAPEDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableCWmax.setStatus("current")


class _Qtechdot11QAPEDCATableAIFSN_Type(Integer32):
    """Custom type qtechdot11QAPEDCATableAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Qtechdot11QAPEDCATableAIFSN_Type.__name__ = "Integer32"
_Qtechdot11QAPEDCATableAIFSN_Object = MibTableColumn
qtechdot11QAPEDCATableAIFSN = _Qtechdot11QAPEDCATableAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 4),
    _Qtechdot11QAPEDCATableAIFSN_Type()
)
qtechdot11QAPEDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableAIFSN.setStatus("current")


class _Qtechdot11QAPEDCATableTXOPLimit_Type(Integer32):
    """Custom type qtechdot11QAPEDCATableTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Qtechdot11QAPEDCATableTXOPLimit_Type.__name__ = "Integer32"
_Qtechdot11QAPEDCATableTXOPLimit_Object = MibTableColumn
qtechdot11QAPEDCATableTXOPLimit = _Qtechdot11QAPEDCATableTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 5),
    _Qtechdot11QAPEDCATableTXOPLimit_Type()
)
qtechdot11QAPEDCATableTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableTXOPLimit.setStatus("current")


class _Qtechdot11QAPEDCATableMSDULifetime_Type(Integer32):
    """Custom type qtechdot11QAPEDCATableMSDULifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Qtechdot11QAPEDCATableMSDULifetime_Type.__name__ = "Integer32"
_Qtechdot11QAPEDCATableMSDULifetime_Object = MibTableColumn
qtechdot11QAPEDCATableMSDULifetime = _Qtechdot11QAPEDCATableMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 6),
    _Qtechdot11QAPEDCATableMSDULifetime_Type()
)
qtechdot11QAPEDCATableMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableMSDULifetime.setStatus("current")
_Qtechdot11QAPEDCATableMandatory_Type = TruthValue
_Qtechdot11QAPEDCATableMandatory_Object = MibTableColumn
qtechdot11QAPEDCATableMandatory = _Qtechdot11QAPEDCATableMandatory_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 2, 1, 7),
    _Qtechdot11QAPEDCATableMandatory_Type()
)
qtechdot11QAPEDCATableMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot11QAPEDCATableMandatory.setStatus("current")
_QtechWlanEDCATable_Object = MibTable
qtechWlanEDCATable = _QtechWlanEDCATable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 3)
)
if mibBuilder.loadTexts:
    qtechWlanEDCATable.setStatus("current")
_QtechEDCAStatusEntry_Object = MibTableRow
qtechEDCAStatusEntry = _QtechEDCAStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 3, 1)
)
qtechEDCAStatusEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApCfgRadioId"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    qtechEDCAStatusEntry.setStatus("current")


class _QtechQAPEDCAqueuedepth_Type(Integer32):
    """Custom type qtechQAPEDCAqueuedepth based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_QtechQAPEDCAqueuedepth_Type.__name__ = "Integer32"
_QtechQAPEDCAqueuedepth_Object = MibTableColumn
qtechQAPEDCAqueuedepth = _QtechQAPEDCAqueuedepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 3, 1, 1),
    _QtechQAPEDCAqueuedepth_Type()
)
qtechQAPEDCAqueuedepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQAPEDCAqueuedepth.setStatus("current")


class _QtechQAPEDCAcacPolicy_Type(Integer32):
    """Custom type qtechQAPEDCAcacPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nocac", 0),
          ("usernum-based", 1),
          ("channelutilization-based", 2))
    )


_QtechQAPEDCAcacPolicy_Type.__name__ = "Integer32"
_QtechQAPEDCAcacPolicy_Object = MibTableColumn
qtechQAPEDCAcacPolicy = _QtechQAPEDCAcacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 3, 1, 2),
    _QtechQAPEDCAcacPolicy_Type()
)
qtechQAPEDCAcacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQAPEDCAcacPolicy.setStatus("current")


class _QtechQAPEDCAcacParam_Type(Integer32):
    """Custom type qtechQAPEDCAcacParam based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechQAPEDCAcacParam_Type.__name__ = "Integer32"
_QtechQAPEDCAcacParam_Object = MibTableColumn
qtechQAPEDCAcacParam = _QtechQAPEDCAcacParam_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 2, 3, 1, 3),
    _QtechQAPEDCAcacParam_Type()
)
qtechQAPEDCAcacParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQAPEDCAcacParam.setStatus("current")
_QtechWlanDevicePrivMappingObjects_ObjectIdentity = ObjectIdentity
qtechWlanDevicePrivMappingObjects = _QtechWlanDevicePrivMappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3)
)
_QtechWlanDevicePrivMappingWlanDefaultObjects_ObjectIdentity = ObjectIdentity
qtechWlanDevicePrivMappingWlanDefaultObjects = _QtechWlanDevicePrivMappingWlanDefaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 1)
)
_QtechWlanDefaultACTable_Object = MibTable
qtechWlanDefaultACTable = _QtechWlanDefaultACTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWlanDefaultACTable.setStatus("current")
_QtechWlanDefaultACEntry_Object = MibTableRow
qtechWlanDefaultACEntry = _QtechWlanDefaultACEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 1, 1, 1)
)
qtechWlanDefaultACEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
)
if mibBuilder.loadTexts:
    qtechWlanDefaultACEntry.setStatus("current")
_QtechWlanDefualtACnum_Type = Integer32
_QtechWlanDefualtACnum_Object = MibTableColumn
qtechWlanDefualtACnum = _QtechWlanDefualtACnum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 1, 1, 1, 1),
    _QtechWlanDefualtACnum_Type()
)
qtechWlanDefualtACnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanDefualtACnum.setStatus("current")
_QtechWlanMaxstadot1ptag_Type = Integer32
_QtechWlanMaxstadot1ptag_Object = MibTableColumn
qtechWlanMaxstadot1ptag = _QtechWlanMaxstadot1ptag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 1, 1, 1, 2),
    _QtechWlanMaxstadot1ptag_Type()
)
qtechWlanMaxstadot1ptag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanMaxstadot1ptag.setStatus("current")
_QtechWlanDevicePrivMappingAPDefaultObjects_ObjectIdentity = ObjectIdentity
qtechWlanDevicePrivMappingAPDefaultObjects = _QtechWlanDevicePrivMappingAPDefaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2)
)
_QtechPrivMappingAPstatusTable_Object = MibTable
qtechPrivMappingAPstatusTable = _QtechPrivMappingAPstatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 1)
)
if mibBuilder.loadTexts:
    qtechPrivMappingAPstatusTable.setStatus("current")
_QtechAPdefaultStatusMappingEntry_Object = MibTableRow
qtechAPdefaultStatusMappingEntry = _QtechAPdefaultStatusMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 1, 1)
)
qtechAPdefaultStatusMappingEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechAPdefaultStatusMappingEntry.setStatus("current")


class _Qtechdot1pmappingstatus_Type(Integer32):
    """Custom type qtechdot1pmappingstatus based on Integer32"""
    defaultValue = 0


_Qtechdot1pmappingstatus_Type.__name__ = "Integer32"
_Qtechdot1pmappingstatus_Object = MibTableColumn
qtechdot1pmappingstatus = _Qtechdot1pmappingstatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 1, 1, 1),
    _Qtechdot1pmappingstatus_Type()
)
qtechdot1pmappingstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdot1pmappingstatus.setStatus("current")


class _Qtechdscpmappingstatus_Type(Integer32):
    """Custom type qtechdscpmappingstatus based on Integer32"""
    defaultValue = 0


_Qtechdscpmappingstatus_Type.__name__ = "Integer32"
_Qtechdscpmappingstatus_Object = MibTableColumn
qtechdscpmappingstatus = _Qtechdscpmappingstatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 1, 1, 2),
    _Qtechdscpmappingstatus_Type()
)
qtechdscpmappingstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechdscpmappingstatus.setStatus("current")
_QtechPrivMappingAPDefaultTable_Object = MibTable
qtechPrivMappingAPDefaultTable = _QtechPrivMappingAPDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 2)
)
if mibBuilder.loadTexts:
    qtechPrivMappingAPDefaultTable.setStatus("current")
_QtechPrivMappingAPDefaultEntry_Object = MibTableRow
qtechPrivMappingAPDefaultEntry = _QtechPrivMappingAPDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 2, 1)
)
qtechPrivMappingAPDefaultEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    qtechPrivMappingAPDefaultEntry.setStatus("current")


class _QtechAPdefaultDSCPTag_Type(Integer32):
    """Custom type qtechAPdefaultDSCPTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QtechAPdefaultDSCPTag_Type.__name__ = "Integer32"
_QtechAPdefaultDSCPTag_Object = MibTableColumn
qtechAPdefaultDSCPTag = _QtechAPdefaultDSCPTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 2, 1, 1),
    _QtechAPdefaultDSCPTag_Type()
)
qtechAPdefaultDSCPTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPdefaultDSCPTag.setStatus("current")
_QtechAPdefaultDot1pTag_Type = Integer32
_QtechAPdefaultDot1pTag_Object = MibTableColumn
qtechAPdefaultDot1pTag = _QtechAPdefaultDot1pTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 2, 2, 1, 2),
    _QtechAPdefaultDot1pTag_Type()
)
qtechAPdefaultDot1pTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPdefaultDot1pTag.setStatus("current")
_QtechWlanDevicePrivMappingTableObjects_ObjectIdentity = ObjectIdentity
qtechWlanDevicePrivMappingTableObjects = _QtechWlanDevicePrivMappingTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 3)
)
_QtechSVPMappingTable_Object = MibTable
qtechSVPMappingTable = _QtechSVPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 3, 1)
)
if mibBuilder.loadTexts:
    qtechSVPMappingTable.setStatus("current")
_QtechSVPMappingEntry_Object = MibTableRow
qtechSVPMappingEntry = _QtechSVPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 3, 1, 1)
)
qtechSVPMappingEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
)
if mibBuilder.loadTexts:
    qtechSVPMappingEntry.setStatus("current")


class _QtechSVPmappingStatus_Type(Integer32):
    """Custom type qtechSVPmappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_QtechSVPmappingStatus_Type.__name__ = "Integer32"
_QtechSVPmappingStatus_Object = MibTableColumn
qtechSVPmappingStatus = _QtechSVPmappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 3, 1, 1, 1),
    _QtechSVPmappingStatus_Type()
)
qtechSVPmappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSVPmappingStatus.setStatus("current")


class _QtechSVPmappingAC_Type(Integer32):
    """Custom type qtechSVPmappingAC based on Integer32"""
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
        *(("wmmvo", 1),
          ("wmmvi", 2),
          ("wmmbe", 3),
          ("wmmbk", 4))
    )


_QtechSVPmappingAC_Type.__name__ = "Integer32"
_QtechSVPmappingAC_Object = MibTableColumn
qtechSVPmappingAC = _QtechSVPmappingAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 3, 3, 1, 1, 2),
    _QtechSVPmappingAC_Type()
)
qtechSVPmappingAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSVPmappingAC.setStatus("current")
_QtechWlanDeviceRatelimitObjects_ObjectIdentity = ObjectIdentity
qtechWlanDeviceRatelimitObjects = _QtechWlanDeviceRatelimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4)
)
_QtechWlanRatelimitTable_Object = MibTable
qtechWlanRatelimitTable = _QtechWlanRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 1)
)
if mibBuilder.loadTexts:
    qtechWlanRatelimitTable.setStatus("current")
_QtechWlanRatelimitEntry_Object = MibTableRow
qtechWlanRatelimitEntry = _QtechWlanRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 1, 1)
)
qtechWlanRatelimitEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanRateLimitDirect"),
)
if mibBuilder.loadTexts:
    qtechWlanRatelimitEntry.setStatus("current")


class _QtechWlanRateLimitDirect_Type(Integer32):
    """Custom type qtechWlanRateLimitDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanRateLimitDirect_Type.__name__ = "Integer32"
_QtechWlanRateLimitDirect_Object = MibTableColumn
qtechWlanRateLimitDirect = _QtechWlanRateLimitDirect_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 1, 1, 1),
    _QtechWlanRateLimitDirect_Type()
)
qtechWlanRateLimitDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanRateLimitDirect.setStatus("current")


class _QtechWlanRatelimitStatus_Type(Integer32):
    """Custom type qtechWlanRatelimitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanRatelimitStatus_Type.__name__ = "Integer32"
_QtechWlanRatelimitStatus_Object = MibTableColumn
qtechWlanRatelimitStatus = _QtechWlanRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 1, 1, 2),
    _QtechWlanRatelimitStatus_Type()
)
qtechWlanRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanRatelimitStatus.setStatus("current")
_QtechWlanAverageRate_Type = Integer32
_QtechWlanAverageRate_Object = MibTableColumn
qtechWlanAverageRate = _QtechWlanAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 1, 1, 3),
    _QtechWlanAverageRate_Type()
)
qtechWlanAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanAverageRate.setStatus("current")
_QtechWlanBurstRate_Type = Integer32
_QtechWlanBurstRate_Object = MibTableColumn
qtechWlanBurstRate = _QtechWlanBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 1, 1, 4),
    _QtechWlanBurstRate_Type()
)
qtechWlanBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanBurstRate.setStatus("current")
_QtechAPRatelimitTable_Object = MibTable
qtechAPRatelimitTable = _QtechAPRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 2)
)
if mibBuilder.loadTexts:
    qtechAPRatelimitTable.setStatus("current")
_QtechAPRatelimitEntry_Object = MibTableRow
qtechAPRatelimitEntry = _QtechAPRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 2, 1)
)
qtechAPRatelimitEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPRateLimitDirect"),
)
if mibBuilder.loadTexts:
    qtechAPRatelimitEntry.setStatus("current")


class _QtechAPRateLimitDirect_Type(Integer32):
    """Custom type qtechAPRateLimitDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAPRateLimitDirect_Type.__name__ = "Integer32"
_QtechAPRateLimitDirect_Object = MibTableColumn
qtechAPRateLimitDirect = _QtechAPRateLimitDirect_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 2, 1, 1),
    _QtechAPRateLimitDirect_Type()
)
qtechAPRateLimitDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAPRateLimitDirect.setStatus("current")


class _QtechAPRatelimitStatus_Type(Integer32):
    """Custom type qtechAPRatelimitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAPRatelimitStatus_Type.__name__ = "Integer32"
_QtechAPRatelimitStatus_Object = MibTableColumn
qtechAPRatelimitStatus = _QtechAPRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 2, 1, 2),
    _QtechAPRatelimitStatus_Type()
)
qtechAPRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPRatelimitStatus.setStatus("current")
_QtechAPAverageRate_Type = Integer32
_QtechAPAverageRate_Object = MibTableColumn
qtechAPAverageRate = _QtechAPAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 2, 1, 3),
    _QtechAPAverageRate_Type()
)
qtechAPAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPAverageRate.setStatus("current")
_QtechAPBurstRate_Type = Integer32
_QtechAPBurstRate_Object = MibTableColumn
qtechAPBurstRate = _QtechAPBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 2, 1, 4),
    _QtechAPBurstRate_Type()
)
qtechAPBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPBurstRate.setStatus("current")
_QtechUserRatelimitTable_Object = MibTable
qtechUserRatelimitTable = _QtechUserRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 3)
)
if mibBuilder.loadTexts:
    qtechUserRatelimitTable.setStatus("current")
_QtechUserRatelimitEntry_Object = MibTableRow
qtechUserRatelimitEntry = _QtechUserRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 3, 1)
)
qtechUserRatelimitEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechStaMacAddr"),
    (0, "QTECH-WLAN-QOS-EXTRA-MIB", "qtechUserRateLimitDirect"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
)
if mibBuilder.loadTexts:
    qtechUserRatelimitEntry.setStatus("current")


class _QtechUserRateLimitDirect_Type(Integer32):
    """Custom type qtechUserRateLimitDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechUserRateLimitDirect_Type.__name__ = "Integer32"
_QtechUserRateLimitDirect_Object = MibTableColumn
qtechUserRateLimitDirect = _QtechUserRateLimitDirect_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 3, 1, 1),
    _QtechUserRateLimitDirect_Type()
)
qtechUserRateLimitDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechUserRateLimitDirect.setStatus("current")


class _QtechUserRatelimitStatus_Type(Integer32):
    """Custom type qtechUserRatelimitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechUserRatelimitStatus_Type.__name__ = "Integer32"
_QtechUserRatelimitStatus_Object = MibTableColumn
qtechUserRatelimitStatus = _QtechUserRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 3, 1, 2),
    _QtechUserRatelimitStatus_Type()
)
qtechUserRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUserRatelimitStatus.setStatus("current")
_QtechUserAverageRate_Type = Integer32
_QtechUserAverageRate_Object = MibTableColumn
qtechUserAverageRate = _QtechUserAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 3, 1, 3),
    _QtechUserAverageRate_Type()
)
qtechUserAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUserAverageRate.setStatus("current")
_QtechUserBurstRate_Type = Integer32
_QtechUserBurstRate_Object = MibTableColumn
qtechUserBurstRate = _QtechUserBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 4, 3, 1, 4),
    _QtechUserBurstRate_Type()
)
qtechUserBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUserBurstRate.setStatus("current")
_QtechWlanQosMIBConform_ObjectIdentity = ObjectIdentity
qtechWlanQosMIBConform = _QtechWlanQosMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5)
)
_QtechWlanQosMIBCompliances_ObjectIdentity = ObjectIdentity
qtechWlanQosMIBCompliances = _QtechWlanQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5, 1)
)
_QtechWlanQosMIBGroups_ObjectIdentity = ObjectIdentity
qtechWlanQosMIBGroups = _QtechWlanQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5, 2)
)

# Managed Objects groups

qtechWlanQosWMMEDCAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5, 2, 1)
)
qtechWlanQosWMMEDCAConfigGroup.setObjects(
      *(("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWMMStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPSDStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechSMPSStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechQAPEDCAqueuedepth"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechQAPEDCAcacPolicy"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechQAPEDCAcacParam"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanDefualtACnum"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanMaxstadot1ptag"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot1pmappingstatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdscpmappingstatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPdefaultDSCPTag"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPdefaultDot1pTag"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableCWmin"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableCWmax"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableAIFSN"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableTXOPLimit"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableMSDULifetime"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11EDCATableMandatory"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableCWmin"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableCWmax"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableAIFSN"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableTXOPLimit"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableMSDULifetime"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechdot11QAPEDCATableMandatory"))
)
if mibBuilder.loadTexts:
    qtechWlanQosWMMEDCAConfigGroup.setStatus("current")

qtechWlanQosRatelimitConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5, 2, 2)
)
qtechWlanQosRatelimitConfigGroup.setObjects(
      *(("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanRateLimitDirect"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanRatelimitStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanAverageRate"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanBurstRate"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPRatelimitStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPAverageRate"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechAPBurstRate"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechUserRatelimitStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechUserAverageRate"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechUserBurstRate"))
)
if mibBuilder.loadTexts:
    qtechWlanQosRatelimitConfigGroup.setStatus("current")

qtechWlanQosPriMappingonfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5, 2, 3)
)
qtechWlanQosPriMappingonfigGroup.setObjects(
      *(("QTECH-WLAN-QOS-EXTRA-MIB", "qtechSVPmappingStatus"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechSVPmappingAC"))
)
if mibBuilder.loadTexts:
    qtechWlanQosPriMappingonfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechWlanQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 60, 5, 1, 1)
)
qtechWlanQosMIBCompliance.setObjects(
      *(("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanQosWMMEDCAConfigGroup"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanQosRatelimitConfigGroup"),
        ("QTECH-WLAN-QOS-EXTRA-MIB", "qtechWlanQosPriMappingonfigGroup"))
)
if mibBuilder.loadTexts:
    qtechWlanQosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-WLAN-QOS-EXTRA-MIB",
    **{"qtechWlanQosExtraMib": qtechWlanQosExtraMib,
       "qtechWlanDeviceWMMObjects": qtechWlanDeviceWMMObjects,
       "qtechWMMStatusTable": qtechWMMStatusTable,
       "qtechWMMStatusEntry": qtechWMMStatusEntry,
       "qtechWMMStatus": qtechWMMStatus,
       "qtechAPSDStatus": qtechAPSDStatus,
       "qtechSMPSStatus": qtechSMPSStatus,
       "qtechWlanDeviceEDCAObjects": qtechWlanDeviceEDCAObjects,
       "qtechdot11EDCATable": qtechdot11EDCATable,
       "qtechdot11EDCAEntry": qtechdot11EDCAEntry,
       "qtechdot11EDCATableIndex": qtechdot11EDCATableIndex,
       "qtechdot11EDCATableCWmin": qtechdot11EDCATableCWmin,
       "qtechdot11EDCATableCWmax": qtechdot11EDCATableCWmax,
       "qtechdot11EDCATableAIFSN": qtechdot11EDCATableAIFSN,
       "qtechdot11EDCATableTXOPLimit": qtechdot11EDCATableTXOPLimit,
       "qtechdot11EDCATableMSDULifetime": qtechdot11EDCATableMSDULifetime,
       "qtechdot11EDCATableMandatory": qtechdot11EDCATableMandatory,
       "qtechdot11QAPEDCATable": qtechdot11QAPEDCATable,
       "qtechdot11QAPEDCAEntry": qtechdot11QAPEDCAEntry,
       "qtechdot11QAPEDCATableIndex": qtechdot11QAPEDCATableIndex,
       "qtechdot11QAPEDCATableCWmin": qtechdot11QAPEDCATableCWmin,
       "qtechdot11QAPEDCATableCWmax": qtechdot11QAPEDCATableCWmax,
       "qtechdot11QAPEDCATableAIFSN": qtechdot11QAPEDCATableAIFSN,
       "qtechdot11QAPEDCATableTXOPLimit": qtechdot11QAPEDCATableTXOPLimit,
       "qtechdot11QAPEDCATableMSDULifetime": qtechdot11QAPEDCATableMSDULifetime,
       "qtechdot11QAPEDCATableMandatory": qtechdot11QAPEDCATableMandatory,
       "qtechWlanEDCATable": qtechWlanEDCATable,
       "qtechEDCAStatusEntry": qtechEDCAStatusEntry,
       "qtechQAPEDCAqueuedepth": qtechQAPEDCAqueuedepth,
       "qtechQAPEDCAcacPolicy": qtechQAPEDCAcacPolicy,
       "qtechQAPEDCAcacParam": qtechQAPEDCAcacParam,
       "qtechWlanDevicePrivMappingObjects": qtechWlanDevicePrivMappingObjects,
       "qtechWlanDevicePrivMappingWlanDefaultObjects": qtechWlanDevicePrivMappingWlanDefaultObjects,
       "qtechWlanDefaultACTable": qtechWlanDefaultACTable,
       "qtechWlanDefaultACEntry": qtechWlanDefaultACEntry,
       "qtechWlanDefualtACnum": qtechWlanDefualtACnum,
       "qtechWlanMaxstadot1ptag": qtechWlanMaxstadot1ptag,
       "qtechWlanDevicePrivMappingAPDefaultObjects": qtechWlanDevicePrivMappingAPDefaultObjects,
       "qtechPrivMappingAPstatusTable": qtechPrivMappingAPstatusTable,
       "qtechAPdefaultStatusMappingEntry": qtechAPdefaultStatusMappingEntry,
       "qtechdot1pmappingstatus": qtechdot1pmappingstatus,
       "qtechdscpmappingstatus": qtechdscpmappingstatus,
       "qtechPrivMappingAPDefaultTable": qtechPrivMappingAPDefaultTable,
       "qtechPrivMappingAPDefaultEntry": qtechPrivMappingAPDefaultEntry,
       "qtechAPdefaultDSCPTag": qtechAPdefaultDSCPTag,
       "qtechAPdefaultDot1pTag": qtechAPdefaultDot1pTag,
       "qtechWlanDevicePrivMappingTableObjects": qtechWlanDevicePrivMappingTableObjects,
       "qtechSVPMappingTable": qtechSVPMappingTable,
       "qtechSVPMappingEntry": qtechSVPMappingEntry,
       "qtechSVPmappingStatus": qtechSVPmappingStatus,
       "qtechSVPmappingAC": qtechSVPmappingAC,
       "qtechWlanDeviceRatelimitObjects": qtechWlanDeviceRatelimitObjects,
       "qtechWlanRatelimitTable": qtechWlanRatelimitTable,
       "qtechWlanRatelimitEntry": qtechWlanRatelimitEntry,
       "qtechWlanRateLimitDirect": qtechWlanRateLimitDirect,
       "qtechWlanRatelimitStatus": qtechWlanRatelimitStatus,
       "qtechWlanAverageRate": qtechWlanAverageRate,
       "qtechWlanBurstRate": qtechWlanBurstRate,
       "qtechAPRatelimitTable": qtechAPRatelimitTable,
       "qtechAPRatelimitEntry": qtechAPRatelimitEntry,
       "qtechAPRateLimitDirect": qtechAPRateLimitDirect,
       "qtechAPRatelimitStatus": qtechAPRatelimitStatus,
       "qtechAPAverageRate": qtechAPAverageRate,
       "qtechAPBurstRate": qtechAPBurstRate,
       "qtechUserRatelimitTable": qtechUserRatelimitTable,
       "qtechUserRatelimitEntry": qtechUserRatelimitEntry,
       "qtechUserRateLimitDirect": qtechUserRateLimitDirect,
       "qtechUserRatelimitStatus": qtechUserRatelimitStatus,
       "qtechUserAverageRate": qtechUserAverageRate,
       "qtechUserBurstRate": qtechUserBurstRate,
       "qtechWlanQosMIBConform": qtechWlanQosMIBConform,
       "qtechWlanQosMIBCompliances": qtechWlanQosMIBCompliances,
       "qtechWlanQosMIBCompliance": qtechWlanQosMIBCompliance,
       "qtechWlanQosMIBGroups": qtechWlanQosMIBGroups,
       "qtechWlanQosWMMEDCAConfigGroup": qtechWlanQosWMMEDCAConfigGroup,
       "qtechWlanQosRatelimitConfigGroup": qtechWlanQosRatelimitConfigGroup,
       "qtechWlanQosPriMappingonfigGroup": qtechWlanQosPriMappingonfigGroup}
)
