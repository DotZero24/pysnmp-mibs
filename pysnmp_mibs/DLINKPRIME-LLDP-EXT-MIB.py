# SNMP MIB module (DLINKPRIME-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-LLDP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:44 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

dlinkPrimeLldpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 8)
)
if mibBuilder.loadTexts:
    dlinkPrimeLldpExtMIB.setRevisions(
        ("2014-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpLldpExtMIBNotifications_ObjectIdentity = ObjectIdentity
dpLldpExtMIBNotifications = _DpLldpExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 0)
)
_DpLldpExtMIBObjects_ObjectIdentity = ObjectIdentity
dpLldpExtMIBObjects = _DpLldpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1)
)
_DpLldpExtLldpEnabled_Type = TruthValue
_DpLldpExtLldpEnabled_Object = MibScalar
dpLldpExtLldpEnabled = _DpLldpExtLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 1),
    _DpLldpExtLldpEnabled_Type()
)
dpLldpExtLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLldpExtLldpEnabled.setStatus("current")
_DpLldpExtLldpTrapEnabled_Type = TruthValue
_DpLldpExtLldpTrapEnabled_Object = MibScalar
dpLldpExtLldpTrapEnabled = _DpLldpExtLldpTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 2),
    _DpLldpExtLldpTrapEnabled_Type()
)
dpLldpExtLldpTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpLldpExtLldpTrapEnabled.setStatus("current")
_DpLldpExtRemTable_Object = MibTable
dpLldpExtRemTable = _DpLldpExtRemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3)
)
if mibBuilder.loadTexts:
    dpLldpExtRemTable.setStatus("current")
_DpLldpExtRemEntry_Object = MibTableRow
dpLldpExtRemEntry = _DpLldpExtRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1)
)
dpLldpExtRemEntry.setIndexNames(
    (0, "DLINKPRIME-LLDP-EXT-MIB", "dpLldpExtRemLocalPortNum"),
    (0, "DLINKPRIME-LLDP-EXT-MIB", "dpLldpExtRemIndex"),
)
if mibBuilder.loadTexts:
    dpLldpExtRemEntry.setStatus("current")


class _DpLldpExtRemLocalPortNum_Type(Integer32):
    """Custom type dpLldpExtRemLocalPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_DpLldpExtRemLocalPortNum_Type.__name__ = "Integer32"
_DpLldpExtRemLocalPortNum_Object = MibTableColumn
dpLldpExtRemLocalPortNum = _DpLldpExtRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 1),
    _DpLldpExtRemLocalPortNum_Type()
)
dpLldpExtRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpLldpExtRemLocalPortNum.setStatus("current")


class _DpLldpExtRemIndex_Type(Integer32):
    """Custom type dpLldpExtRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DpLldpExtRemIndex_Type.__name__ = "Integer32"
_DpLldpExtRemIndex_Object = MibTableColumn
dpLldpExtRemIndex = _DpLldpExtRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 2),
    _DpLldpExtRemIndex_Type()
)
dpLldpExtRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpLldpExtRemIndex.setStatus("current")


class _DpLldpExtRemChassisIdSubtype_Type(Integer32):
    """Custom type dpLldpExtRemChassisIdSubtype based on Integer32"""
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


_DpLldpExtRemChassisIdSubtype_Type.__name__ = "Integer32"
_DpLldpExtRemChassisIdSubtype_Object = MibTableColumn
dpLldpExtRemChassisIdSubtype = _DpLldpExtRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 3),
    _DpLldpExtRemChassisIdSubtype_Type()
)
dpLldpExtRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpLldpExtRemChassisIdSubtype.setStatus("current")


class _DpLldpExtRemChassisId_Type(OctetString):
    """Custom type dpLldpExtRemChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DpLldpExtRemChassisId_Type.__name__ = "OctetString"
_DpLldpExtRemChassisId_Object = MibTableColumn
dpLldpExtRemChassisId = _DpLldpExtRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 4),
    _DpLldpExtRemChassisId_Type()
)
dpLldpExtRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpLldpExtRemChassisId.setStatus("current")


class _DpLldpExtRemPortIdSubtype_Type(Integer32):
    """Custom type dpLldpExtRemPortIdSubtype based on Integer32"""
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


_DpLldpExtRemPortIdSubtype_Type.__name__ = "Integer32"
_DpLldpExtRemPortIdSubtype_Object = MibTableColumn
dpLldpExtRemPortIdSubtype = _DpLldpExtRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 5),
    _DpLldpExtRemPortIdSubtype_Type()
)
dpLldpExtRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpLldpExtRemPortIdSubtype.setStatus("current")


class _DpLldpExtRemPortId_Type(OctetString):
    """Custom type dpLldpExtRemPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DpLldpExtRemPortId_Type.__name__ = "OctetString"
_DpLldpExtRemPortId_Object = MibTableColumn
dpLldpExtRemPortId = _DpLldpExtRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 6),
    _DpLldpExtRemPortId_Type()
)
dpLldpExtRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpLldpExtRemPortId.setStatus("current")


class _DpLldpExtRemPortDesc_Type(SnmpAdminString):
    """Custom type dpLldpExtRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DpLldpExtRemPortDesc_Type.__name__ = "SnmpAdminString"
_DpLldpExtRemPortDesc_Object = MibTableColumn
dpLldpExtRemPortDesc = _DpLldpExtRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 1, 3, 1, 7),
    _DpLldpExtRemPortDesc_Type()
)
dpLldpExtRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpLldpExtRemPortDesc.setStatus("current")
_DpLldpExtMIBConformance_ObjectIdentity = ObjectIdentity
dpLldpExtMIBConformance = _DpLldpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 2)
)
_DpLldpExtMIBCompliances_ObjectIdentity = ObjectIdentity
dpLldpExtMIBCompliances = _DpLldpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 2, 1)
)
_DpLldpExtMIBGroups_ObjectIdentity = ObjectIdentity
dpLldpExtMIBGroups = _DpLldpExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 2, 2)
)

# Managed Objects groups

dpLldpExtBasicCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 2, 2, 1)
)
dpLldpExtBasicCfgGroup.setObjects(
      *(("DLINKPRIME-LLDP-EXT-MIB", "dpLldpExtLldpEnabled"),
        ("DLINKPRIME-LLDP-EXT-MIB", "dpLldpExtLldpTrapEnabled"))
)
if mibBuilder.loadTexts:
    dpLldpExtBasicCfgGroup.setStatus("current")


# Notification objects

dpLldpExtDatabaseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 0, 1)
)
if mibBuilder.loadTexts:
    dpLldpExtDatabaseChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

dpLldpExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 8, 2, 1, 1)
)
dpLldpExtMIBCompliance.setObjects(
    ("DLINKPRIME-LLDP-EXT-MIB", "dpLldpExtBasicCfgGroup")
)
if mibBuilder.loadTexts:
    dpLldpExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-LLDP-EXT-MIB",
    **{"dlinkPrimeLldpExtMIB": dlinkPrimeLldpExtMIB,
       "dpLldpExtMIBNotifications": dpLldpExtMIBNotifications,
       "dpLldpExtDatabaseChanged": dpLldpExtDatabaseChanged,
       "dpLldpExtMIBObjects": dpLldpExtMIBObjects,
       "dpLldpExtLldpEnabled": dpLldpExtLldpEnabled,
       "dpLldpExtLldpTrapEnabled": dpLldpExtLldpTrapEnabled,
       "dpLldpExtRemTable": dpLldpExtRemTable,
       "dpLldpExtRemEntry": dpLldpExtRemEntry,
       "dpLldpExtRemLocalPortNum": dpLldpExtRemLocalPortNum,
       "dpLldpExtRemIndex": dpLldpExtRemIndex,
       "dpLldpExtRemChassisIdSubtype": dpLldpExtRemChassisIdSubtype,
       "dpLldpExtRemChassisId": dpLldpExtRemChassisId,
       "dpLldpExtRemPortIdSubtype": dpLldpExtRemPortIdSubtype,
       "dpLldpExtRemPortId": dpLldpExtRemPortId,
       "dpLldpExtRemPortDesc": dpLldpExtRemPortDesc,
       "dpLldpExtMIBConformance": dpLldpExtMIBConformance,
       "dpLldpExtMIBCompliances": dpLldpExtMIBCompliances,
       "dpLldpExtMIBCompliance": dpLldpExtMIBCompliance,
       "dpLldpExtMIBGroups": dpLldpExtMIBGroups,
       "dpLldpExtBasicCfgGroup": dpLldpExtBasicCfgGroup}
)
