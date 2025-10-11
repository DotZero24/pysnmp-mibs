# SNMP MIB module (LEFTHAND-NETWORKS-NSM-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:33:05 2025
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

(lhnNsmNTP,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmNTP")

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

lhnNsmNTPModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lhnNsmNTPModule.setRevisions(
        ("2013-11-19 00:00",
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

_LhnNsmNTPModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmNTPModuleConformance = _LhnNsmNTPModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1)
)
_LhnNsmNTPModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmNTPModuleCompliances = _LhnNsmNTPModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 1)
)
_LhnNsmNTPModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmNTPModuleGroups = _LhnNsmNTPModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 2)
)
_NtpCount_Type = Integer32
_NtpCount_Object = MibScalar
ntpCount = _NtpCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 1),
    _NtpCount_Type()
)
ntpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpCount.setStatus("current")
_NtpTable_Object = MibTable
ntpTable = _NtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ntpTable.setStatus("current")
_NtpEntry_Object = MibTableRow
ntpEntry = _NtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1)
)
ntpEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpIndex"),
)
if mibBuilder.loadTexts:
    ntpEntry.setStatus("current")
_NtpIndex_Type = Unsigned32
_NtpIndex_Object = MibTableColumn
ntpIndex = _NtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 1),
    _NtpIndex_Type()
)
ntpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpIndex.setStatus("current")
_NtpPreferred_Type = TruthValue
_NtpPreferred_Object = MibTableColumn
ntpPreferred = _NtpPreferred_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 2),
    _NtpPreferred_Type()
)
ntpPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPreferred.setStatus("current")
_NtpServer_Type = DisplayString
_NtpServer_Object = MibTableColumn
ntpServer = _NtpServer_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 3),
    _NtpServer_Type()
)
ntpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServer.setStatus("current")
_NtpRowStatus_Type = RowStatus
_NtpRowStatus_Object = MibTableColumn
ntpRowStatus = _NtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 4),
    _NtpRowStatus_Type()
)
ntpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpRowStatus.setStatus("obsolete")
_TimeGMTTime_Type = DisplayString
_TimeGMTTime_Object = MibScalar
timeGMTTime = _TimeGMTTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 7),
    _TimeGMTTime_Type()
)
timeGMTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeGMTTime.setStatus("current")
_TimeTimeZone_Type = DisplayString
_TimeTimeZone_Object = MibScalar
timeTimeZone = _TimeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 8),
    _TimeTimeZone_Type()
)
timeTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeTimeZone.setStatus("current")

# Managed Objects groups

lefthandNetworksNsmNtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 2, 1)
)
lefthandNetworksNsmNtpGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpCount"),
        ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "timeGMTTime"),
        ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "timeTimeZone"),
        ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpPreferred"),
        ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpServer"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNtpGroup.setStatus("current")

lefthandNetworksNsmNtpGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 2, 2)
)
lefthandNetworksNsmNtpGroupObsolete.setObjects(
    ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpRowStatus")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNtpGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmNTPMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 1, 1)
)
lefthandNetworksNsmNTPMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "lefthandNetworksNsmNtpGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNTPMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-NTP-MIB",
    **{"lhnNsmNTPModule": lhnNsmNTPModule,
       "lhnNsmNTPModuleConformance": lhnNsmNTPModuleConformance,
       "lhnNsmNTPModuleCompliances": lhnNsmNTPModuleCompliances,
       "lefthandNetworksNsmNTPMibCompliance": lefthandNetworksNsmNTPMibCompliance,
       "lhnNsmNTPModuleGroups": lhnNsmNTPModuleGroups,
       "lefthandNetworksNsmNtpGroup": lefthandNetworksNsmNtpGroup,
       "lefthandNetworksNsmNtpGroupObsolete": lefthandNetworksNsmNtpGroupObsolete,
       "ntpCount": ntpCount,
       "ntpTable": ntpTable,
       "ntpEntry": ntpEntry,
       "ntpIndex": ntpIndex,
       "ntpPreferred": ntpPreferred,
       "ntpServer": ntpServer,
       "ntpRowStatus": ntpRowStatus,
       "timeGMTTime": timeGMTTime,
       "timeTimeZone": timeTimeZone}
)
