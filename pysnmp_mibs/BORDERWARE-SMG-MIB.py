# SNMP MIB module (BORDERWARE-SMG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/watchguard/BORDERWARE-SMG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:17:36 2025
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

(borderware,
 bwProductId,
 bwProducts) = mibBuilder.importSymbols(
    "BORDERWARE-MIB",
    "borderware",
    "bwProductId",
    "bwProducts")

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

bwMailFirewall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11)
)
if mibBuilder.loadTexts:
    bwMailFirewall.setRevisions(
        ("2004-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BwMailFirewall4_ObjectIdentity = ObjectIdentity
bwMailFirewall4 = _BwMailFirewall4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 2, 11)
)
_BwMailFirewallConformance_ObjectIdentity = ObjectIdentity
bwMailFirewallConformance = _BwMailFirewallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 3)
)
_BwMailFirewallCompliances_ObjectIdentity = ObjectIdentity
bwMailFirewallCompliances = _BwMailFirewallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 3, 1)
)
_BwMailFirewallGroups_ObjectIdentity = ObjectIdentity
bwMailFirewallGroups = _BwMailFirewallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 3, 2)
)
_MailEntry_Object = MibTable
mailEntry = _MailEntry_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1)
)
if mibBuilder.loadTexts:
    mailEntry.setStatus("current")
_MailInterval_Type = DisplayString
_MailInterval_Object = MibTableColumn
mailInterval = _MailInterval_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 1),
    _MailInterval_Type()
)
mailInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailInterval.setStatus("current")
_MailRcvd_Type = Counter32
_MailRcvd_Object = MibTableColumn
mailRcvd = _MailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 2),
    _MailRcvd_Type()
)
mailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailRcvd.setStatus("current")
_MailSent_Type = Counter32
_MailSent_Object = MibTableColumn
mailSent = _MailSent_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 3),
    _MailSent_Type()
)
mailSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailSent.setStatus("current")
_MailSpam_Type = Counter32
_MailSpam_Object = MibTableColumn
mailSpam = _MailSpam_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 4),
    _MailSpam_Type()
)
mailSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailSpam.setStatus("current")
_MailReject_Type = Counter32
_MailReject_Object = MibTableColumn
mailReject = _MailReject_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 5),
    _MailReject_Type()
)
mailReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailReject.setStatus("current")
_MailVirus_Type = Counter32
_MailVirus_Object = MibTableColumn
mailVirus = _MailVirus_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 6),
    _MailVirus_Type()
)
mailVirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailVirus.setStatus("current")
_MailClean_Type = Counter32
_MailClean_Object = MibTableColumn
mailClean = _MailClean_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 1, 7),
    _MailClean_Type()
)
mailClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailClean.setStatus("current")
_MailStatus_ObjectIdentity = ObjectIdentity
mailStatus = _MailStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 2)
)
if mibBuilder.loadTexts:
    mailStatus.setStatus("current")
_QueuedMessages_Type = Counter32
_QueuedMessages_Object = MibScalar
queuedMessages = _QueuedMessages_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 2, 1),
    _QueuedMessages_Type()
)
queuedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuedMessages.setStatus("current")
_DeferredMessages_Type = Counter32
_DeferredMessages_Object = MibScalar
deferredMessages = _DeferredMessages_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 2, 2),
    _DeferredMessages_Type()
)
deferredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deferredMessages.setStatus("current")
_TotalMessages_Type = Counter32
_TotalMessages_Object = MibScalar
totalMessages = _TotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10, 2, 3),
    _TotalMessages_Type()
)
totalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMessages.setStatus("current")

# Managed Objects groups

bwMessagesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 3, 2, 1)
)
bwMessagesGroup.setObjects(
      *(("BORDERWARE-SMG-MIB", "queuedMessages"),
        ("BORDERWARE-SMG-MIB", "deferredMessages"),
        ("BORDERWARE-SMG-MIB", "totalMessages"))
)
if mibBuilder.loadTexts:
    bwMessagesGroup.setStatus("current")

bwMailStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 3, 2, 2)
)
bwMailStatsGroup.setObjects(
      *(("BORDERWARE-SMG-MIB", "mailInterval"),
        ("BORDERWARE-SMG-MIB", "mailRcvd"),
        ("BORDERWARE-SMG-MIB", "mailSent"),
        ("BORDERWARE-SMG-MIB", "mailSpam"),
        ("BORDERWARE-SMG-MIB", "mailReject"),
        ("BORDERWARE-SMG-MIB", "mailVirus"),
        ("BORDERWARE-SMG-MIB", "mailClean"))
)
if mibBuilder.loadTexts:
    bwMailStatsGroup.setStatus("current")

mailTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 10)
)
mailTable.setObjects(
      *(("BORDERWARE-SMG-MIB", "bwMailStatsGroup"),
        ("BORDERWARE-SMG-MIB", "bwMessagesGroup"))
)
if mibBuilder.loadTexts:
    mailTable.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwMailFirewallCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8673, 1, 11, 3, 1, 1)
)
bwMailFirewallCompliance.setObjects(
    ("BORDERWARE-SMG-MIB", "bwMessagesGroup")
)
if mibBuilder.loadTexts:
    bwMailFirewallCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BORDERWARE-SMG-MIB",
    **{"bwMailFirewall4": bwMailFirewall4,
       "bwMailFirewall": bwMailFirewall,
       "bwMailFirewallConformance": bwMailFirewallConformance,
       "bwMailFirewallCompliances": bwMailFirewallCompliances,
       "bwMailFirewallCompliance": bwMailFirewallCompliance,
       "bwMailFirewallGroups": bwMailFirewallGroups,
       "bwMessagesGroup": bwMessagesGroup,
       "bwMailStatsGroup": bwMailStatsGroup,
       "mailTable": mailTable,
       "mailEntry": mailEntry,
       "mailInterval": mailInterval,
       "mailRcvd": mailRcvd,
       "mailSent": mailSent,
       "mailSpam": mailSpam,
       "mailReject": mailReject,
       "mailVirus": mailVirus,
       "mailClean": mailClean,
       "mailStatus": mailStatus,
       "queuedMessages": queuedMessages,
       "deferredMessages": deferredMessages,
       "totalMessages": totalMessages}
)
