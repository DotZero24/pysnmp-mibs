# SNMP MIB module (ADTRAN-TA5K-ATM-LM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-ATM-LM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:06 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kAtmLM,
 adGenTa5kAtmLMID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kAtmLM",
    "adGenTa5kAtmLMID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adTa5kAtmLMModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 14, 1)
)
if mibBuilder.loadTexts:
    adTa5kAtmLMModuleIdentity.setRevisions(
        ("2013-08-05 00:00",
         "2012-01-30 00:00",
         "2012-01-04 00:00",
         "2011-10-07 00:00",
         "2011-08-31 00:00",
         "2011-06-01 00:00",
         "2011-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenTa5kAtmLMConfig_ObjectIdentity = ObjectIdentity
adGenTa5kAtmLMConfig = _AdGenTa5kAtmLMConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1)
)
_AdGenTa5kAtmLMConfigTable_Object = MibTable
adGenTa5kAtmLMConfigTable = _AdGenTa5kAtmLMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigTable.setStatus("current")
_AdGenTa5kAtmLMConfigEntry_Object = MibTableRow
adGenTa5kAtmLMConfigEntry = _AdGenTa5kAtmLMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1)
)
adGenTa5kAtmLMConfigEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigEntry.setStatus("current")
_AdGenTa5kAtmLMConfigBootCodeRev_Type = DisplayString
_AdGenTa5kAtmLMConfigBootCodeRev_Object = MibTableColumn
adGenTa5kAtmLMConfigBootCodeRev = _AdGenTa5kAtmLMConfigBootCodeRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 1),
    _AdGenTa5kAtmLMConfigBootCodeRev_Type()
)
adGenTa5kAtmLMConfigBootCodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigBootCodeRev.setStatus("current")
_AdGenTa5kAtmLMConfigSystemSWRev_Type = DisplayString
_AdGenTa5kAtmLMConfigSystemSWRev_Object = MibTableColumn
adGenTa5kAtmLMConfigSystemSWRev = _AdGenTa5kAtmLMConfigSystemSWRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 2),
    _AdGenTa5kAtmLMConfigSystemSWRev_Type()
)
adGenTa5kAtmLMConfigSystemSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigSystemSWRev.setStatus("current")
_AdGenTa5kAtmLMConfigBootSysSWRev_Type = DisplayString
_AdGenTa5kAtmLMConfigBootSysSWRev_Object = MibTableColumn
adGenTa5kAtmLMConfigBootSysSWRev = _AdGenTa5kAtmLMConfigBootSysSWRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 3),
    _AdGenTa5kAtmLMConfigBootSysSWRev_Type()
)
adGenTa5kAtmLMConfigBootSysSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigBootSysSWRev.setStatus("current")
_AdGenTa5kAtmLMConfigMacAddress_Type = MacAddress
_AdGenTa5kAtmLMConfigMacAddress_Object = MibTableColumn
adGenTa5kAtmLMConfigMacAddress = _AdGenTa5kAtmLMConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 4),
    _AdGenTa5kAtmLMConfigMacAddress_Type()
)
adGenTa5kAtmLMConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigMacAddress.setStatus("current")
_AdGenTa5kAtmLMConfigFPGARev_Type = DisplayString
_AdGenTa5kAtmLMConfigFPGARev_Object = MibTableColumn
adGenTa5kAtmLMConfigFPGARev = _AdGenTa5kAtmLMConfigFPGARev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 5),
    _AdGenTa5kAtmLMConfigFPGARev_Type()
)
adGenTa5kAtmLMConfigFPGARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigFPGARev.setStatus("current")
_AdGenTa5kAtmLMConfigCPLDRev_Type = DisplayString
_AdGenTa5kAtmLMConfigCPLDRev_Object = MibTableColumn
adGenTa5kAtmLMConfigCPLDRev = _AdGenTa5kAtmLMConfigCPLDRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 6),
    _AdGenTa5kAtmLMConfigCPLDRev_Type()
)
adGenTa5kAtmLMConfigCPLDRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigCPLDRev.setStatus("current")
_AdGenTa5kAtmLMConfigWDDIRev_Type = DisplayString
_AdGenTa5kAtmLMConfigWDDIRev_Object = MibTableColumn
adGenTa5kAtmLMConfigWDDIRev = _AdGenTa5kAtmLMConfigWDDIRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 7),
    _AdGenTa5kAtmLMConfigWDDIRev_Type()
)
adGenTa5kAtmLMConfigWDDIRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigWDDIRev.setStatus("current")
_AdGenTa5kAtmLMConfigDPSRev_Type = DisplayString
_AdGenTa5kAtmLMConfigDPSRev_Object = MibTableColumn
adGenTa5kAtmLMConfigDPSRev = _AdGenTa5kAtmLMConfigDPSRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 1, 1, 1, 8),
    _AdGenTa5kAtmLMConfigDPSRev_Type()
)
adGenTa5kAtmLMConfigDPSRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMConfigDPSRev.setStatus("current")
_AdGenTa5kAtmLMProvisioning_ObjectIdentity = ObjectIdentity
adGenTa5kAtmLMProvisioning = _AdGenTa5kAtmLMProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2)
)
_AdGenTa5kAtmPortProvisioningTable_Object = MibTable
adGenTa5kAtmPortProvisioningTable = _AdGenTa5kAtmPortProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvisioningTable.setStatus("current")
_AdGenTa5kAtmPortProvisioningEntry_Object = MibTableRow
adGenTa5kAtmPortProvisioningEntry = _AdGenTa5kAtmPortProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1)
)
adGenTa5kAtmPortProvisioningEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvisioningEntry.setStatus("current")
_AdGenTa5kAtmPortProvPortID_Type = DisplayString
_AdGenTa5kAtmPortProvPortID_Object = MibTableColumn
adGenTa5kAtmPortProvPortID = _AdGenTa5kAtmPortProvPortID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 1),
    _AdGenTa5kAtmPortProvPortID_Type()
)
adGenTa5kAtmPortProvPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvPortID.setStatus("current")


class _AdGenTa5kAtmPortProvPortType_Type(Integer32):
    """Custom type adGenTa5kAtmPortProvPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uni", 1),
          ("nni", 2))
    )


_AdGenTa5kAtmPortProvPortType_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortProvPortType_Object = MibTableColumn
adGenTa5kAtmPortProvPortType = _AdGenTa5kAtmPortProvPortType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 2),
    _AdGenTa5kAtmPortProvPortType_Type()
)
adGenTa5kAtmPortProvPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvPortType.setStatus("current")


class _AdGenTa5kAtmPortProvScrambler_Type(Integer32):
    """Custom type adGenTa5kAtmPortProvScrambler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenTa5kAtmPortProvScrambler_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortProvScrambler_Object = MibTableColumn
adGenTa5kAtmPortProvScrambler = _AdGenTa5kAtmPortProvScrambler_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 3),
    _AdGenTa5kAtmPortProvScrambler_Type()
)
adGenTa5kAtmPortProvScrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvScrambler.setStatus("current")


class _AdGenTa5kAtmPortProvIdleCellType_Type(Integer32):
    """Custom type adGenTa5kAtmPortProvIdleCellType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bellcore", 1),
          ("itu", 2))
    )


_AdGenTa5kAtmPortProvIdleCellType_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortProvIdleCellType_Object = MibTableColumn
adGenTa5kAtmPortProvIdleCellType = _AdGenTa5kAtmPortProvIdleCellType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 4),
    _AdGenTa5kAtmPortProvIdleCellType_Type()
)
adGenTa5kAtmPortProvIdleCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvIdleCellType.setStatus("current")
_AdGenTa5kAtmPortProvMaxVccs_Type = Integer32
_AdGenTa5kAtmPortProvMaxVccs_Object = MibTableColumn
adGenTa5kAtmPortProvMaxVccs = _AdGenTa5kAtmPortProvMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 5),
    _AdGenTa5kAtmPortProvMaxVccs_Type()
)
adGenTa5kAtmPortProvMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvMaxVccs.setStatus("current")


class _AdGenTa5kAtmPortProvAISRDIGen_Type(Integer32):
    """Custom type adGenTa5kAtmPortProvAISRDIGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenTa5kAtmPortProvAISRDIGen_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortProvAISRDIGen_Object = MibTableColumn
adGenTa5kAtmPortProvAISRDIGen = _AdGenTa5kAtmPortProvAISRDIGen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 6),
    _AdGenTa5kAtmPortProvAISRDIGen_Type()
)
adGenTa5kAtmPortProvAISRDIGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvAISRDIGen.setStatus("current")


class _AdGenTa5kAtmPortProvInterfaceMode_Type(Integer32):
    """Custom type adGenTa5kAtmPortProvInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 1),
          ("aggregation", 2))
    )


_AdGenTa5kAtmPortProvInterfaceMode_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortProvInterfaceMode_Object = MibTableColumn
adGenTa5kAtmPortProvInterfaceMode = _AdGenTa5kAtmPortProvInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 7),
    _AdGenTa5kAtmPortProvInterfaceMode_Type()
)
adGenTa5kAtmPortProvInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvInterfaceMode.setStatus("current")


class _AdGenTa5kAtmPortProvDhcpCircuitIdFormat_Type(DisplayString):
    """Custom type adGenTa5kAtmPortProvDhcpCircuitIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenTa5kAtmPortProvDhcpCircuitIdFormat_Type.__name__ = "DisplayString"
_AdGenTa5kAtmPortProvDhcpCircuitIdFormat_Object = MibTableColumn
adGenTa5kAtmPortProvDhcpCircuitIdFormat = _AdGenTa5kAtmPortProvDhcpCircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 8),
    _AdGenTa5kAtmPortProvDhcpCircuitIdFormat_Type()
)
adGenTa5kAtmPortProvDhcpCircuitIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvDhcpCircuitIdFormat.setStatus("current")


class _AdGenTa5kAtmPortProvShapingUBR_Type(Integer32):
    """Custom type adGenTa5kAtmPortProvShapingUBR based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenTa5kAtmPortProvShapingUBR_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortProvShapingUBR_Object = MibTableColumn
adGenTa5kAtmPortProvShapingUBR = _AdGenTa5kAtmPortProvShapingUBR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 1, 1, 9),
    _AdGenTa5kAtmPortProvShapingUBR_Type()
)
adGenTa5kAtmPortProvShapingUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortProvShapingUBR.setStatus("current")
_AdGenTa5kManagementChannelTable_Object = MibTable
adGenTa5kManagementChannelTable = _AdGenTa5kManagementChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelTable.setStatus("current")
_AdGenTa5kManagementChannelEntry_Object = MibTableRow
adGenTa5kManagementChannelEntry = _AdGenTa5kManagementChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1)
)
adGenTa5kManagementChannelEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelEntry.setStatus("current")


class _AdGenTa5kManagementChannelVpi_Type(Integer32):
    """Custom type adGenTa5kManagementChannelVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdGenTa5kManagementChannelVpi_Type.__name__ = "Integer32"
_AdGenTa5kManagementChannelVpi_Object = MibTableColumn
adGenTa5kManagementChannelVpi = _AdGenTa5kManagementChannelVpi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 1),
    _AdGenTa5kManagementChannelVpi_Type()
)
adGenTa5kManagementChannelVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelVpi.setStatus("current")


class _AdGenTa5kManagementChannelVci_Type(Integer32):
    """Custom type adGenTa5kManagementChannelVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdGenTa5kManagementChannelVci_Type.__name__ = "Integer32"
_AdGenTa5kManagementChannelVci_Object = MibTableColumn
adGenTa5kManagementChannelVci = _AdGenTa5kManagementChannelVci_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 2),
    _AdGenTa5kManagementChannelVci_Type()
)
adGenTa5kManagementChannelVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelVci.setStatus("current")


class _AdGenTa5kManagementChannelMode_Type(Integer32):
    """Custom type adGenTa5kManagementChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("routed", 1)
    )


_AdGenTa5kManagementChannelMode_Type.__name__ = "Integer32"
_AdGenTa5kManagementChannelMode_Object = MibTableColumn
adGenTa5kManagementChannelMode = _AdGenTa5kManagementChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 3),
    _AdGenTa5kManagementChannelMode_Type()
)
adGenTa5kManagementChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelMode.setStatus("current")


class _AdGenTa5kManagementChannelEncap_Type(Integer32):
    """Custom type adGenTa5kManagementChannelEncap based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("vcMultiplexRoutedProtocol", 1),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("llcEncapsulation", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("unknown", 10))
    )


_AdGenTa5kManagementChannelEncap_Type.__name__ = "Integer32"
_AdGenTa5kManagementChannelEncap_Object = MibTableColumn
adGenTa5kManagementChannelEncap = _AdGenTa5kManagementChannelEncap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 4),
    _AdGenTa5kManagementChannelEncap_Type()
)
adGenTa5kManagementChannelEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelEncap.setStatus("current")


class _AdGenTa5kManagementChannelMultiplex_Type(Integer32):
    """Custom type adGenTa5kManagementChannelMultiplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("llc", 1)
    )


_AdGenTa5kManagementChannelMultiplex_Type.__name__ = "Integer32"
_AdGenTa5kManagementChannelMultiplex_Object = MibTableColumn
adGenTa5kManagementChannelMultiplex = _AdGenTa5kManagementChannelMultiplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 5),
    _AdGenTa5kManagementChannelMultiplex_Type()
)
adGenTa5kManagementChannelMultiplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelMultiplex.setStatus("current")


class _AdGenTa5kManagementChannelEnable_Type(Integer32):
    """Custom type adGenTa5kManagementChannelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenTa5kManagementChannelEnable_Type.__name__ = "Integer32"
_AdGenTa5kManagementChannelEnable_Object = MibTableColumn
adGenTa5kManagementChannelEnable = _AdGenTa5kManagementChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 6),
    _AdGenTa5kManagementChannelEnable_Type()
)
adGenTa5kManagementChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelEnable.setStatus("current")
_AdGenTa5kManagementChannelPort_Type = Integer32
_AdGenTa5kManagementChannelPort_Object = MibTableColumn
adGenTa5kManagementChannelPort = _AdGenTa5kManagementChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 2, 1, 7),
    _AdGenTa5kManagementChannelPort_Type()
)
adGenTa5kManagementChannelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kManagementChannelPort.setStatus("current")
_AdGenTa5kAtmLMSWUploadTable_Object = MibTable
adGenTa5kAtmLMSWUploadTable = _AdGenTa5kAtmLMSWUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 3)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMSWUploadTable.setStatus("current")
_AdGenTa5kAtmLMSWUploadEntry_Object = MibTableRow
adGenTa5kAtmLMSWUploadEntry = _AdGenTa5kAtmLMSWUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 3, 1)
)
adGenTa5kAtmLMSWUploadEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMSWUploadEntry.setStatus("current")
_AdGenTa5kAtmLMReboot_Type = Integer32
_AdGenTa5kAtmLMReboot_Object = MibTableColumn
adGenTa5kAtmLMReboot = _AdGenTa5kAtmLMReboot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 3, 1, 1),
    _AdGenTa5kAtmLMReboot_Type()
)
adGenTa5kAtmLMReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMReboot.setStatus("current")
_AdGenTa5kAtmLMCardProvTable_Object = MibTable
adGenTa5kAtmLMCardProvTable = _AdGenTa5kAtmLMCardProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardProvTable.setStatus("current")
_AdGenTa5kAtmLMCardProvEntry_Object = MibTableRow
adGenTa5kAtmLMCardProvEntry = _AdGenTa5kAtmLMCardProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1)
)
adGenTa5kAtmLMCardProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardProvEntry.setStatus("current")


class _AdGenTa5kAtmLMCardProvLearningMode_Type(Integer32):
    """Custom type adGenTa5kAtmLMCardProvLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenTa5kAtmLMCardProvLearningMode_Type.__name__ = "Integer32"
_AdGenTa5kAtmLMCardProvLearningMode_Object = MibTableColumn
adGenTa5kAtmLMCardProvLearningMode = _AdGenTa5kAtmLMCardProvLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1, 1),
    _AdGenTa5kAtmLMCardProvLearningMode_Type()
)
adGenTa5kAtmLMCardProvLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardProvLearningMode.setStatus("current")
_AdGenTa5kAtmLMCardVclLearnedCount_Type = Integer32
_AdGenTa5kAtmLMCardVclLearnedCount_Object = MibTableColumn
adGenTa5kAtmLMCardVclLearnedCount = _AdGenTa5kAtmLMCardVclLearnedCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1, 2),
    _AdGenTa5kAtmLMCardVclLearnedCount_Type()
)
adGenTa5kAtmLMCardVclLearnedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardVclLearnedCount.setStatus("current")


class _AdGenTa5kAtmLMCardCurrentOAMID_Type(OctetString):
    """Custom type adGenTa5kAtmLMCardCurrentOAMID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenTa5kAtmLMCardCurrentOAMID_Type.__name__ = "OctetString"
_AdGenTa5kAtmLMCardCurrentOAMID_Object = MibTableColumn
adGenTa5kAtmLMCardCurrentOAMID = _AdGenTa5kAtmLMCardCurrentOAMID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1, 3),
    _AdGenTa5kAtmLMCardCurrentOAMID_Type()
)
adGenTa5kAtmLMCardCurrentOAMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardCurrentOAMID.setStatus("current")


class _AdGenTa5kAtmLMCardFutureOAMID_Type(OctetString):
    """Custom type adGenTa5kAtmLMCardFutureOAMID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenTa5kAtmLMCardFutureOAMID_Type.__name__ = "OctetString"
_AdGenTa5kAtmLMCardFutureOAMID_Object = MibTableColumn
adGenTa5kAtmLMCardFutureOAMID = _AdGenTa5kAtmLMCardFutureOAMID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1, 4),
    _AdGenTa5kAtmLMCardFutureOAMID_Type()
)
adGenTa5kAtmLMCardFutureOAMID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardFutureOAMID.setStatus("current")


class _AdGenTa5kAtmLMCardResetDHCPPMStats_Type(Integer32):
    """Custom type adGenTa5kAtmLMCardResetDHCPPMStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenTa5kAtmLMCardResetDHCPPMStats_Type.__name__ = "Integer32"
_AdGenTa5kAtmLMCardResetDHCPPMStats_Object = MibTableColumn
adGenTa5kAtmLMCardResetDHCPPMStats = _AdGenTa5kAtmLMCardResetDHCPPMStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1, 5),
    _AdGenTa5kAtmLMCardResetDHCPPMStats_Type()
)
adGenTa5kAtmLMCardResetDHCPPMStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardResetDHCPPMStats.setStatus("current")


class _AdGenTa5kAtmLMCardResetDHCPRollingCounters_Type(Integer32):
    """Custom type adGenTa5kAtmLMCardResetDHCPRollingCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenTa5kAtmLMCardResetDHCPRollingCounters_Type.__name__ = "Integer32"
_AdGenTa5kAtmLMCardResetDHCPRollingCounters_Object = MibTableColumn
adGenTa5kAtmLMCardResetDHCPRollingCounters = _AdGenTa5kAtmLMCardResetDHCPRollingCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 4, 1, 6),
    _AdGenTa5kAtmLMCardResetDHCPRollingCounters_Type()
)
adGenTa5kAtmLMCardResetDHCPRollingCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMCardResetDHCPRollingCounters.setStatus("current")
_AdGenTa5kAtmLMLoopTimingTable_Object = MibTable
adGenTa5kAtmLMLoopTimingTable = _AdGenTa5kAtmLMLoopTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 5)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMLoopTimingTable.setStatus("current")
_AdGenTa5kAtmLMLoopTimingEntry_Object = MibTableRow
adGenTa5kAtmLMLoopTimingEntry = _AdGenTa5kAtmLMLoopTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 5, 1)
)
adGenTa5kAtmLMLoopTimingEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMLoopTimingEntry.setStatus("current")


class _AdGenTa5kAtmLMLoopTimingA_Type(Integer32):
    """Custom type adGenTa5kAtmLMLoopTimingA based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("loop1", 1),
          ("loop2", 2),
          ("loop3", 3),
          ("loop4", 4),
          ("loop5", 5),
          ("loop6", 6),
          ("loop7", 7),
          ("loop8", 8),
          ("loop9", 9),
          ("loop10", 10),
          ("loop11", 11),
          ("loop12", 12),
          ("loop13", 13),
          ("loop14", 14),
          ("loop15", 15),
          ("loop16", 16),
          ("loop17", 17),
          ("loop18", 18),
          ("loop19", 19),
          ("loop20", 20),
          ("loop21", 21),
          ("loop22", 22),
          ("loop23", 23),
          ("loop24", 24),
          ("loop25", 25),
          ("loop26", 26),
          ("loop27", 27),
          ("loop28", 28),
          ("loop29", 29),
          ("loop30", 30),
          ("loop31", 31),
          ("loop32", 32),
          ("none", 255))
    )


_AdGenTa5kAtmLMLoopTimingA_Type.__name__ = "Integer32"
_AdGenTa5kAtmLMLoopTimingA_Object = MibTableColumn
adGenTa5kAtmLMLoopTimingA = _AdGenTa5kAtmLMLoopTimingA_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 5, 1, 1),
    _AdGenTa5kAtmLMLoopTimingA_Type()
)
adGenTa5kAtmLMLoopTimingA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMLoopTimingA.setStatus("current")


class _AdGenTa5kAtmLMLoopTimingB_Type(Integer32):
    """Custom type adGenTa5kAtmLMLoopTimingB based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("loop1", 1),
          ("loop2", 2),
          ("loop3", 3),
          ("loop4", 4),
          ("loop5", 5),
          ("loop6", 6),
          ("loop7", 7),
          ("loop8", 8),
          ("loop9", 9),
          ("loop10", 10),
          ("loop11", 11),
          ("loop12", 12),
          ("loop13", 13),
          ("loop14", 14),
          ("loop15", 15),
          ("loop16", 16),
          ("loop17", 17),
          ("loop18", 18),
          ("loop19", 19),
          ("loop20", 20),
          ("loop21", 21),
          ("loop22", 22),
          ("loop23", 23),
          ("loop24", 24),
          ("loop25", 25),
          ("loop26", 26),
          ("loop27", 27),
          ("loop28", 28),
          ("loop29", 29),
          ("loop30", 30),
          ("loop31", 31),
          ("loop32", 32),
          ("none", 255))
    )


_AdGenTa5kAtmLMLoopTimingB_Type.__name__ = "Integer32"
_AdGenTa5kAtmLMLoopTimingB_Object = MibTableColumn
adGenTa5kAtmLMLoopTimingB = _AdGenTa5kAtmLMLoopTimingB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 2, 5, 1, 2),
    _AdGenTa5kAtmLMLoopTimingB_Type()
)
adGenTa5kAtmLMLoopTimingB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMLoopTimingB.setStatus("current")
_AdGenTa5kAtmLMPMStats_ObjectIdentity = ObjectIdentity
adGenTa5kAtmLMPMStats = _AdGenTa5kAtmLMPMStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3)
)
_AdGenTa5kAtmPortStatsCurrentTable_Object = MibTable
adGenTa5kAtmPortStatsCurrentTable = _AdGenTa5kAtmPortStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentTable.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentEntry_Object = MibTableRow
adGenTa5kAtmPortStatsCurrentEntry = _AdGenTa5kAtmPortStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1)
)
adGenTa5kAtmPortStatsCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentEntry.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentRxCells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentRxCells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentRxCells = _AdGenTa5kAtmPortStatsCurrentRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 1),
    _AdGenTa5kAtmPortStatsCurrentRxCells_Type()
)
adGenTa5kAtmPortStatsCurrentRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentRxCells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentRxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentRxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentRxClp1Cells = _AdGenTa5kAtmPortStatsCurrentRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 2),
    _AdGenTa5kAtmPortStatsCurrentRxClp1Cells_Type()
)
adGenTa5kAtmPortStatsCurrentRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentRxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentRxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentRxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentRxClp0Cells = _AdGenTa5kAtmPortStatsCurrentRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 3),
    _AdGenTa5kAtmPortStatsCurrentRxClp0Cells_Type()
)
adGenTa5kAtmPortStatsCurrentRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentRxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentRxOamCells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentRxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentRxOamCells = _AdGenTa5kAtmPortStatsCurrentRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 4),
    _AdGenTa5kAtmPortStatsCurrentRxOamCells_Type()
)
adGenTa5kAtmPortStatsCurrentRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentRxOamCells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentTxCells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentTxCells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentTxCells = _AdGenTa5kAtmPortStatsCurrentTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 5),
    _AdGenTa5kAtmPortStatsCurrentTxCells_Type()
)
adGenTa5kAtmPortStatsCurrentTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentTxCells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentTxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentTxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentTxClp1Cells = _AdGenTa5kAtmPortStatsCurrentTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 6),
    _AdGenTa5kAtmPortStatsCurrentTxClp1Cells_Type()
)
adGenTa5kAtmPortStatsCurrentTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentTxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentTxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentTxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentTxClp0Cells = _AdGenTa5kAtmPortStatsCurrentTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 7),
    _AdGenTa5kAtmPortStatsCurrentTxClp0Cells_Type()
)
adGenTa5kAtmPortStatsCurrentTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentTxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentTxOamCells_Type = Counter32
_AdGenTa5kAtmPortStatsCurrentTxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentTxOamCells = _AdGenTa5kAtmPortStatsCurrentTxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 8),
    _AdGenTa5kAtmPortStatsCurrentTxOamCells_Type()
)
adGenTa5kAtmPortStatsCurrentTxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentTxOamCells.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentResetStats_Type = Integer32
_AdGenTa5kAtmPortStatsCurrentResetStats_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentResetStats = _AdGenTa5kAtmPortStatsCurrentResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 9),
    _AdGenTa5kAtmPortStatsCurrentResetStats_Type()
)
adGenTa5kAtmPortStatsCurrentResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentResetStats.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentRxCellsPercentUtil_Type = Gauge32
_AdGenTa5kAtmPortStatsCurrentRxCellsPercentUtil_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentRxCellsPercentUtil = _AdGenTa5kAtmPortStatsCurrentRxCellsPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 10),
    _AdGenTa5kAtmPortStatsCurrentRxCellsPercentUtil_Type()
)
adGenTa5kAtmPortStatsCurrentRxCellsPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentRxCellsPercentUtil.setStatus("current")
_AdGenTa5kAtmPortStatsCurrentTxCellsPercentUtil_Type = Gauge32
_AdGenTa5kAtmPortStatsCurrentTxCellsPercentUtil_Object = MibTableColumn
adGenTa5kAtmPortStatsCurrentTxCellsPercentUtil = _AdGenTa5kAtmPortStatsCurrentTxCellsPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 1, 1, 11),
    _AdGenTa5kAtmPortStatsCurrentTxCellsPercentUtil_Type()
)
adGenTa5kAtmPortStatsCurrentTxCellsPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCurrentTxCellsPercentUtil.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTable_Object = MibTable
adGenTa5kAtmPortStatsIntervalTable = _AdGenTa5kAtmPortStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTable.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalEntry_Object = MibTableRow
adGenTa5kAtmPortStatsIntervalEntry = _AdGenTa5kAtmPortStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1)
)
adGenTa5kAtmPortStatsIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmPortStatsIntervalIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalEntry.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalIndex_Type = Integer32
_AdGenTa5kAtmPortStatsIntervalIndex_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalIndex = _AdGenTa5kAtmPortStatsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 1),
    _AdGenTa5kAtmPortStatsIntervalIndex_Type()
)
adGenTa5kAtmPortStatsIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalIndex.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalRxCells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalRxCells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalRxCells = _AdGenTa5kAtmPortStatsIntervalRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 2),
    _AdGenTa5kAtmPortStatsIntervalRxCells_Type()
)
adGenTa5kAtmPortStatsIntervalRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalRxCells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalRxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalRxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalRxClp1Cells = _AdGenTa5kAtmPortStatsIntervalRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 3),
    _AdGenTa5kAtmPortStatsIntervalRxClp1Cells_Type()
)
adGenTa5kAtmPortStatsIntervalRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalRxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalRxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalRxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalRxClp0Cells = _AdGenTa5kAtmPortStatsIntervalRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 4),
    _AdGenTa5kAtmPortStatsIntervalRxClp0Cells_Type()
)
adGenTa5kAtmPortStatsIntervalRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalRxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalRxOamCells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalRxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalRxOamCells = _AdGenTa5kAtmPortStatsIntervalRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 5),
    _AdGenTa5kAtmPortStatsIntervalRxOamCells_Type()
)
adGenTa5kAtmPortStatsIntervalRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalRxOamCells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTxCells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalTxCells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalTxCells = _AdGenTa5kAtmPortStatsIntervalTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 6),
    _AdGenTa5kAtmPortStatsIntervalTxCells_Type()
)
adGenTa5kAtmPortStatsIntervalTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTxCells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalTxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalTxClp1Cells = _AdGenTa5kAtmPortStatsIntervalTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 7),
    _AdGenTa5kAtmPortStatsIntervalTxClp1Cells_Type()
)
adGenTa5kAtmPortStatsIntervalTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalTxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalTxClp0Cells = _AdGenTa5kAtmPortStatsIntervalTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 8),
    _AdGenTa5kAtmPortStatsIntervalTxClp0Cells_Type()
)
adGenTa5kAtmPortStatsIntervalTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTxOamCells_Type = Counter32
_AdGenTa5kAtmPortStatsIntervalTxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalTxOamCells = _AdGenTa5kAtmPortStatsIntervalTxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 9),
    _AdGenTa5kAtmPortStatsIntervalTxOamCells_Type()
)
adGenTa5kAtmPortStatsIntervalTxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTxOamCells.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTimeStamp_Type = DisplayString
_AdGenTa5kAtmPortStatsIntervalTimeStamp_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalTimeStamp = _AdGenTa5kAtmPortStatsIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 10),
    _AdGenTa5kAtmPortStatsIntervalTimeStamp_Type()
)
adGenTa5kAtmPortStatsIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTimeStamp.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalRxCellsPercentUtil_Type = Gauge32
_AdGenTa5kAtmPortStatsIntervalRxCellsPercentUtil_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalRxCellsPercentUtil = _AdGenTa5kAtmPortStatsIntervalRxCellsPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 11),
    _AdGenTa5kAtmPortStatsIntervalRxCellsPercentUtil_Type()
)
adGenTa5kAtmPortStatsIntervalRxCellsPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalRxCellsPercentUtil.setStatus("current")
_AdGenTa5kAtmPortStatsIntervalTxCellsPercentUtil_Type = Gauge32
_AdGenTa5kAtmPortStatsIntervalTxCellsPercentUtil_Object = MibTableColumn
adGenTa5kAtmPortStatsIntervalTxCellsPercentUtil = _AdGenTa5kAtmPortStatsIntervalTxCellsPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 2, 1, 12),
    _AdGenTa5kAtmPortStatsIntervalTxCellsPercentUtil_Type()
)
adGenTa5kAtmPortStatsIntervalTxCellsPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsIntervalTxCellsPercentUtil.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentTable_Object = MibTable
adGenTa5kAtmPortStats24hrCurrentTable = _AdGenTa5kAtmPortStats24hrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentTable.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentEntry_Object = MibTableRow
adGenTa5kAtmPortStats24hrCurrentEntry = _AdGenTa5kAtmPortStats24hrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1)
)
adGenTa5kAtmPortStats24hrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentEntry.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentRxCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentRxCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentRxCells = _AdGenTa5kAtmPortStats24hrCurrentRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 1),
    _AdGenTa5kAtmPortStats24hrCurrentRxCells_Type()
)
adGenTa5kAtmPortStats24hrCurrentRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentRxCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentRxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentRxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentRxClp1Cells = _AdGenTa5kAtmPortStats24hrCurrentRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 2),
    _AdGenTa5kAtmPortStats24hrCurrentRxClp1Cells_Type()
)
adGenTa5kAtmPortStats24hrCurrentRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentRxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentRxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentRxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentRxClp0Cells = _AdGenTa5kAtmPortStats24hrCurrentRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 3),
    _AdGenTa5kAtmPortStats24hrCurrentRxClp0Cells_Type()
)
adGenTa5kAtmPortStats24hrCurrentRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentRxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentRxOamCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentRxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentRxOamCells = _AdGenTa5kAtmPortStats24hrCurrentRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 4),
    _AdGenTa5kAtmPortStats24hrCurrentRxOamCells_Type()
)
adGenTa5kAtmPortStats24hrCurrentRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentRxOamCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentTxCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentTxCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentTxCells = _AdGenTa5kAtmPortStats24hrCurrentTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 5),
    _AdGenTa5kAtmPortStats24hrCurrentTxCells_Type()
)
adGenTa5kAtmPortStats24hrCurrentTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentTxCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentTxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentTxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentTxClp1Cells = _AdGenTa5kAtmPortStats24hrCurrentTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 6),
    _AdGenTa5kAtmPortStats24hrCurrentTxClp1Cells_Type()
)
adGenTa5kAtmPortStats24hrCurrentTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentTxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentTxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentTxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentTxClp0Cells = _AdGenTa5kAtmPortStats24hrCurrentTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 7),
    _AdGenTa5kAtmPortStats24hrCurrentTxClp0Cells_Type()
)
adGenTa5kAtmPortStats24hrCurrentTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentTxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrCurrentTxOamCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrCurrentTxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrCurrentTxOamCells = _AdGenTa5kAtmPortStats24hrCurrentTxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 3, 1, 8),
    _AdGenTa5kAtmPortStats24hrCurrentTxOamCells_Type()
)
adGenTa5kAtmPortStats24hrCurrentTxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrCurrentTxOamCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrTable_Object = MibTable
adGenTa5kAtmPortStats24hrTable = _AdGenTa5kAtmPortStats24hrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrTable.setStatus("current")
_AdGenTa5kAtmPortStats24hrEntry_Object = MibTableRow
adGenTa5kAtmPortStats24hrEntry = _AdGenTa5kAtmPortStats24hrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1)
)
adGenTa5kAtmPortStats24hrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmPortStats24hrIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrEntry.setStatus("current")
_AdGenTa5kAtmPortStats24hrIndex_Type = Integer32
_AdGenTa5kAtmPortStats24hrIndex_Object = MibTableColumn
adGenTa5kAtmPortStats24hrIndex = _AdGenTa5kAtmPortStats24hrIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 1),
    _AdGenTa5kAtmPortStats24hrIndex_Type()
)
adGenTa5kAtmPortStats24hrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrIndex.setStatus("current")
_AdGenTa5kAtmPortStats24hrRxCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrRxCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrRxCells = _AdGenTa5kAtmPortStats24hrRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 2),
    _AdGenTa5kAtmPortStats24hrRxCells_Type()
)
adGenTa5kAtmPortStats24hrRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrRxCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrRxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrRxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrRxClp1Cells = _AdGenTa5kAtmPortStats24hrRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 3),
    _AdGenTa5kAtmPortStats24hrRxClp1Cells_Type()
)
adGenTa5kAtmPortStats24hrRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrRxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrRxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrRxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrRxClp0Cells = _AdGenTa5kAtmPortStats24hrRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 4),
    _AdGenTa5kAtmPortStats24hrRxClp0Cells_Type()
)
adGenTa5kAtmPortStats24hrRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrRxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrRxOamCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrRxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrRxOamCells = _AdGenTa5kAtmPortStats24hrRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 5),
    _AdGenTa5kAtmPortStats24hrRxOamCells_Type()
)
adGenTa5kAtmPortStats24hrRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrRxOamCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrTxCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrTxCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrTxCells = _AdGenTa5kAtmPortStats24hrTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 6),
    _AdGenTa5kAtmPortStats24hrTxCells_Type()
)
adGenTa5kAtmPortStats24hrTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrTxCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrTxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrTxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrTxClp1Cells = _AdGenTa5kAtmPortStats24hrTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 7),
    _AdGenTa5kAtmPortStats24hrTxClp1Cells_Type()
)
adGenTa5kAtmPortStats24hrTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrTxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrTxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStats24hrTxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrTxClp0Cells = _AdGenTa5kAtmPortStats24hrTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 8),
    _AdGenTa5kAtmPortStats24hrTxClp0Cells_Type()
)
adGenTa5kAtmPortStats24hrTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrTxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStats24hrTxOamCells_Type = Counter32
_AdGenTa5kAtmPortStats24hrTxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStats24hrTxOamCells = _AdGenTa5kAtmPortStats24hrTxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 9),
    _AdGenTa5kAtmPortStats24hrTxOamCells_Type()
)
adGenTa5kAtmPortStats24hrTxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrTxOamCells.setStatus("current")
_AdGenTa5kAtmPortStats24hrTimeStamp_Type = DisplayString
_AdGenTa5kAtmPortStats24hrTimeStamp_Object = MibTableColumn
adGenTa5kAtmPortStats24hrTimeStamp = _AdGenTa5kAtmPortStats24hrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 4, 1, 10),
    _AdGenTa5kAtmPortStats24hrTimeStamp_Type()
)
adGenTa5kAtmPortStats24hrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStats24hrTimeStamp.setStatus("current")
_AdGenTa5kAtmVclStatsTable_Object = MibTable
adGenTa5kAtmVclStatsTable = _AdGenTa5kAtmVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsTable.setStatus("current")
_AdGenTa5kAtmVclStatsEntry_Object = MibTableRow
adGenTa5kAtmVclStatsEntry = _AdGenTa5kAtmVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1)
)
adGenTa5kAtmVclStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsEntry.setStatus("current")
_AdGenTa5kAtmVclStatsResetPM_Type = Integer32
_AdGenTa5kAtmVclStatsResetPM_Object = MibTableColumn
adGenTa5kAtmVclStatsResetPM = _AdGenTa5kAtmVclStatsResetPM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 1),
    _AdGenTa5kAtmVclStatsResetPM_Type()
)
adGenTa5kAtmVclStatsResetPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsResetPM.setStatus("current")


class _AdGenTa5kAtmVclStatsRxAIS_Type(Integer32):
    """Custom type adGenTa5kAtmVclStatsRxAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("na", 3))
    )


_AdGenTa5kAtmVclStatsRxAIS_Type.__name__ = "Integer32"
_AdGenTa5kAtmVclStatsRxAIS_Object = MibTableColumn
adGenTa5kAtmVclStatsRxAIS = _AdGenTa5kAtmVclStatsRxAIS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 2),
    _AdGenTa5kAtmVclStatsRxAIS_Type()
)
adGenTa5kAtmVclStatsRxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsRxAIS.setStatus("current")


class _AdGenTa5kAtmVclStatsRxRDI_Type(Integer32):
    """Custom type adGenTa5kAtmVclStatsRxRDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("na", 3))
    )


_AdGenTa5kAtmVclStatsRxRDI_Type.__name__ = "Integer32"
_AdGenTa5kAtmVclStatsRxRDI_Object = MibTableColumn
adGenTa5kAtmVclStatsRxRDI = _AdGenTa5kAtmVclStatsRxRDI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 3),
    _AdGenTa5kAtmVclStatsRxRDI_Type()
)
adGenTa5kAtmVclStatsRxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsRxRDI.setStatus("current")
_AdGenTa5kAtmVclStatsGenAISRDI_Type = TruthValue
_AdGenTa5kAtmVclStatsGenAISRDI_Object = MibTableColumn
adGenTa5kAtmVclStatsGenAISRDI = _AdGenTa5kAtmVclStatsGenAISRDI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 4),
    _AdGenTa5kAtmVclStatsGenAISRDI_Type()
)
adGenTa5kAtmVclStatsGenAISRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsGenAISRDI.setStatus("current")
_AdGenTa5kAtmVclStatsOamTxLbReqs_Type = Integer32
_AdGenTa5kAtmVclStatsOamTxLbReqs_Object = MibTableColumn
adGenTa5kAtmVclStatsOamTxLbReqs = _AdGenTa5kAtmVclStatsOamTxLbReqs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 5),
    _AdGenTa5kAtmVclStatsOamTxLbReqs_Type()
)
adGenTa5kAtmVclStatsOamTxLbReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsOamTxLbReqs.setStatus("current")
_AdGenTa5kAtmVclStatsOamRxLbReqs_Type = Integer32
_AdGenTa5kAtmVclStatsOamRxLbReqs_Object = MibTableColumn
adGenTa5kAtmVclStatsOamRxLbReqs = _AdGenTa5kAtmVclStatsOamRxLbReqs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 6),
    _AdGenTa5kAtmVclStatsOamRxLbReqs_Type()
)
adGenTa5kAtmVclStatsOamRxLbReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsOamRxLbReqs.setStatus("current")
_AdGenTa5kAtmVclStatsOamTxLbResps_Type = Integer32
_AdGenTa5kAtmVclStatsOamTxLbResps_Object = MibTableColumn
adGenTa5kAtmVclStatsOamTxLbResps = _AdGenTa5kAtmVclStatsOamTxLbResps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 7),
    _AdGenTa5kAtmVclStatsOamTxLbResps_Type()
)
adGenTa5kAtmVclStatsOamTxLbResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsOamTxLbResps.setStatus("current")
_AdGenTa5kAtmVclStatsOamRxLbResps_Type = Integer32
_AdGenTa5kAtmVclStatsOamRxLbResps_Object = MibTableColumn
adGenTa5kAtmVclStatsOamRxLbResps = _AdGenTa5kAtmVclStatsOamRxLbResps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 8),
    _AdGenTa5kAtmVclStatsOamRxLbResps_Type()
)
adGenTa5kAtmVclStatsOamRxLbResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsOamRxLbResps.setStatus("current")
_AdGenTa5kAtmVclStatsOamLbTimeouts_Type = Integer32
_AdGenTa5kAtmVclStatsOamLbTimeouts_Object = MibTableColumn
adGenTa5kAtmVclStatsOamLbTimeouts = _AdGenTa5kAtmVclStatsOamLbTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 9),
    _AdGenTa5kAtmVclStatsOamLbTimeouts_Type()
)
adGenTa5kAtmVclStatsOamLbTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsOamLbTimeouts.setStatus("current")


class _AdGenTa5kAtmVclStatsOamLbLastResult_Type(Integer32):
    """Custom type adGenTa5kAtmVclStatsOamLbLastResult based on Integer32"""
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
        *(("noneSent", 0),
          ("cellOutstanding", 1),
          ("responseReceived", 2),
          ("timedOut", 3))
    )


_AdGenTa5kAtmVclStatsOamLbLastResult_Type.__name__ = "Integer32"
_AdGenTa5kAtmVclStatsOamLbLastResult_Object = MibTableColumn
adGenTa5kAtmVclStatsOamLbLastResult = _AdGenTa5kAtmVclStatsOamLbLastResult_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 10),
    _AdGenTa5kAtmVclStatsOamLbLastResult_Type()
)
adGenTa5kAtmVclStatsOamLbLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsOamLbLastResult.setStatus("current")
_AdGenTa5kAtmVclStatsConnectionInfo_Type = DisplayString
_AdGenTa5kAtmVclStatsConnectionInfo_Object = MibTableColumn
adGenTa5kAtmVclStatsConnectionInfo = _AdGenTa5kAtmVclStatsConnectionInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 5, 1, 11),
    _AdGenTa5kAtmVclStatsConnectionInfo_Type()
)
adGenTa5kAtmVclStatsConnectionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVclStatsConnectionInfo.setStatus("current")
_AdGenTa5kAtmVplStatsTable_Object = MibTable
adGenTa5kAtmVplStatsTable = _AdGenTa5kAtmVplStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsTable.setStatus("current")
_AdGenTa5kAtmVplStatsEntry_Object = MibTableRow
adGenTa5kAtmVplStatsEntry = _AdGenTa5kAtmVplStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1)
)
adGenTa5kAtmVplStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsEntry.setStatus("current")
_AdGenTa5kAtmVplStatsResetPM_Type = Integer32
_AdGenTa5kAtmVplStatsResetPM_Object = MibTableColumn
adGenTa5kAtmVplStatsResetPM = _AdGenTa5kAtmVplStatsResetPM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 1),
    _AdGenTa5kAtmVplStatsResetPM_Type()
)
adGenTa5kAtmVplStatsResetPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsResetPM.setStatus("current")


class _AdGenTa5kAtmVplStatsRxAIS_Type(Integer32):
    """Custom type adGenTa5kAtmVplStatsRxAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("na", 3))
    )


_AdGenTa5kAtmVplStatsRxAIS_Type.__name__ = "Integer32"
_AdGenTa5kAtmVplStatsRxAIS_Object = MibTableColumn
adGenTa5kAtmVplStatsRxAIS = _AdGenTa5kAtmVplStatsRxAIS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 2),
    _AdGenTa5kAtmVplStatsRxAIS_Type()
)
adGenTa5kAtmVplStatsRxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsRxAIS.setStatus("current")


class _AdGenTa5kAtmVplStatsRxRDI_Type(Integer32):
    """Custom type adGenTa5kAtmVplStatsRxRDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("na", 3))
    )


_AdGenTa5kAtmVplStatsRxRDI_Type.__name__ = "Integer32"
_AdGenTa5kAtmVplStatsRxRDI_Object = MibTableColumn
adGenTa5kAtmVplStatsRxRDI = _AdGenTa5kAtmVplStatsRxRDI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 3),
    _AdGenTa5kAtmVplStatsRxRDI_Type()
)
adGenTa5kAtmVplStatsRxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsRxRDI.setStatus("current")
_AdGenTa5kAtmVplStatsGenAISRDI_Type = TruthValue
_AdGenTa5kAtmVplStatsGenAISRDI_Object = MibTableColumn
adGenTa5kAtmVplStatsGenAISRDI = _AdGenTa5kAtmVplStatsGenAISRDI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 4),
    _AdGenTa5kAtmVplStatsGenAISRDI_Type()
)
adGenTa5kAtmVplStatsGenAISRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsGenAISRDI.setStatus("current")
_AdGenTa5kAtmVplStatsOamTxLbReqs_Type = Integer32
_AdGenTa5kAtmVplStatsOamTxLbReqs_Object = MibTableColumn
adGenTa5kAtmVplStatsOamTxLbReqs = _AdGenTa5kAtmVplStatsOamTxLbReqs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 5),
    _AdGenTa5kAtmVplStatsOamTxLbReqs_Type()
)
adGenTa5kAtmVplStatsOamTxLbReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsOamTxLbReqs.setStatus("current")
_AdGenTa5kAtmVplStatsOamRxLbReqs_Type = Integer32
_AdGenTa5kAtmVplStatsOamRxLbReqs_Object = MibTableColumn
adGenTa5kAtmVplStatsOamRxLbReqs = _AdGenTa5kAtmVplStatsOamRxLbReqs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 6),
    _AdGenTa5kAtmVplStatsOamRxLbReqs_Type()
)
adGenTa5kAtmVplStatsOamRxLbReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsOamRxLbReqs.setStatus("current")
_AdGenTa5kAtmVplStatsOamTxLbResps_Type = Integer32
_AdGenTa5kAtmVplStatsOamTxLbResps_Object = MibTableColumn
adGenTa5kAtmVplStatsOamTxLbResps = _AdGenTa5kAtmVplStatsOamTxLbResps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 7),
    _AdGenTa5kAtmVplStatsOamTxLbResps_Type()
)
adGenTa5kAtmVplStatsOamTxLbResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsOamTxLbResps.setStatus("current")
_AdGenTa5kAtmVplStatsOamRxLbResps_Type = Integer32
_AdGenTa5kAtmVplStatsOamRxLbResps_Object = MibTableColumn
adGenTa5kAtmVplStatsOamRxLbResps = _AdGenTa5kAtmVplStatsOamRxLbResps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 8),
    _AdGenTa5kAtmVplStatsOamRxLbResps_Type()
)
adGenTa5kAtmVplStatsOamRxLbResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsOamRxLbResps.setStatus("current")
_AdGenTa5kAtmVplStatsOamLbTimeouts_Type = Integer32
_AdGenTa5kAtmVplStatsOamLbTimeouts_Object = MibTableColumn
adGenTa5kAtmVplStatsOamLbTimeouts = _AdGenTa5kAtmVplStatsOamLbTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 9),
    _AdGenTa5kAtmVplStatsOamLbTimeouts_Type()
)
adGenTa5kAtmVplStatsOamLbTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsOamLbTimeouts.setStatus("current")


class _AdGenTa5kAtmVplStatsOamLbLastResult_Type(Integer32):
    """Custom type adGenTa5kAtmVplStatsOamLbLastResult based on Integer32"""
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
        *(("noneSent", 0),
          ("cellOutstanding", 1),
          ("responseReceived", 2),
          ("timedOut", 3))
    )


_AdGenTa5kAtmVplStatsOamLbLastResult_Type.__name__ = "Integer32"
_AdGenTa5kAtmVplStatsOamLbLastResult_Object = MibTableColumn
adGenTa5kAtmVplStatsOamLbLastResult = _AdGenTa5kAtmVplStatsOamLbLastResult_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 10),
    _AdGenTa5kAtmVplStatsOamLbLastResult_Type()
)
adGenTa5kAtmVplStatsOamLbLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsOamLbLastResult.setStatus("current")
_AdGenTa5kAtmVplStatsAal5InPkts_Type = Counter32
_AdGenTa5kAtmVplStatsAal5InPkts_Object = MibTableColumn
adGenTa5kAtmVplStatsAal5InPkts = _AdGenTa5kAtmVplStatsAal5InPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 11),
    _AdGenTa5kAtmVplStatsAal5InPkts_Type()
)
adGenTa5kAtmVplStatsAal5InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsAal5InPkts.setStatus("current")
_AdGenTa5kAtmVplStatsAal5OutPkts_Type = Counter32
_AdGenTa5kAtmVplStatsAal5OutPkts_Object = MibTableColumn
adGenTa5kAtmVplStatsAal5OutPkts = _AdGenTa5kAtmVplStatsAal5OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 12),
    _AdGenTa5kAtmVplStatsAal5OutPkts_Type()
)
adGenTa5kAtmVplStatsAal5OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsAal5OutPkts.setStatus("current")
_AdGenTa5kAtmVplStatsAal5InOctets_Type = Counter32
_AdGenTa5kAtmVplStatsAal5InOctets_Object = MibTableColumn
adGenTa5kAtmVplStatsAal5InOctets = _AdGenTa5kAtmVplStatsAal5InOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 13),
    _AdGenTa5kAtmVplStatsAal5InOctets_Type()
)
adGenTa5kAtmVplStatsAal5InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsAal5InOctets.setStatus("current")
_AdGenTa5kAtmVplStatsAal5OutOctets_Type = Counter32
_AdGenTa5kAtmVplStatsAal5OutOctets_Object = MibTableColumn
adGenTa5kAtmVplStatsAal5OutOctets = _AdGenTa5kAtmVplStatsAal5OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 14),
    _AdGenTa5kAtmVplStatsAal5OutOctets_Type()
)
adGenTa5kAtmVplStatsAal5OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsAal5OutOctets.setStatus("current")
_AdGenTa5kAtmVplStatsConnectionInfo_Type = DisplayString
_AdGenTa5kAtmVplStatsConnectionInfo_Object = MibTableColumn
adGenTa5kAtmVplStatsConnectionInfo = _AdGenTa5kAtmVplStatsConnectionInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 6, 1, 15),
    _AdGenTa5kAtmVplStatsConnectionInfo_Type()
)
adGenTa5kAtmVplStatsConnectionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVplStatsConnectionInfo.setStatus("current")
_AdGenTa5kAtmPortStatsTable_Object = MibTable
adGenTa5kAtmPortStatsTable = _AdGenTa5kAtmPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsTable.setStatus("current")
_AdGenTa5kAtmPortStatsEntry_Object = MibTableRow
adGenTa5kAtmPortStatsEntry = _AdGenTa5kAtmPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1)
)
adGenTa5kAtmPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsEntry.setStatus("current")
_AdGenTa5kAtmPortStatsRxCells_Type = Counter32
_AdGenTa5kAtmPortStatsRxCells_Object = MibTableColumn
adGenTa5kAtmPortStatsRxCells = _AdGenTa5kAtmPortStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 1),
    _AdGenTa5kAtmPortStatsRxCells_Type()
)
adGenTa5kAtmPortStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsRxCells.setStatus("current")
_AdGenTa5kAtmPortStatsRxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStatsRxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsRxClp1Cells = _AdGenTa5kAtmPortStatsRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 2),
    _AdGenTa5kAtmPortStatsRxClp1Cells_Type()
)
adGenTa5kAtmPortStatsRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsRxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStatsRxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStatsRxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsRxClp0Cells = _AdGenTa5kAtmPortStatsRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 3),
    _AdGenTa5kAtmPortStatsRxClp0Cells_Type()
)
adGenTa5kAtmPortStatsRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsRxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStatsRxOamCells_Type = Counter32
_AdGenTa5kAtmPortStatsRxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStatsRxOamCells = _AdGenTa5kAtmPortStatsRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 4),
    _AdGenTa5kAtmPortStatsRxOamCells_Type()
)
adGenTa5kAtmPortStatsRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsRxOamCells.setStatus("current")
_AdGenTa5kAtmPortStatsTxCells_Type = Counter32
_AdGenTa5kAtmPortStatsTxCells_Object = MibTableColumn
adGenTa5kAtmPortStatsTxCells = _AdGenTa5kAtmPortStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 5),
    _AdGenTa5kAtmPortStatsTxCells_Type()
)
adGenTa5kAtmPortStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsTxCells.setStatus("current")
_AdGenTa5kAtmPortStatsTxClp1Cells_Type = Counter32
_AdGenTa5kAtmPortStatsTxClp1Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsTxClp1Cells = _AdGenTa5kAtmPortStatsTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 6),
    _AdGenTa5kAtmPortStatsTxClp1Cells_Type()
)
adGenTa5kAtmPortStatsTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsTxClp1Cells.setStatus("current")
_AdGenTa5kAtmPortStatsTxClp0Cells_Type = Counter32
_AdGenTa5kAtmPortStatsTxClp0Cells_Object = MibTableColumn
adGenTa5kAtmPortStatsTxClp0Cells = _AdGenTa5kAtmPortStatsTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 7),
    _AdGenTa5kAtmPortStatsTxClp0Cells_Type()
)
adGenTa5kAtmPortStatsTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsTxClp0Cells.setStatus("current")
_AdGenTa5kAtmPortStatsTxOamCells_Type = Counter32
_AdGenTa5kAtmPortStatsTxOamCells_Object = MibTableColumn
adGenTa5kAtmPortStatsTxOamCells = _AdGenTa5kAtmPortStatsTxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 8),
    _AdGenTa5kAtmPortStatsTxOamCells_Type()
)
adGenTa5kAtmPortStatsTxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsTxOamCells.setStatus("current")


class _AdGenTa5kAtmPortStatsResetStats_Type(Integer32):
    """Custom type adGenTa5kAtmPortStatsResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenTa5kAtmPortStatsResetStats_Type.__name__ = "Integer32"
_AdGenTa5kAtmPortStatsResetStats_Object = MibTableColumn
adGenTa5kAtmPortStatsResetStats = _AdGenTa5kAtmPortStatsResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 9),
    _AdGenTa5kAtmPortStatsResetStats_Type()
)
adGenTa5kAtmPortStatsResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsResetStats.setStatus("current")
_AdGenTa5kAtmPortStatsCellDelineation_Type = TruthValue
_AdGenTa5kAtmPortStatsCellDelineation_Object = MibTableColumn
adGenTa5kAtmPortStatsCellDelineation = _AdGenTa5kAtmPortStatsCellDelineation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 7, 1, 10),
    _AdGenTa5kAtmPortStatsCellDelineation_Type()
)
adGenTa5kAtmPortStatsCellDelineation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmPortStatsCellDelineation.setStatus("current")
_AdGenTa5kAtmDhcpStatsCurrentTable_Object = MibTable
adGenTa5kAtmDhcpStatsCurrentTable = _AdGenTa5kAtmDhcpStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 8)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsCurrentTable.setStatus("current")
_AdGenTa5kAtmDhcpStatsCurrentEntry_Object = MibTableRow
adGenTa5kAtmDhcpStatsCurrentEntry = _AdGenTa5kAtmDhcpStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 8, 1)
)
adGenTa5kAtmDhcpStatsCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsCurrentEntry.setStatus("current")
_AdGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt = _AdGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 8, 1, 1),
    _AdGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt = _AdGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 8, 1, 2),
    _AdGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 8, 1, 3),
    _AdGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 8, 1, 4),
    _AdGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalTable_Object = MibTable
adGenTa5kAtmDhcpStatsIntervalTable = _AdGenTa5kAtmDhcpStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalTable.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalEntry_Object = MibTableRow
adGenTa5kAtmDhcpStatsIntervalEntry = _AdGenTa5kAtmDhcpStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1)
)
adGenTa5kAtmDhcpStatsIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmDhcpStatsIntervalIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalEntry.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalIndex_Type = Integer32
_AdGenTa5kAtmDhcpStatsIntervalIndex_Object = MibTableColumn
adGenTa5kAtmDhcpStatsIntervalIndex = _AdGenTa5kAtmDhcpStatsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1, 1),
    _AdGenTa5kAtmDhcpStatsIntervalIndex_Type()
)
adGenTa5kAtmDhcpStatsIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalIndex.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt = _AdGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1, 2),
    _AdGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt = _AdGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1, 3),
    _AdGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1, 4),
    _AdGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1, 5),
    _AdGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsIntervalTimeStamp_Type = DisplayString
_AdGenTa5kAtmDhcpStatsIntervalTimeStamp_Object = MibTableColumn
adGenTa5kAtmDhcpStatsIntervalTimeStamp = _AdGenTa5kAtmDhcpStatsIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 9, 1, 6),
    _AdGenTa5kAtmDhcpStatsIntervalTimeStamp_Type()
)
adGenTa5kAtmDhcpStatsIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsIntervalTimeStamp.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrCurrentTable_Object = MibTable
adGenTa5kAtmDhcpStats24hrCurrentTable = _AdGenTa5kAtmDhcpStats24hrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 10)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrCurrentTable.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrCurrentEntry_Object = MibTableRow
adGenTa5kAtmDhcpStats24hrCurrentEntry = _AdGenTa5kAtmDhcpStats24hrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 10, 1)
)
adGenTa5kAtmDhcpStats24hrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrCurrentEntry.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt = _AdGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 10, 1, 1),
    _AdGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt = _AdGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 10, 1, 2),
    _AdGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 10, 1, 3),
    _AdGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 10, 1, 4),
    _AdGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrTable_Object = MibTable
adGenTa5kAtmDhcpStats24hrTable = _AdGenTa5kAtmDhcpStats24hrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrTable.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrEntry_Object = MibTableRow
adGenTa5kAtmDhcpStats24hrEntry = _AdGenTa5kAtmDhcpStats24hrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1)
)
adGenTa5kAtmDhcpStats24hrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmDhcpStats24hrIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrEntry.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrIndex_Type = Integer32
_AdGenTa5kAtmDhcpStats24hrIndex_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrIndex = _AdGenTa5kAtmDhcpStats24hrIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1, 1),
    _AdGenTa5kAtmDhcpStats24hrIndex_Type()
)
adGenTa5kAtmDhcpStats24hrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrIndex.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt = _AdGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1, 2),
    _AdGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt = _AdGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1, 3),
    _AdGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1, 4),
    _AdGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1, 5),
    _AdGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStats24hrTimeStamp_Type = DisplayString
_AdGenTa5kAtmDhcpStats24hrTimeStamp_Object = MibTableColumn
adGenTa5kAtmDhcpStats24hrTimeStamp = _AdGenTa5kAtmDhcpStats24hrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 11, 1, 6),
    _AdGenTa5kAtmDhcpStats24hrTimeStamp_Type()
)
adGenTa5kAtmDhcpStats24hrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStats24hrTimeStamp.setStatus("current")
_AdGenTa5kAtmDhcpStatsTable_Object = MibTable
adGenTa5kAtmDhcpStatsTable = _AdGenTa5kAtmDhcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 12)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsTable.setStatus("current")
_AdGenTa5kAtmDhcpStatsEntry_Object = MibTableRow
adGenTa5kAtmDhcpStatsEntry = _AdGenTa5kAtmDhcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 12, 1)
)
adGenTa5kAtmDhcpStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsEntry.setStatus("current")
_AdGenTa5kAtmDhcpStatsUpstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsUpstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsUpstreamFwdPktCnt = _AdGenTa5kAtmDhcpStatsUpstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 12, 1, 1),
    _AdGenTa5kAtmDhcpStatsUpstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStatsUpstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsUpstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsDownstreamFwdPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsDownstreamFwdPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsDownstreamFwdPktCnt = _AdGenTa5kAtmDhcpStatsDownstreamFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 12, 1, 2),
    _AdGenTa5kAtmDhcpStatsDownstreamFwdPktCnt_Type()
)
adGenTa5kAtmDhcpStatsDownstreamFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsDownstreamFwdPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 12, 1, 3),
    _AdGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt = _AdGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 12, 1, 4),
    _AdGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt_Type()
)
adGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsCurrentTable_Object = MibTable
adGenTa5kAtmDhcpPerCardStatsCurrentTable = _AdGenTa5kAtmDhcpPerCardStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 13)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsCurrentTable.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsCurrentEntry_Object = MibTableRow
adGenTa5kAtmDhcpPerCardStatsCurrentEntry = _AdGenTa5kAtmDhcpPerCardStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 13, 1)
)
adGenTa5kAtmDhcpPerCardStatsCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsCurrentEntry.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 13, 1, 1),
    _AdGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 13, 1, 2),
    _AdGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsIntervalTable_Object = MibTable
adGenTa5kAtmDhcpPerCardStatsIntervalTable = _AdGenTa5kAtmDhcpPerCardStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 14)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsIntervalTable.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsIntervalEntry_Object = MibTableRow
adGenTa5kAtmDhcpPerCardStatsIntervalEntry = _AdGenTa5kAtmDhcpPerCardStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 14, 1)
)
adGenTa5kAtmDhcpPerCardStatsIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmDhcpPerCardStatsIntervalIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsIntervalEntry.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsIntervalIndex_Type = Integer32
_AdGenTa5kAtmDhcpPerCardStatsIntervalIndex_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsIntervalIndex = _AdGenTa5kAtmDhcpPerCardStatsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 14, 1, 1),
    _AdGenTa5kAtmDhcpPerCardStatsIntervalIndex_Type()
)
adGenTa5kAtmDhcpPerCardStatsIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsIntervalIndex.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 14, 1, 2),
    _AdGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 14, 1, 3),
    _AdGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp_Type = DisplayString
_AdGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp = _AdGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 14, 1, 4),
    _AdGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp_Type()
)
adGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrCurrentTable_Object = MibTable
adGenTa5kAtmDhcpPerCardStats24hrCurrentTable = _AdGenTa5kAtmDhcpPerCardStats24hrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 15)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrCurrentTable.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrCurrentEntry_Object = MibTableRow
adGenTa5kAtmDhcpPerCardStats24hrCurrentEntry = _AdGenTa5kAtmDhcpPerCardStats24hrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 15, 1)
)
adGenTa5kAtmDhcpPerCardStats24hrCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrCurrentEntry.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 15, 1, 1),
    _AdGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 15, 1, 2),
    _AdGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrTable_Object = MibTable
adGenTa5kAtmDhcpPerCardStats24hrTable = _AdGenTa5kAtmDhcpPerCardStats24hrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 16)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrTable.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrEntry_Object = MibTableRow
adGenTa5kAtmDhcpPerCardStats24hrEntry = _AdGenTa5kAtmDhcpPerCardStats24hrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 16, 1)
)
adGenTa5kAtmDhcpPerCardStats24hrEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmDhcpPerCardStats24hrIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrEntry.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrIndex_Type = Integer32
_AdGenTa5kAtmDhcpPerCardStats24hrIndex_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStats24hrIndex = _AdGenTa5kAtmDhcpPerCardStats24hrIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 16, 1, 1),
    _AdGenTa5kAtmDhcpPerCardStats24hrIndex_Type()
)
adGenTa5kAtmDhcpPerCardStats24hrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrIndex.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 16, 1, 2),
    _AdGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 16, 1, 3),
    _AdGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStats24hrTimeStamp_Type = DisplayString
_AdGenTa5kAtmDhcpPerCardStats24hrTimeStamp_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStats24hrTimeStamp = _AdGenTa5kAtmDhcpPerCardStats24hrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 16, 1, 4),
    _AdGenTa5kAtmDhcpPerCardStats24hrTimeStamp_Type()
)
adGenTa5kAtmDhcpPerCardStats24hrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStats24hrTimeStamp.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsTable_Object = MibTable
adGenTa5kAtmDhcpPerCardStatsTable = _AdGenTa5kAtmDhcpPerCardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 17)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsTable.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsEntry_Object = MibTableRow
adGenTa5kAtmDhcpPerCardStatsEntry = _AdGenTa5kAtmDhcpPerCardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 17, 1)
)
adGenTa5kAtmDhcpPerCardStatsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsEntry.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 17, 1, 1),
    _AdGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt_Type = Counter32
_AdGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt_Object = MibTableColumn
adGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt = _AdGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 3, 17, 1, 2),
    _AdGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt_Type()
)
adGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt.setStatus("current")
_AdGenTa5kAtmLMVpStatus_ObjectIdentity = ObjectIdentity
adGenTa5kAtmLMVpStatus = _AdGenTa5kAtmLMVpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4)
)
_AdGenTa5kAtmLMErrorVcTable_Object = MibTable
adGenTa5kAtmLMErrorVcTable = _AdGenTa5kAtmLMErrorVcTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMErrorVcTable.setStatus("current")
_AdGenTa5kAtmLMErrorVcEntry_Object = MibTableRow
adGenTa5kAtmLMErrorVcEntry = _AdGenTa5kAtmLMErrorVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 1, 1)
)
adGenTa5kAtmLMErrorVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMErrorVcEntry.setStatus("current")
_AdGenTa5kAtmLMRecentErrorVC_Type = DisplayString
_AdGenTa5kAtmLMRecentErrorVC_Object = MibTableColumn
adGenTa5kAtmLMRecentErrorVC = _AdGenTa5kAtmLMRecentErrorVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 1, 1, 1),
    _AdGenTa5kAtmLMRecentErrorVC_Type()
)
adGenTa5kAtmLMRecentErrorVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMRecentErrorVC.setStatus("current")


class _AdGenTa5kAtmLMRecentErrorVCClear_Type(Integer32):
    """Custom type adGenTa5kAtmLMRecentErrorVCClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenTa5kAtmLMRecentErrorVCClear_Type.__name__ = "Integer32"
_AdGenTa5kAtmLMRecentErrorVCClear_Object = MibTableColumn
adGenTa5kAtmLMRecentErrorVCClear = _AdGenTa5kAtmLMRecentErrorVCClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 1, 1, 2),
    _AdGenTa5kAtmLMRecentErrorVCClear_Type()
)
adGenTa5kAtmLMRecentErrorVCClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmLMRecentErrorVCClear.setStatus("current")
_AdGenTa5kAtmVpStatusTable_Object = MibTable
adGenTa5kAtmVpStatusTable = _AdGenTa5kAtmVpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 2)
)
if mibBuilder.loadTexts:
    adGenTa5kAtmVpStatusTable.setStatus("current")
_AdGenTa5kAtmVpStatusEntry_Object = MibTableRow
adGenTa5kAtmVpStatusEntry = _AdGenTa5kAtmVpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 2, 1)
)
adGenTa5kAtmVpStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    adGenTa5kAtmVpStatusEntry.setStatus("current")


class _AdGenTa5kAtmVpStatusVc_Type(Integer32):
    """Custom type adGenTa5kAtmVpStatusVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("missing", 2))
    )


_AdGenTa5kAtmVpStatusVc_Type.__name__ = "Integer32"
_AdGenTa5kAtmVpStatusVc_Object = MibTableColumn
adGenTa5kAtmVpStatusVc = _AdGenTa5kAtmVpStatusVc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 2, 1, 1),
    _AdGenTa5kAtmVpStatusVc_Type()
)
adGenTa5kAtmVpStatusVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVpStatusVc.setStatus("current")


class _AdGenTa5kAtmVpStatusVcEncaps_Type(Integer32):
    """Custom type adGenTa5kAtmVpStatusVcEncaps based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("vcmuxrouted", 1),
          ("vcmuxbridged8023", 2),
          ("vcmuxbridged8025", 3),
          ("vcmuxbridged8026", 4),
          ("lanemul8023", 5),
          ("lanemul8025", 6),
          ("llcencap", 7),
          ("framerelay", 8),
          ("other", 9),
          ("unknown", 10),
          ("vcmuxpppoapppoeiw", 11),
          ("llcpppoapppoeiw", 12),
          ("llcautodiscover", 13))
    )


_AdGenTa5kAtmVpStatusVcEncaps_Type.__name__ = "Integer32"
_AdGenTa5kAtmVpStatusVcEncaps_Object = MibTableColumn
adGenTa5kAtmVpStatusVcEncaps = _AdGenTa5kAtmVpStatusVcEncaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 2, 1, 2),
    _AdGenTa5kAtmVpStatusVcEncaps_Type()
)
adGenTa5kAtmVpStatusVcEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kAtmVpStatusVcEncaps.setStatus("current")


class _AdGenTa5kAtmVpStatusVcDelete_Type(Integer32):
    """Custom type adGenTa5kAtmVpStatusVcDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_AdGenTa5kAtmVpStatusVcDelete_Type.__name__ = "Integer32"
_AdGenTa5kAtmVpStatusVcDelete_Object = MibTableColumn
adGenTa5kAtmVpStatusVcDelete = _AdGenTa5kAtmVpStatusVcDelete_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 4, 2, 1, 3),
    _AdGenTa5kAtmVpStatusVcDelete_Type()
)
adGenTa5kAtmVpStatusVcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kAtmVpStatusVcDelete.setStatus("current")
_AdGenTa5kAtmLMAlarmPrefix_ObjectIdentity = ObjectIdentity
adGenTa5kAtmLMAlarmPrefix = _AdGenTa5kAtmLMAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 5)
)
_AdGenTa5kAtmLMAlarm_ObjectIdentity = ObjectIdentity
adGenTa5kAtmLMAlarm = _AdGenTa5kAtmLMAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 5, 0)
)

# Managed Objects groups


# Notification objects

adGenTa5kAtmLMUnlearnableVCL = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 14, 5, 0, 1)
)
adGenTa5kAtmLMUnlearnableVCL.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TA5K-ATM-LM-MIB", "adGenTa5kAtmLMRecentErrorVC"))
)
if mibBuilder.loadTexts:
    adGenTa5kAtmLMUnlearnableVCL.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-ATM-LM-MIB",
    **{"adGenTa5kAtmLMConfig": adGenTa5kAtmLMConfig,
       "adGenTa5kAtmLMConfigTable": adGenTa5kAtmLMConfigTable,
       "adGenTa5kAtmLMConfigEntry": adGenTa5kAtmLMConfigEntry,
       "adGenTa5kAtmLMConfigBootCodeRev": adGenTa5kAtmLMConfigBootCodeRev,
       "adGenTa5kAtmLMConfigSystemSWRev": adGenTa5kAtmLMConfigSystemSWRev,
       "adGenTa5kAtmLMConfigBootSysSWRev": adGenTa5kAtmLMConfigBootSysSWRev,
       "adGenTa5kAtmLMConfigMacAddress": adGenTa5kAtmLMConfigMacAddress,
       "adGenTa5kAtmLMConfigFPGARev": adGenTa5kAtmLMConfigFPGARev,
       "adGenTa5kAtmLMConfigCPLDRev": adGenTa5kAtmLMConfigCPLDRev,
       "adGenTa5kAtmLMConfigWDDIRev": adGenTa5kAtmLMConfigWDDIRev,
       "adGenTa5kAtmLMConfigDPSRev": adGenTa5kAtmLMConfigDPSRev,
       "adGenTa5kAtmLMProvisioning": adGenTa5kAtmLMProvisioning,
       "adGenTa5kAtmPortProvisioningTable": adGenTa5kAtmPortProvisioningTable,
       "adGenTa5kAtmPortProvisioningEntry": adGenTa5kAtmPortProvisioningEntry,
       "adGenTa5kAtmPortProvPortID": adGenTa5kAtmPortProvPortID,
       "adGenTa5kAtmPortProvPortType": adGenTa5kAtmPortProvPortType,
       "adGenTa5kAtmPortProvScrambler": adGenTa5kAtmPortProvScrambler,
       "adGenTa5kAtmPortProvIdleCellType": adGenTa5kAtmPortProvIdleCellType,
       "adGenTa5kAtmPortProvMaxVccs": adGenTa5kAtmPortProvMaxVccs,
       "adGenTa5kAtmPortProvAISRDIGen": adGenTa5kAtmPortProvAISRDIGen,
       "adGenTa5kAtmPortProvInterfaceMode": adGenTa5kAtmPortProvInterfaceMode,
       "adGenTa5kAtmPortProvDhcpCircuitIdFormat": adGenTa5kAtmPortProvDhcpCircuitIdFormat,
       "adGenTa5kAtmPortProvShapingUBR": adGenTa5kAtmPortProvShapingUBR,
       "adGenTa5kManagementChannelTable": adGenTa5kManagementChannelTable,
       "adGenTa5kManagementChannelEntry": adGenTa5kManagementChannelEntry,
       "adGenTa5kManagementChannelVpi": adGenTa5kManagementChannelVpi,
       "adGenTa5kManagementChannelVci": adGenTa5kManagementChannelVci,
       "adGenTa5kManagementChannelMode": adGenTa5kManagementChannelMode,
       "adGenTa5kManagementChannelEncap": adGenTa5kManagementChannelEncap,
       "adGenTa5kManagementChannelMultiplex": adGenTa5kManagementChannelMultiplex,
       "adGenTa5kManagementChannelEnable": adGenTa5kManagementChannelEnable,
       "adGenTa5kManagementChannelPort": adGenTa5kManagementChannelPort,
       "adGenTa5kAtmLMSWUploadTable": adGenTa5kAtmLMSWUploadTable,
       "adGenTa5kAtmLMSWUploadEntry": adGenTa5kAtmLMSWUploadEntry,
       "adGenTa5kAtmLMReboot": adGenTa5kAtmLMReboot,
       "adGenTa5kAtmLMCardProvTable": adGenTa5kAtmLMCardProvTable,
       "adGenTa5kAtmLMCardProvEntry": adGenTa5kAtmLMCardProvEntry,
       "adGenTa5kAtmLMCardProvLearningMode": adGenTa5kAtmLMCardProvLearningMode,
       "adGenTa5kAtmLMCardVclLearnedCount": adGenTa5kAtmLMCardVclLearnedCount,
       "adGenTa5kAtmLMCardCurrentOAMID": adGenTa5kAtmLMCardCurrentOAMID,
       "adGenTa5kAtmLMCardFutureOAMID": adGenTa5kAtmLMCardFutureOAMID,
       "adGenTa5kAtmLMCardResetDHCPPMStats": adGenTa5kAtmLMCardResetDHCPPMStats,
       "adGenTa5kAtmLMCardResetDHCPRollingCounters": adGenTa5kAtmLMCardResetDHCPRollingCounters,
       "adGenTa5kAtmLMLoopTimingTable": adGenTa5kAtmLMLoopTimingTable,
       "adGenTa5kAtmLMLoopTimingEntry": adGenTa5kAtmLMLoopTimingEntry,
       "adGenTa5kAtmLMLoopTimingA": adGenTa5kAtmLMLoopTimingA,
       "adGenTa5kAtmLMLoopTimingB": adGenTa5kAtmLMLoopTimingB,
       "adGenTa5kAtmLMPMStats": adGenTa5kAtmLMPMStats,
       "adGenTa5kAtmPortStatsCurrentTable": adGenTa5kAtmPortStatsCurrentTable,
       "adGenTa5kAtmPortStatsCurrentEntry": adGenTa5kAtmPortStatsCurrentEntry,
       "adGenTa5kAtmPortStatsCurrentRxCells": adGenTa5kAtmPortStatsCurrentRxCells,
       "adGenTa5kAtmPortStatsCurrentRxClp1Cells": adGenTa5kAtmPortStatsCurrentRxClp1Cells,
       "adGenTa5kAtmPortStatsCurrentRxClp0Cells": adGenTa5kAtmPortStatsCurrentRxClp0Cells,
       "adGenTa5kAtmPortStatsCurrentRxOamCells": adGenTa5kAtmPortStatsCurrentRxOamCells,
       "adGenTa5kAtmPortStatsCurrentTxCells": adGenTa5kAtmPortStatsCurrentTxCells,
       "adGenTa5kAtmPortStatsCurrentTxClp1Cells": adGenTa5kAtmPortStatsCurrentTxClp1Cells,
       "adGenTa5kAtmPortStatsCurrentTxClp0Cells": adGenTa5kAtmPortStatsCurrentTxClp0Cells,
       "adGenTa5kAtmPortStatsCurrentTxOamCells": adGenTa5kAtmPortStatsCurrentTxOamCells,
       "adGenTa5kAtmPortStatsCurrentResetStats": adGenTa5kAtmPortStatsCurrentResetStats,
       "adGenTa5kAtmPortStatsCurrentRxCellsPercentUtil": adGenTa5kAtmPortStatsCurrentRxCellsPercentUtil,
       "adGenTa5kAtmPortStatsCurrentTxCellsPercentUtil": adGenTa5kAtmPortStatsCurrentTxCellsPercentUtil,
       "adGenTa5kAtmPortStatsIntervalTable": adGenTa5kAtmPortStatsIntervalTable,
       "adGenTa5kAtmPortStatsIntervalEntry": adGenTa5kAtmPortStatsIntervalEntry,
       "adGenTa5kAtmPortStatsIntervalIndex": adGenTa5kAtmPortStatsIntervalIndex,
       "adGenTa5kAtmPortStatsIntervalRxCells": adGenTa5kAtmPortStatsIntervalRxCells,
       "adGenTa5kAtmPortStatsIntervalRxClp1Cells": adGenTa5kAtmPortStatsIntervalRxClp1Cells,
       "adGenTa5kAtmPortStatsIntervalRxClp0Cells": adGenTa5kAtmPortStatsIntervalRxClp0Cells,
       "adGenTa5kAtmPortStatsIntervalRxOamCells": adGenTa5kAtmPortStatsIntervalRxOamCells,
       "adGenTa5kAtmPortStatsIntervalTxCells": adGenTa5kAtmPortStatsIntervalTxCells,
       "adGenTa5kAtmPortStatsIntervalTxClp1Cells": adGenTa5kAtmPortStatsIntervalTxClp1Cells,
       "adGenTa5kAtmPortStatsIntervalTxClp0Cells": adGenTa5kAtmPortStatsIntervalTxClp0Cells,
       "adGenTa5kAtmPortStatsIntervalTxOamCells": adGenTa5kAtmPortStatsIntervalTxOamCells,
       "adGenTa5kAtmPortStatsIntervalTimeStamp": adGenTa5kAtmPortStatsIntervalTimeStamp,
       "adGenTa5kAtmPortStatsIntervalRxCellsPercentUtil": adGenTa5kAtmPortStatsIntervalRxCellsPercentUtil,
       "adGenTa5kAtmPortStatsIntervalTxCellsPercentUtil": adGenTa5kAtmPortStatsIntervalTxCellsPercentUtil,
       "adGenTa5kAtmPortStats24hrCurrentTable": adGenTa5kAtmPortStats24hrCurrentTable,
       "adGenTa5kAtmPortStats24hrCurrentEntry": adGenTa5kAtmPortStats24hrCurrentEntry,
       "adGenTa5kAtmPortStats24hrCurrentRxCells": adGenTa5kAtmPortStats24hrCurrentRxCells,
       "adGenTa5kAtmPortStats24hrCurrentRxClp1Cells": adGenTa5kAtmPortStats24hrCurrentRxClp1Cells,
       "adGenTa5kAtmPortStats24hrCurrentRxClp0Cells": adGenTa5kAtmPortStats24hrCurrentRxClp0Cells,
       "adGenTa5kAtmPortStats24hrCurrentRxOamCells": adGenTa5kAtmPortStats24hrCurrentRxOamCells,
       "adGenTa5kAtmPortStats24hrCurrentTxCells": adGenTa5kAtmPortStats24hrCurrentTxCells,
       "adGenTa5kAtmPortStats24hrCurrentTxClp1Cells": adGenTa5kAtmPortStats24hrCurrentTxClp1Cells,
       "adGenTa5kAtmPortStats24hrCurrentTxClp0Cells": adGenTa5kAtmPortStats24hrCurrentTxClp0Cells,
       "adGenTa5kAtmPortStats24hrCurrentTxOamCells": adGenTa5kAtmPortStats24hrCurrentTxOamCells,
       "adGenTa5kAtmPortStats24hrTable": adGenTa5kAtmPortStats24hrTable,
       "adGenTa5kAtmPortStats24hrEntry": adGenTa5kAtmPortStats24hrEntry,
       "adGenTa5kAtmPortStats24hrIndex": adGenTa5kAtmPortStats24hrIndex,
       "adGenTa5kAtmPortStats24hrRxCells": adGenTa5kAtmPortStats24hrRxCells,
       "adGenTa5kAtmPortStats24hrRxClp1Cells": adGenTa5kAtmPortStats24hrRxClp1Cells,
       "adGenTa5kAtmPortStats24hrRxClp0Cells": adGenTa5kAtmPortStats24hrRxClp0Cells,
       "adGenTa5kAtmPortStats24hrRxOamCells": adGenTa5kAtmPortStats24hrRxOamCells,
       "adGenTa5kAtmPortStats24hrTxCells": adGenTa5kAtmPortStats24hrTxCells,
       "adGenTa5kAtmPortStats24hrTxClp1Cells": adGenTa5kAtmPortStats24hrTxClp1Cells,
       "adGenTa5kAtmPortStats24hrTxClp0Cells": adGenTa5kAtmPortStats24hrTxClp0Cells,
       "adGenTa5kAtmPortStats24hrTxOamCells": adGenTa5kAtmPortStats24hrTxOamCells,
       "adGenTa5kAtmPortStats24hrTimeStamp": adGenTa5kAtmPortStats24hrTimeStamp,
       "adGenTa5kAtmVclStatsTable": adGenTa5kAtmVclStatsTable,
       "adGenTa5kAtmVclStatsEntry": adGenTa5kAtmVclStatsEntry,
       "adGenTa5kAtmVclStatsResetPM": adGenTa5kAtmVclStatsResetPM,
       "adGenTa5kAtmVclStatsRxAIS": adGenTa5kAtmVclStatsRxAIS,
       "adGenTa5kAtmVclStatsRxRDI": adGenTa5kAtmVclStatsRxRDI,
       "adGenTa5kAtmVclStatsGenAISRDI": adGenTa5kAtmVclStatsGenAISRDI,
       "adGenTa5kAtmVclStatsOamTxLbReqs": adGenTa5kAtmVclStatsOamTxLbReqs,
       "adGenTa5kAtmVclStatsOamRxLbReqs": adGenTa5kAtmVclStatsOamRxLbReqs,
       "adGenTa5kAtmVclStatsOamTxLbResps": adGenTa5kAtmVclStatsOamTxLbResps,
       "adGenTa5kAtmVclStatsOamRxLbResps": adGenTa5kAtmVclStatsOamRxLbResps,
       "adGenTa5kAtmVclStatsOamLbTimeouts": adGenTa5kAtmVclStatsOamLbTimeouts,
       "adGenTa5kAtmVclStatsOamLbLastResult": adGenTa5kAtmVclStatsOamLbLastResult,
       "adGenTa5kAtmVclStatsConnectionInfo": adGenTa5kAtmVclStatsConnectionInfo,
       "adGenTa5kAtmVplStatsTable": adGenTa5kAtmVplStatsTable,
       "adGenTa5kAtmVplStatsEntry": adGenTa5kAtmVplStatsEntry,
       "adGenTa5kAtmVplStatsResetPM": adGenTa5kAtmVplStatsResetPM,
       "adGenTa5kAtmVplStatsRxAIS": adGenTa5kAtmVplStatsRxAIS,
       "adGenTa5kAtmVplStatsRxRDI": adGenTa5kAtmVplStatsRxRDI,
       "adGenTa5kAtmVplStatsGenAISRDI": adGenTa5kAtmVplStatsGenAISRDI,
       "adGenTa5kAtmVplStatsOamTxLbReqs": adGenTa5kAtmVplStatsOamTxLbReqs,
       "adGenTa5kAtmVplStatsOamRxLbReqs": adGenTa5kAtmVplStatsOamRxLbReqs,
       "adGenTa5kAtmVplStatsOamTxLbResps": adGenTa5kAtmVplStatsOamTxLbResps,
       "adGenTa5kAtmVplStatsOamRxLbResps": adGenTa5kAtmVplStatsOamRxLbResps,
       "adGenTa5kAtmVplStatsOamLbTimeouts": adGenTa5kAtmVplStatsOamLbTimeouts,
       "adGenTa5kAtmVplStatsOamLbLastResult": adGenTa5kAtmVplStatsOamLbLastResult,
       "adGenTa5kAtmVplStatsAal5InPkts": adGenTa5kAtmVplStatsAal5InPkts,
       "adGenTa5kAtmVplStatsAal5OutPkts": adGenTa5kAtmVplStatsAal5OutPkts,
       "adGenTa5kAtmVplStatsAal5InOctets": adGenTa5kAtmVplStatsAal5InOctets,
       "adGenTa5kAtmVplStatsAal5OutOctets": adGenTa5kAtmVplStatsAal5OutOctets,
       "adGenTa5kAtmVplStatsConnectionInfo": adGenTa5kAtmVplStatsConnectionInfo,
       "adGenTa5kAtmPortStatsTable": adGenTa5kAtmPortStatsTable,
       "adGenTa5kAtmPortStatsEntry": adGenTa5kAtmPortStatsEntry,
       "adGenTa5kAtmPortStatsRxCells": adGenTa5kAtmPortStatsRxCells,
       "adGenTa5kAtmPortStatsRxClp1Cells": adGenTa5kAtmPortStatsRxClp1Cells,
       "adGenTa5kAtmPortStatsRxClp0Cells": adGenTa5kAtmPortStatsRxClp0Cells,
       "adGenTa5kAtmPortStatsRxOamCells": adGenTa5kAtmPortStatsRxOamCells,
       "adGenTa5kAtmPortStatsTxCells": adGenTa5kAtmPortStatsTxCells,
       "adGenTa5kAtmPortStatsTxClp1Cells": adGenTa5kAtmPortStatsTxClp1Cells,
       "adGenTa5kAtmPortStatsTxClp0Cells": adGenTa5kAtmPortStatsTxClp0Cells,
       "adGenTa5kAtmPortStatsTxOamCells": adGenTa5kAtmPortStatsTxOamCells,
       "adGenTa5kAtmPortStatsResetStats": adGenTa5kAtmPortStatsResetStats,
       "adGenTa5kAtmPortStatsCellDelineation": adGenTa5kAtmPortStatsCellDelineation,
       "adGenTa5kAtmDhcpStatsCurrentTable": adGenTa5kAtmDhcpStatsCurrentTable,
       "adGenTa5kAtmDhcpStatsCurrentEntry": adGenTa5kAtmDhcpStatsCurrentEntry,
       "adGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt": adGenTa5kAtmDhcpStatsCurrentUpstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt": adGenTa5kAtmDhcpStatsCurrentDownstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt": adGenTa5kAtmDhcpStatsCurrentUpstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt": adGenTa5kAtmDhcpStatsCurrentDownstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStatsIntervalTable": adGenTa5kAtmDhcpStatsIntervalTable,
       "adGenTa5kAtmDhcpStatsIntervalEntry": adGenTa5kAtmDhcpStatsIntervalEntry,
       "adGenTa5kAtmDhcpStatsIntervalIndex": adGenTa5kAtmDhcpStatsIntervalIndex,
       "adGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt": adGenTa5kAtmDhcpStatsIntervalUpstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt": adGenTa5kAtmDhcpStatsIntervalDownstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt": adGenTa5kAtmDhcpStatsIntervalUpstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt": adGenTa5kAtmDhcpStatsIntervalDownstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStatsIntervalTimeStamp": adGenTa5kAtmDhcpStatsIntervalTimeStamp,
       "adGenTa5kAtmDhcpStats24hrCurrentTable": adGenTa5kAtmDhcpStats24hrCurrentTable,
       "adGenTa5kAtmDhcpStats24hrCurrentEntry": adGenTa5kAtmDhcpStats24hrCurrentEntry,
       "adGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt": adGenTa5kAtmDhcpStats24hrCurrentUpstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt": adGenTa5kAtmDhcpStats24hrCurrentDownstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt": adGenTa5kAtmDhcpStats24hrCurrentUpstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt": adGenTa5kAtmDhcpStats24hrCurrentDownstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStats24hrTable": adGenTa5kAtmDhcpStats24hrTable,
       "adGenTa5kAtmDhcpStats24hrEntry": adGenTa5kAtmDhcpStats24hrEntry,
       "adGenTa5kAtmDhcpStats24hrIndex": adGenTa5kAtmDhcpStats24hrIndex,
       "adGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt": adGenTa5kAtmDhcpStats24hrUpstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt": adGenTa5kAtmDhcpStats24hrDownstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt": adGenTa5kAtmDhcpStats24hrUpstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt": adGenTa5kAtmDhcpStats24hrDownstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStats24hrTimeStamp": adGenTa5kAtmDhcpStats24hrTimeStamp,
       "adGenTa5kAtmDhcpStatsTable": adGenTa5kAtmDhcpStatsTable,
       "adGenTa5kAtmDhcpStatsEntry": adGenTa5kAtmDhcpStatsEntry,
       "adGenTa5kAtmDhcpStatsUpstreamFwdPktCnt": adGenTa5kAtmDhcpStatsUpstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStatsDownstreamFwdPktCnt": adGenTa5kAtmDhcpStatsDownstreamFwdPktCnt,
       "adGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt": adGenTa5kAtmDhcpStatsUpstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt": adGenTa5kAtmDhcpStatsDownstreamDiscardPktCnt,
       "adGenTa5kAtmDhcpPerCardStatsCurrentTable": adGenTa5kAtmDhcpPerCardStatsCurrentTable,
       "adGenTa5kAtmDhcpPerCardStatsCurrentEntry": adGenTa5kAtmDhcpPerCardStatsCurrentEntry,
       "adGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStatsCurrentUpstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStatsCurrentDownstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStatsIntervalTable": adGenTa5kAtmDhcpPerCardStatsIntervalTable,
       "adGenTa5kAtmDhcpPerCardStatsIntervalEntry": adGenTa5kAtmDhcpPerCardStatsIntervalEntry,
       "adGenTa5kAtmDhcpPerCardStatsIntervalIndex": adGenTa5kAtmDhcpPerCardStatsIntervalIndex,
       "adGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStatsIntervalUpstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStatsIntervalDownstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp": adGenTa5kAtmDhcpPerCardStatsIntervalTimeStamp,
       "adGenTa5kAtmDhcpPerCardStats24hrCurrentTable": adGenTa5kAtmDhcpPerCardStats24hrCurrentTable,
       "adGenTa5kAtmDhcpPerCardStats24hrCurrentEntry": adGenTa5kAtmDhcpPerCardStats24hrCurrentEntry,
       "adGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStats24hrCurrentUpstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStats24hrCurrentDownstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStats24hrTable": adGenTa5kAtmDhcpPerCardStats24hrTable,
       "adGenTa5kAtmDhcpPerCardStats24hrEntry": adGenTa5kAtmDhcpPerCardStats24hrEntry,
       "adGenTa5kAtmDhcpPerCardStats24hrIndex": adGenTa5kAtmDhcpPerCardStats24hrIndex,
       "adGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStats24hrUpstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStats24hrDownstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStats24hrTimeStamp": adGenTa5kAtmDhcpPerCardStats24hrTimeStamp,
       "adGenTa5kAtmDhcpPerCardStatsTable": adGenTa5kAtmDhcpPerCardStatsTable,
       "adGenTa5kAtmDhcpPerCardStatsEntry": adGenTa5kAtmDhcpPerCardStatsEntry,
       "adGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStatsUpstreamDroppedPktCnt,
       "adGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt": adGenTa5kAtmDhcpPerCardStatsDownstreamDroppedPktCnt,
       "adGenTa5kAtmLMVpStatus": adGenTa5kAtmLMVpStatus,
       "adGenTa5kAtmLMErrorVcTable": adGenTa5kAtmLMErrorVcTable,
       "adGenTa5kAtmLMErrorVcEntry": adGenTa5kAtmLMErrorVcEntry,
       "adGenTa5kAtmLMRecentErrorVC": adGenTa5kAtmLMRecentErrorVC,
       "adGenTa5kAtmLMRecentErrorVCClear": adGenTa5kAtmLMRecentErrorVCClear,
       "adGenTa5kAtmVpStatusTable": adGenTa5kAtmVpStatusTable,
       "adGenTa5kAtmVpStatusEntry": adGenTa5kAtmVpStatusEntry,
       "adGenTa5kAtmVpStatusVc": adGenTa5kAtmVpStatusVc,
       "adGenTa5kAtmVpStatusVcEncaps": adGenTa5kAtmVpStatusVcEncaps,
       "adGenTa5kAtmVpStatusVcDelete": adGenTa5kAtmVpStatusVcDelete,
       "adGenTa5kAtmLMAlarmPrefix": adGenTa5kAtmLMAlarmPrefix,
       "adGenTa5kAtmLMAlarm": adGenTa5kAtmLMAlarm,
       "adGenTa5kAtmLMUnlearnableVCL": adGenTa5kAtmLMUnlearnableVCL,
       "adTa5kAtmLMModuleIdentity": adTa5kAtmLMModuleIdentity}
)
