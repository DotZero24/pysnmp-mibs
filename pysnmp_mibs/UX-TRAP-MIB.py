# SNMP MIB module (UX-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonus/UX-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:50 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(uxAlarmActiveCancelType,
 uxAlarmActiveCategory,
 uxAlarmActiveClrEvtID,
 uxAlarmActiveClrEvtSubID,
 uxAlarmActiveCondition,
 uxAlarmActiveCount,
 uxAlarmActiveDecodeKey,
 uxAlarmActiveDescription,
 uxAlarmActiveFirstOccur,
 uxAlarmActiveHardWareID,
 uxAlarmActiveHighestSeverityAlarm,
 uxAlarmActiveID,
 uxAlarmActiveIndex,
 uxAlarmActiveLastOccur,
 uxAlarmActiveSeverity,
 uxAlarmActiveSourceInstance,
 uxAlarmActiveState,
 uxAlarmActiveSubID,
 uxAlarmConfigIndex) = mibBuilder.importSymbols(
    "UX-OBJECTS-MIB",
    "uxAlarmActiveCancelType",
    "uxAlarmActiveCategory",
    "uxAlarmActiveClrEvtID",
    "uxAlarmActiveClrEvtSubID",
    "uxAlarmActiveCondition",
    "uxAlarmActiveCount",
    "uxAlarmActiveDecodeKey",
    "uxAlarmActiveDescription",
    "uxAlarmActiveFirstOccur",
    "uxAlarmActiveHardWareID",
    "uxAlarmActiveHighestSeverityAlarm",
    "uxAlarmActiveID",
    "uxAlarmActiveIndex",
    "uxAlarmActiveLastOccur",
    "uxAlarmActiveSeverity",
    "uxAlarmActiveSourceInstance",
    "uxAlarmActiveState",
    "uxAlarmActiveSubID",
    "uxAlarmConfigIndex")


# MODULE-IDENTITY

ux = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177)
)
_UxObjects_ObjectIdentity = ObjectIdentity
uxObjects = _UxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1)
)
_UxTraps_ObjectIdentity = ObjectIdentity
uxTraps = _UxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 2)
)

# Managed Objects groups


# Notification objects

uxAlmADcachingfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65537)
)
uxAlmADcachingfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADcachingfailed.setStatus(
        "current"
    )

uxAlmOnlineADqueryfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65538)
)
uxAlmOnlineADqueryfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmOnlineADqueryfailed.setStatus(
        "current"
    )

uxAlmUserloggedin = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65540)
)
uxAlmUserloggedin.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmUserloggedin.setStatus(
        "current"
    )

uxAlmUserloginfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65541)
)
uxAlmUserloginfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmUserloginfailed.setStatus(
        "current"
    )

uxAlmADUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65542)
)
uxAlmADUnreachable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADUnreachable.setStatus(
        "current"
    )

uxAlmADReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65543)
)
uxAlmADReachable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADReachable.setStatus(
        "current"
    )

uxAlmADcachingsuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65544)
)
uxAlmADcachingsuccessful.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADcachingsuccessful.setStatus(
        "current"
    )

uxAlmADbackupfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65545)
)
uxAlmADbackupfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADbackupfailed.setStatus(
        "current"
    )

uxAlmADsuccessfullybackedup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65546)
)
uxAlmADsuccessfullybackedup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADsuccessfullybackedup.setStatus(
        "current"
    )

uxAlmADcachetruncated = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65547)
)
uxAlmADcachetruncated.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmADcachetruncated.setStatus(
        "current"
    )

uxAlmRADIUSServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65548)
)
uxAlmRADIUSServerUnreachable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRADIUSServerUnreachable.setStatus(
        "current"
    )

uxAlmRADIUSReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65549)
)
uxAlmRADIUSReachable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRADIUSReachable.setStatus(
        "current"
    )

uxAlmCDRloggingfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65550)
)
uxAlmCDRloggingfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCDRloggingfailed.setStatus(
        "current"
    )

uxAlmCDRbackupfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 65551)
)
uxAlmCDRbackupfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCDRbackupfailed.setStatus(
        "current"
    )

uxAlmInvalidCardIDEEPROMData = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131073)
)
uxAlmInvalidCardIDEEPROMData.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInvalidCardIDEEPROMData.setStatus(
        "current"
    )

uxAlmCardHealthySignalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131074)
)
uxAlmCardHealthySignalFailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCardHealthySignalFailure.setStatus(
        "current"
    )

uxAlmCardnotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131075)
)
uxAlmCardnotSupported.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCardnotSupported.setStatus(
        "current"
    )

uxAlmPowerSupplyinputfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131076)
)
uxAlmPowerSupplyinputfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPowerSupplyinputfailure.setStatus(
        "current"
    )

uxAlmPowerSupplyinputrestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131077)
)
uxAlmPowerSupplyinputrestored.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPowerSupplyinputrestored.setStatus(
        "current"
    )

uxAlmPowerSupplyoutputfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131078)
)
uxAlmPowerSupplyoutputfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPowerSupplyoutputfailure.setStatus(
        "current"
    )

uxAlmSingleFanfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131079)
)
uxAlmSingleFanfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSingleFanfailure.setStatus(
        "current"
    )

uxAlmMultipleFanFailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131080)
)
uxAlmMultipleFanFailures.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmMultipleFanFailures.setStatus(
        "current"
    )

uxAlmSystemTemperatureWarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131081)
)
uxAlmSystemTemperatureWarm.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemTemperatureWarm.setStatus(
        "current"
    )

uxAlmSystemTemperatureWarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131082)
)
uxAlmSystemTemperatureWarmCleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemTemperatureWarmCleared.setStatus(
        "current"
    )

uxAlmSystemTemperatureHot = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131083)
)
uxAlmSystemTemperatureHot.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemTemperatureHot.setStatus(
        "current"
    )

uxAlmSystemTemperatureHotCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 131084)
)
uxAlmSystemTemperatureHotCleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemTemperatureHotCleared.setStatus(
        "current"
    )

uxAlmLicensesexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 196609)
)
uxAlmLicensesexpired.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLicensesexpired.setStatus(
        "current"
    )

uxAlmLicenseexpiresin2weeks = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 196610)
)
uxAlmLicenseexpiresin2weeks.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLicenseexpiresin2weeks.setStatus(
        "current"
    )

uxAlmNewLicenseapplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 196611)
)
uxAlmNewLicenseapplied.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNewLicenseapplied.setStatus(
        "current"
    )

uxAlmFailedtoApplyLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 196612)
)
uxAlmFailedtoApplyLicense.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedtoApplyLicense.setStatus(
        "current"
    )

uxAlmFailedtoacquirelicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 196613)
)
uxAlmFailedtoacquirelicense.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedtoacquirelicense.setStatus(
        "current"
    )

uxAlmASMUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327681)
)
uxAlmASMUnreachable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMUnreachable.setStatus(
        "current"
    )

uxAlmClearASMUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327682)
)
uxAlmClearASMUnreachable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmClearASMUnreachable.setStatus(
        "current"
    )

uxAlmASMFailureRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327683)
)
uxAlmASMFailureRecovered.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMFailureRecovered.setStatus(
        "current"
    )

uxAlmASMServicesNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327684)
)
uxAlmASMServicesNotRunning.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMServicesNotRunning.setStatus(
        "current"
    )

uxAlmClearASMServicesNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327685)
)
uxAlmClearASMServicesNotRunning.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmClearASMServicesNotRunning.setStatus(
        "current"
    )

uxAlmASMServicesRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327686)
)
uxAlmASMServicesRecovered.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMServicesRecovered.setStatus(
        "current"
    )

uxAlmASMServiceRestartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327687)
)
uxAlmASMServiceRestartFailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMServiceRestartFailed.setStatus(
        "current"
    )

uxAlmASMSystemStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327688)
)
uxAlmASMSystemStarted.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMSystemStarted.setStatus(
        "current"
    )

uxAlmASMSystemShuttingdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327689)
)
uxAlmASMSystemShuttingdown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMSystemShuttingdown.setStatus(
        "current"
    )

uxAlmEthernetLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327690)
)
uxAlmEthernetLinkDown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmEthernetLinkDown.setStatus(
        "current"
    )

uxAlmEthernetLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327691)
)
uxAlmEthernetLinkUp.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmEthernetLinkUp.setStatus(
        "current"
    )

uxAlmASMSBCIPSubnetMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327692)
)
uxAlmASMSBCIPSubnetMismatch.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMSBCIPSubnetMismatch.setStatus(
        "current"
    )

uxAlmASMSBCIPSubnetMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 327693)
)
uxAlmASMSBCIPSubnetMatch.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmASMSBCIPSubnetMatch.setStatus(
        "current"
    )

uxAlmConfigurationchangeoccurredonActionSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458753)
)
uxAlmConfigurationchangeoccurredonActionSet.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigurationchangeoccurredonActionSet.setStatus(
        "current"
    )

uxAlmConfigurationchangeoccurredonNormalizationTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458754)
)
uxAlmConfigurationchangeoccurredonNormalizationTable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigurationchangeoccurredonNormalizationTable.setStatus(
        "current"
    )

uxAlmConfigurationchangeoccurredonRouteTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458755)
)
uxAlmConfigurationchangeoccurredonRouteTable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigurationchangeoccurredonRouteTable.setStatus(
        "current"
    )

uxAlmConfigurationchangeoccurredonTransformationTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458756)
)
uxAlmConfigurationchangeoccurredonTransformationTables.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigurationchangeoccurredonTransformationTables.setStatus(
        "current"
    )

uxAlmRoutetemporarilydisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458757)
)
uxAlmRoutetemporarilydisabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRoutetemporarilydisabled.setStatus(
        "current"
    )

uxAlmRouteenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458758)
)
uxAlmRouteenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRouteenabled.setStatus(
        "current"
    )

uxAlmACallexceededthelimitfornumberofdestinations = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458759)
)
uxAlmACallexceededthelimitfornumberofdestinations.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmACallexceededthelimitfornumberofdestinations.setStatus(
        "current"
    )

uxAlmCallforkingusedwithnoforkinglicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458760)
)
uxAlmCallforkingusedwithnoforkinglicense.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCallforkingusedwithnoforkinglicense.setStatus(
        "current"
    )

uxAlmInvocationofInvokeActionSetexceededthemaximumnestinglimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458761)
)
uxAlmInvocationofInvokeActionSetexceededthemaximumnestinglimit.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInvocationofInvokeActionSetexceededthemaximumnestinglimit.setStatus(
        "current"
    )

uxAlmConfigurationchangeoccurredonCallbackTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 458762)
)
uxAlmConfigurationchangeoccurredonCallbackTables.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigurationchangeoccurredonCallbackTables.setStatus(
        "current"
    )

uxAlmChannelisinservice = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 524289)
)
uxAlmChannelisinservice.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmChannelisinservice.setStatus(
        "current"
    )

uxAlmChannelisoutofservice = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 524290)
)
uxAlmChannelisoutofservice.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmChannelisoutofservice.setStatus(
        "current"
    )

uxAlmEmergencyCallAttempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 524291)
)
uxAlmEmergencyCallAttempted.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmEmergencyCallAttempted.setStatus(
        "current"
    )

uxAlmEmergencyCallCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 524292)
)
uxAlmEmergencyCallCompleted.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmEmergencyCallCompleted.setStatus(
        "current"
    )

uxAlmSIPServernotresponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589825)
)
uxAlmSIPServernotresponding.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPServernotresponding.setStatus(
        "current"
    )

uxAlmSignalingGrouptakenoutofservice = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589826)
)
uxAlmSignalingGrouptakenoutofservice.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSignalingGrouptakenoutofservice.setStatus(
        "current"
    )

uxAlmSignalingGroupdisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589827)
)
uxAlmSignalingGroupdisabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSignalingGroupdisabled.setStatus(
        "current"
    )

uxAlmSIPTLSHandshakeAlertFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589828)
)
uxAlmSIPTLSHandshakeAlertFailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPTLSHandshakeAlertFailure.setStatus(
        "current"
    )

uxAlmSIPTLSHandshakeInactivityTimeoutFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589829)
)
uxAlmSIPTLSHandshakeInactivityTimeoutFailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPTLSHandshakeInactivityTimeoutFailure.setStatus(
        "current"
    )

uxAlmConfiguredportnumbermismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589830)
)
uxAlmConfiguredportnumbermismatch.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfiguredportnumbermismatch.setStatus(
        "current"
    )

uxAlmSIPServerbecameresponsive = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589831)
)
uxAlmSIPServerbecameresponsive.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPServerbecameresponsive.setStatus(
        "current"
    )

uxAlmSIPclusterwentdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589832)
)
uxAlmSIPclusterwentdown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPclusterwentdown.setStatus(
        "current"
    )

uxAlmSIPClusterenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589833)
)
uxAlmSIPClusterenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPClusterenabled.setStatus(
        "current"
    )

uxAlmSIPSignalinggroupenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589834)
)
uxAlmSIPSignalinggroupenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPSignalinggroupenabled.setStatus(
        "current"
    )

uxAlmSIPSignalinggroupconfigDNSfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589835)
)
uxAlmSIPSignalinggroupconfigDNSfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPSignalinggroupconfigDNSfailure.setStatus(
        "current"
    )

uxAlmSIPSignalinggroupconfigFQDNresolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589836)
)
uxAlmSIPSignalinggroupconfigFQDNresolved.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPSignalinggroupconfigFQDNresolved.setStatus(
        "current"
    )

uxAlmSIPServerconfigDNSfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589837)
)
uxAlmSIPServerconfigDNSfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPServerconfigDNSfailure.setStatus(
        "current"
    )

uxAlmSIPServerconfigFQDNresolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589838)
)
uxAlmSIPServerconfigFQDNresolved.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPServerconfigFQDNresolved.setStatus(
        "current"
    )

uxAlmSIPcallsessionDNSfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589839)
)
uxAlmSIPcallsessionDNSfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPcallsessionDNSfailure.setStatus(
        "current"
    )

uxAlmAcquiringlicenseforRegisterfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589840)
)
uxAlmAcquiringlicenseforRegisterfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmAcquiringlicenseforRegisterfailed.setStatus(
        "current"
    )

uxAlmSessionleakorsomeotherresourceleak = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589841)
)
uxAlmSessionleakorsomeotherresourceleak.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSessionleakorsomeotherresourceleak.setStatus(
        "current"
    )

uxAlmFailedtobindtonetworkinterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589842)
)
uxAlmFailedtobindtonetworkinterface.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedtobindtonetworkinterface.setStatus(
        "current"
    )

uxAlmSuccessfullyboundtonetworkinterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589843)
)
uxAlmSuccessfullyboundtonetworkinterface.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSuccessfullyboundtonetworkinterface.setStatus(
        "current"
    )

uxAlmSIPRegisterServernotresponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589844)
)
uxAlmSIPRegisterServernotresponding.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPRegisterServernotresponding.setStatus(
        "current"
    )

uxAlmSIPRegisterServerbecameresponsive = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589845)
)
uxAlmSIPRegisterServerbecameresponsive.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSIPRegisterServerbecameresponsive.setStatus(
        "current"
    )

uxAlmRegistrationnotvalidreceivedstalefalse = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589846)
)
uxAlmRegistrationnotvalidreceivedstalefalse.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRegistrationnotvalidreceivedstalefalse.setStatus(
        "current"
    )

uxAlmConfigchangeforSIPendpointthatreceivedstalefalse = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 589847)
)
uxAlmConfigchangeforSIPendpointthatreceivedstalefalse.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigchangeforSIPendpointthatreceivedstalefalse.setStatus(
        "current"
    )

uxAlmDChanneldown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 655361)
)
uxAlmDChanneldown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDChanneldown.setStatus(
        "current"
    )

uxAlmDChannelup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 655362)
)
uxAlmDChannelup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDChannelup.setStatus(
        "current"
    )

uxAlmCallreleasedduetochannelrestartbyfarend = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 655363)
)
uxAlmCallreleasedduetochannelrestartbyfarend.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCallreleasedduetochannelrestartbyfarend.setStatus(
        "current"
    )

uxAlmPortdisabledbyoperator = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720897)
)
uxAlmPortdisabledbyoperator.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortdisabledbyoperator.setStatus(
        "current"
    )

uxAlmPortenabledbyoperator = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720898)
)
uxAlmPortenabledbyoperator.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortenabledbyoperator.setStatus(
        "current"
    )

uxAlmDS1LoopbackEnter = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720899)
)
uxAlmDS1LoopbackEnter.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDS1LoopbackEnter.setStatus(
        "current"
    )

uxAlmDS1LoopbackExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720900)
)
uxAlmDS1LoopbackExit.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDS1LoopbackExit.setStatus(
        "current"
    )

uxAlmRedAlarmLossofSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720901)
)
uxAlmRedAlarmLossofSignal.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRedAlarmLossofSignal.setStatus(
        "current"
    )

uxAlmRedAlarmLossofSignalcleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720902)
)
uxAlmRedAlarmLossofSignalcleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRedAlarmLossofSignalcleared.setStatus(
        "current"
    )

uxAlmRedAlarmLossofFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720903)
)
uxAlmRedAlarmLossofFrame.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRedAlarmLossofFrame.setStatus(
        "current"
    )

uxAlmRedAlarmLossofFramecleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720904)
)
uxAlmRedAlarmLossofFramecleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRedAlarmLossofFramecleared.setStatus(
        "current"
    )

uxAlmBlueAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720905)
)
uxAlmBlueAlarm.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmBlueAlarm.setStatus(
        "current"
    )

uxAlmBlueAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720906)
)
uxAlmBlueAlarmCleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmBlueAlarmCleared.setStatus(
        "current"
    )

uxAlmYellowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720907)
)
uxAlmYellowAlarm.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmYellowAlarm.setStatus(
        "current"
    )

uxAlmYellowAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720908)
)
uxAlmYellowAlarmCleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmYellowAlarmCleared.setStatus(
        "current"
    )

uxAlmPortdisabledasportnotfoundonDS1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720909)
)
uxAlmPortdisabledasportnotfoundonDS1.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortdisabledasportnotfoundonDS1.setStatus(
        "current"
    )

uxAlmClockrecoveryswitchedtoportconfiguredassecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720910)
)
uxAlmClockrecoveryswitchedtoportconfiguredassecondary.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmClockrecoveryswitchedtoportconfiguredassecondary.setStatus(
        "current"
    )

uxAlmClockrecoveryswitchovertosecondaryportcleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720911)
)
uxAlmClockrecoveryswitchovertosecondaryportcleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmClockrecoveryswitchovertosecondaryportcleared.setStatus(
        "current"
    )

uxAlmClockrecoveryswitchedtofreerunclock = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720912)
)
uxAlmClockrecoveryswitchedtofreerunclock.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmClockrecoveryswitchedtofreerunclock.setStatus(
        "current"
    )

uxAlmClockrecoveryswitchovertofreerunclockcleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720913)
)
uxAlmClockrecoveryswitchovertofreerunclockcleared.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmClockrecoveryswitchovertofreerunclockcleared.setStatus(
        "current"
    )

uxAlmLinecardnotdetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720914)
)
uxAlmLinecardnotdetected.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLinecardnotdetected.setStatus(
        "current"
    )

uxAlmLinecarddetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720915)
)
uxAlmLinecarddetected.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLinecarddetected.setStatus(
        "current"
    )

uxAlmPortdisabledforrelaypassthroughstateactivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720916)
)
uxAlmPortdisabledforrelaypassthroughstateactivation.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortdisabledforrelaypassthroughstateactivation.setStatus(
        "current"
    )

uxAlmPortenabledforrelayonlinestateactivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720917)
)
uxAlmPortenabledforrelayonlinestateactivation.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortenabledforrelayonlinestateactivation.setStatus(
        "current"
    )

uxAlmLayer1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720918)
)
uxAlmLayer1down.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLayer1down.setStatus(
        "current"
    )

uxAlmLayer1up = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720919)
)
uxAlmLayer1up.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLayer1up.setStatus(
        "current"
    )

uxAlmPortdisabledasportnotfoundonanalogcard = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720920)
)
uxAlmPortdisabledasportnotfoundonanalogcard.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortdisabledasportnotfoundonanalogcard.setStatus(
        "current"
    )

uxAlmPortsdisabledforrelaypassthrustatechgonanalogrelaycards = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720921)
)
uxAlmPortsdisabledforrelaypassthrustatechgonanalogrelaycards.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortsdisabledforrelaypassthrustatechgonanalogrelaycards.setStatus(
        "current"
    )

uxAlmPortsenabledforrelayonlinestatechangeonanalogrelaycardpairs = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720922)
)
uxAlmPortsenabledforrelayonlinestatechangeonanalogrelaycardpairs.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortsenabledforrelayonlinestatechangeonanalogrelaycardpairs.setStatus(
        "current"
    )

uxAlmPortstatusdowndetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720923)
)
uxAlmPortstatusdowndetected.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortstatusdowndetected.setStatus(
        "current"
    )

uxAlmPortstatusup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720924)
)
uxAlmPortstatusup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortstatusup.setStatus(
        "current"
    )

uxAlmPortdisabledasportnotfoundonBRI = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720925)
)
uxAlmPortdisabledasportnotfoundonBRI.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortdisabledasportnotfoundonBRI.setStatus(
        "current"
    )

uxAlmSystemnotoperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 720926)
)
uxAlmSystemnotoperational.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemnotoperational.setStatus(
        "current"
    )

uxAlmDSPnotcomingup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 786433)
)
uxAlmDSPnotcomingup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDSPnotcomingup.setStatus(
        "current"
    )

uxAlmDSPreset = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 786434)
)
uxAlmDSPreset.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDSPreset.setStatus(
        "current"
    )

uxAlmDSPCardisUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 786435)
)
uxAlmDSPCardisUP.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDSPCardisUP.setStatus(
        "current"
    )

uxAlmDSPChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 786436)
)
uxAlmDSPChannelFailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDSPChannelFailure.setStatus(
        "current"
    )

uxAlmTLSOwnServerCertificatewillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 851969)
)
uxAlmTLSOwnServerCertificatewillExpire.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTLSOwnServerCertificatewillExpire.setStatus(
        "current"
    )

uxAlmTLSOwnServerCertificatehasExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 851970)
)
uxAlmTLSOwnServerCertificatehasExpired.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTLSOwnServerCertificatehasExpired.setStatus(
        "current"
    )

uxAlmTLSOwnServerCertificateismissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 851971)
)
uxAlmTLSOwnServerCertificateismissing.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTLSOwnServerCertificateismissing.setStatus(
        "current"
    )

uxAlmTLSSelfSignCertificateGenerationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 851972)
)
uxAlmTLSSelfSignCertificateGenerationFailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTLSSelfSignCertificateGenerationFailed.setStatus(
        "current"
    )

uxAlmNewandValidTLSOwnServerCertificateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 851973)
)
uxAlmNewandValidTLSOwnServerCertificateDetected.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNewandValidTLSOwnServerCertificateDetected.setStatus(
        "current"
    )

uxAlmInvalidSessionofaTLSconnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 917505)
)
uxAlmInvalidSessionofaTLSconnection.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInvalidSessionofaTLSconnection.setStatus(
        "current"
    )

uxAlmBMPTLSHandshakeAlertFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 917506)
)
uxAlmBMPTLSHandshakeAlertFailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmBMPTLSHandshakeAlertFailure.setStatus(
        "current"
    )

uxAlmBMPTLSHandshakeInactivityTimeoutFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 917507)
)
uxAlmBMPTLSHandshakeInactivityTimeoutFailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmBMPTLSHandshakeInactivityTimeoutFailure.setStatus(
        "current"
    )

uxAlmInterfaceoperdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983041)
)
uxAlmInterfaceoperdown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInterfaceoperdown.setStatus(
        "current"
    )

uxAlmInterfaceoperup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983042)
)
uxAlmInterfaceoperup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInterfaceoperup.setStatus(
        "current"
    )

uxAlmInterfaceadminup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983043)
)
uxAlmInterfaceadminup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInterfaceadminup.setStatus(
        "current"
    )

uxAlmInterfaceadmindown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983044)
)
uxAlmInterfaceadmindown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInterfaceadmindown.setStatus(
        "current"
    )

uxAlmAdminPortoperdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983045)
)
uxAlmAdminPortoperdown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmAdminPortoperdown.setStatus(
        "current"
    )

uxAlmAdminPortoperup = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983046)
)
uxAlmAdminPortoperup.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmAdminPortoperup.setStatus(
        "current"
    )

uxAlmPortoperdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983047)
)
uxAlmPortoperdown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPortoperdown.setStatus(
        "current"
    )

uxAlmRIPlicensenotenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983048)
)
uxAlmRIPlicensenotenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRIPlicensenotenabled.setStatus(
        "current"
    )

uxAlmOSPFlicensenotenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983049)
)
uxAlmOSPFlicensenotenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmOSPFlicensenotenabled.setStatus(
        "current"
    )

uxAlmLinkMonitorPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983050)
)
uxAlmLinkMonitorPeerDown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLinkMonitorPeerDown.setStatus(
        "current"
    )

uxAlmLinkMonitorPeerReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983051)
)
uxAlmLinkMonitorPeerReady.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmLinkMonitorPeerReady.setStatus(
        "current"
    )

uxAlmTunnelconnectiondisabledbyoperator = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983052)
)
uxAlmTunnelconnectiondisabledbyoperator.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnelconnectiondisabledbyoperator.setStatus(
        "current"
    )

uxAlmTunnelconnectionenabledbyoperator = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983053)
)
uxAlmTunnelconnectionenabledbyoperator.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnelconnectionenabledbyoperator.setStatus(
        "current"
    )

uxAlmTunnellinklost = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983054)
)
uxAlmTunnellinklost.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnellinklost.setStatus(
        "current"
    )

uxAlmTunnellinkrestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983055)
)
uxAlmTunnellinkrestored.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnellinkrestored.setStatus(
        "current"
    )

uxAlmIPseclicensenotenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983056)
)
uxAlmIPseclicensenotenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmIPseclicensenotenabled.setStatus(
        "current"
    )

uxAlmNegotiatedDuplexityHalf = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983057)
)
uxAlmNegotiatedDuplexityHalf.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNegotiatedDuplexityHalf.setStatus(
        "current"
    )

uxAlmNegotiatedDuplexityFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983058)
)
uxAlmNegotiatedDuplexityFull.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNegotiatedDuplexityFull.setStatus(
        "current"
    )

uxAlmPreferredlinkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983059)
)
uxAlmPreferredlinkdown.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPreferredlinkdown.setStatus(
        "current"
    )

uxAlmPreferredlinkready = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983060)
)
uxAlmPreferredlinkready.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmPreferredlinkready.setStatus(
        "current"
    )

uxAlmTunnelnotificationfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983061)
)
uxAlmTunnelnotificationfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnelnotificationfailure.setStatus(
        "current"
    )

uxAlmTunnellocalsubnetsarenonnegotiable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983062)
)
uxAlmTunnellocalsubnetsarenonnegotiable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnellocalsubnetsarenonnegotiable.setStatus(
        "current"
    )

uxAlmTunnelremotesubnetsarenonnegotiable = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 983063)
)
uxAlmTunnelremotesubnetsarenonnegotiable.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmTunnelremotesubnetsarenonnegotiable.setStatus(
        "current"
    )

uxAlmApplicationServicerestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048577)
)
uxAlmApplicationServicerestarted.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmApplicationServicerestarted.setStatus(
        "current"
    )

uxAlmActivepartitionswitched = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048578)
)
uxAlmActivepartitionswitched.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmActivepartitionswitched.setStatus(
        "current"
    )

uxAlmFailedtomountpartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048579)
)
uxAlmFailedtomountpartition.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedtomountpartition.setStatus(
        "current"
    )

uxAlmFailedtosetactivepartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048580)
)
uxAlmFailedtosetactivepartition.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedtosetactivepartition.setStatus(
        "current"
    )

uxAlmAttempttorepairbootparametermismatchfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048581)
)
uxAlmAttempttorepairbootparametermismatchfailed.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmAttempttorepairbootparametermismatchfailed.setStatus(
        "current"
    )

uxAlmBootparametermismatchdetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048582)
)
uxAlmBootparametermismatchdetected.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmBootparametermismatchdetected.setStatus(
        "current"
    )

uxAlmFailedPoweronmemoryselftest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048583)
)
uxAlmFailedPoweronmemoryselftest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronmemoryselftest.setStatus(
        "current"
    )

uxAlmFailedPoweronCoreSwitchtest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048584)
)
uxAlmFailedPoweronCoreSwitchtest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronCoreSwitchtest.setStatus(
        "current"
    )

uxAlmFailedPoweronSecondarySwitchtest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048585)
)
uxAlmFailedPoweronSecondarySwitchtest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronSecondarySwitchtest.setStatus(
        "current"
    )

uxAlmFailedPoweronexternalQuadPHYtest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048586)
)
uxAlmFailedPoweronexternalQuadPHYtest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronexternalQuadPHYtest.setStatus(
        "current"
    )

uxAlmFailedPoweronexternalSinglePHYtest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048587)
)
uxAlmFailedPoweronexternalSinglePHYtest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronexternalSinglePHYtest.setStatus(
        "current"
    )

uxAlmFailedPoweronCPUPHYtest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048588)
)
uxAlmFailedPoweronCPUPHYtest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronCPUPHYtest.setStatus(
        "current"
    )

uxAlmFailedPoweronTSItest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048589)
)
uxAlmFailedPoweronTSItest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweronTSItest.setStatus(
        "current"
    )

uxAlmFailedPoweroninternal5PortPHYtest = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048590)
)
uxAlmFailedPoweroninternal5PortPHYtest.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmFailedPoweroninternal5PortPHYtest.setStatus(
        "current"
    )

uxAlmSystemUpAfterPlannedRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048591)
)
uxAlmSystemUpAfterPlannedRestart.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemUpAfterPlannedRestart.setStatus(
        "current"
    )

uxAlmSystemUpAfterUnplannedRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1048592)
)
uxAlmSystemUpAfterUnplannedRestart.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmSystemUpAfterUnplannedRestart.setStatus(
        "current"
    )

uxAlmNoresponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114113)
)
uxAlmNoresponse.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNoresponse.setStatus(
        "current"
    )

uxAlmRemoteenddidnotbackoffinglare = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114114)
)
uxAlmRemoteenddidnotbackoffinglare.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmRemoteenddidnotbackoffinglare.setStatus(
        "current"
    )

uxAlmWinkexpecteddidnotarrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114115)
)
uxAlmWinkexpecteddidnotarrive.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmWinkexpecteddidnotarrive.setStatus(
        "current"
    )

uxAlmNodialtone = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114116)
)
uxAlmNodialtone.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNodialtone.setStatus(
        "current"
    )

uxAlmCASsignalinggroupdisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114117)
)
uxAlmCASsignalinggroupdisabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCASsignalinggroupdisabled.setStatus(
        "current"
    )

uxAlmCASlicensenotenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114118)
)
uxAlmCASlicensenotenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCASlicensenotenabled.setStatus(
        "current"
    )

uxAlmCASlicenseenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114119)
)
uxAlmCASlicenseenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCASlicenseenabled.setStatus(
        "current"
    )

uxAlmWinkReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114120)
)
uxAlmWinkReceived.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmWinkReceived.setStatus(
        "current"
    )

uxAlmDialToneReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114121)
)
uxAlmDialToneReceived.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmDialToneReceived.setStatus(
        "current"
    )

uxAlmResponseReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114122)
)
uxAlmResponseReceived.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmResponseReceived.setStatus(
        "current"
    )

uxAlmInvalidcharactersincallingnumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114123)
)
uxAlmInvalidcharactersincallingnumber.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInvalidcharactersincallingnumber.setStatus(
        "current"
    )

uxAlmInvalidcharactersincallednumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114124)
)
uxAlmInvalidcharactersincallednumber.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmInvalidcharactersincallednumber.setStatus(
        "current"
    )

uxAlmCASsignalinggroupenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114125)
)
uxAlmCASsignalinggroupenabled.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCASsignalinggroupenabled.setStatus(
        "current"
    )

uxAlmCASR2CDBiterror = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114126)
)
uxAlmCASR2CDBiterror.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCASR2CDBiterror.setStatus(
        "current"
    )

uxAlmCASR2CDBiterrorclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114127)
)
uxAlmCASR2CDBiterrorclear.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmCASR2CDBiterrorclear.setStatus(
        "current"
    )

uxAlmNetworkGlareoccured = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1114128)
)
uxAlmNetworkGlareoccured.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmNetworkGlareoccured.setStatus(
        "current"
    )

uxAlmConfigvalidationfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 177, 15, 2, 1179649)
)
uxAlmConfigvalidationfailure.setObjects(
      *(("UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmConfigIndex"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCondition"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSeverity"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCategory"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCancelType"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDecodeKey"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveCount"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveState"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveSourceInstance"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveFirstOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveLastOccur"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveClrEvtSubID"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveDescription"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHighestSeverityAlarm"),
        ("UX-OBJECTS-MIB", "uxAlarmActiveHardWareID"))
)
if mibBuilder.loadTexts:
    uxAlmConfigvalidationfailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UX-TRAP-MIB",
    **{"net": net,
       "ux": ux,
       "uxObjects": uxObjects,
       "uxTraps": uxTraps,
       "uxAlmADcachingfailed": uxAlmADcachingfailed,
       "uxAlmOnlineADqueryfailed": uxAlmOnlineADqueryfailed,
       "uxAlmUserloggedin": uxAlmUserloggedin,
       "uxAlmUserloginfailed": uxAlmUserloginfailed,
       "uxAlmADUnreachable": uxAlmADUnreachable,
       "uxAlmADReachable": uxAlmADReachable,
       "uxAlmADcachingsuccessful": uxAlmADcachingsuccessful,
       "uxAlmADbackupfailed": uxAlmADbackupfailed,
       "uxAlmADsuccessfullybackedup": uxAlmADsuccessfullybackedup,
       "uxAlmADcachetruncated": uxAlmADcachetruncated,
       "uxAlmRADIUSServerUnreachable": uxAlmRADIUSServerUnreachable,
       "uxAlmRADIUSReachable": uxAlmRADIUSReachable,
       "uxAlmCDRloggingfailed": uxAlmCDRloggingfailed,
       "uxAlmCDRbackupfailed": uxAlmCDRbackupfailed,
       "uxAlmInvalidCardIDEEPROMData": uxAlmInvalidCardIDEEPROMData,
       "uxAlmCardHealthySignalFailure": uxAlmCardHealthySignalFailure,
       "uxAlmCardnotSupported": uxAlmCardnotSupported,
       "uxAlmPowerSupplyinputfailure": uxAlmPowerSupplyinputfailure,
       "uxAlmPowerSupplyinputrestored": uxAlmPowerSupplyinputrestored,
       "uxAlmPowerSupplyoutputfailure": uxAlmPowerSupplyoutputfailure,
       "uxAlmSingleFanfailure": uxAlmSingleFanfailure,
       "uxAlmMultipleFanFailures": uxAlmMultipleFanFailures,
       "uxAlmSystemTemperatureWarm": uxAlmSystemTemperatureWarm,
       "uxAlmSystemTemperatureWarmCleared": uxAlmSystemTemperatureWarmCleared,
       "uxAlmSystemTemperatureHot": uxAlmSystemTemperatureHot,
       "uxAlmSystemTemperatureHotCleared": uxAlmSystemTemperatureHotCleared,
       "uxAlmLicensesexpired": uxAlmLicensesexpired,
       "uxAlmLicenseexpiresin2weeks": uxAlmLicenseexpiresin2weeks,
       "uxAlmNewLicenseapplied": uxAlmNewLicenseapplied,
       "uxAlmFailedtoApplyLicense": uxAlmFailedtoApplyLicense,
       "uxAlmFailedtoacquirelicense": uxAlmFailedtoacquirelicense,
       "uxAlmASMUnreachable": uxAlmASMUnreachable,
       "uxAlmClearASMUnreachable": uxAlmClearASMUnreachable,
       "uxAlmASMFailureRecovered": uxAlmASMFailureRecovered,
       "uxAlmASMServicesNotRunning": uxAlmASMServicesNotRunning,
       "uxAlmClearASMServicesNotRunning": uxAlmClearASMServicesNotRunning,
       "uxAlmASMServicesRecovered": uxAlmASMServicesRecovered,
       "uxAlmASMServiceRestartFailed": uxAlmASMServiceRestartFailed,
       "uxAlmASMSystemStarted": uxAlmASMSystemStarted,
       "uxAlmASMSystemShuttingdown": uxAlmASMSystemShuttingdown,
       "uxAlmEthernetLinkDown": uxAlmEthernetLinkDown,
       "uxAlmEthernetLinkUp": uxAlmEthernetLinkUp,
       "uxAlmASMSBCIPSubnetMismatch": uxAlmASMSBCIPSubnetMismatch,
       "uxAlmASMSBCIPSubnetMatch": uxAlmASMSBCIPSubnetMatch,
       "uxAlmConfigurationchangeoccurredonActionSet": uxAlmConfigurationchangeoccurredonActionSet,
       "uxAlmConfigurationchangeoccurredonNormalizationTable": uxAlmConfigurationchangeoccurredonNormalizationTable,
       "uxAlmConfigurationchangeoccurredonRouteTable": uxAlmConfigurationchangeoccurredonRouteTable,
       "uxAlmConfigurationchangeoccurredonTransformationTables": uxAlmConfigurationchangeoccurredonTransformationTables,
       "uxAlmRoutetemporarilydisabled": uxAlmRoutetemporarilydisabled,
       "uxAlmRouteenabled": uxAlmRouteenabled,
       "uxAlmACallexceededthelimitfornumberofdestinations": uxAlmACallexceededthelimitfornumberofdestinations,
       "uxAlmCallforkingusedwithnoforkinglicense": uxAlmCallforkingusedwithnoforkinglicense,
       "uxAlmInvocationofInvokeActionSetexceededthemaximumnestinglimit": uxAlmInvocationofInvokeActionSetexceededthemaximumnestinglimit,
       "uxAlmConfigurationchangeoccurredonCallbackTables": uxAlmConfigurationchangeoccurredonCallbackTables,
       "uxAlmChannelisinservice": uxAlmChannelisinservice,
       "uxAlmChannelisoutofservice": uxAlmChannelisoutofservice,
       "uxAlmEmergencyCallAttempted": uxAlmEmergencyCallAttempted,
       "uxAlmEmergencyCallCompleted": uxAlmEmergencyCallCompleted,
       "uxAlmSIPServernotresponding": uxAlmSIPServernotresponding,
       "uxAlmSignalingGrouptakenoutofservice": uxAlmSignalingGrouptakenoutofservice,
       "uxAlmSignalingGroupdisabled": uxAlmSignalingGroupdisabled,
       "uxAlmSIPTLSHandshakeAlertFailure": uxAlmSIPTLSHandshakeAlertFailure,
       "uxAlmSIPTLSHandshakeInactivityTimeoutFailure": uxAlmSIPTLSHandshakeInactivityTimeoutFailure,
       "uxAlmConfiguredportnumbermismatch": uxAlmConfiguredportnumbermismatch,
       "uxAlmSIPServerbecameresponsive": uxAlmSIPServerbecameresponsive,
       "uxAlmSIPclusterwentdown": uxAlmSIPclusterwentdown,
       "uxAlmSIPClusterenabled": uxAlmSIPClusterenabled,
       "uxAlmSIPSignalinggroupenabled": uxAlmSIPSignalinggroupenabled,
       "uxAlmSIPSignalinggroupconfigDNSfailure": uxAlmSIPSignalinggroupconfigDNSfailure,
       "uxAlmSIPSignalinggroupconfigFQDNresolved": uxAlmSIPSignalinggroupconfigFQDNresolved,
       "uxAlmSIPServerconfigDNSfailure": uxAlmSIPServerconfigDNSfailure,
       "uxAlmSIPServerconfigFQDNresolved": uxAlmSIPServerconfigFQDNresolved,
       "uxAlmSIPcallsessionDNSfailure": uxAlmSIPcallsessionDNSfailure,
       "uxAlmAcquiringlicenseforRegisterfailed": uxAlmAcquiringlicenseforRegisterfailed,
       "uxAlmSessionleakorsomeotherresourceleak": uxAlmSessionleakorsomeotherresourceleak,
       "uxAlmFailedtobindtonetworkinterface": uxAlmFailedtobindtonetworkinterface,
       "uxAlmSuccessfullyboundtonetworkinterface": uxAlmSuccessfullyboundtonetworkinterface,
       "uxAlmSIPRegisterServernotresponding": uxAlmSIPRegisterServernotresponding,
       "uxAlmSIPRegisterServerbecameresponsive": uxAlmSIPRegisterServerbecameresponsive,
       "uxAlmRegistrationnotvalidreceivedstalefalse": uxAlmRegistrationnotvalidreceivedstalefalse,
       "uxAlmConfigchangeforSIPendpointthatreceivedstalefalse": uxAlmConfigchangeforSIPendpointthatreceivedstalefalse,
       "uxAlmDChanneldown": uxAlmDChanneldown,
       "uxAlmDChannelup": uxAlmDChannelup,
       "uxAlmCallreleasedduetochannelrestartbyfarend": uxAlmCallreleasedduetochannelrestartbyfarend,
       "uxAlmPortdisabledbyoperator": uxAlmPortdisabledbyoperator,
       "uxAlmPortenabledbyoperator": uxAlmPortenabledbyoperator,
       "uxAlmDS1LoopbackEnter": uxAlmDS1LoopbackEnter,
       "uxAlmDS1LoopbackExit": uxAlmDS1LoopbackExit,
       "uxAlmRedAlarmLossofSignal": uxAlmRedAlarmLossofSignal,
       "uxAlmRedAlarmLossofSignalcleared": uxAlmRedAlarmLossofSignalcleared,
       "uxAlmRedAlarmLossofFrame": uxAlmRedAlarmLossofFrame,
       "uxAlmRedAlarmLossofFramecleared": uxAlmRedAlarmLossofFramecleared,
       "uxAlmBlueAlarm": uxAlmBlueAlarm,
       "uxAlmBlueAlarmCleared": uxAlmBlueAlarmCleared,
       "uxAlmYellowAlarm": uxAlmYellowAlarm,
       "uxAlmYellowAlarmCleared": uxAlmYellowAlarmCleared,
       "uxAlmPortdisabledasportnotfoundonDS1": uxAlmPortdisabledasportnotfoundonDS1,
       "uxAlmClockrecoveryswitchedtoportconfiguredassecondary": uxAlmClockrecoveryswitchedtoportconfiguredassecondary,
       "uxAlmClockrecoveryswitchovertosecondaryportcleared": uxAlmClockrecoveryswitchovertosecondaryportcleared,
       "uxAlmClockrecoveryswitchedtofreerunclock": uxAlmClockrecoveryswitchedtofreerunclock,
       "uxAlmClockrecoveryswitchovertofreerunclockcleared": uxAlmClockrecoveryswitchovertofreerunclockcleared,
       "uxAlmLinecardnotdetected": uxAlmLinecardnotdetected,
       "uxAlmLinecarddetected": uxAlmLinecarddetected,
       "uxAlmPortdisabledforrelaypassthroughstateactivation": uxAlmPortdisabledforrelaypassthroughstateactivation,
       "uxAlmPortenabledforrelayonlinestateactivation": uxAlmPortenabledforrelayonlinestateactivation,
       "uxAlmLayer1down": uxAlmLayer1down,
       "uxAlmLayer1up": uxAlmLayer1up,
       "uxAlmPortdisabledasportnotfoundonanalogcard": uxAlmPortdisabledasportnotfoundonanalogcard,
       "uxAlmPortsdisabledforrelaypassthrustatechgonanalogrelaycards": uxAlmPortsdisabledforrelaypassthrustatechgonanalogrelaycards,
       "uxAlmPortsenabledforrelayonlinestatechangeonanalogrelaycardpairs": uxAlmPortsenabledforrelayonlinestatechangeonanalogrelaycardpairs,
       "uxAlmPortstatusdowndetected": uxAlmPortstatusdowndetected,
       "uxAlmPortstatusup": uxAlmPortstatusup,
       "uxAlmPortdisabledasportnotfoundonBRI": uxAlmPortdisabledasportnotfoundonBRI,
       "uxAlmSystemnotoperational": uxAlmSystemnotoperational,
       "uxAlmDSPnotcomingup": uxAlmDSPnotcomingup,
       "uxAlmDSPreset": uxAlmDSPreset,
       "uxAlmDSPCardisUP": uxAlmDSPCardisUP,
       "uxAlmDSPChannelFailure": uxAlmDSPChannelFailure,
       "uxAlmTLSOwnServerCertificatewillExpire": uxAlmTLSOwnServerCertificatewillExpire,
       "uxAlmTLSOwnServerCertificatehasExpired": uxAlmTLSOwnServerCertificatehasExpired,
       "uxAlmTLSOwnServerCertificateismissing": uxAlmTLSOwnServerCertificateismissing,
       "uxAlmTLSSelfSignCertificateGenerationFailed": uxAlmTLSSelfSignCertificateGenerationFailed,
       "uxAlmNewandValidTLSOwnServerCertificateDetected": uxAlmNewandValidTLSOwnServerCertificateDetected,
       "uxAlmInvalidSessionofaTLSconnection": uxAlmInvalidSessionofaTLSconnection,
       "uxAlmBMPTLSHandshakeAlertFailure": uxAlmBMPTLSHandshakeAlertFailure,
       "uxAlmBMPTLSHandshakeInactivityTimeoutFailure": uxAlmBMPTLSHandshakeInactivityTimeoutFailure,
       "uxAlmInterfaceoperdown": uxAlmInterfaceoperdown,
       "uxAlmInterfaceoperup": uxAlmInterfaceoperup,
       "uxAlmInterfaceadminup": uxAlmInterfaceadminup,
       "uxAlmInterfaceadmindown": uxAlmInterfaceadmindown,
       "uxAlmAdminPortoperdown": uxAlmAdminPortoperdown,
       "uxAlmAdminPortoperup": uxAlmAdminPortoperup,
       "uxAlmPortoperdown": uxAlmPortoperdown,
       "uxAlmRIPlicensenotenabled": uxAlmRIPlicensenotenabled,
       "uxAlmOSPFlicensenotenabled": uxAlmOSPFlicensenotenabled,
       "uxAlmLinkMonitorPeerDown": uxAlmLinkMonitorPeerDown,
       "uxAlmLinkMonitorPeerReady": uxAlmLinkMonitorPeerReady,
       "uxAlmTunnelconnectiondisabledbyoperator": uxAlmTunnelconnectiondisabledbyoperator,
       "uxAlmTunnelconnectionenabledbyoperator": uxAlmTunnelconnectionenabledbyoperator,
       "uxAlmTunnellinklost": uxAlmTunnellinklost,
       "uxAlmTunnellinkrestored": uxAlmTunnellinkrestored,
       "uxAlmIPseclicensenotenabled": uxAlmIPseclicensenotenabled,
       "uxAlmNegotiatedDuplexityHalf": uxAlmNegotiatedDuplexityHalf,
       "uxAlmNegotiatedDuplexityFull": uxAlmNegotiatedDuplexityFull,
       "uxAlmPreferredlinkdown": uxAlmPreferredlinkdown,
       "uxAlmPreferredlinkready": uxAlmPreferredlinkready,
       "uxAlmTunnelnotificationfailure": uxAlmTunnelnotificationfailure,
       "uxAlmTunnellocalsubnetsarenonnegotiable": uxAlmTunnellocalsubnetsarenonnegotiable,
       "uxAlmTunnelremotesubnetsarenonnegotiable": uxAlmTunnelremotesubnetsarenonnegotiable,
       "uxAlmApplicationServicerestarted": uxAlmApplicationServicerestarted,
       "uxAlmActivepartitionswitched": uxAlmActivepartitionswitched,
       "uxAlmFailedtomountpartition": uxAlmFailedtomountpartition,
       "uxAlmFailedtosetactivepartition": uxAlmFailedtosetactivepartition,
       "uxAlmAttempttorepairbootparametermismatchfailed": uxAlmAttempttorepairbootparametermismatchfailed,
       "uxAlmBootparametermismatchdetected": uxAlmBootparametermismatchdetected,
       "uxAlmFailedPoweronmemoryselftest": uxAlmFailedPoweronmemoryselftest,
       "uxAlmFailedPoweronCoreSwitchtest": uxAlmFailedPoweronCoreSwitchtest,
       "uxAlmFailedPoweronSecondarySwitchtest": uxAlmFailedPoweronSecondarySwitchtest,
       "uxAlmFailedPoweronexternalQuadPHYtest": uxAlmFailedPoweronexternalQuadPHYtest,
       "uxAlmFailedPoweronexternalSinglePHYtest": uxAlmFailedPoweronexternalSinglePHYtest,
       "uxAlmFailedPoweronCPUPHYtest": uxAlmFailedPoweronCPUPHYtest,
       "uxAlmFailedPoweronTSItest": uxAlmFailedPoweronTSItest,
       "uxAlmFailedPoweroninternal5PortPHYtest": uxAlmFailedPoweroninternal5PortPHYtest,
       "uxAlmSystemUpAfterPlannedRestart": uxAlmSystemUpAfterPlannedRestart,
       "uxAlmSystemUpAfterUnplannedRestart": uxAlmSystemUpAfterUnplannedRestart,
       "uxAlmNoresponse": uxAlmNoresponse,
       "uxAlmRemoteenddidnotbackoffinglare": uxAlmRemoteenddidnotbackoffinglare,
       "uxAlmWinkexpecteddidnotarrive": uxAlmWinkexpecteddidnotarrive,
       "uxAlmNodialtone": uxAlmNodialtone,
       "uxAlmCASsignalinggroupdisabled": uxAlmCASsignalinggroupdisabled,
       "uxAlmCASlicensenotenabled": uxAlmCASlicensenotenabled,
       "uxAlmCASlicenseenabled": uxAlmCASlicenseenabled,
       "uxAlmWinkReceived": uxAlmWinkReceived,
       "uxAlmDialToneReceived": uxAlmDialToneReceived,
       "uxAlmResponseReceived": uxAlmResponseReceived,
       "uxAlmInvalidcharactersincallingnumber": uxAlmInvalidcharactersincallingnumber,
       "uxAlmInvalidcharactersincallednumber": uxAlmInvalidcharactersincallednumber,
       "uxAlmCASsignalinggroupenabled": uxAlmCASsignalinggroupenabled,
       "uxAlmCASR2CDBiterror": uxAlmCASR2CDBiterror,
       "uxAlmCASR2CDBiterrorclear": uxAlmCASR2CDBiterrorclear,
       "uxAlmNetworkGlareoccured": uxAlmNetworkGlareoccured,
       "uxAlmConfigvalidationfailure": uxAlmConfigvalidationfailure}
)
