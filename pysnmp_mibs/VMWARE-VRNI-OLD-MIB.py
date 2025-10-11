# SNMP MIB module (VMWARE-VRNI-OLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vmware/VMWARE-VRNI-OLD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:17 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwNetworkInsight,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNetworkInsight")

(VmwLongSnmpAdminString,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwLongSnmpAdminString")


# MODULE-IDENTITY

vmwNetworkInsightMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1)
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIB.setRevisions(
        ("2017-09-05 00:00",
         "2017-06-01 00:00",
         "2017-02-20 00:00",
         "2016-10-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwVrniSeverity(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("info", 1),
          ("major", 2))
    )



# MIB Managed Objects in the order of their OIDs

_VmwVRNIEvents_ObjectIdentity = ObjectIdentity
vmwVRNIEvents = _VmwVRNIEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0)
)
if mibBuilder.loadTexts:
    vmwVRNIEvents.setStatus("obsolete")
_VmwVRNIData_ObjectIdentity = ObjectIdentity
vmwVRNIData = _VmwVRNIData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1)
)
if mibBuilder.loadTexts:
    vmwVRNIData.setStatus("obsolete")
_VmwAffectedObject_Type = SnmpAdminString
_VmwAffectedObject_Object = MibScalar
vmwAffectedObject = _VmwAffectedObject_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 102),
    _VmwAffectedObject_Type()
)
vmwAffectedObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAffectedObject.setStatus("obsolete")
_VmwEventSeverity_Type = VmwVrniSeverity
_VmwEventSeverity_Object = MibScalar
vmwEventSeverity = _VmwEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 103),
    _VmwEventSeverity_Type()
)
vmwEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEventSeverity.setStatus("obsolete")
_VmwVrniUrl_Type = SnmpAdminString
_VmwVrniUrl_Object = MibScalar
vmwVrniUrl = _VmwVrniUrl_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 104),
    _VmwVrniUrl_Type()
)
vmwVrniUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVrniUrl.setStatus("obsolete")
_VmwTimestamp_Type = DateAndTime
_VmwTimestamp_Object = MibScalar
vmwTimestamp = _VmwTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 105),
    _VmwTimestamp_Type()
)
vmwTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwTimestamp.setStatus("obsolete")
_VmwOperatorDesc_Type = VmwLongSnmpAdminString
_VmwOperatorDesc_Object = MibScalar
vmwOperatorDesc = _VmwOperatorDesc_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 106),
    _VmwOperatorDesc_Type()
)
vmwOperatorDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwOperatorDesc.setStatus("obsolete")
_VmwEventName_Type = VmwLongSnmpAdminString
_VmwEventName_Object = MibScalar
vmwEventName = _VmwEventName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 107),
    _VmwEventName_Type()
)
vmwEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEventName.setStatus("obsolete")
_VmwNetworkInsightMIBConformance_ObjectIdentity = ObjectIdentity
vmwNetworkInsightMIBConformance = _VmwNetworkInsightMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99)
)
_VmwNetworkInsightMIBCompliances_ObjectIdentity = ObjectIdentity
vmwNetworkInsightMIBCompliances = _VmwNetworkInsightMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1)
)
_VmwNetworkInsightMIBGroups_ObjectIdentity = ObjectIdentity
vmwNetworkInsightMIBGroups = _VmwNetworkInsightMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2)
)

# Managed Objects groups

vmwNetworkInsightNotificationInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 2)
)
vmwNetworkInsightNotificationInfoGroup1.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationInfoGroup1.setStatus("deprecated")

vmwNetworkInsightNotificationInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 20)
)
vmwNetworkInsightNotificationInfoGroup2.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationInfoGroup2.setStatus("obsolete")


# Notification objects

vmwSnmpTrapsAreConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 101)
)
vmwSnmpTrapsAreConfigured.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSnmpTrapsAreConfigured.setStatus(
        "obsolete"
    )

vmwSnmpTrapsAreDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 102)
)
vmwSnmpTrapsAreDisabled.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSnmpTrapsAreDisabled.setStatus(
        "obsolete"
    )

vmwTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 103)
)
vmwTestTrap.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwTestTrap.setStatus(
        "obsolete"
    )

vmwEntityDiscoveryChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20001)
)
vmwEntityDiscoveryChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEntityDiscoveryChangeEvent.setStatus(
        "obsolete"
    )

vmwEntityPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20002)
)
vmwEntityPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEntityPropertiesChangeEvent.setStatus(
        "obsolete"
    )

vmwFirewallNotInstalledOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20003)
)
vmwFirewallNotInstalledOnHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallNotInstalledOnHostEvent.setStatus(
        "obsolete"
    )

vmwHostWithStaleFirewallRulesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20004)
)
vmwHostWithStaleFirewallRulesEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostWithStaleFirewallRulesEvent.setStatus(
        "obsolete"
    )

vmwIpAddressChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20005)
)
vmwIpAddressChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIpAddressChangeEvent.setStatus(
        "obsolete"
    )

vmwL2GatewayAnomalyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20006)
)
vmwL2GatewayAnomalyEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2GatewayAnomalyEvent.setStatus(
        "obsolete"
    )

vmwL2NetworkAddressAnomalyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20007)
)
vmwL2NetworkAddressAnomalyEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkAddressAnomalyEvent.setStatus(
        "obsolete"
    )

vmwL2NetworkDiameterExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20008)
)
vmwL2NetworkDiameterExceededEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkDiameterExceededEvent.setStatus(
        "obsolete"
    )

vmwL2NetworkUplinkMissingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20009)
)
vmwL2NetworkUplinkMissingEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkUplinkMissingEvent.setStatus(
        "obsolete"
    )

vmwL2NetworkWithNoVMsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20010)
)
vmwL2NetworkWithNoVMsEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkWithNoVMsEvent.setStatus(
        "obsolete"
    )

vmwLayer2NetworkDiameterChangedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20011)
)
vmwLayer2NetworkDiameterChangedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLayer2NetworkDiameterChangedEvent.setStatus(
        "obsolete"
    )

vmwMTUMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20012)
)
vmwMTUMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwMTUMismatchEvent.setStatus(
        "obsolete"
    )

vmwNetworkIsolationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20013)
)
vmwNetworkIsolationEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNetworkIsolationEvent.setStatus(
        "obsolete"
    )

vmwNoPathEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20014)
)
vmwNoPathEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNoPathEvent.setStatus(
        "obsolete"
    )

vmwSpoofguardDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20015)
)
vmwSpoofguardDisabledEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSpoofguardDisabledEvent.setStatus(
        "obsolete"
    )

vmwVMotionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20018)
)
vmwVMotionEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMotionEvent.setStatus(
        "obsolete"
    )

vmwVMWithDisconnectedVnicsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20019)
)
vmwVMWithDisconnectedVnicsEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithDisconnectedVnicsEvent.setStatus(
        "obsolete"
    )

vmwVMWithMulipleVnicsOnDifferentVxlansEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20020)
)
vmwVMWithMulipleVnicsOnDifferentVxlansEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithMulipleVnicsOnDifferentVxlansEvent.setStatus(
        "obsolete"
    )

vmwVMWithMulipleVnicsOnSameL2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20021)
)
vmwVMWithMulipleVnicsOnSameL2Event.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithMulipleVnicsOnSameL2Event.setStatus(
        "obsolete"
    )

vmwVMWithNoIpAddressEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20022)
)
vmwVMWithNoIpAddressEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithNoIpAddressEvent.setStatus(
        "obsolete"
    )

vmwVTEPMissingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20023)
)
vmwVTEPMissingEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVTEPMissingEvent.setStatus(
        "obsolete"
    )

vmwL2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20024)
)
vmwL2Event.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2Event.setStatus(
        "obsolete"
    )

vmwMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20025)
)
vmwMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwSecurityGroupMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20026)
)
vmwSecurityGroupMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityGroupMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwFirewallRuleMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20027)
)
vmwFirewallRuleMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallRuleMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwVlanMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20028)
)
vmwVlanMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVlanMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwVxlanMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20029)
)
vmwVxlanMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVxlanMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwDeleteChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20030)
)
vmwDeleteChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDeleteChangeEvent.setStatus(
        "obsolete"
    )

vmwVtepFailedPingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20031)
)
vmwVtepFailedPingEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepFailedPingEvent.setStatus(
        "obsolete"
    )

vmwEmptySearchStreamChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20034)
)
vmwEmptySearchStreamChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEmptySearchStreamChangeEvent.setStatus(
        "obsolete"
    )

vmwSearchStreamMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20035)
)
vmwSearchStreamMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSearchStreamMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwEmptySearchStreamProblemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20036)
)
vmwEmptySearchStreamProblemEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEmptySearchStreamProblemEvent.setStatus(
        "obsolete"
    )

vmwSearchStreamMembershipProblemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20037)
)
vmwSearchStreamMembershipProblemEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSearchStreamMembershipProblemEvent.setStatus(
        "obsolete"
    )

vmwOspfConfigurationMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20038)
)
vmwOspfConfigurationMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwOspfConfigurationMismatchEvent.setStatus(
        "obsolete"
    )

vmwServiceVMNotHealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20039)
)
vmwServiceVMNotHealthyEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMNotHealthyEvent.setStatus(
        "obsolete"
    )

vmwServiceVMNotPoweredOnEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20040)
)
vmwServiceVMNotPoweredOnEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMNotPoweredOnEvent.setStatus(
        "obsolete"
    )

vmwServiceVMHighCPUUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20041)
)
vmwServiceVMHighCPUUsageEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMHighCPUUsageEvent.setStatus(
        "obsolete"
    )

vmwServiceVMHighMemoryUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20042)
)
vmwServiceVMHighMemoryUsageEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMHighMemoryUsageEvent.setStatus(
        "obsolete"
    )

vmwServiceVMHighDiskUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20043)
)
vmwServiceVMHighDiskUsageEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMHighDiskUsageEvent.setStatus(
        "obsolete"
    )

vmwIPSetPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20050)
)
vmwIPSetPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPSetPropertiesChangeEvent.setStatus(
        "obsolete"
    )

vmwFirewallRulePropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20051)
)
vmwFirewallRulePropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallRulePropertiesChangeEvent.setStatus(
        "obsolete"
    )

vmwSecurityGroupPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20052)
)
vmwSecurityGroupPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityGroupPropertiesChangeEvent.setStatus(
        "obsolete"
    )

vmwIPSetMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20053)
)
vmwIPSetMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPSetMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwFirewallRuleMaskEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20054)
)
vmwFirewallRuleMaskEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallRuleMaskEvent.setStatus(
        "obsolete"
    )

vmwSecurityMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20056)
)
vmwSecurityMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwSecurityTagPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20057)
)
vmwSecurityTagPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityTagPropertiesChangeEvent.setStatus(
        "obsolete"
    )

vmwSecurityTagMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20058)
)
vmwSecurityTagMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityTagMembershipChangeEvent.setStatus(
        "obsolete"
    )

vmwHostDatastoreChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20059)
)
vmwHostDatastoreChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostDatastoreChangeEvent.setStatus(
        "obsolete"
    )

vmwVMDatastoreChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20060)
)
vmwVMDatastoreChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMDatastoreChangeEvent.setStatus(
        "obsolete"
    )

vmwVMSnapshotChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20061)
)
vmwVMSnapshotChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMSnapshotChangeEvent.setStatus(
        "obsolete"
    )

vmwVMVirtualDiskChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20062)
)
vmwVMVirtualDiskChangeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMVirtualDiskChangeEvent.setStatus(
        "obsolete"
    )

vmwIPSetDefinitionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20063)
)
vmwIPSetDefinitionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPSetDefinitionMismatchEvent.setStatus(
        "obsolete"
    )

vmwSegmentMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20064)
)
vmwSegmentMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSegmentMismatchEvent.setStatus(
        "obsolete"
    )

vmwVtepEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20065)
)
vmwVtepEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepEvent.setStatus(
        "obsolete"
    )

vmwVtepConfigurationFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20066)
)
vmwVtepConfigurationFaultEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepConfigurationFaultEvent.setStatus(
        "obsolete"
    )

vmwDLRNetworksNotReachableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20067)
)
vmwDLRNetworksNotReachableEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDLRNetworksNotReachableEvent.setStatus(
        "obsolete"
    )

vmwVtepSubnetMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20068)
)
vmwVtepSubnetMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepSubnetMismatchEvent.setStatus(
        "obsolete"
    )

vmwVtepCountMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20069)
)
vmwVtepCountMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepCountMismatchEvent.setStatus(
        "obsolete"
    )

vmwEdgeNetworksNotReachableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20070)
)
vmwEdgeNetworksNotReachableEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeNetworksNotReachableEvent.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventCpuReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30001)
)
vmwThresholdExceededEventCpuReady.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventCpuReady.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventCpuCoStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30002)
)
vmwThresholdExceededEventCpuCoStop.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventCpuCoStop.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventDiskCommandAbortRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30003)
)
vmwThresholdExceededEventDiskCommandAbortRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDiskCommandAbortRule.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventIODeviceLatencyRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30004)
)
vmwThresholdExceededEventIODeviceLatencyRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventIODeviceLatencyRule.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventIOKernelLatencyRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30005)
)
vmwThresholdExceededEventIOKernelLatencyRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventIOKernelLatencyRule.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventMemorySwapInRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30006)
)
vmwThresholdExceededEventMemorySwapInRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventMemorySwapInRule.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventMemorySwapOutRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30007)
)
vmwThresholdExceededEventMemorySwapOutRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventMemorySwapOutRule.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventNetworkRxDropRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30008)
)
vmwThresholdExceededEventNetworkRxDropRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventNetworkRxDropRule.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventNetworkTxDropRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30009)
)
vmwThresholdExceededEventNetworkTxDropRule.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventNetworkTxDropRule.setStatus(
        "obsolete"
    )

vmwPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30100)
)
vmwPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPacketDropEvent.setStatus(
        "obsolete"
    )

vmwSwitchPortPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30101)
)
vmwSwitchPortPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSwitchPortPacketDropEvent.setStatus(
        "obsolete"
    )

vmwRouterInterfacePacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30102)
)
vmwRouterInterfacePacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwRouterInterfacePacketDropEvent.setStatus(
        "obsolete"
    )

vmwVnicPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30103)
)
vmwVnicPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVnicPacketDropEvent.setStatus(
        "obsolete"
    )

vmwVTEPUnderlayPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30104)
)
vmwVTEPUnderlayPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVTEPUnderlayPacketDropEvent.setStatus(
        "obsolete"
    )

vmwPnicUnderlyingSwitchPortPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30105)
)
vmwPnicUnderlyingSwitchPortPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPnicUnderlyingSwitchPortPacketDropEvent.setStatus(
        "obsolete"
    )

vmwDevicePacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30106)
)
vmwDevicePacketDropEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDevicePacketDropEvent.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventDatastoreFreeSpaceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30203)
)
vmwThresholdExceededEventDatastoreFreeSpaceWarning.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreFreeSpaceWarning.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventDatastoreFreeSpaceCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30204)
)
vmwThresholdExceededEventDatastoreFreeSpaceCritical.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreFreeSpaceCritical.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventDatastoreReadLatency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30205)
)
vmwThresholdExceededEventDatastoreReadLatency.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreReadLatency.setStatus(
        "obsolete"
    )

vmwThresholdExceededEventDatastoreWriteLatency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30206)
)
vmwThresholdExceededEventDatastoreWriteLatency.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreWriteLatency.setStatus(
        "obsolete"
    )

vmwDistributedFirewallApplyHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35001)
)
vmwDistributedFirewallApplyHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDistributedFirewallApplyHostEvent.setStatus(
        "obsolete"
    )

vmwDistributedFirewallApplyVMEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35002)
)
vmwDistributedFirewallApplyVMEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDistributedFirewallApplyVMEvent.setStatus(
        "obsolete"
    )

vmwNsxEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35003)
)
vmwNsxEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxEvent.setStatus(
        "obsolete"
    )

vmwFeatureImpactedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35004)
)
vmwFeatureImpactedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFeatureImpactedEvent.setStatus(
        "obsolete"
    )

vmwNSXComponentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35221)
)
vmwNSXComponentEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXComponentEvent.setStatus(
        "obsolete"
    )

vmwNSXBackupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35222)
)
vmwNSXBackupEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupEvent.setStatus(
        "obsolete"
    )

vmwNSXBackupAuditLogExcludedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35223)
)
vmwNSXBackupAuditLogExcludedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupAuditLogExcludedEvent.setStatus(
        "obsolete"
    )

vmwNSXUnsecureBackupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35224)
)
vmwNSXUnsecureBackupEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXUnsecureBackupEvent.setStatus(
        "obsolete"
    )

vmwNSXBackupSystemEventsExcludedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35225)
)
vmwNSXBackupSystemEventsExcludedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupSystemEventsExcludedEvent.setStatus(
        "obsolete"
    )

vmwNSXBackupNotScheduledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35226)
)
vmwNSXBackupNotScheduledEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupNotScheduledEvent.setStatus(
        "obsolete"
    )

vmwNSXBackupNotRecordedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35227)
)
vmwNSXBackupNotRecordedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupNotRecordedEvent.setStatus(
        "obsolete"
    )

vmwNSXNtpServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35228)
)
vmwNSXNtpServerEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXNtpServerEvent.setStatus(
        "obsolete"
    )

vmwNSXSysLogServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35229)
)
vmwNSXSysLogServerEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXSysLogServerEvent.setStatus(
        "obsolete"
    )

vmwControllerSysLogServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35230)
)
vmwControllerSysLogServerEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwControllerSysLogServerEvent.setStatus(
        "obsolete"
    )

vmwNSXIpV6EnabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35231)
)
vmwNSXIpV6EnabledEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXIpV6EnabledEvent.setStatus(
        "obsolete"
    )

vmwNSXOspfNeighborDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35232)
)
vmwNSXOspfNeighborDownEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXOspfNeighborDownEvent.setStatus(
        "obsolete"
    )

vmwClusterFeatureVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36022)
)
vmwClusterFeatureVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwClusterFeatureVersionMismatchEvent.setStatus(
        "obsolete"
    )

vmwHostFeatureVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36023)
)
vmwHostFeatureVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostFeatureVersionMismatchEvent.setStatus(
        "obsolete"
    )

vmwFeatureVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36024)
)
vmwFeatureVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFeatureVersionMismatchEvent.setStatus(
        "obsolete"
    )

vmwHostFeatureEnabledMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36025)
)
vmwHostFeatureEnabledMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostFeatureEnabledMismatchEvent.setStatus(
        "obsolete"
    )

vmwHostFeatureInstalledMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36026)
)
vmwHostFeatureInstalledMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostFeatureInstalledMismatchEvent.setStatus(
        "obsolete"
    )

vmwHostVtepNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36027)
)
vmwHostVtepNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostVtepNotFoundEvent.setStatus(
        "obsolete"
    )

vmwHostVtepDisconnectedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36028)
)
vmwHostVtepDisconnectedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostVtepDisconnectedEvent.setStatus(
        "obsolete"
    )

vmwHostVtepEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36029)
)
vmwHostVtepEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostVtepEvent.setStatus(
        "obsolete"
    )

vmwClusterHostsVtepMTUMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36030)
)
vmwClusterHostsVtepMTUMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwClusterHostsVtepMTUMismatchEvent.setStatus(
        "obsolete"
    )

vmwFeatureUnhealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36031)
)
vmwFeatureUnhealthyEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFeatureUnhealthyEvent.setStatus(
        "obsolete"
    )

vmwEdgeHANotConfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36032)
)
vmwEdgeHANotConfiguredEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeHANotConfiguredEvent.setStatus(
        "obsolete"
    )

vmwEdgeInterfacesDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36033)
)
vmwEdgeInterfacesDownEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeInterfacesDownEvent.setStatus(
        "obsolete"
    )

vmwModuleUnhealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36041)
)
vmwModuleUnhealthyEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwModuleUnhealthyEvent.setStatus(
        "obsolete"
    )

vmwModuleNotLoadedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36042)
)
vmwModuleNotLoadedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwModuleNotLoadedEvent.setStatus(
        "obsolete"
    )

vmwModuleNetworkConnectionFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36043)
)
vmwModuleNetworkConnectionFailureEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwModuleNetworkConnectionFailureEvent.setStatus(
        "obsolete"
    )

vmwHostNetworkControlPlaneMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36044)
)
vmwHostNetworkControlPlaneMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNetworkControlPlaneMismatchEvent.setStatus(
        "obsolete"
    )

vmwHostNetworkControlPlaneConnectionFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36045)
)
vmwHostNetworkControlPlaneConnectionFailureEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNetworkControlPlaneConnectionFailureEvent.setStatus(
        "obsolete"
    )

vmwHostNetworkControlPlaneNotSyncedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36046)
)
vmwHostNetworkControlPlaneNotSyncedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNetworkControlPlaneNotSyncedEvent.setStatus(
        "obsolete"
    )

vmwNSXControllerClusterMajorityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36047)
)
vmwNSXControllerClusterMajorityEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerClusterMajorityEvent.setStatus(
        "obsolete"
    )

vmwNSXControllersVMOnSameHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36048)
)
vmwNSXControllersVMOnSameHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllersVMOnSameHostEvent.setStatus(
        "obsolete"
    )

vmwVxLanRangeExhaustEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36049)
)
vmwVxLanRangeExhaustEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVxLanRangeExhaustEvent.setStatus(
        "obsolete"
    )

vmwNSXFirewallDefaultAllowAllRulesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36050)
)
vmwNSXFirewallDefaultAllowAllRulesEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXFirewallDefaultAllowAllRulesEvent.setStatus(
        "obsolete"
    )

vmwLogicalRouterNoUplinkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36051)
)
vmwLogicalRouterNoUplinkEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLogicalRouterNoUplinkEvent.setStatus(
        "obsolete"
    )

vmwEdgeNotHAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36052)
)
vmwEdgeNotHAEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeNotHAEvent.setStatus(
        "obsolete"
    )

vmwEdgeNotDeployedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36053)
)
vmwEdgeNotDeployedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeNotDeployedEvent.setStatus(
        "obsolete"
    )

vmwEcmpIsEnabledAndStatefulServicesAreUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36054)
)
vmwEcmpIsEnabledAndStatefulServicesAreUpEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEcmpIsEnabledAndStatefulServicesAreUpEvent.setStatus(
        "obsolete"
    )

vmwLogicalRouterDeployedOnEcmpEdgeHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36055)
)
vmwLogicalRouterDeployedOnEcmpEdgeHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLogicalRouterDeployedOnEcmpEdgeHostEvent.setStatus(
        "obsolete"
    )

vmwEdgeMissingInterfaceOSPFAreaMappingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36056)
)
vmwEdgeMissingInterfaceOSPFAreaMappingEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeMissingInterfaceOSPFAreaMappingEvent.setStatus(
        "obsolete"
    )

vmwOspfInsecureAuthRouterEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36057)
)
vmwOspfInsecureAuthRouterEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwOspfInsecureAuthRouterEvent.setStatus(
        "obsolete"
    )

vmwNSXControllersDeployedCountEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36058)
)
vmwNSXControllersDeployedCountEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllersDeployedCountEvent.setStatus(
        "obsolete"
    )

vmwNSXControllerNotActiveCountEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36059)
)
vmwNSXControllerNotActiveCountEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerNotActiveCountEvent.setStatus(
        "obsolete"
    )

vmwNSXControllerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36060)
)
vmwNSXControllerEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerEvent.setStatus(
        "obsolete"
    )

vmwNSXEcmpEdgeDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36061)
)
vmwNSXEcmpEdgeDownEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEcmpEdgeDownEvent.setStatus(
        "obsolete"
    )

vmwNSXMajorityEcmpEdgesDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36062)
)
vmwNSXMajorityEcmpEdgesDownEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXMajorityEcmpEdgesDownEvent.setStatus(
        "obsolete"
    )

vmwNSXAllEcmpEdgesDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36063)
)
vmwNSXAllEcmpEdgesDownEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXAllEcmpEdgesDownEvent.setStatus(
        "obsolete"
    )

vmwNSXEdgeMtuMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36064)
)
vmwNSXEdgeMtuMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeMtuMismatchEvent.setStatus(
        "obsolete"
    )

vmwNSXEdgeSplitBrainEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36065)
)
vmwNSXEdgeSplitBrainEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeSplitBrainEvent.setStatus(
        "obsolete"
    )

vmwCriticalHostNotAccessibleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 40001)
)
vmwCriticalHostNotAccessibleEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCriticalHostNotAccessibleEvent.setStatus(
        "obsolete"
    )

vmwGenericNSXSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70000)
)
vmwGenericNSXSystemEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwGenericNSXSystemEvent.setStatus(
        "obsolete"
    )

vmwFilterConfigApplyOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70001)
)
vmwFilterConfigApplyOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFilterConfigApplyOnHostFailedEvent.setStatus(
        "obsolete"
    )

vmwRulesetLoadOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70002)
)
vmwRulesetLoadOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwRulesetLoadOnHostFailedEvent.setStatus(
        "obsolete"
    )

vmwConfigUpdateOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70003)
)
vmwConfigUpdateOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwConfigUpdateOnHostFailedEvent.setStatus(
        "obsolete"
    )

vmwSpoofguardConfigUpdateOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70004)
)
vmwSpoofguardConfigUpdateOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSpoofguardConfigUpdateOnHostFailedEvent.setStatus(
        "obsolete"
    )

vmwApplyRuleToVnicFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70005)
)
vmwApplyRuleToVnicFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwApplyRuleToVnicFailedEvent.setStatus(
        "obsolete"
    )

vmwContainerConfigUpdateOnVnicFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70006)
)
vmwContainerConfigUpdateOnVnicFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwContainerConfigUpdateOnVnicFailedEvent.setStatus(
        "obsolete"
    )

vmwSpoofguardApplyToVnicFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70007)
)
vmwSpoofguardApplyToVnicFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSpoofguardApplyToVnicFailedEvent.setStatus(
        "obsolete"
    )

vmwHostMessagingConfigurationFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70008)
)
vmwHostMessagingConfigurationFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingConfigurationFailedEvent.setStatus(
        "obsolete"
    )

vmwHostMessagingConnectionReconfigurationFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70009)
)
vmwHostMessagingConnectionReconfigurationFailedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingConnectionReconfigurationFailedEvent.setStatus(
        "obsolete"
    )

vmwHostMessagingConfigurationFailedNotificationSkippedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70010)
)
vmwHostMessagingConfigurationFailedNotificationSkippedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingConfigurationFailedNotificationSkippedEvent.setStatus(
        "obsolete"
    )

vmwHostMessagingInfrastructureDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70011)
)
vmwHostMessagingInfrastructureDownEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingInfrastructureDownEvent.setStatus(
        "obsolete"
    )

vmwEdgeVMNotRespondingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70012)
)
vmwEdgeVMNotRespondingEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeVMNotRespondingEvent.setStatus(
        "obsolete"
    )

vmwEdgeUnhealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70013)
)
vmwEdgeUnhealthyEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeUnhealthyEvent.setStatus(
        "obsolete"
    )

vmwEdgeVMCommunicationFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70014)
)
vmwEdgeVMCommunicationFailureEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeVMCommunicationFailureEvent.setStatus(
        "obsolete"
    )

vmwNSXEdgeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70015)
)
vmwNSXEdgeEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeEvent.setStatus(
        "obsolete"
    )

vmwOtherCriticalNSXEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 71000)
)
vmwOtherCriticalNSXEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwOtherCriticalNSXEvent.setStatus(
        "obsolete"
    )

vmwPanEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80000)
)
vmwPanEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanEvent.setStatus(
        "obsolete"
    )

vmwPanNsxNotInRegisteredStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80001)
)
vmwPanNsxNotInRegisteredStateEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxNotInRegisteredStateEvent.setStatus(
        "obsolete"
    )

vmwPanNsxDynamicUpdateDelayedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80002)
)
vmwPanNsxDynamicUpdateDelayedEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxDynamicUpdateDelayedEvent.setStatus(
        "obsolete"
    )

vmwPanDeviceInDisconnectedStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80003)
)
vmwPanDeviceInDisconnectedStateEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanDeviceInDisconnectedStateEvent.setStatus(
        "obsolete"
    )

vmwPanNsxServiceApplianceViewMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80004)
)
vmwPanNsxServiceApplianceViewMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxServiceApplianceViewMismatchEvent.setStatus(
        "obsolete"
    )

vmwPanNsxFabricAgentNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80005)
)
vmwPanNsxFabricAgentNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxFabricAgentNotFoundOnHostEvent.setStatus(
        "obsolete"
    )

vmwPanNsxServiceVMNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80006)
)
vmwPanNsxServiceVMNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxServiceVMNotFoundOnHostEvent.setStatus(
        "obsolete"
    )

vmwCheckpointEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80100)
)
vmwCheckpointEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointEvent.setStatus(
        "obsolete"
    )

vmwCheckpointNsxFabricAgentNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80102)
)
vmwCheckpointNsxFabricAgentNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointNsxFabricAgentNotFoundOnHostEvent.setStatus(
        "obsolete"
    )

vmwCheckpointNsxServiceVMNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80103)
)
vmwCheckpointNsxServiceVMNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointNsxServiceVMNotFoundOnHostEvent.setStatus(
        "obsolete"
    )

vmwCheckpointGatewaySicStatusNotCommunicatingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80104)
)
vmwCheckpointGatewaySicStatusNotCommunicatingEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointGatewaySicStatusNotCommunicatingEvent.setStatus(
        "obsolete"
    )

vmwCheckpointNsxServiceApplianceViewMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80105)
)
vmwCheckpointNsxServiceApplianceViewMismatchEvent.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointNsxServiceApplianceViewMismatchEvent.setStatus(
        "obsolete"
    )


# Notifications groups

vmwNetworkInsightNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 3)
)
vmwNetworkInsightNotificationGroup1.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwSnmpTrapsAreConfigured"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSnmpTrapsAreDisabled"),
        ("VMWARE-VRNI-OLD-MIB", "vmwTestTrap"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEntityDiscoveryChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEntityPropertiesChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFirewallNotInstalledOnHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostWithStaleFirewallRulesEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwIpAddressChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwL2GatewayAnomalyEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwL2NetworkAddressAnomalyEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwL2NetworkDiameterExceededEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwL2NetworkUplinkMissingEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwL2NetworkWithNoVMsEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwLayer2NetworkDiameterChangedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwMTUMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkIsolationEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNoPathEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSpoofguardDisabledEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMotionEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMWithDisconnectedVnicsEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMWithMulipleVnicsOnDifferentVxlansEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMWithMulipleVnicsOnSameL2Event"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMWithNoIpAddressEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVTEPMissingEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwL2Event"),
        ("VMWARE-VRNI-OLD-MIB", "vmwMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityGroupMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFirewallRuleMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVlanMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVxlanMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwDeleteChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVtepFailedPingEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEmptySearchStreamChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSearchStreamMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEmptySearchStreamProblemEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSearchStreamMembershipProblemEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOspfConfigurationMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwServiceVMNotHealthyEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwServiceVMNotPoweredOnEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwServiceVMHighCPUUsageEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwServiceVMHighMemoryUsageEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwServiceVMHighDiskUsageEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwIPSetPropertiesChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFirewallRulePropertiesChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityGroupPropertiesChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwIPSetMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFirewallRuleMaskEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityTagPropertiesChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityTagMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostDatastoreChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMDatastoreChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMSnapshotChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMVirtualDiskChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwIPSetDefinitionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSegmentMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVtepEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVtepConfigurationFaultEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVtepSubnetMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVtepCountMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwDLRNetworksNotReachableEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeNetworksNotReachableEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventCpuReady"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventCpuCoStop"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventDiskCommandAbortRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventIODeviceLatencyRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventIOKernelLatencyRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventMemorySwapInRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventMemorySwapOutRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventNetworkRxDropRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventNetworkTxDropRule"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwRouterInterfacePacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVnicPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVTEPUnderlayPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPnicUnderlyingSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwDevicePacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventDatastoreFreeSpaceWarning"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventDatastoreFreeSpaceCritical"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventDatastoreReadLatency"),
        ("VMWARE-VRNI-OLD-MIB", "vmwThresholdExceededEventDatastoreWriteLatency"),
        ("VMWARE-VRNI-OLD-MIB", "vmwDistributedFirewallApplyHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwDistributedFirewallApplyVMEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNsxEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFeatureImpactedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwClusterFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostFeatureEnabledMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostFeatureInstalledMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostVtepNotFoundEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostVtepDisconnectedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostVtepEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwClusterHostsVtepMTUMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFeatureUnhealthyEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeHANotConfiguredEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeInterfacesDownEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwModuleUnhealthyEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwModuleNotLoadedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwModuleNetworkConnectionFailureEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostNetworkControlPlaneMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostNetworkControlPlaneConnectionFailureEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostNetworkControlPlaneNotSyncedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXControllerClusterMajorityEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXControllersVMOnSameHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVxLanRangeExhaustEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXFirewallDefaultAllowAllRulesEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeNotHAEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeNotDeployedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEcmpIsEnabledAndStatefulServicesAreUpEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwLogicalRouterDeployedOnEcmpEdgeHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeMissingInterfaceOSPFAreaMappingEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOspfInsecureAuthRouterEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXControllersDeployedCountEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXControllerNotActiveCountEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXControllerEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXUnsecureBackupEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupSystemEventsExcludedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupNotScheduledEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupNotRecordedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXNtpServerEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXSysLogServerEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwControllerSysLogServerEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwGenericNSXSystemEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwOtherCriticalNSXEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFilterConfigApplyOnHostFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwRulesetLoadOnHostFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwConfigUpdateOnHostFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSpoofguardConfigUpdateOnHostFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwApplyRuleToVnicFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwContainerConfigUpdateOnVnicFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSpoofguardApplyToVnicFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostMessagingConfigurationFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostMessagingConnectionReconfigurationFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostMessagingConfigurationFailedNotificationSkippedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostMessagingInfrastructureDownEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeVMNotRespondingEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeUnhealthyEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwEdgeVMCommunicationFailureEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXEdgeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanNsxNotInRegisteredStateEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanNsxDynamicUpdateDelayedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanDeviceInDisconnectedStateEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanNsxServiceApplianceViewMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanNsxFabricAgentNotFoundOnHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPanNsxServiceVMNotFoundOnHostEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup1.setStatus(
        "obsolete"
    )

vmwNetworkInsightNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 30)
)
vmwNetworkInsightNotificationGroup2.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwLogicalRouterNoUplinkEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXComponentEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupAuditLogExcludedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXUnsecureBackupEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupSystemEventsExcludedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupNotScheduledEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXBackupNotRecordedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXNtpServerEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXSysLogServerEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwControllerSysLogServerEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup2.setStatus(
        "obsolete"
    )

vmwNetworkInsightNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 40)
)
vmwNetworkInsightNotificationGroup3.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwMTUMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVMWithMulipleVnicsOnSameL2Event"),
        ("VMWARE-VRNI-OLD-MIB", "vmwMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityGroupMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwFirewallRuleMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVlanMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVxlanMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSearchStreamMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwIPSetMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSecurityMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVtepEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwRouterInterfacePacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVnicPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVTEPUnderlayPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwPnicUnderlyingSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwSpoofguardConfigUpdateOnHostFailedEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXEcmpEdgeDownEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXMajorityEcmpEdgesDownEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXAllEcmpEdgesDownEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup3.setStatus(
        "obsolete"
    )

vmwNetworkInsightNotificationGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 50)
)
vmwNetworkInsightNotificationGroup4.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwNSXEdgeSplitBrainEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXIpV6EnabledEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXOspfNeighborDownEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwCheckpointEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNSXEdgeMtuMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwCheckpointNsxFabricAgentNotFoundOnHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwCheckpointNsxServiceVMNotFoundOnHostEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwCheckpointGatewaySicStatusNotCommunicatingEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwCheckpointNsxServiceApplianceViewMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwCriticalHostNotAccessibleEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwVlanMembershipChangeEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwClusterFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwHostFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-OLD-MIB", "vmwConfigUpdateOnHostFailedEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup4.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

vmwNetworkInsightMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 3)
)
vmwNetworkInsightMIBBasicCompliance.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationInfoGroup1"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup1"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 30)
)
vmwNetworkInsightMIBBasicCompliance2.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationInfoGroup2"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup2"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance2.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 35)
)
vmwNetworkInsightMIBBasicCompliance3.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationInfoGroup2"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup3"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance3.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 45)
)
vmwNetworkInsightMIBBasicCompliance4.setObjects(
      *(("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationInfoGroup2"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-OLD-MIB", "vmwNetworkInsightNotificationGroup4"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance4.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VRNI-OLD-MIB",
    **{"VmwVrniSeverity": VmwVrniSeverity,
       "vmwNetworkInsightMIB": vmwNetworkInsightMIB,
       "vmwVRNIEvents": vmwVRNIEvents,
       "vmwSnmpTrapsAreConfigured": vmwSnmpTrapsAreConfigured,
       "vmwSnmpTrapsAreDisabled": vmwSnmpTrapsAreDisabled,
       "vmwTestTrap": vmwTestTrap,
       "vmwEntityDiscoveryChangeEvent": vmwEntityDiscoveryChangeEvent,
       "vmwEntityPropertiesChangeEvent": vmwEntityPropertiesChangeEvent,
       "vmwFirewallNotInstalledOnHostEvent": vmwFirewallNotInstalledOnHostEvent,
       "vmwHostWithStaleFirewallRulesEvent": vmwHostWithStaleFirewallRulesEvent,
       "vmwIpAddressChangeEvent": vmwIpAddressChangeEvent,
       "vmwL2GatewayAnomalyEvent": vmwL2GatewayAnomalyEvent,
       "vmwL2NetworkAddressAnomalyEvent": vmwL2NetworkAddressAnomalyEvent,
       "vmwL2NetworkDiameterExceededEvent": vmwL2NetworkDiameterExceededEvent,
       "vmwL2NetworkUplinkMissingEvent": vmwL2NetworkUplinkMissingEvent,
       "vmwL2NetworkWithNoVMsEvent": vmwL2NetworkWithNoVMsEvent,
       "vmwLayer2NetworkDiameterChangedEvent": vmwLayer2NetworkDiameterChangedEvent,
       "vmwMTUMismatchEvent": vmwMTUMismatchEvent,
       "vmwNetworkIsolationEvent": vmwNetworkIsolationEvent,
       "vmwNoPathEvent": vmwNoPathEvent,
       "vmwSpoofguardDisabledEvent": vmwSpoofguardDisabledEvent,
       "vmwVMotionEvent": vmwVMotionEvent,
       "vmwVMWithDisconnectedVnicsEvent": vmwVMWithDisconnectedVnicsEvent,
       "vmwVMWithMulipleVnicsOnDifferentVxlansEvent": vmwVMWithMulipleVnicsOnDifferentVxlansEvent,
       "vmwVMWithMulipleVnicsOnSameL2Event": vmwVMWithMulipleVnicsOnSameL2Event,
       "vmwVMWithNoIpAddressEvent": vmwVMWithNoIpAddressEvent,
       "vmwVTEPMissingEvent": vmwVTEPMissingEvent,
       "vmwL2Event": vmwL2Event,
       "vmwMembershipChangeEvent": vmwMembershipChangeEvent,
       "vmwSecurityGroupMembershipChangeEvent": vmwSecurityGroupMembershipChangeEvent,
       "vmwFirewallRuleMembershipChangeEvent": vmwFirewallRuleMembershipChangeEvent,
       "vmwVlanMembershipChangeEvent": vmwVlanMembershipChangeEvent,
       "vmwVxlanMembershipChangeEvent": vmwVxlanMembershipChangeEvent,
       "vmwDeleteChangeEvent": vmwDeleteChangeEvent,
       "vmwVtepFailedPingEvent": vmwVtepFailedPingEvent,
       "vmwEmptySearchStreamChangeEvent": vmwEmptySearchStreamChangeEvent,
       "vmwSearchStreamMembershipChangeEvent": vmwSearchStreamMembershipChangeEvent,
       "vmwEmptySearchStreamProblemEvent": vmwEmptySearchStreamProblemEvent,
       "vmwSearchStreamMembershipProblemEvent": vmwSearchStreamMembershipProblemEvent,
       "vmwOspfConfigurationMismatchEvent": vmwOspfConfigurationMismatchEvent,
       "vmwServiceVMNotHealthyEvent": vmwServiceVMNotHealthyEvent,
       "vmwServiceVMNotPoweredOnEvent": vmwServiceVMNotPoweredOnEvent,
       "vmwServiceVMHighCPUUsageEvent": vmwServiceVMHighCPUUsageEvent,
       "vmwServiceVMHighMemoryUsageEvent": vmwServiceVMHighMemoryUsageEvent,
       "vmwServiceVMHighDiskUsageEvent": vmwServiceVMHighDiskUsageEvent,
       "vmwIPSetPropertiesChangeEvent": vmwIPSetPropertiesChangeEvent,
       "vmwFirewallRulePropertiesChangeEvent": vmwFirewallRulePropertiesChangeEvent,
       "vmwSecurityGroupPropertiesChangeEvent": vmwSecurityGroupPropertiesChangeEvent,
       "vmwIPSetMembershipChangeEvent": vmwIPSetMembershipChangeEvent,
       "vmwFirewallRuleMaskEvent": vmwFirewallRuleMaskEvent,
       "vmwSecurityMembershipChangeEvent": vmwSecurityMembershipChangeEvent,
       "vmwSecurityTagPropertiesChangeEvent": vmwSecurityTagPropertiesChangeEvent,
       "vmwSecurityTagMembershipChangeEvent": vmwSecurityTagMembershipChangeEvent,
       "vmwHostDatastoreChangeEvent": vmwHostDatastoreChangeEvent,
       "vmwVMDatastoreChangeEvent": vmwVMDatastoreChangeEvent,
       "vmwVMSnapshotChangeEvent": vmwVMSnapshotChangeEvent,
       "vmwVMVirtualDiskChangeEvent": vmwVMVirtualDiskChangeEvent,
       "vmwIPSetDefinitionMismatchEvent": vmwIPSetDefinitionMismatchEvent,
       "vmwSegmentMismatchEvent": vmwSegmentMismatchEvent,
       "vmwVtepEvent": vmwVtepEvent,
       "vmwVtepConfigurationFaultEvent": vmwVtepConfigurationFaultEvent,
       "vmwDLRNetworksNotReachableEvent": vmwDLRNetworksNotReachableEvent,
       "vmwVtepSubnetMismatchEvent": vmwVtepSubnetMismatchEvent,
       "vmwVtepCountMismatchEvent": vmwVtepCountMismatchEvent,
       "vmwEdgeNetworksNotReachableEvent": vmwEdgeNetworksNotReachableEvent,
       "vmwThresholdExceededEventCpuReady": vmwThresholdExceededEventCpuReady,
       "vmwThresholdExceededEventCpuCoStop": vmwThresholdExceededEventCpuCoStop,
       "vmwThresholdExceededEventDiskCommandAbortRule": vmwThresholdExceededEventDiskCommandAbortRule,
       "vmwThresholdExceededEventIODeviceLatencyRule": vmwThresholdExceededEventIODeviceLatencyRule,
       "vmwThresholdExceededEventIOKernelLatencyRule": vmwThresholdExceededEventIOKernelLatencyRule,
       "vmwThresholdExceededEventMemorySwapInRule": vmwThresholdExceededEventMemorySwapInRule,
       "vmwThresholdExceededEventMemorySwapOutRule": vmwThresholdExceededEventMemorySwapOutRule,
       "vmwThresholdExceededEventNetworkRxDropRule": vmwThresholdExceededEventNetworkRxDropRule,
       "vmwThresholdExceededEventNetworkTxDropRule": vmwThresholdExceededEventNetworkTxDropRule,
       "vmwPacketDropEvent": vmwPacketDropEvent,
       "vmwSwitchPortPacketDropEvent": vmwSwitchPortPacketDropEvent,
       "vmwRouterInterfacePacketDropEvent": vmwRouterInterfacePacketDropEvent,
       "vmwVnicPacketDropEvent": vmwVnicPacketDropEvent,
       "vmwVTEPUnderlayPacketDropEvent": vmwVTEPUnderlayPacketDropEvent,
       "vmwPnicUnderlyingSwitchPortPacketDropEvent": vmwPnicUnderlyingSwitchPortPacketDropEvent,
       "vmwDevicePacketDropEvent": vmwDevicePacketDropEvent,
       "vmwThresholdExceededEventDatastoreFreeSpaceWarning": vmwThresholdExceededEventDatastoreFreeSpaceWarning,
       "vmwThresholdExceededEventDatastoreFreeSpaceCritical": vmwThresholdExceededEventDatastoreFreeSpaceCritical,
       "vmwThresholdExceededEventDatastoreReadLatency": vmwThresholdExceededEventDatastoreReadLatency,
       "vmwThresholdExceededEventDatastoreWriteLatency": vmwThresholdExceededEventDatastoreWriteLatency,
       "vmwDistributedFirewallApplyHostEvent": vmwDistributedFirewallApplyHostEvent,
       "vmwDistributedFirewallApplyVMEvent": vmwDistributedFirewallApplyVMEvent,
       "vmwNsxEvent": vmwNsxEvent,
       "vmwFeatureImpactedEvent": vmwFeatureImpactedEvent,
       "vmwNSXComponentEvent": vmwNSXComponentEvent,
       "vmwNSXBackupEvent": vmwNSXBackupEvent,
       "vmwNSXBackupAuditLogExcludedEvent": vmwNSXBackupAuditLogExcludedEvent,
       "vmwNSXUnsecureBackupEvent": vmwNSXUnsecureBackupEvent,
       "vmwNSXBackupSystemEventsExcludedEvent": vmwNSXBackupSystemEventsExcludedEvent,
       "vmwNSXBackupNotScheduledEvent": vmwNSXBackupNotScheduledEvent,
       "vmwNSXBackupNotRecordedEvent": vmwNSXBackupNotRecordedEvent,
       "vmwNSXNtpServerEvent": vmwNSXNtpServerEvent,
       "vmwNSXSysLogServerEvent": vmwNSXSysLogServerEvent,
       "vmwControllerSysLogServerEvent": vmwControllerSysLogServerEvent,
       "vmwNSXIpV6EnabledEvent": vmwNSXIpV6EnabledEvent,
       "vmwNSXOspfNeighborDownEvent": vmwNSXOspfNeighborDownEvent,
       "vmwClusterFeatureVersionMismatchEvent": vmwClusterFeatureVersionMismatchEvent,
       "vmwHostFeatureVersionMismatchEvent": vmwHostFeatureVersionMismatchEvent,
       "vmwFeatureVersionMismatchEvent": vmwFeatureVersionMismatchEvent,
       "vmwHostFeatureEnabledMismatchEvent": vmwHostFeatureEnabledMismatchEvent,
       "vmwHostFeatureInstalledMismatchEvent": vmwHostFeatureInstalledMismatchEvent,
       "vmwHostVtepNotFoundEvent": vmwHostVtepNotFoundEvent,
       "vmwHostVtepDisconnectedEvent": vmwHostVtepDisconnectedEvent,
       "vmwHostVtepEvent": vmwHostVtepEvent,
       "vmwClusterHostsVtepMTUMismatchEvent": vmwClusterHostsVtepMTUMismatchEvent,
       "vmwFeatureUnhealthyEvent": vmwFeatureUnhealthyEvent,
       "vmwEdgeHANotConfiguredEvent": vmwEdgeHANotConfiguredEvent,
       "vmwEdgeInterfacesDownEvent": vmwEdgeInterfacesDownEvent,
       "vmwModuleUnhealthyEvent": vmwModuleUnhealthyEvent,
       "vmwModuleNotLoadedEvent": vmwModuleNotLoadedEvent,
       "vmwModuleNetworkConnectionFailureEvent": vmwModuleNetworkConnectionFailureEvent,
       "vmwHostNetworkControlPlaneMismatchEvent": vmwHostNetworkControlPlaneMismatchEvent,
       "vmwHostNetworkControlPlaneConnectionFailureEvent": vmwHostNetworkControlPlaneConnectionFailureEvent,
       "vmwHostNetworkControlPlaneNotSyncedEvent": vmwHostNetworkControlPlaneNotSyncedEvent,
       "vmwNSXControllerClusterMajorityEvent": vmwNSXControllerClusterMajorityEvent,
       "vmwNSXControllersVMOnSameHostEvent": vmwNSXControllersVMOnSameHostEvent,
       "vmwVxLanRangeExhaustEvent": vmwVxLanRangeExhaustEvent,
       "vmwNSXFirewallDefaultAllowAllRulesEvent": vmwNSXFirewallDefaultAllowAllRulesEvent,
       "vmwLogicalRouterNoUplinkEvent": vmwLogicalRouterNoUplinkEvent,
       "vmwEdgeNotHAEvent": vmwEdgeNotHAEvent,
       "vmwEdgeNotDeployedEvent": vmwEdgeNotDeployedEvent,
       "vmwEcmpIsEnabledAndStatefulServicesAreUpEvent": vmwEcmpIsEnabledAndStatefulServicesAreUpEvent,
       "vmwLogicalRouterDeployedOnEcmpEdgeHostEvent": vmwLogicalRouterDeployedOnEcmpEdgeHostEvent,
       "vmwEdgeMissingInterfaceOSPFAreaMappingEvent": vmwEdgeMissingInterfaceOSPFAreaMappingEvent,
       "vmwOspfInsecureAuthRouterEvent": vmwOspfInsecureAuthRouterEvent,
       "vmwNSXControllersDeployedCountEvent": vmwNSXControllersDeployedCountEvent,
       "vmwNSXControllerNotActiveCountEvent": vmwNSXControllerNotActiveCountEvent,
       "vmwNSXControllerEvent": vmwNSXControllerEvent,
       "vmwNSXEcmpEdgeDownEvent": vmwNSXEcmpEdgeDownEvent,
       "vmwNSXMajorityEcmpEdgesDownEvent": vmwNSXMajorityEcmpEdgesDownEvent,
       "vmwNSXAllEcmpEdgesDownEvent": vmwNSXAllEcmpEdgesDownEvent,
       "vmwNSXEdgeMtuMismatchEvent": vmwNSXEdgeMtuMismatchEvent,
       "vmwNSXEdgeSplitBrainEvent": vmwNSXEdgeSplitBrainEvent,
       "vmwCriticalHostNotAccessibleEvent": vmwCriticalHostNotAccessibleEvent,
       "vmwGenericNSXSystemEvent": vmwGenericNSXSystemEvent,
       "vmwFilterConfigApplyOnHostFailedEvent": vmwFilterConfigApplyOnHostFailedEvent,
       "vmwRulesetLoadOnHostFailedEvent": vmwRulesetLoadOnHostFailedEvent,
       "vmwConfigUpdateOnHostFailedEvent": vmwConfigUpdateOnHostFailedEvent,
       "vmwSpoofguardConfigUpdateOnHostFailedEvent": vmwSpoofguardConfigUpdateOnHostFailedEvent,
       "vmwApplyRuleToVnicFailedEvent": vmwApplyRuleToVnicFailedEvent,
       "vmwContainerConfigUpdateOnVnicFailedEvent": vmwContainerConfigUpdateOnVnicFailedEvent,
       "vmwSpoofguardApplyToVnicFailedEvent": vmwSpoofguardApplyToVnicFailedEvent,
       "vmwHostMessagingConfigurationFailedEvent": vmwHostMessagingConfigurationFailedEvent,
       "vmwHostMessagingConnectionReconfigurationFailedEvent": vmwHostMessagingConnectionReconfigurationFailedEvent,
       "vmwHostMessagingConfigurationFailedNotificationSkippedEvent": vmwHostMessagingConfigurationFailedNotificationSkippedEvent,
       "vmwHostMessagingInfrastructureDownEvent": vmwHostMessagingInfrastructureDownEvent,
       "vmwEdgeVMNotRespondingEvent": vmwEdgeVMNotRespondingEvent,
       "vmwEdgeUnhealthyEvent": vmwEdgeUnhealthyEvent,
       "vmwEdgeVMCommunicationFailureEvent": vmwEdgeVMCommunicationFailureEvent,
       "vmwNSXEdgeEvent": vmwNSXEdgeEvent,
       "vmwOtherCriticalNSXEvent": vmwOtherCriticalNSXEvent,
       "vmwPanEvent": vmwPanEvent,
       "vmwPanNsxNotInRegisteredStateEvent": vmwPanNsxNotInRegisteredStateEvent,
       "vmwPanNsxDynamicUpdateDelayedEvent": vmwPanNsxDynamicUpdateDelayedEvent,
       "vmwPanDeviceInDisconnectedStateEvent": vmwPanDeviceInDisconnectedStateEvent,
       "vmwPanNsxServiceApplianceViewMismatchEvent": vmwPanNsxServiceApplianceViewMismatchEvent,
       "vmwPanNsxFabricAgentNotFoundOnHostEvent": vmwPanNsxFabricAgentNotFoundOnHostEvent,
       "vmwPanNsxServiceVMNotFoundOnHostEvent": vmwPanNsxServiceVMNotFoundOnHostEvent,
       "vmwCheckpointEvent": vmwCheckpointEvent,
       "vmwCheckpointNsxFabricAgentNotFoundOnHostEvent": vmwCheckpointNsxFabricAgentNotFoundOnHostEvent,
       "vmwCheckpointNsxServiceVMNotFoundOnHostEvent": vmwCheckpointNsxServiceVMNotFoundOnHostEvent,
       "vmwCheckpointGatewaySicStatusNotCommunicatingEvent": vmwCheckpointGatewaySicStatusNotCommunicatingEvent,
       "vmwCheckpointNsxServiceApplianceViewMismatchEvent": vmwCheckpointNsxServiceApplianceViewMismatchEvent,
       "vmwVRNIData": vmwVRNIData,
       "vmwAffectedObject": vmwAffectedObject,
       "vmwEventSeverity": vmwEventSeverity,
       "vmwVrniUrl": vmwVrniUrl,
       "vmwTimestamp": vmwTimestamp,
       "vmwOperatorDesc": vmwOperatorDesc,
       "vmwEventName": vmwEventName,
       "vmwNetworkInsightMIBConformance": vmwNetworkInsightMIBConformance,
       "vmwNetworkInsightMIBCompliances": vmwNetworkInsightMIBCompliances,
       "vmwNetworkInsightMIBBasicCompliance": vmwNetworkInsightMIBBasicCompliance,
       "vmwNetworkInsightMIBBasicCompliance2": vmwNetworkInsightMIBBasicCompliance2,
       "vmwNetworkInsightMIBBasicCompliance3": vmwNetworkInsightMIBBasicCompliance3,
       "vmwNetworkInsightMIBBasicCompliance4": vmwNetworkInsightMIBBasicCompliance4,
       "vmwNetworkInsightMIBGroups": vmwNetworkInsightMIBGroups,
       "vmwNetworkInsightNotificationInfoGroup1": vmwNetworkInsightNotificationInfoGroup1,
       "vmwNetworkInsightNotificationGroup1": vmwNetworkInsightNotificationGroup1,
       "vmwNetworkInsightNotificationInfoGroup2": vmwNetworkInsightNotificationInfoGroup2,
       "vmwNetworkInsightNotificationGroup2": vmwNetworkInsightNotificationGroup2,
       "vmwNetworkInsightNotificationGroup3": vmwNetworkInsightNotificationGroup3,
       "vmwNetworkInsightNotificationGroup4": vmwNetworkInsightNotificationGroup4}
)
