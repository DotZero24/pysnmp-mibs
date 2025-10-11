# SNMP MIB module (ZTE-AN-QOS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-QOS3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:13 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnQos3Objects_ObjectIdentity = ObjectIdentity
zxAnQos3Objects = _ZxAnQos3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4)
)
_ZxAnQos3GlobalObjects_ObjectIdentity = ObjectIdentity
zxAnQos3GlobalObjects = _ZxAnQos3GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 1)
)


class _ZxAnQos3MgmtCapabilities_Type(Bits):
    """Custom type zxAnQos3MgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("supportQos3", 0),
          ("supportTrafficPrfType", 1),
          ("supportPvc2Queue", 2),
          ("supportTrafficColorMode", 3))
    )

_ZxAnQos3MgmtCapabilities_Type.__name__ = "Bits"
_ZxAnQos3MgmtCapabilities_Object = MibScalar
zxAnQos3MgmtCapabilities = _ZxAnQos3MgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 1, 1),
    _ZxAnQos3MgmtCapabilities_Type()
)
zxAnQos3MgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQos3MgmtCapabilities.setStatus("current")
_ZxAnQos3QueueGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnQos3QueueGlobalObjects = _ZxAnQos3QueueGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 1, 2)
)


class _ZxAnQosEthCosToQueue_Type(OctetString):
    """Custom type zxAnQosEthCosToQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosEthCosToQueue_Type.__name__ = "OctetString"
_ZxAnQosEthCosToQueue_Object = MibScalar
zxAnQosEthCosToQueue = _ZxAnQosEthCosToQueue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 1, 2, 1),
    _ZxAnQosEthCosToQueue_Type()
)
zxAnQosEthCosToQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosEthCosToQueue.setStatus("current")
_ZxAnQos3MappingProfile_ObjectIdentity = ObjectIdentity
zxAnQos3MappingProfile = _ZxAnQos3MappingProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2)
)
_ZxAnQos3CosRemarkProfileTable_Object = MibTable
zxAnQos3CosRemarkProfileTable = _ZxAnQos3CosRemarkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnQos3CosRemarkProfileTable.setStatus("current")
_ZxAnQos3CosRemarkProfileEntry_Object = MibTableRow
zxAnQos3CosRemarkProfileEntry = _ZxAnQos3CosRemarkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 1, 1)
)
zxAnQos3CosRemarkProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosCosToCosPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3CosRemarkProfileEntry.setStatus("current")


class _ZxAnQosCosToCosPrfName_Type(DisplayString):
    """Custom type zxAnQosCosToCosPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosCosToCosPrfName_Type.__name__ = "DisplayString"
_ZxAnQosCosToCosPrfName_Object = MibTableColumn
zxAnQosCosToCosPrfName = _ZxAnQosCosToCosPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 1, 1, 1),
    _ZxAnQosCosToCosPrfName_Type()
)
zxAnQosCosToCosPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosCosToCosPrfName.setStatus("current")


class _ZxAnQosCosToCos_Type(OctetString):
    """Custom type zxAnQosCosToCos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosCosToCos_Type.__name__ = "OctetString"
_ZxAnQosCosToCos_Object = MibTableColumn
zxAnQosCosToCos = _ZxAnQosCosToCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 1, 1, 2),
    _ZxAnQosCosToCos_Type()
)
zxAnQosCosToCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosCosToCos.setStatus("current")
_ZxAnQosCosToCosPrfRowStatus_Type = RowStatus
_ZxAnQosCosToCosPrfRowStatus_Object = MibTableColumn
zxAnQosCosToCosPrfRowStatus = _ZxAnQosCosToCosPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 1, 1, 20),
    _ZxAnQosCosToCosPrfRowStatus_Type()
)
zxAnQosCosToCosPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosCosToCosPrfRowStatus.setStatus("current")
_ZxAnQos3DscpRemarkProfileTable_Object = MibTable
zxAnQos3DscpRemarkProfileTable = _ZxAnQos3DscpRemarkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnQos3DscpRemarkProfileTable.setStatus("current")
_ZxAnQos3DscpRemarkProfileEntry_Object = MibTableRow
zxAnQos3DscpRemarkProfileEntry = _ZxAnQos3DscpRemarkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 2, 1)
)
zxAnQos3DscpRemarkProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosDscpToDscpPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3DscpRemarkProfileEntry.setStatus("current")


class _ZxAnQosDscpToDscpPrfName_Type(DisplayString):
    """Custom type zxAnQosDscpToDscpPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosDscpToDscpPrfName_Type.__name__ = "DisplayString"
_ZxAnQosDscpToDscpPrfName_Object = MibTableColumn
zxAnQosDscpToDscpPrfName = _ZxAnQosDscpToDscpPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 2, 1, 1),
    _ZxAnQosDscpToDscpPrfName_Type()
)
zxAnQosDscpToDscpPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosDscpToDscpPrfName.setStatus("current")


class _ZxAnQosDscpToDscp_Type(OctetString):
    """Custom type zxAnQosDscpToDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_ZxAnQosDscpToDscp_Type.__name__ = "OctetString"
_ZxAnQosDscpToDscp_Object = MibTableColumn
zxAnQosDscpToDscp = _ZxAnQosDscpToDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 2, 1, 2),
    _ZxAnQosDscpToDscp_Type()
)
zxAnQosDscpToDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosDscpToDscp.setStatus("current")
_ZxAnQosDscpToDscpPrfRowStatus_Type = RowStatus
_ZxAnQosDscpToDscpPrfRowStatus_Object = MibTableColumn
zxAnQosDscpToDscpPrfRowStatus = _ZxAnQosDscpToDscpPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 2, 1, 20),
    _ZxAnQosDscpToDscpPrfRowStatus_Type()
)
zxAnQosDscpToDscpPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosDscpToDscpPrfRowStatus.setStatus("current")
_ZxAnQos3Dscp2CosProfileTable_Object = MibTable
zxAnQos3Dscp2CosProfileTable = _ZxAnQos3Dscp2CosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnQos3Dscp2CosProfileTable.setStatus("current")
_ZxAnQos3Dscp2CosProfileEntry_Object = MibTableRow
zxAnQos3Dscp2CosProfileEntry = _ZxAnQos3Dscp2CosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 3, 1)
)
zxAnQos3Dscp2CosProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosDscpToCosPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3Dscp2CosProfileEntry.setStatus("current")


class _ZxAnQosDscpToCosPrfName_Type(DisplayString):
    """Custom type zxAnQosDscpToCosPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosDscpToCosPrfName_Type.__name__ = "DisplayString"
_ZxAnQosDscpToCosPrfName_Object = MibTableColumn
zxAnQosDscpToCosPrfName = _ZxAnQosDscpToCosPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 3, 1, 1),
    _ZxAnQosDscpToCosPrfName_Type()
)
zxAnQosDscpToCosPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosDscpToCosPrfName.setStatus("current")


class _ZxAnQosDscpToCos_Type(OctetString):
    """Custom type zxAnQosDscpToCos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_ZxAnQosDscpToCos_Type.__name__ = "OctetString"
_ZxAnQosDscpToCos_Object = MibTableColumn
zxAnQosDscpToCos = _ZxAnQosDscpToCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 3, 1, 2),
    _ZxAnQosDscpToCos_Type()
)
zxAnQosDscpToCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosDscpToCos.setStatus("current")
_ZxAnQosDscpToCosPrfRowStatus_Type = RowStatus
_ZxAnQosDscpToCosPrfRowStatus_Object = MibTableColumn
zxAnQosDscpToCosPrfRowStatus = _ZxAnQosDscpToCosPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 3, 1, 20),
    _ZxAnQosDscpToCosPrfRowStatus_Type()
)
zxAnQosDscpToCosPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosDscpToCosPrfRowStatus.setStatus("current")
_ZxAnQos3Dscp2DropProfileTable_Object = MibTable
zxAnQos3Dscp2DropProfileTable = _ZxAnQos3Dscp2DropProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnQos3Dscp2DropProfileTable.setStatus("current")
_ZxAnQos3Dscp2DropProfileEntry_Object = MibTableRow
zxAnQos3Dscp2DropProfileEntry = _ZxAnQos3Dscp2DropProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 4, 1)
)
zxAnQos3Dscp2DropProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosDscpToDropPrecedePrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3Dscp2DropProfileEntry.setStatus("current")


class _ZxAnQosDscpToDropPrecedePrfName_Type(DisplayString):
    """Custom type zxAnQosDscpToDropPrecedePrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosDscpToDropPrecedePrfName_Type.__name__ = "DisplayString"
_ZxAnQosDscpToDropPrecedePrfName_Object = MibTableColumn
zxAnQosDscpToDropPrecedePrfName = _ZxAnQosDscpToDropPrecedePrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 4, 1, 1),
    _ZxAnQosDscpToDropPrecedePrfName_Type()
)
zxAnQosDscpToDropPrecedePrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosDscpToDropPrecedePrfName.setStatus("current")


class _ZxAnQosDscpToDropPrecedence_Type(OctetString):
    """Custom type zxAnQosDscpToDropPrecedence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_ZxAnQosDscpToDropPrecedence_Type.__name__ = "OctetString"
_ZxAnQosDscpToDropPrecedence_Object = MibTableColumn
zxAnQosDscpToDropPrecedence = _ZxAnQosDscpToDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 4, 1, 2),
    _ZxAnQosDscpToDropPrecedence_Type()
)
zxAnQosDscpToDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosDscpToDropPrecedence.setStatus("current")
_ZxAnQosDscpToDropPrePrfRowStatus_Type = RowStatus
_ZxAnQosDscpToDropPrePrfRowStatus_Object = MibTableColumn
zxAnQosDscpToDropPrePrfRowStatus = _ZxAnQosDscpToDropPrePrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 4, 1, 20),
    _ZxAnQosDscpToDropPrePrfRowStatus_Type()
)
zxAnQosDscpToDropPrePrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosDscpToDropPrePrfRowStatus.setStatus("current")
_ZxAnQos3MplsTc2CosProfileTable_Object = MibTable
zxAnQos3MplsTc2CosProfileTable = _ZxAnQos3MplsTc2CosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnQos3MplsTc2CosProfileTable.setStatus("current")
_ZxAnQos3MplsTc2CosProfileEntry_Object = MibTableRow
zxAnQos3MplsTc2CosProfileEntry = _ZxAnQos3MplsTc2CosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 5, 1)
)
zxAnQos3MplsTc2CosProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosMplsTcToCosPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3MplsTc2CosProfileEntry.setStatus("current")


class _ZxAnQosMplsTcToCosPrfName_Type(DisplayString):
    """Custom type zxAnQosMplsTcToCosPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosMplsTcToCosPrfName_Type.__name__ = "DisplayString"
_ZxAnQosMplsTcToCosPrfName_Object = MibTableColumn
zxAnQosMplsTcToCosPrfName = _ZxAnQosMplsTcToCosPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 5, 1, 1),
    _ZxAnQosMplsTcToCosPrfName_Type()
)
zxAnQosMplsTcToCosPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosMplsTcToCosPrfName.setStatus("current")


class _ZxAnQosMplsTcToCos_Type(OctetString):
    """Custom type zxAnQosMplsTcToCos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosMplsTcToCos_Type.__name__ = "OctetString"
_ZxAnQosMplsTcToCos_Object = MibTableColumn
zxAnQosMplsTcToCos = _ZxAnQosMplsTcToCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 5, 1, 2),
    _ZxAnQosMplsTcToCos_Type()
)
zxAnQosMplsTcToCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosMplsTcToCos.setStatus("current")
_ZxAnQosMplsTcToCosPrfRowStatus_Type = RowStatus
_ZxAnQosMplsTcToCosPrfRowStatus_Object = MibTableColumn
zxAnQosMplsTcToCosPrfRowStatus = _ZxAnQosMplsTcToCosPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 5, 1, 20),
    _ZxAnQosMplsTcToCosPrfRowStatus_Type()
)
zxAnQosMplsTcToCosPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosMplsTcToCosPrfRowStatus.setStatus("current")
_ZxAnQos3Cos2MplsTcProfileTable_Object = MibTable
zxAnQos3Cos2MplsTcProfileTable = _ZxAnQos3Cos2MplsTcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnQos3Cos2MplsTcProfileTable.setStatus("current")
_ZxAnQos3Cos2MplsTcProfileEntry_Object = MibTableRow
zxAnQos3Cos2MplsTcProfileEntry = _ZxAnQos3Cos2MplsTcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 6, 1)
)
zxAnQos3Cos2MplsTcProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosCosToMplsTcPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3Cos2MplsTcProfileEntry.setStatus("current")


class _ZxAnQosCosToMplsTcPrfName_Type(DisplayString):
    """Custom type zxAnQosCosToMplsTcPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosCosToMplsTcPrfName_Type.__name__ = "DisplayString"
_ZxAnQosCosToMplsTcPrfName_Object = MibTableColumn
zxAnQosCosToMplsTcPrfName = _ZxAnQosCosToMplsTcPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 6, 1, 1),
    _ZxAnQosCosToMplsTcPrfName_Type()
)
zxAnQosCosToMplsTcPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosCosToMplsTcPrfName.setStatus("current")


class _ZxAnQosCosToMplsTc_Type(OctetString):
    """Custom type zxAnQosCosToMplsTc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosCosToMplsTc_Type.__name__ = "OctetString"
_ZxAnQosCosToMplsTc_Object = MibTableColumn
zxAnQosCosToMplsTc = _ZxAnQosCosToMplsTc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 6, 1, 2),
    _ZxAnQosCosToMplsTc_Type()
)
zxAnQosCosToMplsTc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosCosToMplsTc.setStatus("current")
_ZxAnQosCosToMplsTcPrfRowStatus_Type = RowStatus
_ZxAnQosCosToMplsTcPrfRowStatus_Object = MibTableColumn
zxAnQosCosToMplsTcPrfRowStatus = _ZxAnQosCosToMplsTcPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 2, 6, 1, 20),
    _ZxAnQosCosToMplsTcPrfRowStatus_Type()
)
zxAnQosCosToMplsTcPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosCosToMplsTcPrfRowStatus.setStatus("current")
_ZxAnQos3PortConfig_ObjectIdentity = ObjectIdentity
zxAnQos3PortConfig = _ZxAnQos3PortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3)
)
_ZxAnQos3PortConfigTable_Object = MibTable
zxAnQos3PortConfigTable = _ZxAnQos3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnQos3PortConfigTable.setStatus("current")
_ZxAnQos3PortConfigEntry_Object = MibTableRow
zxAnQos3PortConfigEntry = _ZxAnQos3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1)
)
zxAnQos3PortConfigEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Rack"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Shelf"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Slot"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Port"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Onu"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3VCircuitType"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3LogicalId"),
)
if mibBuilder.loadTexts:
    zxAnQos3PortConfigEntry.setStatus("current")
_ZxAnQos3Rack_Type = Integer32
_ZxAnQos3Rack_Object = MibTableColumn
zxAnQos3Rack = _ZxAnQos3Rack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 1),
    _ZxAnQos3Rack_Type()
)
zxAnQos3Rack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3Rack.setStatus("current")
_ZxAnQos3Shelf_Type = Integer32
_ZxAnQos3Shelf_Object = MibTableColumn
zxAnQos3Shelf = _ZxAnQos3Shelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 2),
    _ZxAnQos3Shelf_Type()
)
zxAnQos3Shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3Shelf.setStatus("current")
_ZxAnQos3Slot_Type = Integer32
_ZxAnQos3Slot_Object = MibTableColumn
zxAnQos3Slot = _ZxAnQos3Slot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 3),
    _ZxAnQos3Slot_Type()
)
zxAnQos3Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3Slot.setStatus("current")
_ZxAnQos3Port_Type = Integer32
_ZxAnQos3Port_Object = MibTableColumn
zxAnQos3Port = _ZxAnQos3Port_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 4),
    _ZxAnQos3Port_Type()
)
zxAnQos3Port.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3Port.setStatus("current")
_ZxAnQos3Onu_Type = Integer32
_ZxAnQos3Onu_Object = MibTableColumn
zxAnQos3Onu = _ZxAnQos3Onu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 5),
    _ZxAnQos3Onu_Type()
)
zxAnQos3Onu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3Onu.setStatus("current")


class _ZxAnQos3VCircuitType_Type(Integer32):
    """Custom type zxAnQos3VCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("eponOnu", 3),
          ("gpon", 4),
          ("servicePort", 11),
          ("vlan", 12),
          ("queue", 13))
    )


_ZxAnQos3VCircuitType_Type.__name__ = "Integer32"
_ZxAnQos3VCircuitType_Object = MibTableColumn
zxAnQos3VCircuitType = _ZxAnQos3VCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 6),
    _ZxAnQos3VCircuitType_Type()
)
zxAnQos3VCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3VCircuitType.setStatus("current")
_ZxAnQos3LogicalId_Type = ObjectIdentifier
_ZxAnQos3LogicalId_Object = MibTableColumn
zxAnQos3LogicalId = _ZxAnQos3LogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 7),
    _ZxAnQos3LogicalId_Type()
)
zxAnQos3LogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQos3LogicalId.setStatus("current")


class _ZxAnQosIfRateLimit_Type(Integer32):
    """Custom type zxAnQosIfRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 10000000),
    )


_ZxAnQosIfRateLimit_Type.__name__ = "Integer32"
_ZxAnQosIfRateLimit_Object = MibTableColumn
zxAnQosIfRateLimit = _ZxAnQosIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 8),
    _ZxAnQosIfRateLimit_Type()
)
zxAnQosIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIfRateLimit.setUnits("kbps")


class _ZxAnQosIfBucketSize_Type(Integer32):
    """Custom type zxAnQosIfBucketSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 16000),
    )


_ZxAnQosIfBucketSize_Type.__name__ = "Integer32"
_ZxAnQosIfBucketSize_Object = MibTableColumn
zxAnQosIfBucketSize = _ZxAnQosIfBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 9),
    _ZxAnQosIfBucketSize_Type()
)
zxAnQosIfBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfBucketSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIfBucketSize.setUnits("kbytes")


class _ZxAnQosIfTrustMode_Type(Integer32):
    """Custom type zxAnQosIfTrustMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 2))
    )


_ZxAnQosIfTrustMode_Type.__name__ = "Integer32"
_ZxAnQosIfTrustMode_Object = MibTableColumn
zxAnQosIfTrustMode = _ZxAnQosIfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 10),
    _ZxAnQosIfTrustMode_Type()
)
zxAnQosIfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfTrustMode.setStatus("current")


class _ZxAnQosIfDefaultCos_Type(Integer32):
    """Custom type zxAnQosIfDefaultCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosIfDefaultCos_Type.__name__ = "Integer32"
_ZxAnQosIfDefaultCos_Object = MibTableColumn
zxAnQosIfDefaultCos = _ZxAnQosIfDefaultCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 11),
    _ZxAnQosIfDefaultCos_Type()
)
zxAnQosIfDefaultCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfDefaultCos.setStatus("current")


class _ZxAnQosIfDscpToCosPrf_Type(DisplayString):
    """Custom type zxAnQosIfDscpToCosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIfDscpToCosPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfDscpToCosPrf_Object = MibTableColumn
zxAnQosIfDscpToCosPrf = _ZxAnQosIfDscpToCosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 12),
    _ZxAnQosIfDscpToCosPrf_Type()
)
zxAnQosIfDscpToCosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfDscpToCosPrf.setStatus("current")


class _ZxAnQosIfDscpToDropPrecedencePrf_Type(DisplayString):
    """Custom type zxAnQosIfDscpToDropPrecedencePrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfDscpToDropPrecedencePrf_Type.__name__ = "DisplayString"
_ZxAnQosIfDscpToDropPrecedencePrf_Object = MibTableColumn
zxAnQosIfDscpToDropPrecedencePrf = _ZxAnQosIfDscpToDropPrecedencePrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 13),
    _ZxAnQosIfDscpToDropPrecedencePrf_Type()
)
zxAnQosIfDscpToDropPrecedencePrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfDscpToDropPrecedencePrf.setStatus("current")


class _ZxAnQosIfDscpToDscpPrf_Type(DisplayString):
    """Custom type zxAnQosIfDscpToDscpPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfDscpToDscpPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfDscpToDscpPrf_Object = MibTableColumn
zxAnQosIfDscpToDscpPrf = _ZxAnQosIfDscpToDscpPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 14),
    _ZxAnQosIfDscpToDscpPrf_Type()
)
zxAnQosIfDscpToDscpPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfDscpToDscpPrf.setStatus("current")


class _ZxAnQosIfIngressRateLimit_Type(Integer32):
    """Custom type zxAnQosIfIngressRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 10000000),
    )


_ZxAnQosIfIngressRateLimit_Type.__name__ = "Integer32"
_ZxAnQosIfIngressRateLimit_Object = MibTableColumn
zxAnQosIfIngressRateLimit = _ZxAnQosIfIngressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 15),
    _ZxAnQosIfIngressRateLimit_Type()
)
zxAnQosIfIngressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfIngressRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIfIngressRateLimit.setUnits("kbps")


class _ZxAnQosIfIngressBucketSize_Type(Integer32):
    """Custom type zxAnQosIfIngressBucketSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 16000),
    )


_ZxAnQosIfIngressBucketSize_Type.__name__ = "Integer32"
_ZxAnQosIfIngressBucketSize_Object = MibTableColumn
zxAnQosIfIngressBucketSize = _ZxAnQosIfIngressBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 3, 1, 1, 16),
    _ZxAnQosIfIngressBucketSize_Type()
)
zxAnQosIfIngressBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfIngressBucketSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIfIngressBucketSize.setUnits("kbytes")
_ZxAnQos3VPortConfig_ObjectIdentity = ObjectIdentity
zxAnQos3VPortConfig = _ZxAnQos3VPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4)
)
_ZxAnQos3VPortConfigTable_Object = MibTable
zxAnQos3VPortConfigTable = _ZxAnQos3VPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnQos3VPortConfigTable.setStatus("current")
_ZxAnQos3VPortConfigEntry_Object = MibTableRow
zxAnQos3VPortConfigEntry = _ZxAnQos3VPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1)
)
zxAnQos3VPortConfigEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Rack"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Shelf"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Slot"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Port"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Onu"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3VCircuitType"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3LogicalId"),
)
if mibBuilder.loadTexts:
    zxAnQos3VPortConfigEntry.setStatus("current")


class _ZxAnQosIfCosFilter_Type(Integer32):
    """Custom type zxAnQosIfCosFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notSupport", 255))
    )


_ZxAnQosIfCosFilter_Type.__name__ = "Integer32"
_ZxAnQosIfCosFilter_Object = MibTableColumn
zxAnQosIfCosFilter = _ZxAnQosIfCosFilter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 1),
    _ZxAnQosIfCosFilter_Type()
)
zxAnQosIfCosFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfCosFilter.setStatus("current")


class _ZxAnQos3IngressCosMarkMode_Type(Integer32):
    """Custom type zxAnQos3IngressCosMarkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("override", 2),
          ("cosRemark", 3),
          ("dscpToCos", 4),
          ("notSupport", 255))
    )


_ZxAnQos3IngressCosMarkMode_Type.__name__ = "Integer32"
_ZxAnQos3IngressCosMarkMode_Object = MibTableColumn
zxAnQos3IngressCosMarkMode = _ZxAnQos3IngressCosMarkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 2),
    _ZxAnQos3IngressCosMarkMode_Type()
)
zxAnQos3IngressCosMarkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3IngressCosMarkMode.setStatus("current")


class _ZxAnQos3IngressInnerCosMarkMode_Type(Integer32):
    """Custom type zxAnQos3IngressInnerCosMarkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("override", 2),
          ("cosRemark", 3),
          ("dscpToCos", 4),
          ("notSupport", 255))
    )


_ZxAnQos3IngressInnerCosMarkMode_Type.__name__ = "Integer32"
_ZxAnQos3IngressInnerCosMarkMode_Object = MibTableColumn
zxAnQos3IngressInnerCosMarkMode = _ZxAnQos3IngressInnerCosMarkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 3),
    _ZxAnQos3IngressInnerCosMarkMode_Type()
)
zxAnQos3IngressInnerCosMarkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3IngressInnerCosMarkMode.setStatus("current")


class _ZxAnQos3EgressCosMarkMode_Type(Integer32):
    """Custom type zxAnQos3EgressCosMarkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("override", 2),
          ("cosRemark", 3),
          ("dscpToCos", 4),
          ("notSupport", 255))
    )


_ZxAnQos3EgressCosMarkMode_Type.__name__ = "Integer32"
_ZxAnQos3EgressCosMarkMode_Object = MibTableColumn
zxAnQos3EgressCosMarkMode = _ZxAnQos3EgressCosMarkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 4),
    _ZxAnQos3EgressCosMarkMode_Type()
)
zxAnQos3EgressCosMarkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3EgressCosMarkMode.setStatus("current")


class _ZxAnQos3IngressDefaultCos_Type(Integer32):
    """Custom type zxAnQos3IngressDefaultCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQos3IngressDefaultCos_Type.__name__ = "Integer32"
_ZxAnQos3IngressDefaultCos_Object = MibTableColumn
zxAnQos3IngressDefaultCos = _ZxAnQos3IngressDefaultCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 5),
    _ZxAnQos3IngressDefaultCos_Type()
)
zxAnQos3IngressDefaultCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3IngressDefaultCos.setStatus("current")


class _ZxAnQos3IngressDefaultInnerCos_Type(Integer32):
    """Custom type zxAnQos3IngressDefaultInnerCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQos3IngressDefaultInnerCos_Type.__name__ = "Integer32"
_ZxAnQos3IngressDefaultInnerCos_Object = MibTableColumn
zxAnQos3IngressDefaultInnerCos = _ZxAnQos3IngressDefaultInnerCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 6),
    _ZxAnQos3IngressDefaultInnerCos_Type()
)
zxAnQos3IngressDefaultInnerCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3IngressDefaultInnerCos.setStatus("current")


class _ZxAnQosIfDefaultEgressCos_Type(Integer32):
    """Custom type zxAnQosIfDefaultEgressCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIfDefaultEgressCos_Type.__name__ = "Integer32"
_ZxAnQosIfDefaultEgressCos_Object = MibTableColumn
zxAnQosIfDefaultEgressCos = _ZxAnQosIfDefaultEgressCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 7),
    _ZxAnQosIfDefaultEgressCos_Type()
)
zxAnQosIfDefaultEgressCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfDefaultEgressCos.setStatus("current")


class _ZxAnQosIfCosToCosPrf_Type(DisplayString):
    """Custom type zxAnQosIfCosToCosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfCosToCosPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfCosToCosPrf_Object = MibTableColumn
zxAnQosIfCosToCosPrf = _ZxAnQosIfCosToCosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 8),
    _ZxAnQosIfCosToCosPrf_Type()
)
zxAnQosIfCosToCosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfCosToCosPrf.setStatus("current")


class _ZxAnQosIfCtagCosToCosPrf_Type(DisplayString):
    """Custom type zxAnQosIfCtagCosToCosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfCtagCosToCosPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfCtagCosToCosPrf_Object = MibTableColumn
zxAnQosIfCtagCosToCosPrf = _ZxAnQosIfCtagCosToCosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 9),
    _ZxAnQosIfCtagCosToCosPrf_Type()
)
zxAnQosIfCtagCosToCosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfCtagCosToCosPrf.setStatus("current")


class _ZxAnQosIfEgressCosToCosPrf_Type(DisplayString):
    """Custom type zxAnQosIfEgressCosToCosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfEgressCosToCosPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfEgressCosToCosPrf_Object = MibTableColumn
zxAnQosIfEgressCosToCosPrf = _ZxAnQosIfEgressCosToCosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 10),
    _ZxAnQosIfEgressCosToCosPrf_Type()
)
zxAnQosIfEgressCosToCosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfEgressCosToCosPrf.setStatus("current")


class _ZxAnQos3IngressDscp2CosPrf_Type(DisplayString):
    """Custom type zxAnQos3IngressDscp2CosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQos3IngressDscp2CosPrf_Type.__name__ = "DisplayString"
_ZxAnQos3IngressDscp2CosPrf_Object = MibTableColumn
zxAnQos3IngressDscp2CosPrf = _ZxAnQos3IngressDscp2CosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 11),
    _ZxAnQos3IngressDscp2CosPrf_Type()
)
zxAnQos3IngressDscp2CosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3IngressDscp2CosPrf.setStatus("current")


class _ZxAnQos3IngressDscp2InnerCosPrf_Type(DisplayString):
    """Custom type zxAnQos3IngressDscp2InnerCosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQos3IngressDscp2InnerCosPrf_Type.__name__ = "DisplayString"
_ZxAnQos3IngressDscp2InnerCosPrf_Object = MibTableColumn
zxAnQos3IngressDscp2InnerCosPrf = _ZxAnQos3IngressDscp2InnerCosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 12),
    _ZxAnQos3IngressDscp2InnerCosPrf_Type()
)
zxAnQos3IngressDscp2InnerCosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQos3IngressDscp2InnerCosPrf.setStatus("current")


class _ZxAnQosIfEgressDscpToCosPrf_Type(DisplayString):
    """Custom type zxAnQosIfEgressDscpToCosPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfEgressDscpToCosPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfEgressDscpToCosPrf_Object = MibTableColumn
zxAnQosIfEgressDscpToCosPrf = _ZxAnQosIfEgressDscpToCosPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 4, 1, 1, 13),
    _ZxAnQosIfEgressDscpToCosPrf_Type()
)
zxAnQosIfEgressDscpToCosPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfEgressDscpToCosPrf.setStatus("current")
_ZxAnQos3Queue_ObjectIdentity = ObjectIdentity
zxAnQos3Queue = _ZxAnQos3Queue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5)
)
_ZxAnQos3QueueBlockProfileTable_Object = MibTable
zxAnQos3QueueBlockProfileTable = _ZxAnQos3QueueBlockProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnQos3QueueBlockProfileTable.setStatus("current")
_ZxAnQos3QueueBlockProfileEntry_Object = MibTableRow
zxAnQos3QueueBlockProfileEntry = _ZxAnQos3QueueBlockProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1, 1)
)
zxAnQos3QueueBlockProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosQueueBlockPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3QueueBlockProfileEntry.setStatus("current")


class _ZxAnQosQueueBlockPrfName_Type(DisplayString):
    """Custom type zxAnQosQueueBlockPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosQueueBlockPrfName_Type.__name__ = "DisplayString"
_ZxAnQosQueueBlockPrfName_Object = MibTableColumn
zxAnQosQueueBlockPrfName = _ZxAnQosQueueBlockPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1, 1, 1),
    _ZxAnQosQueueBlockPrfName_Type()
)
zxAnQosQueueBlockPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosQueueBlockPrfName.setStatus("current")


class _ZxAnQosQueueBlockQNumber_Type(Integer32):
    """Custom type zxAnQosQueueBlockQNumber based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("two", 2),
          ("four", 4),
          ("eight", 8))
    )


_ZxAnQosQueueBlockQNumber_Type.__name__ = "Integer32"
_ZxAnQosQueueBlockQNumber_Object = MibTableColumn
zxAnQosQueueBlockQNumber = _ZxAnQosQueueBlockQNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1, 1, 2),
    _ZxAnQosQueueBlockQNumber_Type()
)
zxAnQosQueueBlockQNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueBlockQNumber.setStatus("current")


class _ZxAnQosQueueWeight_Type(OctetString):
    """Custom type zxAnQosQueueWeight based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosQueueWeight_Type.__name__ = "OctetString"
_ZxAnQosQueueWeight_Object = MibTableColumn
zxAnQosQueueWeight = _ZxAnQosQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1, 1, 3),
    _ZxAnQosQueueWeight_Type()
)
zxAnQosQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueWeight.setStatus("current")


class _ZxAnQosQueueDepth_Type(OctetString):
    """Custom type zxAnQosQueueDepth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosQueueDepth_Type.__name__ = "OctetString"
_ZxAnQosQueueDepth_Object = MibTableColumn
zxAnQosQueueDepth = _ZxAnQosQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1, 1, 4),
    _ZxAnQosQueueDepth_Type()
)
zxAnQosQueueDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueDepth.setStatus("current")
_ZxAnQosQueueBlockRowStatus_Type = RowStatus
_ZxAnQosQueueBlockRowStatus_Object = MibTableColumn
zxAnQosQueueBlockRowStatus = _ZxAnQosQueueBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 1, 1, 20),
    _ZxAnQosQueueBlockRowStatus_Type()
)
zxAnQosQueueBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueBlockRowStatus.setStatus("current")
_ZxAnQos3QueueMapProfileTable_Object = MibTable
zxAnQos3QueueMapProfileTable = _ZxAnQos3QueueMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2)
)
if mibBuilder.loadTexts:
    zxAnQos3QueueMapProfileTable.setStatus("current")
_ZxAnQos3QueueMapProfileEntry_Object = MibTableRow
zxAnQos3QueueMapProfileEntry = _ZxAnQos3QueueMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1)
)
zxAnQos3QueueMapProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosQueueMapPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3QueueMapProfileEntry.setStatus("current")


class _ZxAnQosQueueMapPrfName_Type(DisplayString):
    """Custom type zxAnQosQueueMapPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosQueueMapPrfName_Type.__name__ = "DisplayString"
_ZxAnQosQueueMapPrfName_Object = MibTableColumn
zxAnQosQueueMapPrfName = _ZxAnQosQueueMapPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1, 1),
    _ZxAnQosQueueMapPrfName_Type()
)
zxAnQosQueueMapPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosQueueMapPrfName.setStatus("current")


class _ZxAnQosQueueMapQNumber_Type(Integer32):
    """Custom type zxAnQosQueueMapQNumber based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("two", 2),
          ("four", 4),
          ("eight", 8))
    )


_ZxAnQosQueueMapQNumber_Type.__name__ = "Integer32"
_ZxAnQosQueueMapQNumber_Object = MibTableColumn
zxAnQosQueueMapQNumber = _ZxAnQosQueueMapQNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1, 2),
    _ZxAnQosQueueMapQNumber_Type()
)
zxAnQosQueueMapQNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueMapQNumber.setStatus("current")


class _ZxAnQosQueueMapMode_Type(Integer32):
    """Custom type zxAnQosQueueMapMode based on Integer32"""
    defaultValue = 1

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
        *(("cos", 1),
          ("servicePort", 2),
          ("gemPort", 3),
          ("pvc", 4))
    )


_ZxAnQosQueueMapMode_Type.__name__ = "Integer32"
_ZxAnQosQueueMapMode_Object = MibTableColumn
zxAnQosQueueMapMode = _ZxAnQosQueueMapMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1, 3),
    _ZxAnQosQueueMapMode_Type()
)
zxAnQosQueueMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueMapMode.setStatus("current")


class _ZxAnQosCosToQueue_Type(OctetString):
    """Custom type zxAnQosCosToQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosCosToQueue_Type.__name__ = "OctetString"
_ZxAnQosCosToQueue_Object = MibTableColumn
zxAnQosCosToQueue = _ZxAnQosCosToQueue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1, 4),
    _ZxAnQosCosToQueue_Type()
)
zxAnQosCosToQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosCosToQueue.setStatus("current")


class _ZxAnQosPvc2Queue_Type(OctetString):
    """Custom type zxAnQosPvc2Queue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosPvc2Queue_Type.__name__ = "OctetString"
_ZxAnQosPvc2Queue_Object = MibTableColumn
zxAnQosPvc2Queue = _ZxAnQosPvc2Queue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1, 5),
    _ZxAnQosPvc2Queue_Type()
)
zxAnQosPvc2Queue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPvc2Queue.setStatus("current")
_ZxAnQosQueueMapRowStatus_Type = RowStatus
_ZxAnQosQueueMapRowStatus_Object = MibTableColumn
zxAnQosQueueMapRowStatus = _ZxAnQosQueueMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 2, 1, 20),
    _ZxAnQosQueueMapRowStatus_Type()
)
zxAnQosQueueMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosQueueMapRowStatus.setStatus("current")
_ZxAnQos3PortQueueConfigTable_Object = MibTable
zxAnQos3PortQueueConfigTable = _ZxAnQos3PortQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 3)
)
if mibBuilder.loadTexts:
    zxAnQos3PortQueueConfigTable.setStatus("current")
_ZxAnQos3PortQueueConfigEntry_Object = MibTableRow
zxAnQos3PortQueueConfigEntry = _ZxAnQos3PortQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 3, 1)
)
zxAnQos3PortQueueConfigEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Rack"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Shelf"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Slot"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Port"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Onu"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3VCircuitType"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3LogicalId"),
)
if mibBuilder.loadTexts:
    zxAnQos3PortQueueConfigEntry.setStatus("current")


class _ZxAnQosIfQueueBlockPrf_Type(DisplayString):
    """Custom type zxAnQosIfQueueBlockPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfQueueBlockPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfQueueBlockPrf_Object = MibTableColumn
zxAnQosIfQueueBlockPrf = _ZxAnQosIfQueueBlockPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 3, 1, 1),
    _ZxAnQosIfQueueBlockPrf_Type()
)
zxAnQosIfQueueBlockPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfQueueBlockPrf.setStatus("current")


class _ZxAnQosIfQueueMapPrf_Type(DisplayString):
    """Custom type zxAnQosIfQueueMapPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIfQueueMapPrf_Type.__name__ = "DisplayString"
_ZxAnQosIfQueueMapPrf_Object = MibTableColumn
zxAnQosIfQueueMapPrf = _ZxAnQosIfQueueMapPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 5, 3, 1, 2),
    _ZxAnQosIfQueueMapPrf_Type()
)
zxAnQosIfQueueMapPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIfQueueMapPrf.setStatus("current")
_ZxAnQos3Traffic_ObjectIdentity = ObjectIdentity
zxAnQos3Traffic = _ZxAnQos3Traffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6)
)
_ZxAnQos3TrafficProfileTable_Object = MibTable
zxAnQos3TrafficProfileTable = _ZxAnQos3TrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1)
)
if mibBuilder.loadTexts:
    zxAnQos3TrafficProfileTable.setStatus("current")
_ZxAnQos3TrafficProfileEntry_Object = MibTableRow
zxAnQos3TrafficProfileEntry = _ZxAnQos3TrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1)
)
zxAnQos3TrafficProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosTrafficPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3TrafficProfileEntry.setStatus("current")


class _ZxAnQosTrafficPrfName_Type(DisplayString):
    """Custom type zxAnQosTrafficPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosTrafficPrfName_Type.__name__ = "DisplayString"
_ZxAnQosTrafficPrfName_Object = MibTableColumn
zxAnQosTrafficPrfName = _ZxAnQosTrafficPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 1),
    _ZxAnQosTrafficPrfName_Type()
)
zxAnQosTrafficPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfName.setStatus("current")


class _ZxAnQosTrafficPrfCir_Type(Integer32):
    """Custom type zxAnQosTrafficPrfCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_ZxAnQosTrafficPrfCir_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfCir_Object = MibTableColumn
zxAnQosTrafficPrfCir = _ZxAnQosTrafficPrfCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 2),
    _ZxAnQosTrafficPrfCir_Type()
)
zxAnQosTrafficPrfCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfCir.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfCir.setUnits("kbps")


class _ZxAnQosTrafficPrfCbs_Type(Integer32):
    """Custom type zxAnQosTrafficPrfCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnQosTrafficPrfCbs_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfCbs_Object = MibTableColumn
zxAnQosTrafficPrfCbs = _ZxAnQosTrafficPrfCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 3),
    _ZxAnQosTrafficPrfCbs_Type()
)
zxAnQosTrafficPrfCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfCbs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfCbs.setUnits("kbytes")


class _ZxAnQosTrafficPrfPir_Type(Integer32):
    """Custom type zxAnQosTrafficPrfPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_ZxAnQosTrafficPrfPir_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfPir_Object = MibTableColumn
zxAnQosTrafficPrfPir = _ZxAnQosTrafficPrfPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 4),
    _ZxAnQosTrafficPrfPir_Type()
)
zxAnQosTrafficPrfPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfPir.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfPir.setUnits("kbps")


class _ZxAnQosTrafficPrfPbs_Type(Integer32):
    """Custom type zxAnQosTrafficPrfPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnQosTrafficPrfPbs_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfPbs_Object = MibTableColumn
zxAnQosTrafficPrfPbs = _ZxAnQosTrafficPrfPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 5),
    _ZxAnQosTrafficPrfPbs_Type()
)
zxAnQosTrafficPrfPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfPbs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfPbs.setUnits("kbytes")


class _ZxAnQosTrafficPrfDiscardMode_Type(Integer32):
    """Custom type zxAnQosTrafficPrfDiscardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDistinction", 1),
          ("lowPriorityFirst", 2))
    )


_ZxAnQosTrafficPrfDiscardMode_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfDiscardMode_Object = MibTableColumn
zxAnQosTrafficPrfDiscardMode = _ZxAnQosTrafficPrfDiscardMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 6),
    _ZxAnQosTrafficPrfDiscardMode_Type()
)
zxAnQosTrafficPrfDiscardMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfDiscardMode.setStatus("current")


class _ZxAnQosTrafficPrfCirCosRemark_Type(Integer32):
    """Custom type zxAnQosTrafficPrfCirCosRemark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosTrafficPrfCirCosRemark_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfCirCosRemark_Object = MibTableColumn
zxAnQosTrafficPrfCirCosRemark = _ZxAnQosTrafficPrfCirCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 7),
    _ZxAnQosTrafficPrfCirCosRemark_Type()
)
zxAnQosTrafficPrfCirCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfCirCosRemark.setStatus("current")


class _ZxAnQosTrafficPrfPirCosRemark_Type(Integer32):
    """Custom type zxAnQosTrafficPrfPirCosRemark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosTrafficPrfPirCosRemark_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfPirCosRemark_Object = MibTableColumn
zxAnQosTrafficPrfPirCosRemark = _ZxAnQosTrafficPrfPirCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 8),
    _ZxAnQosTrafficPrfPirCosRemark_Type()
)
zxAnQosTrafficPrfPirCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfPirCosRemark.setStatus("current")


class _ZxAnQosTrafficPrfColorMode_Type(Integer32):
    """Custom type zxAnQosTrafficPrfColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )


_ZxAnQosTrafficPrfColorMode_Type.__name__ = "Integer32"
_ZxAnQosTrafficPrfColorMode_Object = MibTableColumn
zxAnQosTrafficPrfColorMode = _ZxAnQosTrafficPrfColorMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 9),
    _ZxAnQosTrafficPrfColorMode_Type()
)
zxAnQosTrafficPrfColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfColorMode.setStatus("current")
_ZxAnQosTrafficPrfRowStatus_Type = RowStatus
_ZxAnQosTrafficPrfRowStatus_Object = MibTableColumn
zxAnQosTrafficPrfRowStatus = _ZxAnQosTrafficPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 1, 1, 20),
    _ZxAnQosTrafficPrfRowStatus_Type()
)
zxAnQosTrafficPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficPrfRowStatus.setStatus("current")
_ZxAnQos3TrafficConfigTable_Object = MibTable
zxAnQos3TrafficConfigTable = _ZxAnQos3TrafficConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 2)
)
if mibBuilder.loadTexts:
    zxAnQos3TrafficConfigTable.setStatus("current")
_ZxAnQos3TrafficConfigEntry_Object = MibTableRow
zxAnQos3TrafficConfigEntry = _ZxAnQos3TrafficConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 2, 1)
)
zxAnQos3TrafficConfigEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Rack"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Shelf"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Slot"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Port"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Onu"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3VCircuitType"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3LogicalId"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosTrafficIfVlanDirection"),
)
if mibBuilder.loadTexts:
    zxAnQos3TrafficConfigEntry.setStatus("current")


class _ZxAnQosTrafficIfVlanDirection_Type(Integer32):
    """Custom type zxAnQosTrafficIfVlanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_ZxAnQosTrafficIfVlanDirection_Type.__name__ = "Integer32"
_ZxAnQosTrafficIfVlanDirection_Object = MibTableColumn
zxAnQosTrafficIfVlanDirection = _ZxAnQosTrafficIfVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 2, 1, 1),
    _ZxAnQosTrafficIfVlanDirection_Type()
)
zxAnQosTrafficIfVlanDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosTrafficIfVlanDirection.setStatus("current")


class _ZxAnQosTrafficIfConfPrf_Type(DisplayString):
    """Custom type zxAnQosTrafficIfConfPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosTrafficIfConfPrf_Type.__name__ = "DisplayString"
_ZxAnQosTrafficIfConfPrf_Object = MibTableColumn
zxAnQosTrafficIfConfPrf = _ZxAnQosTrafficIfConfPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 2, 1, 2),
    _ZxAnQosTrafficIfConfPrf_Type()
)
zxAnQosTrafficIfConfPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficIfConfPrf.setStatus("current")


class _ZxAnQosTrafficIfConfPrfType_Type(Integer32):
    """Custom type zxAnQosTrafficIfConfPrfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("atm", 2))
    )


_ZxAnQosTrafficIfConfPrfType_Type.__name__ = "Integer32"
_ZxAnQosTrafficIfConfPrfType_Object = MibTableColumn
zxAnQosTrafficIfConfPrfType = _ZxAnQosTrafficIfConfPrfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 2, 1, 3),
    _ZxAnQosTrafficIfConfPrfType_Type()
)
zxAnQosTrafficIfConfPrfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficIfConfPrfType.setStatus("current")
_ZxAnQosTrafficIfRowStatus_Type = RowStatus
_ZxAnQosTrafficIfRowStatus_Object = MibTableColumn
zxAnQosTrafficIfRowStatus = _ZxAnQosTrafficIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 2, 1, 20),
    _ZxAnQosTrafficIfRowStatus_Type()
)
zxAnQosTrafficIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosTrafficIfRowStatus.setStatus("current")
_ZxAnQos3AtmTrafficProfileTable_Object = MibTable
zxAnQos3AtmTrafficProfileTable = _ZxAnQos3AtmTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3)
)
if mibBuilder.loadTexts:
    zxAnQos3AtmTrafficProfileTable.setStatus("current")
_ZxAnQos3AtmTrafficProfileEntry_Object = MibTableRow
zxAnQos3AtmTrafficProfileEntry = _ZxAnQos3AtmTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1)
)
zxAnQos3AtmTrafficProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQosAtmTrafficPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQos3AtmTrafficProfileEntry.setStatus("current")


class _ZxAnQosAtmTrafficPrfName_Type(DisplayString):
    """Custom type zxAnQosAtmTrafficPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosAtmTrafficPrfName_Type.__name__ = "DisplayString"
_ZxAnQosAtmTrafficPrfName_Object = MibTableColumn
zxAnQosAtmTrafficPrfName = _ZxAnQosAtmTrafficPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 1),
    _ZxAnQosAtmTrafficPrfName_Type()
)
zxAnQosAtmTrafficPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfName.setStatus("current")


class _ZxAnQosAtmTrafficPrfType_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmCbr", 1),
          ("atmUbr", 2),
          ("atmVbr", 3))
    )


_ZxAnQosAtmTrafficPrfType_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfType_Object = MibTableColumn
zxAnQosAtmTrafficPrfType = _ZxAnQosAtmTrafficPrfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 2),
    _ZxAnQosAtmTrafficPrfType_Type()
)
zxAnQosAtmTrafficPrfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfType.setStatus("current")


class _ZxAnQosAtmTrafficPrfPcr_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfPcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_ZxAnQosAtmTrafficPrfPcr_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfPcr_Object = MibTableColumn
zxAnQosAtmTrafficPrfPcr = _ZxAnQosAtmTrafficPrfPcr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 3),
    _ZxAnQosAtmTrafficPrfPcr_Type()
)
zxAnQosAtmTrafficPrfPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfPcr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfPcr.setUnits("kbps")


class _ZxAnQosAtmTrafficPrfPcrCosRemark_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfPcrCosRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosAtmTrafficPrfPcrCosRemark_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfPcrCosRemark_Object = MibTableColumn
zxAnQosAtmTrafficPrfPcrCosRemark = _ZxAnQosAtmTrafficPrfPcrCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 4),
    _ZxAnQosAtmTrafficPrfPcrCosRemark_Type()
)
zxAnQosAtmTrafficPrfPcrCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfPcrCosRemark.setStatus("current")


class _ZxAnQosAtmTrafficPrfMcr_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfMcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_ZxAnQosAtmTrafficPrfMcr_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfMcr_Object = MibTableColumn
zxAnQosAtmTrafficPrfMcr = _ZxAnQosAtmTrafficPrfMcr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 5),
    _ZxAnQosAtmTrafficPrfMcr_Type()
)
zxAnQosAtmTrafficPrfMcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfMcr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfMcr.setUnits("kbps")


class _ZxAnQosAtmTrafficPrfMcrCosRemark_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfMcrCosRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosAtmTrafficPrfMcrCosRemark_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfMcrCosRemark_Object = MibTableColumn
zxAnQosAtmTrafficPrfMcrCosRemark = _ZxAnQosAtmTrafficPrfMcrCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 6),
    _ZxAnQosAtmTrafficPrfMcrCosRemark_Type()
)
zxAnQosAtmTrafficPrfMcrCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfMcrCosRemark.setStatus("current")


class _ZxAnQosAtmTrafficPrfScr_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfScr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_ZxAnQosAtmTrafficPrfScr_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfScr_Object = MibTableColumn
zxAnQosAtmTrafficPrfScr = _ZxAnQosAtmTrafficPrfScr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 7),
    _ZxAnQosAtmTrafficPrfScr_Type()
)
zxAnQosAtmTrafficPrfScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfScr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfScr.setUnits("kbps")


class _ZxAnQosAtmTrafficPrfScrCosRemark_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfScrCosRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosAtmTrafficPrfScrCosRemark_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfScrCosRemark_Object = MibTableColumn
zxAnQosAtmTrafficPrfScrCosRemark = _ZxAnQosAtmTrafficPrfScrCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 8),
    _ZxAnQosAtmTrafficPrfScrCosRemark_Type()
)
zxAnQosAtmTrafficPrfScrCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfScrCosRemark.setStatus("current")


class _ZxAnQosAtmTrafficPrfDiscardMode_Type(Integer32):
    """Custom type zxAnQosAtmTrafficPrfDiscardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDistinction", 1),
          ("lowPriorityFirst", 2))
    )


_ZxAnQosAtmTrafficPrfDiscardMode_Type.__name__ = "Integer32"
_ZxAnQosAtmTrafficPrfDiscardMode_Object = MibTableColumn
zxAnQosAtmTrafficPrfDiscardMode = _ZxAnQosAtmTrafficPrfDiscardMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 9),
    _ZxAnQosAtmTrafficPrfDiscardMode_Type()
)
zxAnQosAtmTrafficPrfDiscardMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfDiscardMode.setStatus("current")
_ZxAnQosAtmTrafficPrfRowStatus_Type = RowStatus
_ZxAnQosAtmTrafficPrfRowStatus_Object = MibTableColumn
zxAnQosAtmTrafficPrfRowStatus = _ZxAnQosAtmTrafficPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 3, 1, 20),
    _ZxAnQosAtmTrafficPrfRowStatus_Type()
)
zxAnQosAtmTrafficPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAtmTrafficPrfRowStatus.setStatus("current")
_ZxAnQos3RemainingBwTable_Object = MibTable
zxAnQos3RemainingBwTable = _ZxAnQos3RemainingBwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 24)
)
if mibBuilder.loadTexts:
    zxAnQos3RemainingBwTable.setStatus("current")
_ZxAnQos3RemainingBwEntry_Object = MibTableRow
zxAnQos3RemainingBwEntry = _ZxAnQos3RemainingBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 24, 1)
)
zxAnQos3RemainingBwEntry.setIndexNames(
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Rack"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Shelf"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Slot"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Port"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3Onu"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3VCircuitType"),
    (0, "ZTE-AN-QOS3-MIB", "zxAnQos3LogicalId"),
)
if mibBuilder.loadTexts:
    zxAnQos3RemainingBwEntry.setStatus("current")
_ZxAnQosTrafficTotalBandwidth_Type = Integer32
_ZxAnQosTrafficTotalBandwidth_Object = MibTableColumn
zxAnQosTrafficTotalBandwidth = _ZxAnQosTrafficTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 24, 1, 1),
    _ZxAnQosTrafficTotalBandwidth_Type()
)
zxAnQosTrafficTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosTrafficTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosTrafficTotalBandwidth.setUnits("kbps")
_ZxAnQosTrafficRemainingBandwidth_Type = Integer32
_ZxAnQosTrafficRemainingBandwidth_Object = MibTableColumn
zxAnQosTrafficRemainingBandwidth = _ZxAnQosTrafficRemainingBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 4, 6, 24, 1, 2),
    _ZxAnQosTrafficRemainingBandwidth_Type()
)
zxAnQosTrafficRemainingBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosTrafficRemainingBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosTrafficRemainingBandwidth.setUnits("kbps")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-QOS3-MIB",
    **{"zxAnQosMib": zxAnQosMib,
       "zxAnQos3Objects": zxAnQos3Objects,
       "zxAnQos3GlobalObjects": zxAnQos3GlobalObjects,
       "zxAnQos3MgmtCapabilities": zxAnQos3MgmtCapabilities,
       "zxAnQos3QueueGlobalObjects": zxAnQos3QueueGlobalObjects,
       "zxAnQosEthCosToQueue": zxAnQosEthCosToQueue,
       "zxAnQos3MappingProfile": zxAnQos3MappingProfile,
       "zxAnQos3CosRemarkProfileTable": zxAnQos3CosRemarkProfileTable,
       "zxAnQos3CosRemarkProfileEntry": zxAnQos3CosRemarkProfileEntry,
       "zxAnQosCosToCosPrfName": zxAnQosCosToCosPrfName,
       "zxAnQosCosToCos": zxAnQosCosToCos,
       "zxAnQosCosToCosPrfRowStatus": zxAnQosCosToCosPrfRowStatus,
       "zxAnQos3DscpRemarkProfileTable": zxAnQos3DscpRemarkProfileTable,
       "zxAnQos3DscpRemarkProfileEntry": zxAnQos3DscpRemarkProfileEntry,
       "zxAnQosDscpToDscpPrfName": zxAnQosDscpToDscpPrfName,
       "zxAnQosDscpToDscp": zxAnQosDscpToDscp,
       "zxAnQosDscpToDscpPrfRowStatus": zxAnQosDscpToDscpPrfRowStatus,
       "zxAnQos3Dscp2CosProfileTable": zxAnQos3Dscp2CosProfileTable,
       "zxAnQos3Dscp2CosProfileEntry": zxAnQos3Dscp2CosProfileEntry,
       "zxAnQosDscpToCosPrfName": zxAnQosDscpToCosPrfName,
       "zxAnQosDscpToCos": zxAnQosDscpToCos,
       "zxAnQosDscpToCosPrfRowStatus": zxAnQosDscpToCosPrfRowStatus,
       "zxAnQos3Dscp2DropProfileTable": zxAnQos3Dscp2DropProfileTable,
       "zxAnQos3Dscp2DropProfileEntry": zxAnQos3Dscp2DropProfileEntry,
       "zxAnQosDscpToDropPrecedePrfName": zxAnQosDscpToDropPrecedePrfName,
       "zxAnQosDscpToDropPrecedence": zxAnQosDscpToDropPrecedence,
       "zxAnQosDscpToDropPrePrfRowStatus": zxAnQosDscpToDropPrePrfRowStatus,
       "zxAnQos3MplsTc2CosProfileTable": zxAnQos3MplsTc2CosProfileTable,
       "zxAnQos3MplsTc2CosProfileEntry": zxAnQos3MplsTc2CosProfileEntry,
       "zxAnQosMplsTcToCosPrfName": zxAnQosMplsTcToCosPrfName,
       "zxAnQosMplsTcToCos": zxAnQosMplsTcToCos,
       "zxAnQosMplsTcToCosPrfRowStatus": zxAnQosMplsTcToCosPrfRowStatus,
       "zxAnQos3Cos2MplsTcProfileTable": zxAnQos3Cos2MplsTcProfileTable,
       "zxAnQos3Cos2MplsTcProfileEntry": zxAnQos3Cos2MplsTcProfileEntry,
       "zxAnQosCosToMplsTcPrfName": zxAnQosCosToMplsTcPrfName,
       "zxAnQosCosToMplsTc": zxAnQosCosToMplsTc,
       "zxAnQosCosToMplsTcPrfRowStatus": zxAnQosCosToMplsTcPrfRowStatus,
       "zxAnQos3PortConfig": zxAnQos3PortConfig,
       "zxAnQos3PortConfigTable": zxAnQos3PortConfigTable,
       "zxAnQos3PortConfigEntry": zxAnQos3PortConfigEntry,
       "zxAnQos3Rack": zxAnQos3Rack,
       "zxAnQos3Shelf": zxAnQos3Shelf,
       "zxAnQos3Slot": zxAnQos3Slot,
       "zxAnQos3Port": zxAnQos3Port,
       "zxAnQos3Onu": zxAnQos3Onu,
       "zxAnQos3VCircuitType": zxAnQos3VCircuitType,
       "zxAnQos3LogicalId": zxAnQos3LogicalId,
       "zxAnQosIfRateLimit": zxAnQosIfRateLimit,
       "zxAnQosIfBucketSize": zxAnQosIfBucketSize,
       "zxAnQosIfTrustMode": zxAnQosIfTrustMode,
       "zxAnQosIfDefaultCos": zxAnQosIfDefaultCos,
       "zxAnQosIfDscpToCosPrf": zxAnQosIfDscpToCosPrf,
       "zxAnQosIfDscpToDropPrecedencePrf": zxAnQosIfDscpToDropPrecedencePrf,
       "zxAnQosIfDscpToDscpPrf": zxAnQosIfDscpToDscpPrf,
       "zxAnQosIfIngressRateLimit": zxAnQosIfIngressRateLimit,
       "zxAnQosIfIngressBucketSize": zxAnQosIfIngressBucketSize,
       "zxAnQos3VPortConfig": zxAnQos3VPortConfig,
       "zxAnQos3VPortConfigTable": zxAnQos3VPortConfigTable,
       "zxAnQos3VPortConfigEntry": zxAnQos3VPortConfigEntry,
       "zxAnQosIfCosFilter": zxAnQosIfCosFilter,
       "zxAnQos3IngressCosMarkMode": zxAnQos3IngressCosMarkMode,
       "zxAnQos3IngressInnerCosMarkMode": zxAnQos3IngressInnerCosMarkMode,
       "zxAnQos3EgressCosMarkMode": zxAnQos3EgressCosMarkMode,
       "zxAnQos3IngressDefaultCos": zxAnQos3IngressDefaultCos,
       "zxAnQos3IngressDefaultInnerCos": zxAnQos3IngressDefaultInnerCos,
       "zxAnQosIfDefaultEgressCos": zxAnQosIfDefaultEgressCos,
       "zxAnQosIfCosToCosPrf": zxAnQosIfCosToCosPrf,
       "zxAnQosIfCtagCosToCosPrf": zxAnQosIfCtagCosToCosPrf,
       "zxAnQosIfEgressCosToCosPrf": zxAnQosIfEgressCosToCosPrf,
       "zxAnQos3IngressDscp2CosPrf": zxAnQos3IngressDscp2CosPrf,
       "zxAnQos3IngressDscp2InnerCosPrf": zxAnQos3IngressDscp2InnerCosPrf,
       "zxAnQosIfEgressDscpToCosPrf": zxAnQosIfEgressDscpToCosPrf,
       "zxAnQos3Queue": zxAnQos3Queue,
       "zxAnQos3QueueBlockProfileTable": zxAnQos3QueueBlockProfileTable,
       "zxAnQos3QueueBlockProfileEntry": zxAnQos3QueueBlockProfileEntry,
       "zxAnQosQueueBlockPrfName": zxAnQosQueueBlockPrfName,
       "zxAnQosQueueBlockQNumber": zxAnQosQueueBlockQNumber,
       "zxAnQosQueueWeight": zxAnQosQueueWeight,
       "zxAnQosQueueDepth": zxAnQosQueueDepth,
       "zxAnQosQueueBlockRowStatus": zxAnQosQueueBlockRowStatus,
       "zxAnQos3QueueMapProfileTable": zxAnQos3QueueMapProfileTable,
       "zxAnQos3QueueMapProfileEntry": zxAnQos3QueueMapProfileEntry,
       "zxAnQosQueueMapPrfName": zxAnQosQueueMapPrfName,
       "zxAnQosQueueMapQNumber": zxAnQosQueueMapQNumber,
       "zxAnQosQueueMapMode": zxAnQosQueueMapMode,
       "zxAnQosCosToQueue": zxAnQosCosToQueue,
       "zxAnQosPvc2Queue": zxAnQosPvc2Queue,
       "zxAnQosQueueMapRowStatus": zxAnQosQueueMapRowStatus,
       "zxAnQos3PortQueueConfigTable": zxAnQos3PortQueueConfigTable,
       "zxAnQos3PortQueueConfigEntry": zxAnQos3PortQueueConfigEntry,
       "zxAnQosIfQueueBlockPrf": zxAnQosIfQueueBlockPrf,
       "zxAnQosIfQueueMapPrf": zxAnQosIfQueueMapPrf,
       "zxAnQos3Traffic": zxAnQos3Traffic,
       "zxAnQos3TrafficProfileTable": zxAnQos3TrafficProfileTable,
       "zxAnQos3TrafficProfileEntry": zxAnQos3TrafficProfileEntry,
       "zxAnQosTrafficPrfName": zxAnQosTrafficPrfName,
       "zxAnQosTrafficPrfCir": zxAnQosTrafficPrfCir,
       "zxAnQosTrafficPrfCbs": zxAnQosTrafficPrfCbs,
       "zxAnQosTrafficPrfPir": zxAnQosTrafficPrfPir,
       "zxAnQosTrafficPrfPbs": zxAnQosTrafficPrfPbs,
       "zxAnQosTrafficPrfDiscardMode": zxAnQosTrafficPrfDiscardMode,
       "zxAnQosTrafficPrfCirCosRemark": zxAnQosTrafficPrfCirCosRemark,
       "zxAnQosTrafficPrfPirCosRemark": zxAnQosTrafficPrfPirCosRemark,
       "zxAnQosTrafficPrfColorMode": zxAnQosTrafficPrfColorMode,
       "zxAnQosTrafficPrfRowStatus": zxAnQosTrafficPrfRowStatus,
       "zxAnQos3TrafficConfigTable": zxAnQos3TrafficConfigTable,
       "zxAnQos3TrafficConfigEntry": zxAnQos3TrafficConfigEntry,
       "zxAnQosTrafficIfVlanDirection": zxAnQosTrafficIfVlanDirection,
       "zxAnQosTrafficIfConfPrf": zxAnQosTrafficIfConfPrf,
       "zxAnQosTrafficIfConfPrfType": zxAnQosTrafficIfConfPrfType,
       "zxAnQosTrafficIfRowStatus": zxAnQosTrafficIfRowStatus,
       "zxAnQos3AtmTrafficProfileTable": zxAnQos3AtmTrafficProfileTable,
       "zxAnQos3AtmTrafficProfileEntry": zxAnQos3AtmTrafficProfileEntry,
       "zxAnQosAtmTrafficPrfName": zxAnQosAtmTrafficPrfName,
       "zxAnQosAtmTrafficPrfType": zxAnQosAtmTrafficPrfType,
       "zxAnQosAtmTrafficPrfPcr": zxAnQosAtmTrafficPrfPcr,
       "zxAnQosAtmTrafficPrfPcrCosRemark": zxAnQosAtmTrafficPrfPcrCosRemark,
       "zxAnQosAtmTrafficPrfMcr": zxAnQosAtmTrafficPrfMcr,
       "zxAnQosAtmTrafficPrfMcrCosRemark": zxAnQosAtmTrafficPrfMcrCosRemark,
       "zxAnQosAtmTrafficPrfScr": zxAnQosAtmTrafficPrfScr,
       "zxAnQosAtmTrafficPrfScrCosRemark": zxAnQosAtmTrafficPrfScrCosRemark,
       "zxAnQosAtmTrafficPrfDiscardMode": zxAnQosAtmTrafficPrfDiscardMode,
       "zxAnQosAtmTrafficPrfRowStatus": zxAnQosAtmTrafficPrfRowStatus,
       "zxAnQos3RemainingBwTable": zxAnQos3RemainingBwTable,
       "zxAnQos3RemainingBwEntry": zxAnQos3RemainingBwEntry,
       "zxAnQosTrafficTotalBandwidth": zxAnQosTrafficTotalBandwidth,
       "zxAnQosTrafficRemainingBandwidth": zxAnQosTrafficRemainingBandwidth}
)
