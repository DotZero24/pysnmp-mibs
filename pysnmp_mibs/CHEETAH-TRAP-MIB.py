# SNMP MIB module (CHEETAH-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/CHEETAH-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:21 2025
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

(vADCCurCfgCompLimit,
 vADCCurCfgFeatADOS,
 vADCCurCfgFeatBWM,
 vADCCurCfgFeatGlobal,
 vADCCurCfgFeatITM,
 vADCCurCfgFeatLLB,
 vADCCurCfgLimit,
 vADCCurCfgSslLimit,
 vADCCurCfgState,
 vADCCurCfgVADCId,
 vADCInfoVRRPStatus) = mibBuilder.importSymbols(
    "ADMIN-ALTEON-AC-vADC-MIB",
    "vADCCurCfgCompLimit",
    "vADCCurCfgFeatADOS",
    "vADCCurCfgFeatBWM",
    "vADCCurCfgFeatGlobal",
    "vADCCurCfgFeatITM",
    "vADCCurCfgFeatLLB",
    "vADCCurCfgLimit",
    "vADCCurCfgSslLimit",
    "vADCCurCfgState",
    "vADCCurCfgVADCId",
    "vADCInfoVRRPStatus")

(fltCurCfgIndx,
 fltCurCfgPortIndx,
 fltCurCfgSrcIp,
 slbCurCfgEnhGroupHealthCheckFormula,
 slbCurCfgEnhGroupIndex,
 slbCurCfgEnhGroupName,
 slbCurCfgEnhRealServerIndex,
 slbCurCfgEnhRealServerIpAddr,
 slbCurCfgEnhRealServerName,
 slbCurCfgEnhVirtServApplicationType,
 slbCurCfgEnhVirtServerIndex,
 slbCurCfgEnhVirtServerIpAddress,
 slbCurCfgEnhVirtServerVname,
 slbCurCfgEnhVirtServiceRealPort,
 slbCurCfgEnhVirtServiceVirtPort,
 slbCurCfgGroupHealthCheckFormula,
 slbCurCfgGroupIndex,
 slbCurCfgGroupName,
 slbCurCfgRealServerIndex,
 slbCurCfgRealServerIpAddr,
 slbCurCfgRealServerName,
 slbCurCfgVirtServerIndex,
 slbCurCfgVirtServerIpAddress,
 slbCurCfgVirtServerVname,
 slbCurCfgVirtServiceRealPort) = mibBuilder.importSymbols(
    "ALTEON-CHEETAH-LAYER4-MIB",
    "fltCurCfgIndx",
    "fltCurCfgPortIndx",
    "fltCurCfgSrcIp",
    "slbCurCfgEnhGroupHealthCheckFormula",
    "slbCurCfgEnhGroupIndex",
    "slbCurCfgEnhGroupName",
    "slbCurCfgEnhRealServerIndex",
    "slbCurCfgEnhRealServerIpAddr",
    "slbCurCfgEnhRealServerName",
    "slbCurCfgEnhVirtServApplicationType",
    "slbCurCfgEnhVirtServerIndex",
    "slbCurCfgEnhVirtServerIpAddress",
    "slbCurCfgEnhVirtServerVname",
    "slbCurCfgEnhVirtServiceRealPort",
    "slbCurCfgEnhVirtServiceVirtPort",
    "slbCurCfgGroupHealthCheckFormula",
    "slbCurCfgGroupIndex",
    "slbCurCfgGroupName",
    "slbCurCfgRealServerIndex",
    "slbCurCfgRealServerIpAddr",
    "slbCurCfgRealServerName",
    "slbCurCfgVirtServerIndex",
    "slbCurCfgVirtServerIpAddress",
    "slbCurCfgVirtServerVname",
    "slbCurCfgVirtServiceRealPort")

(ipCurCfgGwAddr,
 ipCurCfgGwIndex,
 vrrpCurCfgIfIndx,
 vrrpCurCfgIfPasswd,
 vrrpCurCfgVirtRtrAddr,
 vrrpCurCfgVirtRtrIndx) = mibBuilder.importSymbols(
    "ALTEON-CHEETAH-NETWORK-MIB",
    "ipCurCfgGwAddr",
    "ipCurCfgGwIndex",
    "vrrpCurCfgIfIndx",
    "vrrpCurCfgIfPasswd",
    "vrrpCurCfgVirtRtrAddr",
    "vrrpCurCfgVirtRtrIndx")

(vlanCurCfgVlanId,
 vlanCurCfgVlanName) = mibBuilder.importSymbols(
    "ALTEON-CS-PHYSICAL-MIB",
    "vlanCurCfgVlanId",
    "vlanCurCfgVlanName")

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltTraps_ObjectIdentity = ObjectIdentity
altTraps = _AltTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7)
)


class _AltSwTrapDisplayString_Type(DisplayString):
    """Custom type altSwTrapDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AltSwTrapDisplayString_Type.__name__ = "DisplayString"
_AltSwTrapDisplayString_Object = MibScalar
altSwTrapDisplayString = _AltSwTrapDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 1000),
    _AltSwTrapDisplayString_Type()
)
altSwTrapDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSwTrapDisplayString.setStatus("mandatory")
_AltSwTrapRate_Type = Integer32
_AltSwTrapRate_Object = MibScalar
altSwTrapRate = _AltSwTrapRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 1001),
    _AltSwTrapRate_Type()
)
altSwTrapRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSwTrapRate.setStatus("mandatory")
_AltSwTrapSeverity_Type = Integer32
_AltSwTrapSeverity_Object = MibScalar
altSwTrapSeverity = _AltSwTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 1002),
    _AltSwTrapSeverity_Type()
)
altSwTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSwTrapSeverity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

altSwPrimaryPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 1)
)
if mibBuilder.loadTexts:
    altSwPrimaryPowerSupplyFailure.setStatus(
        ""
    )

altSwDefGwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 2)
)
altSwDefGwUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwUp.setStatus(
        ""
    )

altSwDefGwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 3)
)
altSwDefGwDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwDown.setStatus(
        ""
    )

altSwDefGwInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 4)
)
altSwDefGwInService.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwInService.setStatus(
        ""
    )

altSwDefGwNotInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 5)
)
altSwDefGwNotInService.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwNotInService.setStatus(
        ""
    )

altSwSlbRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 6)
)
altSwSlbRealServerUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerUp.setStatus(
        ""
    )

altSwSlbRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 7)
)
altSwSlbRealServerDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerDown.setStatus(
        ""
    )

altSwSlbRealServerMaxConnReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 8)
)
altSwSlbRealServerMaxConnReached.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerMaxConnReached.setStatus(
        ""
    )

altSwSlbBkupRealServerAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 9)
)
altSwSlbBkupRealServerAct.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerAct.setStatus(
        ""
    )

altSwSlbBkupRealServerDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 10)
)
altSwSlbBkupRealServerDeact.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerDeact.setStatus(
        ""
    )

altSwSlbBkupRealServerActOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 11)
)
altSwSlbBkupRealServerActOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerActOverflow.setStatus(
        ""
    )

altSwSlbBkupRealServerDeactOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 12)
)
altSwSlbBkupRealServerDeactOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerDeactOverflow.setStatus(
        ""
    )

altSwfltFilterFired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 13)
)
altSwfltFilterFired.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgIndx"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgPortIndx"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwfltFilterFired.setStatus(
        ""
    )

altSwSlbRealServerServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 14)
)
altSwSlbRealServerServiceUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServiceRealPort"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerServiceUp.setStatus(
        ""
    )

altSwSlbRealServerServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 15)
)
altSwSlbRealServerServiceDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServiceRealPort"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerServiceDown.setStatus(
        ""
    )

altSwVrrpNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 16)
)
altSwVrrpNewMaster.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpNewMaster.setStatus(
        ""
    )

altSwVrrpNewBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 17)
)
altSwVrrpNewBackup.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpNewBackup.setStatus(
        ""
    )

altSwVrrpAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 18)
)
altSwVrrpAuthFailure.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgIfIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgIfPasswd"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpAuthFailure.setStatus(
        ""
    )

altSwLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 19)
)
altSwLoginFailure.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwLoginFailure.setStatus(
        ""
    )

altSwSlbSynAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 20)
)
altSwSlbSynAttack.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapRate"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbSynAttack.setStatus(
        ""
    )

altSwTcpHoldDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 21)
)
altSwTcpHoldDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgSrcIp"),
        ("CHEETAH-TRAP-MIB", "altSwTrapRate"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTcpHoldDown.setStatus(
        ""
    )

altSwTempExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 22)
)
altSwTempExceedThreshold.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTempExceedThreshold.setStatus(
        ""
    )

altSwSlbSessAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 23)
)
altSwSlbSessAttack.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapRate"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbSessAttack.setStatus(
        ""
    )

altSwFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 24)
)
altSwFanFailure.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwFanFailure.setStatus(
        ""
    )

altSwSlbVirtServerServicesUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 25)
)
altSwSlbVirtServerServicesUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerIpAddress"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerVname"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbVirtServerServicesUp.setStatus(
        ""
    )

altSwSlbVirtServerServicesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 26)
)
altSwSlbVirtServerServicesDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerIpAddress"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerVname"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbVirtServerServicesDown.setStatus(
        ""
    )

altSwSlbRealGroupAdvhlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 27)
)
altSwSlbRealGroupAdvhlUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupHealthCheckFormula"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealGroupAdvhlUp.setStatus(
        ""
    )

altSwSlbRealGroupAdvhlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 28)
)
altSwSlbRealGroupAdvhlDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupHealthCheckFormula"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealGroupAdvhlDown.setStatus(
        ""
    )

altSwSlbBkupGroupAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 29)
)
altSwSlbBkupGroupAct.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupGroupAct.setStatus(
        ""
    )

altSwSlbBkupGroupDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 30)
)
altSwSlbBkupGroupDeact.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupGroupDeact.setStatus(
        ""
    )

altSwSlbRemoteRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 31)
)
altSwSlbRemoteRealServerUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRemoteRealServerUp.setStatus(
        ""
    )

altSwSlbRemoteRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 32)
)
altSwSlbRemoteRealServerDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRemoteRealServerDown.setStatus(
        ""
    )

altSwSlbRealServerOperDis = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 33)
)
altSwSlbRealServerOperDis.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerOperDis.setStatus(
        ""
    )

altSwSlbRealServerOperEna = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 34)
)
altSwSlbRealServerOperEna.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerOperEna.setStatus(
        ""
    )

altSwIfcVlanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 35)
)
altSwIfcVlanDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanId"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwIfcVlanDown.setStatus(
        ""
    )

altSwPortVlanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 36)
)
altSwPortVlanDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanId"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwPortVlanDown.setStatus(
        ""
    )

altSwIfcVlanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 37)
)
altSwIfcVlanUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanId"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwIfcVlanUp.setStatus(
        ""
    )

altSwPortVlanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 38)
)
altSwPortVlanUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanId"),
        ("ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwPortVlanUp.setStatus(
        ""
    )

altSwBulkApply = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 39)
)
altSwBulkApply.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwBulkApply.setStatus(
        ""
    )

altSwDeviceTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 40)
)
altSwDeviceTemperatureNormal.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDeviceTemperatureNormal.setStatus(
        ""
    )

altSwDeviceTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 41)
)
altSwDeviceTemperatureHigh.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDeviceTemperatureHigh.setStatus(
        ""
    )

altSwDeviceTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 42)
)
altSwDeviceTemperatureCritical.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDeviceTemperatureCritical.setStatus(
        ""
    )

altSwDualPowerSupplyProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 43)
)
altSwDualPowerSupplyProblem.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDualPowerSupplyProblem.setStatus(
        ""
    )

altSwDualPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 44)
)
altSwDualPowerSupplyUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDualPowerSupplyUp.setStatus(
        ""
    )

altSwTputReachThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 47)
)
altSwTputReachThreshold.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTputReachThreshold.setStatus(
        ""
    )

altSwTputExceedLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 48)
)
altSwTputExceedLimit.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTputExceedLimit.setStatus(
        ""
    )

altSwcompCardNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 49)
)
altSwcompCardNotAvail.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcompCardNotAvail.setStatus(
        ""
    )

altSwsslCardNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 50)
)
altSwsslCardNotAvail.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwsslCardNotAvail.setStatus(
        ""
    )

altSwloginSsh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 51)
)
altSwloginSsh.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwloginSsh.setStatus(
        ""
    )

altSwtmpCecLmtStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 52)
)
altSwtmpCecLmtStop.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtmpCecLmtStop.setStatus(
        ""
    )

altSwcacheLimitShortSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 53)
)
altSwcacheLimitShortSpace.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcacheLimitShortSpace.setStatus(
        ""
    )

altSwcacheReache80 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 54)
)
altSwcacheReache80.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcacheReache80.setStatus(
        ""
    )

altSwcacheBelow80 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 55)
)
altSwcacheBelow80.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcacheBelow80.setStatus(
        ""
    )

altSwlogDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 56)
)
altSwlogDiskSpace.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwlogDiskSpace.setStatus(
        ""
    )

altSwtmpCecLimitMemShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 59)
)
altSwtmpCecLimitMemShort.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtmpCecLimitMemShort.setStatus(
        ""
    )

altSwconfProtectionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 60)
)
altSwconfProtectionActive.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwconfProtectionActive.setStatus(
        ""
    )

altSwkeyLoadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 61)
)
altSwkeyLoadErr.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwkeyLoadErr.setStatus(
        ""
    )

altSwcompCardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 62)
)
altSwcompCardDetect.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcompCardDetect.setStatus(
        ""
    )

altSwfipsEngineNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 63)
)
altSwfipsEngineNotRunning.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwfipsEngineNotRunning.setStatus(
        ""
    )

altSwsslAclTypeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 64)
)
altSwsslAclTypeDetected.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwsslAclTypeDetected.setStatus(
        ""
    )

altSwocspSvrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 65)
)
altSwocspSvrErr.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwocspSvrErr.setStatus(
        ""
    )

altSwocspRespVerifyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 66)
)
altSwocspRespVerifyErr.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwocspRespVerifyErr.setStatus(
        ""
    )

altSwoscpQueryErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 67)
)
altSwoscpQueryErr.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwoscpQueryErr.setStatus(
        ""
    )

altSwcertRevokedID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 68)
)
altSwcertRevokedID.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcertRevokedID.setStatus(
        ""
    )

altSwerrCrlUpdTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 69)
)
altSwerrCrlUpdTime.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwerrCrlUpdTime.setStatus(
        ""
    )

altSwcrlExp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 70)
)
altSwcrlExp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcrlExp.setStatus(
        ""
    )

altSwcertExpDays = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 71)
)
altSwcertExpDays.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcertExpDays.setStatus(
        ""
    )

altSwcompDisDueMemLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 72)
)
altSwcompDisDueMemLimit.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcompDisDueMemLimit.setStatus(
        ""
    )

altSwcompEnaAfterMemLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 73)
)
altSwcompEnaAfterMemLimit.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcompEnaAfterMemLimit.setStatus(
        ""
    )

altSwcompLicenseOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 74)
)
altSwcompLicenseOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcompLicenseOverflow.setStatus(
        ""
    )

altSwsslCpsLicenseOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 75)
)
altSwsslCpsLicenseOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwsslCpsLicenseOverflow.setStatus(
        ""
    )

altSwtslValidationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 76)
)
altSwtslValidationFailure.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslValidationFailure.setStatus(
        ""
    )

altSwtslOcspCertRevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 77)
)
altSwtslOcspCertRevoked.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslOcspCertRevoked.setStatus(
        ""
    )

altSwtslOcspCertUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 78)
)
altSwtslOcspCertUnknown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslOcspCertUnknown.setStatus(
        ""
    )

altSwtslSignatureNodeMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 79)
)
altSwtslSignatureNodeMissing.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslSignatureNodeMissing.setStatus(
        ""
    )

altSwtslSignatureValidFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 80)
)
altSwtslSignatureValidFailure.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslSignatureValidFailure.setStatus(
        ""
    )

altSwtslNewSeqNumLessThanExisting = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 81)
)
altSwtslNewSeqNumLessThanExisting.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslNewSeqNumLessThanExisting.setStatus(
        ""
    )

altSwtslNextUpdateInThePast = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 82)
)
altSwtslNextUpdateInThePast.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslNextUpdateInThePast.setStatus(
        ""
    )

altSwtslNextUpdateOver30Days = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 83)
)
altSwtslNextUpdateOver30Days.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslNextUpdateOver30Days.setStatus(
        ""
    )

altSwtslOcspTimingErrorField = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 84)
)
altSwtslOcspTimingErrorField.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslOcspTimingErrorField.setStatus(
        ""
    )

altSwtslInvalidOcspTimingErrorField = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 85)
)
altSwtslInvalidOcspTimingErrorField.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslInvalidOcspTimingErrorField.setStatus(
        ""
    )

altSwtslFetcherFetchingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 86)
)
altSwtslFetcherFetchingError.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslFetcherFetchingError.setStatus(
        ""
    )

altSwtslFetcherSignatureError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 87)
)
altSwtslFetcherSignatureError.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslFetcherSignatureError.setStatus(
        ""
    )

altSwtslFetcherOcspError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 88)
)
altSwtslFetcherOcspError.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslFetcherOcspError.setStatus(
        ""
    )

altSwtslFetcherXmlParsingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 89)
)
altSwtslFetcherXmlParsingError.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslFetcherXmlParsingError.setStatus(
        ""
    )

altSwtslFetcherIdenticalSeqNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 90)
)
altSwtslFetcherIdenticalSeqNum.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslFetcherIdenticalSeqNum.setStatus(
        ""
    )

altSwtslFetchingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 91)
)
altSwtslFetchingDone.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwtslFetchingDone.setStatus(
        ""
    )

altSwsslCpsLicenseWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 92)
)
altSwsslCpsLicenseWatermark.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwsslCpsLicenseWatermark.setStatus(
        ""
    )

altSwcompressionLicensewatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 93)
)
altSwcompressionLicensewatermark.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwcompressionLicensewatermark.setStatus(
        ""
    )

altSwpipAllocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 94)
)
altSwpipAllocFailed.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwpipAllocFailed.setStatus(
        ""
    )

altAxUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 95)
)
altAxUpdateFailed.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altAxUpdateFailed.setStatus(
        ""
    )

altSwVrrpVsrNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 96)
)
altSwVrrpVsrNewMaster.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpVsrNewMaster.setStatus(
        ""
    )

altSwVrrpVsrNewBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 97)
)
altSwVrrpVsrNewBackup.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpVsrNewBackup.setStatus(
        ""
    )

vadcStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 98)
)
vadcStateChange.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgState"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcStateChange.setStatus(
        ""
    )

vadcStateVrrpMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 103)
)
vadcStateVrrpMaster.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCInfoVRRPStatus"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcStateVrrpMaster.setStatus(
        ""
    )

vadcStateVrrpBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 104)
)
vadcStateVrrpBackup.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCInfoVRRPStatus"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcStateVrrpBackup.setStatus(
        ""
    )

dnssecNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 107)
)
dnssecNotify.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    dnssecNotify.setStatus(
        ""
    )

agTftpActionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 108)
)
agTftpActionStatus.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    agTftpActionStatus.setStatus(
        ""
    )

altSwSlbEnhRealGroupAdvhlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 118)
)
altSwSlbEnhRealGroupAdvhlUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupHealthCheckFormula"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealGroupAdvhlUp.setStatus(
        ""
    )

altSwSlbEnhRealGroupAdvhlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 119)
)
altSwSlbEnhRealGroupAdvhlDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupHealthCheckFormula"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealGroupAdvhlDown.setStatus(
        ""
    )

altSwSlbEnhBkupGroupAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 120)
)
altSwSlbEnhBkupGroupAct.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhBkupGroupAct.setStatus(
        ""
    )

altSwSlbEnhBkupGroupDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 121)
)
altSwSlbEnhBkupGroupDeact.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhBkupGroupDeact.setStatus(
        ""
    )

altSwSlbEnhVirtServerServicesUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 122)
)
altSwSlbEnhVirtServerServicesUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIpAddress"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerVname"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhVirtServerServicesUp.setStatus(
        ""
    )

altSwSlbEnhVirtServerServicesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 123)
)
altSwSlbEnhVirtServerServicesDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIpAddress"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerVname"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhVirtServerServicesDown.setStatus(
        ""
    )

altSwTputAverage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 124)
)
altSwTputAverage.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTputAverage.setStatus(
        ""
    )

altSwSlbEnhRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 125)
)
altSwSlbEnhRealServerDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerDown.setStatus(
        ""
    )

altSwSlbEnhRealServerMaxConnReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 126)
)
altSwSlbEnhRealServerMaxConnReached.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerMaxConnReached.setStatus(
        ""
    )

altSwSlbEnhBkupRealServerAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 127)
)
altSwSlbEnhBkupRealServerAct.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhBkupRealServerAct.setStatus(
        ""
    )

altSwSlbEnhBkupRealServerDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 128)
)
altSwSlbEnhBkupRealServerDeact.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhBkupRealServerDeact.setStatus(
        ""
    )

altSwSlbEnhBkupRealServerActOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 129)
)
altSwSlbEnhBkupRealServerActOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhBkupRealServerActOverflow.setStatus(
        ""
    )

altSwSlbEnhBkupRealServerDeactOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 130)
)
altSwSlbEnhBkupRealServerDeactOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhBkupRealServerDeactOverflow.setStatus(
        ""
    )

altSwSlbEnhRealServerServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 131)
)
altSwSlbEnhRealServerServiceUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServiceRealPort"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerServiceUp.setStatus(
        ""
    )

altSwSlbEnhRealServerServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 132)
)
altSwSlbEnhRealServerServiceDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServiceRealPort"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerServiceDown.setStatus(
        ""
    )

altSwSlbEnhRemoteRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 133)
)
altSwSlbEnhRemoteRealServerUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRemoteRealServerUp.setStatus(
        ""
    )

altSwSlbEnhRemoteRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 134)
)
altSwSlbEnhRemoteRealServerDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRemoteRealServerDown.setStatus(
        ""
    )

altSwSlbEnhRealServerOperDis = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 135)
)
altSwSlbEnhRealServerOperDis.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerOperDis.setStatus(
        ""
    )

altSwSlbEnhRealServerOperEna = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 136)
)
altSwSlbEnhRealServerOperEna.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerOperEna.setStatus(
        ""
    )

vadcDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 137)
)
vadcDelete.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcDelete.setStatus(
        ""
    )

vadcCapUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 138)
)
vadcCapUnit.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcCapUnit.setStatus(
        ""
    )

vadcLicGlobal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 139)
)
vadcLicGlobal.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgFeatGlobal"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgFeatBWM"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgFeatITM"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgFeatADOS"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgFeatLLB"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcLicGlobal.setStatus(
        ""
    )

vadcThrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 140)
)
vadcThrupt.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgLimit"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcThrupt.setStatus(
        ""
    )

vadcSsl = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 141)
)
vadcSsl.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgSslLimit"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcSsl.setStatus(
        ""
    )

vadcComp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 142)
)
vadcComp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgCompLimit"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    vadcComp.setStatus(
        ""
    )

altAPMLicenseWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 143)
)
altAPMLicenseWatermark.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altAPMLicenseWatermark.setStatus(
        ""
    )

altAPMLicenseOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 144)
)
altAPMLicenseOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altAPMLicenseOverflow.setStatus(
        ""
    )

altSwSlbEnhRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 145)
)
altSwSlbEnhRealServerUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerUp.setStatus(
        ""
    )

altSwVrrpNewInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 146)
)
altSwVrrpNewInit.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpNewInit.setStatus(
        ""
    )

altSwVrrpVsrNewInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 147)
)
altSwVrrpVsrNewInit.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpVsrNewInit.setStatus(
        ""
    )

altSwVrrpNewHoldoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 148)
)
altSwVrrpNewHoldoff.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpNewHoldoff.setStatus(
        ""
    )

altSwVrrpVsrNewHoldoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 149)
)
altSwVrrpVsrNewHoldoff.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpVsrNewHoldoff.setStatus(
        ""
    )

altWAFLicenseWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 150)
)
altWAFLicenseWatermark.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altWAFLicenseWatermark.setStatus(
        ""
    )

altWAFLicenseOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 151)
)
altWAFLicenseOverflow.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altWAFLicenseOverflow.setStatus(
        ""
    )

altHAGroupNewInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 152)
)
altHAGroupNewInitTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altHAGroupNewInitTrap.setStatus(
        ""
    )

altHAGroupNewHoldoffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 153)
)
altHAGroupNewHoldoffTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altHAGroupNewHoldoffTrap.setStatus(
        ""
    )

altHAGroupNewMasterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 154)
)
altHAGroupNewMasterTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altHAGroupNewMasterTrap.setStatus(
        ""
    )

altHAGroupNewBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 155)
)
altHAGroupNewBackupTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altHAGroupNewBackupTrap.setStatus(
        ""
    )

virtHighSpCpuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 159)
)
virtHighSpCpuTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    virtHighSpCpuTrap.setStatus(
        ""
    )

virtHighSpCpuClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 160)
)
virtHighSpCpuClearTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    virtHighSpCpuClearTrap.setStatus(
        ""
    )

virtHighMpCpuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 161)
)
virtHighMpCpuTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    virtHighMpCpuTrap.setStatus(
        ""
    )

virtHighMpCpuClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 162)
)
virtHighMpCpuClearTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    virtHighMpCpuClearTrap.setStatus(
        ""
    )

appwallUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 166)
)
appwallUpTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    appwallUpTrap.setStatus(
        ""
    )

appwallDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 167)
)
appwallDownTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    appwallDownTrap.setStatus(
        ""
    )

altMemoryPressureActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 170)
)
altMemoryPressureActivated.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altMemoryPressureActivated.setStatus(
        ""
    )

altMemoryPressureDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 171)
)
altMemoryPressureDeactivated.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altMemoryPressureDeactivated.setStatus(
        ""
    )

altMemoryPressureCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 172)
)
altMemoryPressureCrossed.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altMemoryPressureCrossed.setStatus(
        ""
    )

altMemoryPressureCrossedBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 173)
)
altMemoryPressureCrossedBack.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altMemoryPressureCrossedBack.setStatus(
        ""
    )

dataTableCriticalCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 174)
)
dataTableCriticalCapacity.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    dataTableCriticalCapacity.setStatus(
        ""
    )

dataTableFullCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 175)
)
dataTableFullCapacity.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    dataTableFullCapacity.setStatus(
        ""
    )

dataTableNormalCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 176)
)
dataTableNormalCapacity.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    dataTableNormalCapacity.setStatus(
        ""
    )

altSwfilterGWFailurePIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 180)
)
altSwfilterGWFailurePIP.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwfilterGWFailurePIP.setStatus(
        ""
    )

altSwfilterGWFailureDest = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 181)
)
altSwfilterGWFailureDest.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwfilterGWFailureDest.setStatus(
        ""
    )

dosAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 182)
)
dosAttackTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    dosAttackTrap.setStatus(
        ""
    )

altSwTputAverageCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 183)
)
altSwTputAverageCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTputAverageCef.setStatus(
        ""
    )

apmServiceActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 184)
)
apmServiceActivationFailed.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    apmServiceActivationFailed.setStatus(
        ""
    )

apmServiceActivationSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 185)
)
apmServiceActivationSucceeded.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    apmServiceActivationSucceeded.setStatus(
        ""
    )

highSpCpuTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 186)
)
highSpCpuTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highSpCpuTrapCef.setStatus(
        ""
    )

highSpCpuClearTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 187)
)
highSpCpuClearTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highSpCpuClearTrapCef.setStatus(
        ""
    )

highMpCpuTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 188)
)
highMpCpuTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highMpCpuTrapCef.setStatus(
        ""
    )

highMpCpuClearTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 189)
)
highMpCpuClearTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highMpCpuClearTrapCef.setStatus(
        ""
    )

highProxTableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 190)
)
highProxTableTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highProxTableTrap.setStatus(
        ""
    )

fullProxTableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 191)
)
fullProxTableTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    fullProxTableTrap.setStatus(
        ""
    )

lowProxTableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 192)
)
lowProxTableTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    lowProxTableTrap.setStatus(
        ""
    )

rsEnhMaxBwTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 194)
)
rsEnhMaxBwTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    rsEnhMaxBwTrap.setStatus(
        ""
    )

crossBwThresholdTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 195)
)
crossBwThresholdTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossBwThresholdTrapCef.setStatus(
        ""
    )

crossPpsThresholdTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 196)
)
crossPpsThresholdTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossPpsThresholdTrapCef.setStatus(
        ""
    )

crossCpsThresholdTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 197)
)
crossCpsThresholdTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossCpsThresholdTrapCef.setStatus(
        ""
    )

crossCecThresholdTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 198)
)
crossCecThresholdTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossCecThresholdTrapCef.setStatus(
        ""
    )

crossBwRatioTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 199)
)
crossBwRatioTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossBwRatioTrapCef.setStatus(
        ""
    )

crossPpsRatioTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 200)
)
crossPpsRatioTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossPpsRatioTrapCef.setStatus(
        ""
    )

crossCpsRatioTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 201)
)
crossCpsRatioTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossCpsRatioTrapCef.setStatus(
        ""
    )

crossCecRatioTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 202)
)
crossCecRatioTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    crossCecRatioTrapCef.setStatus(
        ""
    )

currentStatusTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 203)
)
currentStatusTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    currentStatusTrapCef.setStatus(
        ""
    )

highLatencyThresholdTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 204)
)
highLatencyThresholdTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highLatencyThresholdTrapCef.setStatus(
        ""
    )

highLatencyTrapCef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 205)
)
highLatencyTrapCef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    highLatencyTrapCef.setStatus(
        ""
    )

altMemoryHandleRecommendation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 208)
)
altMemoryHandleRecommendation.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altMemoryHandleRecommendation.setStatus(
        ""
    )

altSwSlbEnhVirtServerSpecificServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 209)
)
altSwSlbEnhVirtServerSpecificServiceUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIpAddress"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServApplicationType"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServiceVirtPort"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhVirtServerSpecificServiceUp.setStatus(
        ""
    )

altSwSlbEnhVirtServerSpecificServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 210)
)
altSwSlbEnhVirtServerSpecificServiceDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServerIpAddress"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServApplicationType"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhVirtServiceVirtPort"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhVirtServerSpecificServiceDown.setStatus(
        ""
    )

altSwdynamicCertCacheFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 211)
)
altSwdynamicCertCacheFull.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwdynamicCertCacheFull.setStatus(
        ""
    )

altSwBulkRevertApply = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 212)
)
altSwBulkRevertApply.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwBulkRevertApply.setStatus(
        ""
    )

altSwSessSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 213)
)
altSwSessSyncTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSessSyncTrap.setStatus(
        ""
    )

altSwSpCpuPressureActivatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 214)
)
altSwSpCpuPressureActivatedTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSpCpuPressureActivatedTrap.setStatus(
        ""
    )

altSwSpCpuPressureDeactivatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 215)
)
altSwSpCpuPressureDeactivatedTrap.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSpCpuPressureDeactivatedTrap.setStatus(
        ""
    )

altSwNtpTimezoneUndef = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 216)
)
altSwNtpTimezoneUndef.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwNtpTimezoneUndef.setStatus(
        ""
    )

altSwNtpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 217)
)
altSwNtpError.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwNtpError.setStatus(
        ""
    )

altSwSlbEnhRealServerOperDisGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 218)
)
altSwSlbEnhRealServerOperDisGroup.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupIndex"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerOperDisGroup.setStatus(
        ""
    )

altSwSlbEnhRealServerOperEnaGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 219)
)
altSwSlbEnhRealServerOperEnaGroup.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEnhGroupIndex"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbEnhRealServerOperEnaGroup.setStatus(
        ""
    )

altSwOscpServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 220)
)
altSwOscpServerDown.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwOscpServerDown.setStatus(
        ""
    )

altSwOscpServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 221)
)
altSwOscpServerUp.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("CHEETAH-TRAP-MIB", "altSwTrapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwOscpServerUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHEETAH-TRAP-MIB",
    **{"altTraps": altTraps,
       "altSwPrimaryPowerSupplyFailure": altSwPrimaryPowerSupplyFailure,
       "altSwDefGwUp": altSwDefGwUp,
       "altSwDefGwDown": altSwDefGwDown,
       "altSwDefGwInService": altSwDefGwInService,
       "altSwDefGwNotInService": altSwDefGwNotInService,
       "altSwSlbRealServerUp": altSwSlbRealServerUp,
       "altSwSlbRealServerDown": altSwSlbRealServerDown,
       "altSwSlbRealServerMaxConnReached": altSwSlbRealServerMaxConnReached,
       "altSwSlbBkupRealServerAct": altSwSlbBkupRealServerAct,
       "altSwSlbBkupRealServerDeact": altSwSlbBkupRealServerDeact,
       "altSwSlbBkupRealServerActOverflow": altSwSlbBkupRealServerActOverflow,
       "altSwSlbBkupRealServerDeactOverflow": altSwSlbBkupRealServerDeactOverflow,
       "altSwfltFilterFired": altSwfltFilterFired,
       "altSwSlbRealServerServiceUp": altSwSlbRealServerServiceUp,
       "altSwSlbRealServerServiceDown": altSwSlbRealServerServiceDown,
       "altSwVrrpNewMaster": altSwVrrpNewMaster,
       "altSwVrrpNewBackup": altSwVrrpNewBackup,
       "altSwVrrpAuthFailure": altSwVrrpAuthFailure,
       "altSwLoginFailure": altSwLoginFailure,
       "altSwSlbSynAttack": altSwSlbSynAttack,
       "altSwTcpHoldDown": altSwTcpHoldDown,
       "altSwTempExceedThreshold": altSwTempExceedThreshold,
       "altSwSlbSessAttack": altSwSlbSessAttack,
       "altSwFanFailure": altSwFanFailure,
       "altSwSlbVirtServerServicesUp": altSwSlbVirtServerServicesUp,
       "altSwSlbVirtServerServicesDown": altSwSlbVirtServerServicesDown,
       "altSwSlbRealGroupAdvhlUp": altSwSlbRealGroupAdvhlUp,
       "altSwSlbRealGroupAdvhlDown": altSwSlbRealGroupAdvhlDown,
       "altSwSlbBkupGroupAct": altSwSlbBkupGroupAct,
       "altSwSlbBkupGroupDeact": altSwSlbBkupGroupDeact,
       "altSwSlbRemoteRealServerUp": altSwSlbRemoteRealServerUp,
       "altSwSlbRemoteRealServerDown": altSwSlbRemoteRealServerDown,
       "altSwSlbRealServerOperDis": altSwSlbRealServerOperDis,
       "altSwSlbRealServerOperEna": altSwSlbRealServerOperEna,
       "altSwIfcVlanDown": altSwIfcVlanDown,
       "altSwPortVlanDown": altSwPortVlanDown,
       "altSwIfcVlanUp": altSwIfcVlanUp,
       "altSwPortVlanUp": altSwPortVlanUp,
       "altSwBulkApply": altSwBulkApply,
       "altSwDeviceTemperatureNormal": altSwDeviceTemperatureNormal,
       "altSwDeviceTemperatureHigh": altSwDeviceTemperatureHigh,
       "altSwDeviceTemperatureCritical": altSwDeviceTemperatureCritical,
       "altSwDualPowerSupplyProblem": altSwDualPowerSupplyProblem,
       "altSwDualPowerSupplyUp": altSwDualPowerSupplyUp,
       "altSwTputReachThreshold": altSwTputReachThreshold,
       "altSwTputExceedLimit": altSwTputExceedLimit,
       "altSwcompCardNotAvail": altSwcompCardNotAvail,
       "altSwsslCardNotAvail": altSwsslCardNotAvail,
       "altSwloginSsh": altSwloginSsh,
       "altSwtmpCecLmtStop": altSwtmpCecLmtStop,
       "altSwcacheLimitShortSpace": altSwcacheLimitShortSpace,
       "altSwcacheReache80": altSwcacheReache80,
       "altSwcacheBelow80": altSwcacheBelow80,
       "altSwlogDiskSpace": altSwlogDiskSpace,
       "altSwtmpCecLimitMemShort": altSwtmpCecLimitMemShort,
       "altSwconfProtectionActive": altSwconfProtectionActive,
       "altSwkeyLoadErr": altSwkeyLoadErr,
       "altSwcompCardDetect": altSwcompCardDetect,
       "altSwfipsEngineNotRunning": altSwfipsEngineNotRunning,
       "altSwsslAclTypeDetected": altSwsslAclTypeDetected,
       "altSwocspSvrErr": altSwocspSvrErr,
       "altSwocspRespVerifyErr": altSwocspRespVerifyErr,
       "altSwoscpQueryErr": altSwoscpQueryErr,
       "altSwcertRevokedID": altSwcertRevokedID,
       "altSwerrCrlUpdTime": altSwerrCrlUpdTime,
       "altSwcrlExp": altSwcrlExp,
       "altSwcertExpDays": altSwcertExpDays,
       "altSwcompDisDueMemLimit": altSwcompDisDueMemLimit,
       "altSwcompEnaAfterMemLimit": altSwcompEnaAfterMemLimit,
       "altSwcompLicenseOverflow": altSwcompLicenseOverflow,
       "altSwsslCpsLicenseOverflow": altSwsslCpsLicenseOverflow,
       "altSwtslValidationFailure": altSwtslValidationFailure,
       "altSwtslOcspCertRevoked": altSwtslOcspCertRevoked,
       "altSwtslOcspCertUnknown": altSwtslOcspCertUnknown,
       "altSwtslSignatureNodeMissing": altSwtslSignatureNodeMissing,
       "altSwtslSignatureValidFailure": altSwtslSignatureValidFailure,
       "altSwtslNewSeqNumLessThanExisting": altSwtslNewSeqNumLessThanExisting,
       "altSwtslNextUpdateInThePast": altSwtslNextUpdateInThePast,
       "altSwtslNextUpdateOver30Days": altSwtslNextUpdateOver30Days,
       "altSwtslOcspTimingErrorField": altSwtslOcspTimingErrorField,
       "altSwtslInvalidOcspTimingErrorField": altSwtslInvalidOcspTimingErrorField,
       "altSwtslFetcherFetchingError": altSwtslFetcherFetchingError,
       "altSwtslFetcherSignatureError": altSwtslFetcherSignatureError,
       "altSwtslFetcherOcspError": altSwtslFetcherOcspError,
       "altSwtslFetcherXmlParsingError": altSwtslFetcherXmlParsingError,
       "altSwtslFetcherIdenticalSeqNum": altSwtslFetcherIdenticalSeqNum,
       "altSwtslFetchingDone": altSwtslFetchingDone,
       "altSwsslCpsLicenseWatermark": altSwsslCpsLicenseWatermark,
       "altSwcompressionLicensewatermark": altSwcompressionLicensewatermark,
       "altSwpipAllocFailed": altSwpipAllocFailed,
       "altAxUpdateFailed": altAxUpdateFailed,
       "altSwVrrpVsrNewMaster": altSwVrrpVsrNewMaster,
       "altSwVrrpVsrNewBackup": altSwVrrpVsrNewBackup,
       "vadcStateChange": vadcStateChange,
       "vadcStateVrrpMaster": vadcStateVrrpMaster,
       "vadcStateVrrpBackup": vadcStateVrrpBackup,
       "dnssecNotify": dnssecNotify,
       "agTftpActionStatus": agTftpActionStatus,
       "altSwSlbEnhRealGroupAdvhlUp": altSwSlbEnhRealGroupAdvhlUp,
       "altSwSlbEnhRealGroupAdvhlDown": altSwSlbEnhRealGroupAdvhlDown,
       "altSwSlbEnhBkupGroupAct": altSwSlbEnhBkupGroupAct,
       "altSwSlbEnhBkupGroupDeact": altSwSlbEnhBkupGroupDeact,
       "altSwSlbEnhVirtServerServicesUp": altSwSlbEnhVirtServerServicesUp,
       "altSwSlbEnhVirtServerServicesDown": altSwSlbEnhVirtServerServicesDown,
       "altSwTputAverage": altSwTputAverage,
       "altSwSlbEnhRealServerDown": altSwSlbEnhRealServerDown,
       "altSwSlbEnhRealServerMaxConnReached": altSwSlbEnhRealServerMaxConnReached,
       "altSwSlbEnhBkupRealServerAct": altSwSlbEnhBkupRealServerAct,
       "altSwSlbEnhBkupRealServerDeact": altSwSlbEnhBkupRealServerDeact,
       "altSwSlbEnhBkupRealServerActOverflow": altSwSlbEnhBkupRealServerActOverflow,
       "altSwSlbEnhBkupRealServerDeactOverflow": altSwSlbEnhBkupRealServerDeactOverflow,
       "altSwSlbEnhRealServerServiceUp": altSwSlbEnhRealServerServiceUp,
       "altSwSlbEnhRealServerServiceDown": altSwSlbEnhRealServerServiceDown,
       "altSwSlbEnhRemoteRealServerUp": altSwSlbEnhRemoteRealServerUp,
       "altSwSlbEnhRemoteRealServerDown": altSwSlbEnhRemoteRealServerDown,
       "altSwSlbEnhRealServerOperDis": altSwSlbEnhRealServerOperDis,
       "altSwSlbEnhRealServerOperEna": altSwSlbEnhRealServerOperEna,
       "vadcDelete": vadcDelete,
       "vadcCapUnit": vadcCapUnit,
       "vadcLicGlobal": vadcLicGlobal,
       "vadcThrupt": vadcThrupt,
       "vadcSsl": vadcSsl,
       "vadcComp": vadcComp,
       "altAPMLicenseWatermark": altAPMLicenseWatermark,
       "altAPMLicenseOverflow": altAPMLicenseOverflow,
       "altSwSlbEnhRealServerUp": altSwSlbEnhRealServerUp,
       "altSwVrrpNewInit": altSwVrrpNewInit,
       "altSwVrrpVsrNewInit": altSwVrrpVsrNewInit,
       "altSwVrrpNewHoldoff": altSwVrrpNewHoldoff,
       "altSwVrrpVsrNewHoldoff": altSwVrrpVsrNewHoldoff,
       "altWAFLicenseWatermark": altWAFLicenseWatermark,
       "altWAFLicenseOverflow": altWAFLicenseOverflow,
       "altHAGroupNewInitTrap": altHAGroupNewInitTrap,
       "altHAGroupNewHoldoffTrap": altHAGroupNewHoldoffTrap,
       "altHAGroupNewMasterTrap": altHAGroupNewMasterTrap,
       "altHAGroupNewBackupTrap": altHAGroupNewBackupTrap,
       "virtHighSpCpuTrap": virtHighSpCpuTrap,
       "virtHighSpCpuClearTrap": virtHighSpCpuClearTrap,
       "virtHighMpCpuTrap": virtHighMpCpuTrap,
       "virtHighMpCpuClearTrap": virtHighMpCpuClearTrap,
       "appwallUpTrap": appwallUpTrap,
       "appwallDownTrap": appwallDownTrap,
       "altMemoryPressureActivated": altMemoryPressureActivated,
       "altMemoryPressureDeactivated": altMemoryPressureDeactivated,
       "altMemoryPressureCrossed": altMemoryPressureCrossed,
       "altMemoryPressureCrossedBack": altMemoryPressureCrossedBack,
       "dataTableCriticalCapacity": dataTableCriticalCapacity,
       "dataTableFullCapacity": dataTableFullCapacity,
       "dataTableNormalCapacity": dataTableNormalCapacity,
       "altSwfilterGWFailurePIP": altSwfilterGWFailurePIP,
       "altSwfilterGWFailureDest": altSwfilterGWFailureDest,
       "dosAttackTrap": dosAttackTrap,
       "altSwTputAverageCef": altSwTputAverageCef,
       "apmServiceActivationFailed": apmServiceActivationFailed,
       "apmServiceActivationSucceeded": apmServiceActivationSucceeded,
       "highSpCpuTrapCef": highSpCpuTrapCef,
       "highSpCpuClearTrapCef": highSpCpuClearTrapCef,
       "highMpCpuTrapCef": highMpCpuTrapCef,
       "highMpCpuClearTrapCef": highMpCpuClearTrapCef,
       "highProxTableTrap": highProxTableTrap,
       "fullProxTableTrap": fullProxTableTrap,
       "lowProxTableTrap": lowProxTableTrap,
       "rsEnhMaxBwTrap": rsEnhMaxBwTrap,
       "crossBwThresholdTrapCef": crossBwThresholdTrapCef,
       "crossPpsThresholdTrapCef": crossPpsThresholdTrapCef,
       "crossCpsThresholdTrapCef": crossCpsThresholdTrapCef,
       "crossCecThresholdTrapCef": crossCecThresholdTrapCef,
       "crossBwRatioTrapCef": crossBwRatioTrapCef,
       "crossPpsRatioTrapCef": crossPpsRatioTrapCef,
       "crossCpsRatioTrapCef": crossCpsRatioTrapCef,
       "crossCecRatioTrapCef": crossCecRatioTrapCef,
       "currentStatusTrapCef": currentStatusTrapCef,
       "highLatencyThresholdTrapCef": highLatencyThresholdTrapCef,
       "highLatencyTrapCef": highLatencyTrapCef,
       "altMemoryHandleRecommendation": altMemoryHandleRecommendation,
       "altSwSlbEnhVirtServerSpecificServiceUp": altSwSlbEnhVirtServerSpecificServiceUp,
       "altSwSlbEnhVirtServerSpecificServiceDown": altSwSlbEnhVirtServerSpecificServiceDown,
       "altSwdynamicCertCacheFull": altSwdynamicCertCacheFull,
       "altSwBulkRevertApply": altSwBulkRevertApply,
       "altSwSessSyncTrap": altSwSessSyncTrap,
       "altSwSpCpuPressureActivatedTrap": altSwSpCpuPressureActivatedTrap,
       "altSwSpCpuPressureDeactivatedTrap": altSwSpCpuPressureDeactivatedTrap,
       "altSwNtpTimezoneUndef": altSwNtpTimezoneUndef,
       "altSwNtpError": altSwNtpError,
       "altSwSlbEnhRealServerOperDisGroup": altSwSlbEnhRealServerOperDisGroup,
       "altSwSlbEnhRealServerOperEnaGroup": altSwSlbEnhRealServerOperEnaGroup,
       "altSwOscpServerDown": altSwOscpServerDown,
       "altSwOscpServerUp": altSwOscpServerUp,
       "altSwTrapDisplayString": altSwTrapDisplayString,
       "altSwTrapRate": altSwTrapRate,
       "altSwTrapSeverity": altSwTrapSeverity}
)
