# SNMP MIB module (ADTRAN-GENERIC-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:36 2025
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

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenLldp,
 adGenLldpID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenLldp",
    "adGenLldpID")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 46, 1)
)
if mibBuilder.loadTexts:
    adGenLldpMIB.setRevisions(
        ("2013-09-18 00:00",
         "2011-10-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenChassisIdSubtype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )



class AdGenChassisId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class AdGenPortIdSubtype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("interfaceAlias", 1),
          ("portComponent", 2),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("interfaceName", 5),
          ("agentCircuitId", 6),
          ("local", 7))
    )



class AdGenPortId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class AdGenManAddrIfSubtype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ifIndex", 2),
          ("systemPortNumber", 3))
    )



class AdGenManAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class AdGenSystemCapabilitiesMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("other", 0),
          ("repeater", 1),
          ("bridge", 2),
          ("wlanAccessPoint", 3),
          ("router", 4),
          ("telephone", 5),
          ("docsisCableDevice", 6),
          ("stationOnly", 7))
    )


# MIB Managed Objects in the order of their OIDs

_AdGenLldpConfiguration_ObjectIdentity = ObjectIdentity
adGenLldpConfiguration = _AdGenLldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1)
)
_AdGenLldpProvTable_Object = MibTable
adGenLldpProvTable = _AdGenLldpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1, 1)
)
if mibBuilder.loadTexts:
    adGenLldpProvTable.setStatus("current")
_AdGenLldpProvEntry_Object = MibTableRow
adGenLldpProvEntry = _AdGenLldpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1, 1, 1)
)
adGenLldpProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenLldpProvEntry.setStatus("current")


class _AdGenLldpConfigState_Type(Integer32):
    """Custom type adGenLldpConfigState based on Integer32"""
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
        *(("txOnly", 1),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("disabled", 4))
    )


_AdGenLldpConfigState_Type.__name__ = "Integer32"
_AdGenLldpConfigState_Object = MibTableColumn
adGenLldpConfigState = _AdGenLldpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1, 1, 1, 1),
    _AdGenLldpConfigState_Type()
)
adGenLldpConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenLldpConfigState.setStatus("current")
_AdGenLldpStatistics_ObjectIdentity = ObjectIdentity
adGenLldpStatistics = _AdGenLldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 2)
)
_AdGenLldpLocalSystemData_ObjectIdentity = ObjectIdentity
adGenLldpLocalSystemData = _AdGenLldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 3)
)
_AdGenLldpRemoteSystemData_ObjectIdentity = ObjectIdentity
adGenLldpRemoteSystemData = _AdGenLldpRemoteSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4)
)
_AdGenLldpRemSysDataTable_Object = MibTable
adGenLldpRemSysDataTable = _AdGenLldpRemSysDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1)
)
if mibBuilder.loadTexts:
    adGenLldpRemSysDataTable.setStatus("current")
_AdGenLldpRemSysDataEntry_Object = MibTableRow
adGenLldpRemSysDataEntry = _AdGenLldpRemSysDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1)
)
adGenLldpRemSysDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenLldpRemSysDataEntry.setStatus("current")
_AdGenLldpRemChassisIdSubtype_Type = AdGenChassisIdSubtype
_AdGenLldpRemChassisIdSubtype_Object = MibTableColumn
adGenLldpRemChassisIdSubtype = _AdGenLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 1),
    _AdGenLldpRemChassisIdSubtype_Type()
)
adGenLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemChassisIdSubtype.setStatus("current")
_AdGenLldpRemChassisId_Type = AdGenChassisId
_AdGenLldpRemChassisId_Object = MibTableColumn
adGenLldpRemChassisId = _AdGenLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 2),
    _AdGenLldpRemChassisId_Type()
)
adGenLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemChassisId.setStatus("current")
_AdGenLldpRemPortIdSubtype_Type = AdGenPortIdSubtype
_AdGenLldpRemPortIdSubtype_Object = MibTableColumn
adGenLldpRemPortIdSubtype = _AdGenLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 3),
    _AdGenLldpRemPortIdSubtype_Type()
)
adGenLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemPortIdSubtype.setStatus("current")
_AdGenLldpRemPortId_Type = AdGenPortId
_AdGenLldpRemPortId_Object = MibTableColumn
adGenLldpRemPortId = _AdGenLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 4),
    _AdGenLldpRemPortId_Type()
)
adGenLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemPortId.setStatus("current")


class _AdGenLldpRemPortDesc_Type(SnmpAdminString):
    """Custom type adGenLldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenLldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_AdGenLldpRemPortDesc_Object = MibTableColumn
adGenLldpRemPortDesc = _AdGenLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 5),
    _AdGenLldpRemPortDesc_Type()
)
adGenLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemPortDesc.setStatus("current")


class _AdGenLldpRemSysName_Type(SnmpAdminString):
    """Custom type adGenLldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenLldpRemSysName_Type.__name__ = "SnmpAdminString"
_AdGenLldpRemSysName_Object = MibTableColumn
adGenLldpRemSysName = _AdGenLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 6),
    _AdGenLldpRemSysName_Type()
)
adGenLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemSysName.setStatus("current")


class _AdGenLldpRemSysDesc_Type(SnmpAdminString):
    """Custom type adGenLldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenLldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_AdGenLldpRemSysDesc_Object = MibTableColumn
adGenLldpRemSysDesc = _AdGenLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 7),
    _AdGenLldpRemSysDesc_Type()
)
adGenLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemSysDesc.setStatus("current")
_AdGenLldpRemSysCapSupported_Type = AdGenSystemCapabilitiesMap
_AdGenLldpRemSysCapSupported_Object = MibTableColumn
adGenLldpRemSysCapSupported = _AdGenLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 8),
    _AdGenLldpRemSysCapSupported_Type()
)
adGenLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemSysCapSupported.setStatus("current")
_AdGenLldpRemSysCapEnabled_Type = AdGenSystemCapabilitiesMap
_AdGenLldpRemSysCapEnabled_Object = MibTableColumn
adGenLldpRemSysCapEnabled = _AdGenLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 9),
    _AdGenLldpRemSysCapEnabled_Type()
)
adGenLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemSysCapEnabled.setStatus("current")
_AdGenLldpRemManAddrSubtype_Type = AddressFamilyNumbers
_AdGenLldpRemManAddrSubtype_Object = MibTableColumn
adGenLldpRemManAddrSubtype = _AdGenLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 10),
    _AdGenLldpRemManAddrSubtype_Type()
)
adGenLldpRemManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemManAddrSubtype.setStatus("current")
_AdGenLldpRemManAddr_Type = AdGenManAddress
_AdGenLldpRemManAddr_Object = MibTableColumn
adGenLldpRemManAddr = _AdGenLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 11),
    _AdGenLldpRemManAddr_Type()
)
adGenLldpRemManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemManAddr.setStatus("current")
_AdGenLldpRemManAddrIfSubtype_Type = AdGenManAddrIfSubtype
_AdGenLldpRemManAddrIfSubtype_Object = MibTableColumn
adGenLldpRemManAddrIfSubtype = _AdGenLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 12),
    _AdGenLldpRemManAddrIfSubtype_Type()
)
adGenLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemManAddrIfSubtype.setStatus("current")
_AdGenLldpRemManAddrIfId_Type = Integer32
_AdGenLldpRemManAddrIfId_Object = MibTableColumn
adGenLldpRemManAddrIfId = _AdGenLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 13),
    _AdGenLldpRemManAddrIfId_Type()
)
adGenLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenLldpRemManAddrIfId.setStatus("current")
_AdGenLldpExtentsions_ObjectIdentity = ObjectIdentity
adGenLldpExtentsions = _AdGenLldpExtentsions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 5)
)
_AdGenLldpEvents_ObjectIdentity = ObjectIdentity
adGenLldpEvents = _AdGenLldpEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6)
)
_AdGenLldpTraps_ObjectIdentity = ObjectIdentity
adGenLldpTraps = _AdGenLldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6, 0)
)

# Managed Objects groups


# Notification objects

adGenLldpPeerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6, 0, 1)
)
adGenLldpPeerRemoved.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenLldpPeerRemoved.setStatus(
        "current"
    )

adGenLldpPeerAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6, 0, 2)
)
adGenLldpPeerAdded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenLldpPeerAdded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-LLDP-MIB",
    **{"AdGenChassisIdSubtype": AdGenChassisIdSubtype,
       "AdGenChassisId": AdGenChassisId,
       "AdGenPortIdSubtype": AdGenPortIdSubtype,
       "AdGenPortId": AdGenPortId,
       "AdGenManAddrIfSubtype": AdGenManAddrIfSubtype,
       "AdGenManAddress": AdGenManAddress,
       "AdGenSystemCapabilitiesMap": AdGenSystemCapabilitiesMap,
       "adGenLldpConfiguration": adGenLldpConfiguration,
       "adGenLldpProvTable": adGenLldpProvTable,
       "adGenLldpProvEntry": adGenLldpProvEntry,
       "adGenLldpConfigState": adGenLldpConfigState,
       "adGenLldpStatistics": adGenLldpStatistics,
       "adGenLldpLocalSystemData": adGenLldpLocalSystemData,
       "adGenLldpRemoteSystemData": adGenLldpRemoteSystemData,
       "adGenLldpRemSysDataTable": adGenLldpRemSysDataTable,
       "adGenLldpRemSysDataEntry": adGenLldpRemSysDataEntry,
       "adGenLldpRemChassisIdSubtype": adGenLldpRemChassisIdSubtype,
       "adGenLldpRemChassisId": adGenLldpRemChassisId,
       "adGenLldpRemPortIdSubtype": adGenLldpRemPortIdSubtype,
       "adGenLldpRemPortId": adGenLldpRemPortId,
       "adGenLldpRemPortDesc": adGenLldpRemPortDesc,
       "adGenLldpRemSysName": adGenLldpRemSysName,
       "adGenLldpRemSysDesc": adGenLldpRemSysDesc,
       "adGenLldpRemSysCapSupported": adGenLldpRemSysCapSupported,
       "adGenLldpRemSysCapEnabled": adGenLldpRemSysCapEnabled,
       "adGenLldpRemManAddrSubtype": adGenLldpRemManAddrSubtype,
       "adGenLldpRemManAddr": adGenLldpRemManAddr,
       "adGenLldpRemManAddrIfSubtype": adGenLldpRemManAddrIfSubtype,
       "adGenLldpRemManAddrIfId": adGenLldpRemManAddrIfId,
       "adGenLldpExtentsions": adGenLldpExtentsions,
       "adGenLldpEvents": adGenLldpEvents,
       "adGenLldpTraps": adGenLldpTraps,
       "adGenLldpPeerRemoved": adGenLldpPeerRemoved,
       "adGenLldpPeerAdded": adGenLldpPeerAdded,
       "adGenLldpMIB": adGenLldpMIB}
)
