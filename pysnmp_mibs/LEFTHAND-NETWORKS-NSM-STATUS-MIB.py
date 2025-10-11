# SNMP MIB module (LEFTHAND-NETWORKS-NSM-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-STATUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:51 2025
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

(lhnModules,
 lhnNsm) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    "lhnModules",
    "lhnNsm")

(lhnNsmStatus,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmStatus")

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

lhnNsmStatusModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 99)
)
if mibBuilder.loadTexts:
    lhnNsmStatusModule.setRevisions(
        ("2013-11-21 00:00",
         "2013-06-25 00:00",
         "2012-09-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNsmStatusModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmStatusModuleConformance = _LhnNsmStatusModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1)
)
_LhnNsmStatusModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmStatusModuleCompliances = _LhnNsmStatusModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 1)
)
_LhnNsmStatusModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmStatusModuleGroups = _LhnNsmStatusModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 2)
)


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 1),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")
_StatusMessage_Type = DisplayString
_StatusMessage_Object = MibScalar
statusMessage = _StatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 2),
    _StatusMessage_Type()
)
statusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMessage.setStatus("current")
_StatusSNMPD_Type = DisplayString
_StatusSNMPD_Object = MibScalar
statusSNMPD = _StatusSNMPD_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 3),
    _StatusSNMPD_Type()
)
statusSNMPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSNMPD.setStatus("current")

# Managed Objects groups

lefthandNetworksNsmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 2, 1)
)
lefthandNetworksNsmStatusGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "status"),
        ("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "statusMessage"),
        ("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "statusSNMPD"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmStatusMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 1, 1)
)
lefthandNetworksNsmStatusMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "lefthandNetworksNsmStatusGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmStatusMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-STATUS-MIB",
    **{"lhnNsmStatusModule": lhnNsmStatusModule,
       "lhnNsmStatusModuleConformance": lhnNsmStatusModuleConformance,
       "lhnNsmStatusModuleCompliances": lhnNsmStatusModuleCompliances,
       "lefthandNetworksNsmStatusMibCompliance": lefthandNetworksNsmStatusMibCompliance,
       "lhnNsmStatusModuleGroups": lhnNsmStatusModuleGroups,
       "lefthandNetworksNsmStatusGroup": lefthandNetworksNsmStatusGroup,
       "status": status,
       "statusMessage": statusMessage,
       "statusSNMPD": statusSNMPD}
)
