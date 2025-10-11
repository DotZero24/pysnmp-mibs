# SNMP MIB module (LEFTHAND-NETWORKS-NSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:10 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lhnNsmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lhnNsmMib.setRevisions(
        ("2013-11-22 00:00",
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

_LhnNsmDevices_ObjectIdentity = ObjectIdentity
lhnNsmDevices = _LhnNsmDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lhnNsmDevices.setStatus("current")
_LhnNsmEvents_ObjectIdentity = ObjectIdentity
lhnNsmEvents = _LhnNsmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0)
)
if mibBuilder.loadTexts:
    lhnNsmEvents.setStatus("current")
_LhnNsmCommon_ObjectIdentity = ObjectIdentity
lhnNsmCommon = _LhnNsmCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lhnNsmCommon.setStatus("obsolete")
_LhnNsmObjects_ObjectIdentity = ObjectIdentity
lhnNsmObjects = _LhnNsmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lhnNsmObjects.setStatus("current")
_LhnNsmInfo_ObjectIdentity = ObjectIdentity
lhnNsmInfo = _LhnNsmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lhnNsmInfo.setStatus("current")
_LhnNsmNetwork_ObjectIdentity = ObjectIdentity
lhnNsmNetwork = _LhnNsmNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lhnNsmNetwork.setStatus("current")
_LhnNsmDNS_ObjectIdentity = ObjectIdentity
lhnNsmDNS = _LhnNsmDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lhnNsmDNS.setStatus("current")
_LhnNsmStorage_ObjectIdentity = ObjectIdentity
lhnNsmStorage = _LhnNsmStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lhnNsmStorage.setStatus("current")
_LhnNsmNTP_ObjectIdentity = ObjectIdentity
lhnNsmNTP = _LhnNsmNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    lhnNsmNTP.setStatus("current")
_LhnNsmSecurity_ObjectIdentity = ObjectIdentity
lhnNsmSecurity = _LhnNsmSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    lhnNsmSecurity.setStatus("current")
_LhnNsmClustering_ObjectIdentity = ObjectIdentity
lhnNsmClustering = _LhnNsmClustering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    lhnNsmClustering.setStatus("current")
_LhnNsmOldNotification_ObjectIdentity = ObjectIdentity
lhnNsmOldNotification = _LhnNsmOldNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    lhnNsmOldNotification.setStatus("current")
_LhnNsmNotification_ObjectIdentity = ObjectIdentity
lhnNsmNotification = _LhnNsmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    lhnNsmNotification.setStatus("current")
_LhnNsmStatus_ObjectIdentity = ObjectIdentity
lhnNsmStatus = _LhnNsmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99)
)
if mibBuilder.loadTexts:
    lhnNsmStatus.setStatus("current")
_LhnNsmOldEvents_ObjectIdentity = ObjectIdentity
lhnNsmOldEvents = _LhnNsmOldEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lhnNsmOldEvents.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    **{"lhnNsmMib": lhnNsmMib,
       "lhnNsmDevices": lhnNsmDevices,
       "lhnNsmEvents": lhnNsmEvents,
       "lhnNsmCommon": lhnNsmCommon,
       "lhnNsmObjects": lhnNsmObjects,
       "lhnNsmInfo": lhnNsmInfo,
       "lhnNsmNetwork": lhnNsmNetwork,
       "lhnNsmDNS": lhnNsmDNS,
       "lhnNsmStorage": lhnNsmStorage,
       "lhnNsmNTP": lhnNsmNTP,
       "lhnNsmSecurity": lhnNsmSecurity,
       "lhnNsmClustering": lhnNsmClustering,
       "lhnNsmOldNotification": lhnNsmOldNotification,
       "lhnNsmNotification": lhnNsmNotification,
       "lhnNsmStatus": lhnNsmStatus,
       "lhnNsmOldEvents": lhnNsmOldEvents}
)
