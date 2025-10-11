# SNMP MIB module (H3C-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-LLDP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:21:00 2025
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

(LldpPortNumber,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3clldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100)
)
if mibBuilder.loadTexts:
    h3clldp.setRevisions(
        ("2015-09-01 00:00",
         "2009-03-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3clldpObjects_ObjectIdentity = ObjectIdentity
h3clldpObjects = _H3clldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1)
)
_H3clldpConfiguration_ObjectIdentity = ObjectIdentity
h3clldpConfiguration = _H3clldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1)
)
_H3clldpAdminStatus_Type = TruthValue
_H3clldpAdminStatus_Object = MibScalar
h3clldpAdminStatus = _H3clldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 1),
    _H3clldpAdminStatus_Type()
)
h3clldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpAdminStatus.setStatus("current")
_H3clldpComplianceCDPStatus_Type = TruthValue
_H3clldpComplianceCDPStatus_Object = MibScalar
h3clldpComplianceCDPStatus = _H3clldpComplianceCDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 2),
    _H3clldpComplianceCDPStatus_Type()
)
h3clldpComplianceCDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpComplianceCDPStatus.setStatus("current")
_H3clldpPortConfigTable_Object = MibTable
h3clldpPortConfigTable = _H3clldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3clldpPortConfigTable.setStatus("current")
_H3clldpPortConfigEntry_Object = MibTableRow
h3clldpPortConfigEntry = _H3clldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 3, 1)
)
h3clldpPortConfigEntry.setIndexNames(
    (0, "H3C-LLDP-EXT-MIB", "h3clldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    h3clldpPortConfigEntry.setStatus("current")
_H3clldpPortConfigPortNum_Type = LldpPortNumber
_H3clldpPortConfigPortNum_Object = MibTableColumn
h3clldpPortConfigPortNum = _H3clldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 3, 1, 1),
    _H3clldpPortConfigPortNum_Type()
)
h3clldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3clldpPortConfigPortNum.setStatus("current")


class _H3clldpPortConfigCDPComplianceStatus_Type(Integer32):
    """Custom type h3clldpPortConfigCDPComplianceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("txAndRx", 1),
          ("disabled", 2))
    )


_H3clldpPortConfigCDPComplianceStatus_Type.__name__ = "Integer32"
_H3clldpPortConfigCDPComplianceStatus_Object = MibTableColumn
h3clldpPortConfigCDPComplianceStatus = _H3clldpPortConfigCDPComplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 3, 1, 2),
    _H3clldpPortConfigCDPComplianceStatus_Type()
)
h3clldpPortConfigCDPComplianceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpPortConfigCDPComplianceStatus.setStatus("current")
_H3clldpPortConfigValidationAction_Type = Integer32
_H3clldpPortConfigValidationAction_Object = MibTableColumn
h3clldpPortConfigValidationAction = _H3clldpPortConfigValidationAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 3, 1, 3),
    _H3clldpPortConfigValidationAction_Type()
)
h3clldpPortConfigValidationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpPortConfigValidationAction.setStatus("current")
_H3clldpPortConfigAgingAction_Type = Integer32
_H3clldpPortConfigAgingAction_Object = MibTableColumn
h3clldpPortConfigAgingAction = _H3clldpPortConfigAgingAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 3, 1, 4),
    _H3clldpPortConfigAgingAction_Type()
)
h3clldpPortConfigAgingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpPortConfigAgingAction.setStatus("current")
_H3clldpNbIdentityTable_Object = MibTable
h3clldpNbIdentityTable = _H3clldpNbIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3clldpNbIdentityTable.setStatus("current")
_H3clldpNbIdentityEntry_Object = MibTableRow
h3clldpNbIdentityEntry = _H3clldpNbIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1)
)
h3clldpNbIdentityEntry.setIndexNames(
    (0, "H3C-LLDP-EXT-MIB", "h3clldpNbIdentityPortNum"),
)
if mibBuilder.loadTexts:
    h3clldpNbIdentityEntry.setStatus("current")
_H3clldpNbIdentityPortNum_Type = LldpPortNumber
_H3clldpNbIdentityPortNum_Object = MibTableColumn
h3clldpNbIdentityPortNum = _H3clldpNbIdentityPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1, 1),
    _H3clldpNbIdentityPortNum_Type()
)
h3clldpNbIdentityPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3clldpNbIdentityPortNum.setStatus("current")


class _H3clldpNbIdentityChassisIDSubtype_Type(Integer32):
    """Custom type h3clldpNbIdentityChassisIDSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )


_H3clldpNbIdentityChassisIDSubtype_Type.__name__ = "Integer32"
_H3clldpNbIdentityChassisIDSubtype_Object = MibTableColumn
h3clldpNbIdentityChassisIDSubtype = _H3clldpNbIdentityChassisIDSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1, 2),
    _H3clldpNbIdentityChassisIDSubtype_Type()
)
h3clldpNbIdentityChassisIDSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpNbIdentityChassisIDSubtype.setStatus("current")


class _H3clldpNbIdentityChassisID_Type(OctetString):
    """Custom type h3clldpNbIdentityChassisID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3clldpNbIdentityChassisID_Type.__name__ = "OctetString"
_H3clldpNbIdentityChassisID_Object = MibTableColumn
h3clldpNbIdentityChassisID = _H3clldpNbIdentityChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1, 3),
    _H3clldpNbIdentityChassisID_Type()
)
h3clldpNbIdentityChassisID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpNbIdentityChassisID.setStatus("current")


class _H3clldpNbIdentityPortIDSubtype_Type(Integer32):
    """Custom type h3clldpNbIdentityPortIDSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("interfaceAlias", 1),
          ("portComponent", 2),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("interfaceName", 5),
          ("agentCircuitId", 6),
          ("local", 7))
    )


_H3clldpNbIdentityPortIDSubtype_Type.__name__ = "Integer32"
_H3clldpNbIdentityPortIDSubtype_Object = MibTableColumn
h3clldpNbIdentityPortIDSubtype = _H3clldpNbIdentityPortIDSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1, 4),
    _H3clldpNbIdentityPortIDSubtype_Type()
)
h3clldpNbIdentityPortIDSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpNbIdentityPortIDSubtype.setStatus("current")


class _H3clldpNbIdentityPortID_Type(OctetString):
    """Custom type h3clldpNbIdentityPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3clldpNbIdentityPortID_Type.__name__ = "OctetString"
_H3clldpNbIdentityPortID_Object = MibTableColumn
h3clldpNbIdentityPortID = _H3clldpNbIdentityPortID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1, 5),
    _H3clldpNbIdentityPortID_Type()
)
h3clldpNbIdentityPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpNbIdentityPortID.setStatus("current")
_H3clldpNbIdentityRowStatus_Type = RowStatus
_H3clldpNbIdentityRowStatus_Object = MibTableColumn
h3clldpNbIdentityRowStatus = _H3clldpNbIdentityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 4, 1, 6),
    _H3clldpNbIdentityRowStatus_Type()
)
h3clldpNbIdentityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3clldpNbIdentityRowStatus.setStatus("current")
_H3clldpPortStatusTable_Object = MibTable
h3clldpPortStatusTable = _H3clldpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 5)
)
if mibBuilder.loadTexts:
    h3clldpPortStatusTable.setStatus("current")
_H3clldpPortStatusEntry_Object = MibTableRow
h3clldpPortStatusEntry = _H3clldpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 5, 1)
)
h3clldpPortStatusEntry.setIndexNames(
    (0, "H3C-LLDP-EXT-MIB", "h3clldpPortStatusPortNum"),
)
if mibBuilder.loadTexts:
    h3clldpPortStatusEntry.setStatus("current")
_H3clldpPortStatusPortNum_Type = LldpPortNumber
_H3clldpPortStatusPortNum_Object = MibTableColumn
h3clldpPortStatusPortNum = _H3clldpPortStatusPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 5, 1, 1),
    _H3clldpPortStatusPortNum_Type()
)
h3clldpPortStatusPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3clldpPortStatusPortNum.setStatus("current")
_H3clldpPortValidationStatus_Type = Integer32
_H3clldpPortValidationStatus_Object = MibTableColumn
h3clldpPortValidationStatus = _H3clldpPortValidationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 5, 1, 2),
    _H3clldpPortValidationStatus_Type()
)
h3clldpPortValidationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3clldpPortValidationStatus.setStatus("current")
_H3clldpPortAgingStatus_Type = Integer32
_H3clldpPortAgingStatus_Object = MibTableColumn
h3clldpPortAgingStatus = _H3clldpPortAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 1, 1, 5, 1, 3),
    _H3clldpPortAgingStatus_Type()
)
h3clldpPortAgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3clldpPortAgingStatus.setStatus("current")
_H3clldpNotifications_ObjectIdentity = ObjectIdentity
h3clldpNotifications = _H3clldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 2)
)
_H3clldpPortStatusTrap_ObjectIdentity = ObjectIdentity
h3clldpPortStatusTrap = _H3clldpPortStatusTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 2, 0)
)

# Managed Objects groups


# Notification objects

h3clldpValidationStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 2, 0, 1)
)
h3clldpValidationStatusChange.setObjects(
      *(("H3C-LLDP-EXT-MIB", "h3clldpPortStatusPortNum"),
        ("H3C-LLDP-EXT-MIB", "h3clldpPortValidationStatus"))
)
if mibBuilder.loadTexts:
    h3clldpValidationStatusChange.setStatus(
        "current"
    )

h3clldpAgingStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100, 2, 0, 2)
)
h3clldpAgingStatusChange.setObjects(
      *(("H3C-LLDP-EXT-MIB", "h3clldpPortStatusPortNum"),
        ("H3C-LLDP-EXT-MIB", "h3clldpPortAgingStatus"))
)
if mibBuilder.loadTexts:
    h3clldpAgingStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-LLDP-EXT-MIB",
    **{"h3clldp": h3clldp,
       "h3clldpObjects": h3clldpObjects,
       "h3clldpConfiguration": h3clldpConfiguration,
       "h3clldpAdminStatus": h3clldpAdminStatus,
       "h3clldpComplianceCDPStatus": h3clldpComplianceCDPStatus,
       "h3clldpPortConfigTable": h3clldpPortConfigTable,
       "h3clldpPortConfigEntry": h3clldpPortConfigEntry,
       "h3clldpPortConfigPortNum": h3clldpPortConfigPortNum,
       "h3clldpPortConfigCDPComplianceStatus": h3clldpPortConfigCDPComplianceStatus,
       "h3clldpPortConfigValidationAction": h3clldpPortConfigValidationAction,
       "h3clldpPortConfigAgingAction": h3clldpPortConfigAgingAction,
       "h3clldpNbIdentityTable": h3clldpNbIdentityTable,
       "h3clldpNbIdentityEntry": h3clldpNbIdentityEntry,
       "h3clldpNbIdentityPortNum": h3clldpNbIdentityPortNum,
       "h3clldpNbIdentityChassisIDSubtype": h3clldpNbIdentityChassisIDSubtype,
       "h3clldpNbIdentityChassisID": h3clldpNbIdentityChassisID,
       "h3clldpNbIdentityPortIDSubtype": h3clldpNbIdentityPortIDSubtype,
       "h3clldpNbIdentityPortID": h3clldpNbIdentityPortID,
       "h3clldpNbIdentityRowStatus": h3clldpNbIdentityRowStatus,
       "h3clldpPortStatusTable": h3clldpPortStatusTable,
       "h3clldpPortStatusEntry": h3clldpPortStatusEntry,
       "h3clldpPortStatusPortNum": h3clldpPortStatusPortNum,
       "h3clldpPortValidationStatus": h3clldpPortValidationStatus,
       "h3clldpPortAgingStatus": h3clldpPortAgingStatus,
       "h3clldpNotifications": h3clldpNotifications,
       "h3clldpPortStatusTrap": h3clldpPortStatusTrap,
       "h3clldpValidationStatusChange": h3clldpValidationStatusChange,
       "h3clldpAgingStatusChange": h3clldpAgingStatusChange}
)
