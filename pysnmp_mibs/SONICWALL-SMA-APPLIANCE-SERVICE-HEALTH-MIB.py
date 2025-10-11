# SNMP MIB module (SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:31 2025
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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
 enterprises,
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
    "enterprises",
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

(sonicwallSMAAppliance,) = mibBuilder.importSymbols(
    "SONICWALL-SMA-MIB",
    "sonicwallSMAAppliance")


# MODULE-IDENTITY

sonicwallServiceHealth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("current")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 1, 1)
)
serviceEntry.setIndexNames(
    (0, "SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB", "serviceId"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("current")
_ServiceId_Type = Integer32
_ServiceId_Object = MibTableColumn
serviceId = _ServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 1, 1, 1),
    _ServiceId_Type()
)
serviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceId.setStatus("current")
_ServiceDescription_Type = InternationalDisplayString
_ServiceDescription_Object = MibTableColumn
serviceDescription = _ServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 1, 1, 2),
    _ServiceDescription_Type()
)
serviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceDescription.setStatus("current")
_ServiceState_Type = Integer32
_ServiceState_Object = MibTableColumn
serviceState = _ServiceState_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 1, 1, 3),
    _ServiceState_Type()
)
serviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceState.setStatus("current")
_ServiceTableRowStatus_Type = RowStatus
_ServiceTableRowStatus_Object = MibTableColumn
serviceTableRowStatus = _ServiceTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 1, 1, 4),
    _ServiceTableRowStatus_Type()
)
serviceTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceTableRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

asapServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 2)
)
asapServiceUp.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB", "serviceDescription")
)
if mibBuilder.loadTexts:
    asapServiceUp.setStatus(
        "current"
    )

asapServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 3, 3)
)
asapServiceDown.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB", "serviceDescription")
)
if mibBuilder.loadTexts:
    asapServiceDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB",
    **{"sonicwallServiceHealth": sonicwallServiceHealth,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "serviceId": serviceId,
       "serviceDescription": serviceDescription,
       "serviceState": serviceState,
       "serviceTableRowStatus": serviceTableRowStatus,
       "asapServiceUp": asapServiceUp,
       "asapServiceDown": asapServiceDown}
)
