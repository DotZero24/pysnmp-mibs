# SNMP MIB module (AFFIRMED-SSF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsoft/AFFIRMED-SSF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:37 2025
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

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

affirmedSsf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 7)
)
if mibBuilder.loadTexts:
    affirmedSsf.setRevisions(
        ("2020-01-14 00:00",
         "2019-07-16 00:00",
         "2019-05-20 00:00",
         "2019-04-15 00:00",
         "2019-04-11 00:00",
         "2019-01-15 00:00",
         "2018-10-23 00:00",
         "2018-09-26 00:00",
         "2018-07-31 00:00",
         "2018-04-30 00:00",
         "2017-10-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AffirmedSsfTc_ObjectIdentity = ObjectIdentity
affirmedSsfTc = _AffirmedSsfTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 7, 1)
)
_AffirmedSsfObjects_ObjectIdentity = ObjectIdentity
affirmedSsfObjects = _AffirmedSsfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2)
)
_AffirmedSsfAlarmObjects_ObjectIdentity = ObjectIdentity
affirmedSsfAlarmObjects = _AffirmedSsfAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2, 1)
)
_AffirmedSsfAlarmSeqId_Type = Integer32
_AffirmedSsfAlarmSeqId_Object = MibScalar
affirmedSsfAlarmSeqId = _AffirmedSsfAlarmSeqId_Object(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2, 1, 1),
    _AffirmedSsfAlarmSeqId_Type()
)
affirmedSsfAlarmSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedSsfAlarmSeqId.setStatus("current")


class _AffirmedSsfAlarmDateTime_Type(OctetString):
    """Custom type affirmedSsfAlarmDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AffirmedSsfAlarmDateTime_Type.__name__ = "OctetString"
_AffirmedSsfAlarmDateTime_Object = MibScalar
affirmedSsfAlarmDateTime = _AffirmedSsfAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2, 1, 2),
    _AffirmedSsfAlarmDateTime_Type()
)
affirmedSsfAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedSsfAlarmDateTime.setStatus("current")


class _AffirmedSsfAlarmResource_Type(OctetString):
    """Custom type affirmedSsfAlarmResource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AffirmedSsfAlarmResource_Type.__name__ = "OctetString"
_AffirmedSsfAlarmResource_Object = MibScalar
affirmedSsfAlarmResource = _AffirmedSsfAlarmResource_Object(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2, 1, 3),
    _AffirmedSsfAlarmResource_Type()
)
affirmedSsfAlarmResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedSsfAlarmResource.setStatus("current")
_AffirmedSsfAlarmSeverity_Type = ItuPerceivedSeverity
_AffirmedSsfAlarmSeverity_Object = MibScalar
affirmedSsfAlarmSeverity = _AffirmedSsfAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2, 1, 4),
    _AffirmedSsfAlarmSeverity_Type()
)
affirmedSsfAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedSsfAlarmSeverity.setStatus("current")


class _AffirmedSsfAlarmDetails_Type(OctetString):
    """Custom type affirmedSsfAlarmDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AffirmedSsfAlarmDetails_Type.__name__ = "OctetString"
_AffirmedSsfAlarmDetails_Object = MibScalar
affirmedSsfAlarmDetails = _AffirmedSsfAlarmDetails_Object(
    (1, 3, 6, 1, 4, 1, 37963, 7, 2, 1, 5),
    _AffirmedSsfAlarmDetails_Type()
)
affirmedSsfAlarmDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedSsfAlarmDetails.setStatus("current")
_AffirmedSsfNotifications_ObjectIdentity = ObjectIdentity
affirmedSsfNotifications = _AffirmedSsfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3)
)
_AffirmedSsfTraps_ObjectIdentity = ObjectIdentity
affirmedSsfTraps = _AffirmedSsfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1)
)

# Managed Objects groups


# Notification objects

anSsfAlarmDnsServiceReachability = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 1)
)
anSsfAlarmDnsServiceReachability.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmDnsServiceReachability.setStatus(
        "current"
    )

anSsfAlarmGtpPathStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 2)
)
anSsfAlarmGtpPathStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmGtpPathStatus.setStatus(
        "current"
    )

anSsfAlarmLdapPeerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 3)
)
anSsfAlarmLdapPeerStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmLdapPeerStatus.setStatus(
        "current"
    )

anSsfAlarmNetworkKeepaliveStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 4)
)
anSsfAlarmNetworkKeepaliveStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmNetworkKeepaliveStatus.setStatus(
        "current"
    )

anSsfAlarmLdapDbStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 5)
)
anSsfAlarmLdapDbStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmLdapDbStatus.setStatus(
        "current"
    )

anSsfAlarmOperState = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 6)
)
anSsfAlarmOperState.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmOperState.setStatus(
        "current"
    )

anSsfAlarmRestPeerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 7)
)
anSsfAlarmRestPeerStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmRestPeerStatus.setStatus(
        "current"
    )

anSsfAlarmRestDbStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 8)
)
anSsfAlarmRestDbStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmRestDbStatus.setStatus(
        "current"
    )

anSsfAlarmPgwGxMapping = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 9)
)
anSsfAlarmPgwGxMapping.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmPgwGxMapping.setStatus(
        "current"
    )

anSsfAlarmDiameterPeerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 10)
)
anSsfAlarmDiameterPeerStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmDiameterPeerStatus.setStatus(
        "current"
    )

anSsfAlarmDiameterDbStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 11)
)
anSsfAlarmDiameterDbStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmDiameterDbStatus.setStatus(
        "current"
    )

anSsfAlarmDnsNameError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 12)
)
anSsfAlarmDnsNameError.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmDnsNameError.setStatus(
        "current"
    )

anSsfAlarmConfigSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 13)
)
anSsfAlarmConfigSync.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmConfigSync.setStatus(
        "current"
    )

anSsfAlarmLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 14)
)
anSsfAlarmLoginFailure.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmLoginFailure.setStatus(
        "current"
    )

anSsfAlarmFileSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 15)
)
anSsfAlarmFileSystem.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmFileSystem.setStatus(
        "current"
    )

anSsfAlarmCpu = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 16)
)
anSsfAlarmCpu.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmCpu.setStatus(
        "current"
    )

anSsfAlarmMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 17)
)
anSsfAlarmMemory.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmMemory.setStatus(
        "current"
    )

anSsfAlarmNetworkNextHopStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 18)
)
anSsfAlarmNetworkNextHopStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmNetworkNextHopStatus.setStatus(
        "current"
    )

anSsfAlarmNetworkStaticRouteStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 19)
)
anSsfAlarmNetworkStaticRouteStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmNetworkStaticRouteStatus.setStatus(
        "current"
    )

anSsfAlarmStatusSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 20)
)
anSsfAlarmStatusSync.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmStatusSync.setStatus(
        "current"
    )

anSsfAlarmGatewaySnmpStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 7, 3, 1, 21)
)
anSsfAlarmGatewaySnmpStatus.setObjects(
      *(("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeqId"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDateTime"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmResource"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmSeverity"),
        ("AFFIRMED-SSF-MIB", "affirmedSsfAlarmDetails"))
)
if mibBuilder.loadTexts:
    anSsfAlarmGatewaySnmpStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AFFIRMED-SSF-MIB",
    **{"affirmedSsf": affirmedSsf,
       "affirmedSsfTc": affirmedSsfTc,
       "affirmedSsfObjects": affirmedSsfObjects,
       "affirmedSsfAlarmObjects": affirmedSsfAlarmObjects,
       "affirmedSsfAlarmSeqId": affirmedSsfAlarmSeqId,
       "affirmedSsfAlarmDateTime": affirmedSsfAlarmDateTime,
       "affirmedSsfAlarmResource": affirmedSsfAlarmResource,
       "affirmedSsfAlarmSeverity": affirmedSsfAlarmSeverity,
       "affirmedSsfAlarmDetails": affirmedSsfAlarmDetails,
       "affirmedSsfNotifications": affirmedSsfNotifications,
       "affirmedSsfTraps": affirmedSsfTraps,
       "anSsfAlarmDnsServiceReachability": anSsfAlarmDnsServiceReachability,
       "anSsfAlarmGtpPathStatus": anSsfAlarmGtpPathStatus,
       "anSsfAlarmLdapPeerStatus": anSsfAlarmLdapPeerStatus,
       "anSsfAlarmNetworkKeepaliveStatus": anSsfAlarmNetworkKeepaliveStatus,
       "anSsfAlarmLdapDbStatus": anSsfAlarmLdapDbStatus,
       "anSsfAlarmOperState": anSsfAlarmOperState,
       "anSsfAlarmRestPeerStatus": anSsfAlarmRestPeerStatus,
       "anSsfAlarmRestDbStatus": anSsfAlarmRestDbStatus,
       "anSsfAlarmPgwGxMapping": anSsfAlarmPgwGxMapping,
       "anSsfAlarmDiameterPeerStatus": anSsfAlarmDiameterPeerStatus,
       "anSsfAlarmDiameterDbStatus": anSsfAlarmDiameterDbStatus,
       "anSsfAlarmDnsNameError": anSsfAlarmDnsNameError,
       "anSsfAlarmConfigSync": anSsfAlarmConfigSync,
       "anSsfAlarmLoginFailure": anSsfAlarmLoginFailure,
       "anSsfAlarmFileSystem": anSsfAlarmFileSystem,
       "anSsfAlarmCpu": anSsfAlarmCpu,
       "anSsfAlarmMemory": anSsfAlarmMemory,
       "anSsfAlarmNetworkNextHopStatus": anSsfAlarmNetworkNextHopStatus,
       "anSsfAlarmNetworkStaticRouteStatus": anSsfAlarmNetworkStaticRouteStatus,
       "anSsfAlarmStatusSync": anSsfAlarmStatusSync,
       "anSsfAlarmGatewaySnmpStatus": anSsfAlarmGatewaySnmpStatus}
)
