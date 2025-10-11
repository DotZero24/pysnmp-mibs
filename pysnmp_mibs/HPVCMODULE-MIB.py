# SNMP MIB module (HPVCMODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPVCMODULE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:54 2025
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

(InterfaceIndex,
 ifInErrors,
 ifIndex,
 ifOutErrors) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifInErrors",
    "ifIndex",
    "ifOutErrors")

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
 enterprises,
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TruthValue")

(TransportAddress,
 TransportAddressType) = mibBuilder.importSymbols(
    "TRANSPORT-ADDRESS-MIB",
    "TransportAddress",
    "TransportAddressType")


# MODULE-IDENTITY

vcModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3)
)
if mibBuilder.loadTexts:
    vcModuleMIB.setRevisions(
        ("2020-04-14 00:00",
         "2019-01-29 00:00",
         "2016-03-21 00:00",
         "2014-01-29 00:00",
         "2013-11-07 00:00",
         "2012-09-22 00:00",
         "2012-08-19 00:00",
         "2011-02-01 00:00",
         "2009-02-18 00:00",
         "2008-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VcModuleRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unintegrated", 1),
          ("primaryProtected", 2),
          ("primaryUnprotected", 3),
          ("standby", 4),
          ("other", 5))
    )



class VcEnclosureRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("primary", 2),
          ("secondary", 3))
    )



class VcModuleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vcModuleEnet", 1),
          ("vcModuleFC", 2),
          ("vcModuleOther", 3))
    )



class VcModulePortBpduLoopStatus(TextualConvention, Integer32):
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
          ("loop-detected", 2))
    )



class VcModulePortProtectionStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("pause-flood-detected", 2),
          ("in-pause-condition", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_HpSysMgt_ObjectIdentity = ObjectIdentity
hpSysMgt = _HpSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5)
)
_HpEmbeddedServerMgt_ObjectIdentity = ObjectIdentity
hpEmbeddedServerMgt = _HpEmbeddedServerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7)
)
_HpModuleMgmtProc_ObjectIdentity = ObjectIdentity
hpModuleMgmtProc = _HpModuleMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5)
)
_VirtualConnect_ObjectIdentity = ObjectIdentity
virtualConnect = _VirtualConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2)
)
_VcModuleMIBObjects_ObjectIdentity = ObjectIdentity
vcModuleMIBObjects = _VcModuleMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1)
)
_VcModuleObjects_ObjectIdentity = ObjectIdentity
vcModuleObjects = _VcModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1)
)
_VcModuleDomainName_Type = SnmpAdminString
_VcModuleDomainName_Object = MibScalar
vcModuleDomainName = _VcModuleDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 1),
    _VcModuleDomainName_Type()
)
vcModuleDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainName.setStatus("current")
_VcModuleRole_Type = VcModuleRole
_VcModuleRole_Object = MibScalar
vcModuleRole = _VcModuleRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 2),
    _VcModuleRole_Type()
)
vcModuleRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleRole.setStatus("current")
_VcModuleDomainPrimaryAddressType_Type = TransportAddressType
_VcModuleDomainPrimaryAddressType_Object = MibScalar
vcModuleDomainPrimaryAddressType = _VcModuleDomainPrimaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 3),
    _VcModuleDomainPrimaryAddressType_Type()
)
vcModuleDomainPrimaryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainPrimaryAddressType.setStatus("current")
_VcModuleDomainPrimaryAddress_Type = TransportAddress
_VcModuleDomainPrimaryAddress_Object = MibScalar
vcModuleDomainPrimaryAddress = _VcModuleDomainPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 4),
    _VcModuleDomainPrimaryAddress_Type()
)
vcModuleDomainPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainPrimaryAddress.setStatus("current")
_VcModuleEnclosureRole_Type = VcEnclosureRole
_VcModuleEnclosureRole_Object = MibScalar
vcModuleEnclosureRole = _VcModuleEnclosureRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 5),
    _VcModuleEnclosureRole_Type()
)
vcModuleEnclosureRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleEnclosureRole.setStatus("current")
_VcModulePortTable_Object = MibTable
vcModulePortTable = _VcModulePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vcModulePortTable.setStatus("current")
_VcModulePortEntry_Object = MibTableRow
vcModulePortEntry = _VcModulePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1)
)
vcModulePortEntry.setIndexNames(
    (0, "HPVCMODULE-MIB", "vcModulePort"),
)
if mibBuilder.loadTexts:
    vcModulePortEntry.setStatus("current")


class _VcModulePort_Type(Integer32):
    """Custom type vcModulePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VcModulePort_Type.__name__ = "Integer32"
_VcModulePort_Object = MibTableColumn
vcModulePort = _VcModulePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 1),
    _VcModulePort_Type()
)
vcModulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModulePort.setStatus("current")
_VcModulePortIfIndex_Type = InterfaceIndex
_VcModulePortIfIndex_Object = MibTableColumn
vcModulePortIfIndex = _VcModulePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 2),
    _VcModulePortIfIndex_Type()
)
vcModulePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModulePortIfIndex.setStatus("current")
_VcModulePortBpduLoopStatus_Type = VcModulePortBpduLoopStatus
_VcModulePortBpduLoopStatus_Object = MibTableColumn
vcModulePortBpduLoopStatus = _VcModulePortBpduLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 3),
    _VcModulePortBpduLoopStatus_Type()
)
vcModulePortBpduLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModulePortBpduLoopStatus.setStatus("current")
_VcModulePortProtectionStatus_Type = VcModulePortProtectionStatus
_VcModulePortProtectionStatus_Object = MibTableColumn
vcModulePortProtectionStatus = _VcModulePortProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 4),
    _VcModulePortProtectionStatus_Type()
)
vcModulePortProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModulePortProtectionStatus.setStatus("current")
_VcModuleDomainPrimaryAddressIpv6_Type = TransportAddress
_VcModuleDomainPrimaryAddressIpv6_Object = MibScalar
vcModuleDomainPrimaryAddressIpv6 = _VcModuleDomainPrimaryAddressIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 7),
    _VcModuleDomainPrimaryAddressIpv6_Type()
)
vcModuleDomainPrimaryAddressIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainPrimaryAddressIpv6.setStatus("current")
_VcSwitchMemParityErrorCount_Type = Counter32
_VcSwitchMemParityErrorCount_Object = MibScalar
vcSwitchMemParityErrorCount = _VcSwitchMemParityErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 8),
    _VcSwitchMemParityErrorCount_Type()
)
vcSwitchMemParityErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcSwitchMemParityErrorCount.setStatus("current")
_VcSwitchMemParityErrorNonCorrectableCount_Type = Counter32
_VcSwitchMemParityErrorNonCorrectableCount_Object = MibScalar
vcSwitchMemParityErrorNonCorrectableCount = _VcSwitchMemParityErrorNonCorrectableCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 9),
    _VcSwitchMemParityErrorNonCorrectableCount_Type()
)
vcSwitchMemParityErrorNonCorrectableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcSwitchMemParityErrorNonCorrectableCount.setStatus("current")
_VcModuleMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
vcModuleMIBNotificationPrefix = _VcModuleMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2)
)
_VcModuleMIBNotifications_ObjectIdentity = ObjectIdentity
vcModuleMIBNotifications = _VcModuleMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0)
)
_VcModuleMIBNotificationObjects_ObjectIdentity = ObjectIdentity
vcModuleMIBNotificationObjects = _VcModuleMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 1)
)
_VcModuleMIBConformance_ObjectIdentity = ObjectIdentity
vcModuleMIBConformance = _VcModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3)
)
_VcModuleMIBCompliances_ObjectIdentity = ObjectIdentity
vcModuleMIBCompliances = _VcModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1)
)
_VcModuleMIBGroups_ObjectIdentity = ObjectIdentity
vcModuleMIBGroups = _VcModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2)
)

# Managed Objects groups

vcModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 1)
)
vcModuleGroup.setObjects(
      *(("HPVCMODULE-MIB", "vcModuleDomainName"),
        ("HPVCMODULE-MIB", "vcModuleRole"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressIpv6"),
        ("HPVCMODULE-MIB", "vcSwitchMemParityErrorCount"))
)
if mibBuilder.loadTexts:
    vcModuleGroup.setStatus("deprecated")

vcModuleGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 4)
)
vcModuleGroup2.setObjects(
      *(("HPVCMODULE-MIB", "vcModuleDomainName"),
        ("HPVCMODULE-MIB", "vcModuleRole"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressIpv6"),
        ("HPVCMODULE-MIB", "vcSwitchMemParityErrorCount"),
        ("HPVCMODULE-MIB", "vcSwitchMemParityErrorNonCorrectableCount"))
)
if mibBuilder.loadTexts:
    vcModuleGroup2.setStatus("current")


# Notification objects

vcModuleDomainRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 1)
)
vcModuleDomainRoleChange.setObjects(
    ("HPVCMODULE-MIB", "vcModuleRole")
)
if mibBuilder.loadTexts:
    vcModuleDomainRoleChange.setStatus(
        "current"
    )

vcSwitchMemParityErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 2)
)
vcSwitchMemParityErrorEvent.setObjects(
    ("HPVCMODULE-MIB", "vcSwitchMemParityErrorCount")
)
if mibBuilder.loadTexts:
    vcSwitchMemParityErrorEvent.setStatus(
        "current"
    )

vcSwitchMemParityErrorNonCorrectableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 3)
)
vcSwitchMemParityErrorNonCorrectableEvent.setObjects(
      *(("HPVCMODULE-MIB", "vcSwitchMemParityErrorNonCorrectableCount"),
        ("HPVCMODULE-MIB", "cpqHoFwVerLocation"))
)
if mibBuilder.loadTexts:
    vcSwitchMemParityErrorNonCorrectableEvent.setStatus(
        "current"
    )

vcModPortInputUtilizationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 11)
)
vcModPortInputUtilizationUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortInputUtilizationUp.setStatus(
        "current"
    )

vcModPortInputUtilizationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 12)
)
vcModPortInputUtilizationDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortInputUtilizationDown.setStatus(
        "current"
    )

vcModPortOutputUtilizationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 13)
)
vcModPortOutputUtilizationUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortOutputUtilizationUp.setStatus(
        "current"
    )

vcModPortOutputUtilizationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 14)
)
vcModPortOutputUtilizationDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortOutputUtilizationDown.setStatus(
        "current"
    )

vcModPortInputErrorsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 15)
)
vcModPortInputErrorsUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifInErrors"))
)
if mibBuilder.loadTexts:
    vcModPortInputErrorsUp.setStatus(
        "current"
    )

vcModPortInputErrorsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 16)
)
vcModPortInputErrorsDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifInErrors"))
)
if mibBuilder.loadTexts:
    vcModPortInputErrorsDown.setStatus(
        "current"
    )

vcModPortOutputErrorsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 17)
)
vcModPortOutputErrorsUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    vcModPortOutputErrorsUp.setStatus(
        "current"
    )

vcModPortOutputErrorsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 18)
)
vcModPortOutputErrorsDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    vcModPortOutputErrorsDown.setStatus(
        "current"
    )

vcModPortBpduLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 19)
)
vcModPortBpduLoopDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPVCMODULE-MIB", "vcModulePort"),
        ("HPVCMODULE-MIB", "vcModulePortBpduLoopStatus"))
)
if mibBuilder.loadTexts:
    vcModPortBpduLoopDetected.setStatus(
        "current"
    )

vcModPortBpduLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 20)
)
vcModPortBpduLoopCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPVCMODULE-MIB", "vcModulePort"),
        ("HPVCMODULE-MIB", "vcModulePortBpduLoopStatus"))
)
if mibBuilder.loadTexts:
    vcModPortBpduLoopCleared.setStatus(
        "current"
    )

vcModPortProtectionConditionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 21)
)
vcModPortProtectionConditionDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPVCMODULE-MIB", "vcModulePort"),
        ("HPVCMODULE-MIB", "vcModulePortProtectionStatus"))
)
if mibBuilder.loadTexts:
    vcModPortProtectionConditionDetected.setStatus(
        "current"
    )

vcModPortProtectionConditionCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 22)
)
vcModPortProtectionConditionCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPVCMODULE-MIB", "vcModulePort"),
        ("HPVCMODULE-MIB", "vcModulePortProtectionStatus"))
)
if mibBuilder.loadTexts:
    vcModPortProtectionConditionCleared.setStatus(
        "current"
    )


# Notifications groups

vcModPortThresholdNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 2)
)
vcModPortThresholdNotificationsGroup.setObjects(
      *(("HPVCMODULE-MIB", "vcModPortInputUtilizationUp"),
        ("HPVCMODULE-MIB", "vcModPortInputUtilizationDown"),
        ("HPVCMODULE-MIB", "vcModPortOutputUtilizationUp"),
        ("HPVCMODULE-MIB", "vcModPortOutputUtilizationDown"),
        ("HPVCMODULE-MIB", "vcModPortInputErrorsUp"),
        ("HPVCMODULE-MIB", "vcModPortInputErrorsDown"),
        ("HPVCMODULE-MIB", "vcModPortOutputErrorsUp"),
        ("HPVCMODULE-MIB", "vcModPortOutputErrorsDown"))
)
if mibBuilder.loadTexts:
    vcModPortThresholdNotificationsGroup.setStatus(
        "current"
    )

vcModPortStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 3)
)
vcModPortStatusNotificationsGroup.setObjects(
      *(("HPVCMODULE-MIB", "vcModPortBpduLoopDetected"),
        ("HPVCMODULE-MIB", "vcModPortBpduLoopCleared"),
        ("HPVCMODULE-MIB", "vcModPortProtectionConditionDetected"),
        ("HPVCMODULE-MIB", "vcModPortProtectionConditionCleared"))
)
if mibBuilder.loadTexts:
    vcModPortStatusNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vcModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 1)
)
vcModuleMIBCompliance.setObjects(
      *(("HPVCMODULE-MIB", "vcModuleGroup"),
        ("HPVCMODULE-MIB", "vcModPortThresholdNotificationsGroup"),
        ("HPVCMODULE-MIB", "vcModPortStatusNotificationsGroup"))
)
if mibBuilder.loadTexts:
    vcModuleMIBCompliance.setStatus(
        "deprecated"
    )

vcModuleMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 2)
)
vcModuleMIBCompliance2.setObjects(
      *(("HPVCMODULE-MIB", "vcModuleGroup"),
        ("HPVCMODULE-MIB", "vcModPortThresholdNotificationsGroup"),
        ("HPVCMODULE-MIB", "vcModPortStatusNotificationsGroup"),
        ("HPVCMODULE-MIB", "vcModuleGroup2"))
)
if mibBuilder.loadTexts:
    vcModuleMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPVCMODULE-MIB",
    **{"VcModuleRole": VcModuleRole,
       "VcEnclosureRole": VcEnclosureRole,
       "VcModuleType": VcModuleType,
       "VcModulePortBpduLoopStatus": VcModulePortBpduLoopStatus,
       "VcModulePortProtectionStatus": VcModulePortProtectionStatus,
       "hp": hp,
       "hpSysMgt": hpSysMgt,
       "hpEmbeddedServerMgt": hpEmbeddedServerMgt,
       "hpModuleMgmtProc": hpModuleMgmtProc,
       "virtualConnect": virtualConnect,
       "vcModuleMIB": vcModuleMIB,
       "vcModuleMIBObjects": vcModuleMIBObjects,
       "vcModuleObjects": vcModuleObjects,
       "vcModuleDomainName": vcModuleDomainName,
       "vcModuleRole": vcModuleRole,
       "vcModuleDomainPrimaryAddressType": vcModuleDomainPrimaryAddressType,
       "vcModuleDomainPrimaryAddress": vcModuleDomainPrimaryAddress,
       "vcModuleEnclosureRole": vcModuleEnclosureRole,
       "vcModulePortTable": vcModulePortTable,
       "vcModulePortEntry": vcModulePortEntry,
       "vcModulePort": vcModulePort,
       "vcModulePortIfIndex": vcModulePortIfIndex,
       "vcModulePortBpduLoopStatus": vcModulePortBpduLoopStatus,
       "vcModulePortProtectionStatus": vcModulePortProtectionStatus,
       "vcModuleDomainPrimaryAddressIpv6": vcModuleDomainPrimaryAddressIpv6,
       "vcSwitchMemParityErrorCount": vcSwitchMemParityErrorCount,
       "vcSwitchMemParityErrorNonCorrectableCount": vcSwitchMemParityErrorNonCorrectableCount,
       "vcModuleMIBNotificationPrefix": vcModuleMIBNotificationPrefix,
       "vcModuleMIBNotifications": vcModuleMIBNotifications,
       "vcModuleDomainRoleChange": vcModuleDomainRoleChange,
       "vcSwitchMemParityErrorEvent": vcSwitchMemParityErrorEvent,
       "vcSwitchMemParityErrorNonCorrectableEvent": vcSwitchMemParityErrorNonCorrectableEvent,
       "vcModPortInputUtilizationUp": vcModPortInputUtilizationUp,
       "vcModPortInputUtilizationDown": vcModPortInputUtilizationDown,
       "vcModPortOutputUtilizationUp": vcModPortOutputUtilizationUp,
       "vcModPortOutputUtilizationDown": vcModPortOutputUtilizationDown,
       "vcModPortInputErrorsUp": vcModPortInputErrorsUp,
       "vcModPortInputErrorsDown": vcModPortInputErrorsDown,
       "vcModPortOutputErrorsUp": vcModPortOutputErrorsUp,
       "vcModPortOutputErrorsDown": vcModPortOutputErrorsDown,
       "vcModPortBpduLoopDetected": vcModPortBpduLoopDetected,
       "vcModPortBpduLoopCleared": vcModPortBpduLoopCleared,
       "vcModPortProtectionConditionDetected": vcModPortProtectionConditionDetected,
       "vcModPortProtectionConditionCleared": vcModPortProtectionConditionCleared,
       "vcModuleMIBNotificationObjects": vcModuleMIBNotificationObjects,
       "vcModuleMIBConformance": vcModuleMIBConformance,
       "vcModuleMIBCompliances": vcModuleMIBCompliances,
       "vcModuleMIBCompliance": vcModuleMIBCompliance,
       "vcModuleMIBCompliance2": vcModuleMIBCompliance2,
       "vcModuleMIBGroups": vcModuleMIBGroups,
       "vcModuleGroup": vcModuleGroup,
       "vcModPortThresholdNotificationsGroup": vcModPortThresholdNotificationsGroup,
       "vcModPortStatusNotificationsGroup": vcModPortStatusNotificationsGroup,
       "vcModuleGroup2": vcModuleGroup2}
)
