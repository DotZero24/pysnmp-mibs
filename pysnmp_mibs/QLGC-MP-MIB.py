# SNMP MIB module (QLGC-MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/marvell/QLGC-MP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:47:53 2025
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

(qlogicMgmt,) = mibBuilder.importSymbols(
    "QLOGIC-SMI",
    "qlogicMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qlgcMaintenancePanelModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2)
)
if mibBuilder.loadTexts:
    qlgcMaintenancePanelModule.setRevisions(
        ("2009-09-29 00:00",
         "2007-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MPEpromStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )



# MIB Managed Objects in the order of their OIDs

_QlgcMPNotifications_ObjectIdentity = ObjectIdentity
qlgcMPNotifications = _QlgcMPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 0)
)
_QlgcMPObjects_ObjectIdentity = ObjectIdentity
qlgcMPObjects = _QlgcMPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 1)
)
_QlgcMPStatus_ObjectIdentity = ObjectIdentity
qlgcMPStatus = _QlgcMPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 1, 1)
)
_QlgcMPEpromStatus_Type = MPEpromStatus
_QlgcMPEpromStatus_Object = MibScalar
qlgcMPEpromStatus = _QlgcMPEpromStatus_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 1, 1, 1),
    _QlgcMPEpromStatus_Type()
)
qlgcMPEpromStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qlgcMPEpromStatus.setStatus("current")
_QlgcMPConformance_ObjectIdentity = ObjectIdentity
qlgcMPConformance = _QlgcMPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 2)
)
_QlgcMPGroups_ObjectIdentity = ObjectIdentity
qlgcMPGroups = _QlgcMPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 1)
)
_QlgcMPCompliances_ObjectIdentity = ObjectIdentity
qlgcMPCompliances = _QlgcMPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 2)
)

# Managed Objects groups

qlgcMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 1, 1)
)
qlgcMPGroup.setObjects(
    ("QLGC-MP-MIB", "qlgcMPEpromStatus")
)
if mibBuilder.loadTexts:
    qlgcMPGroup.setStatus("current")


# Notification objects

qlgcMPStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 0, 1)
)
qlgcMPStatusChange.setObjects(
    ("QLGC-MP-MIB", "qlgcMPEpromStatus")
)
if mibBuilder.loadTexts:
    qlgcMPStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qlgcMPComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 2, 1)
)
qlgcMPComplianceV1.setObjects(
    ("QLGC-MP-MIB", "qlgcMPGroup")
)
if mibBuilder.loadTexts:
    qlgcMPComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QLGC-MP-MIB",
    **{"MPEpromStatus": MPEpromStatus,
       "qlgcMaintenancePanelModule": qlgcMaintenancePanelModule,
       "qlgcMPNotifications": qlgcMPNotifications,
       "qlgcMPStatusChange": qlgcMPStatusChange,
       "qlgcMPObjects": qlgcMPObjects,
       "qlgcMPStatus": qlgcMPStatus,
       "qlgcMPEpromStatus": qlgcMPEpromStatus,
       "qlgcMPConformance": qlgcMPConformance,
       "qlgcMPGroups": qlgcMPGroups,
       "qlgcMPGroup": qlgcMPGroup,
       "qlgcMPCompliances": qlgcMPCompliances,
       "qlgcMPComplianceV1": qlgcMPComplianceV1}
)
