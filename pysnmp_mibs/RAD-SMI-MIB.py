# SNMP MIB module (RAD-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-SMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:19 2025
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

rad = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadTokenRing_ObjectIdentity = ObjectIdentity
radTokenRing = _RadTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 1)
)
if mibBuilder.loadTexts:
    radTokenRing.setStatus("current")
_RadFddi_ObjectIdentity = ObjectIdentity
radFddi = _RadFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 2)
)
if mibBuilder.loadTexts:
    radFddi.setStatus("current")
_RadWan_ObjectIdentity = ObjectIdentity
radWan = _RadWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3)
)
if mibBuilder.loadTexts:
    radWan.setStatus("current")
_WanGen_ObjectIdentity = ObjectIdentity
wanGen = _WanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1)
)
_DiverseIfWanGen_ObjectIdentity = ObjectIdentity
diverseIfWanGen = _DiverseIfWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6)
)
_RadBridges_ObjectIdentity = ObjectIdentity
radBridges = _RadBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4)
)
if mibBuilder.loadTexts:
    radBridges.setStatus("current")
_RadConverters_ObjectIdentity = ObjectIdentity
radConverters = _RadConverters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 5)
)
if mibBuilder.loadTexts:
    radConverters.setStatus("current")
_RadGen_ObjectIdentity = ObjectIdentity
radGen = _RadGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6)
)
if mibBuilder.loadTexts:
    radGen.setStatus("current")
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1)
)
_RadSysWan_ObjectIdentity = ObjectIdentity
radSysWan = _RadSysWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3)
)
_RadSysWanEvents_ObjectIdentity = ObjectIdentity
radSysWanEvents = _RadSysWanEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0)
)
if mibBuilder.loadTexts:
    radSysWanEvents.setStatus("current")
_RadSysPS_ObjectIdentity = ObjectIdentity
radSysPS = _RadSysPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8)
)
_RadSysAtm_ObjectIdentity = ObjectIdentity
radSysAtm = _RadSysAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12)
)
_RadSysAtmEvents_ObjectIdentity = ObjectIdentity
radSysAtmEvents = _RadSysAtmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0)
)
if mibBuilder.loadTexts:
    radSysAtmEvents.setStatus("current")
_RadSecurity_ObjectIdentity = ObjectIdentity
radSecurity = _RadSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14)
)
_Agnt_ObjectIdentity = ObjectIdentity
agnt = _Agnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2)
)
_FileTransfer_ObjectIdentity = ObjectIdentity
fileTransfer = _FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12)
)
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3)
)
_RadTransport_ObjectIdentity = ObjectIdentity
radTransport = _RadTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 4)
)
_FmObjects_ObjectIdentity = ObjectIdentity
fmObjects = _FmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 5)
)
_RadStkHub_ObjectIdentity = ObjectIdentity
radStkHub = _RadStkHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 7)
)
if mibBuilder.loadTexts:
    radStkHub.setStatus("current")
_RadPS_ObjectIdentity = ObjectIdentity
radPS = _RadPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 8)
)
if mibBuilder.loadTexts:
    radPS.setStatus("current")
_RadEthRptr_ObjectIdentity = ObjectIdentity
radEthRptr = _RadEthRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 9)
)
if mibBuilder.loadTexts:
    radEthRptr.setStatus("current")
_RadMpls_ObjectIdentity = ObjectIdentity
radMpls = _RadMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 10)
)
if mibBuilder.loadTexts:
    radMpls.setStatus("current")
_RadRouter_ObjectIdentity = ObjectIdentity
radRouter = _RadRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11)
)
if mibBuilder.loadTexts:
    radRouter.setStatus("current")
_RtrBridge_ObjectIdentity = ObjectIdentity
rtrBridge = _RtrBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 7)
)
if mibBuilder.loadTexts:
    rtrBridge.setStatus("current")
_RadAtm_ObjectIdentity = ObjectIdentity
radAtm = _RadAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12)
)
if mibBuilder.loadTexts:
    radAtm.setStatus("current")
_RadPw_ObjectIdentity = ObjectIdentity
radPw = _RadPw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 14)
)
if mibBuilder.loadTexts:
    radPw.setStatus("current")
_RadEMS_ObjectIdentity = ObjectIdentity
radEMS = _RadEMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 15)
)
if mibBuilder.loadTexts:
    radEMS.setStatus("current")
_RadAaw_ObjectIdentity = ObjectIdentity
radAaw = _RadAaw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 16)
)
if mibBuilder.loadTexts:
    radAaw.setStatus("current")
_RadExperimental_ObjectIdentity = ObjectIdentity
radExperimental = _RadExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20)
)
if mibBuilder.loadTexts:
    radExperimental.setStatus("current")
_RadSpecificDevices_ObjectIdentity = ObjectIdentity
radSpecificDevices = _RadSpecificDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 40)
)
if mibBuilder.loadTexts:
    radSpecificDevices.setStatus("current")
_RadTextualConventions_ObjectIdentity = ObjectIdentity
radTextualConventions = _RadTextualConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 100)
)
if mibBuilder.loadTexts:
    radTextualConventions.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-SMI-MIB",
    **{"rad": rad,
       "radTokenRing": radTokenRing,
       "radFddi": radFddi,
       "radWan": radWan,
       "wanGen": wanGen,
       "diverseIfWanGen": diverseIfWanGen,
       "radBridges": radBridges,
       "radConverters": radConverters,
       "radGen": radGen,
       "systems": systems,
       "radSysWan": radSysWan,
       "radSysWanEvents": radSysWanEvents,
       "radSysPS": radSysPS,
       "radSysAtm": radSysAtm,
       "radSysAtmEvents": radSysAtmEvents,
       "radSecurity": radSecurity,
       "agnt": agnt,
       "fileTransfer": fileTransfer,
       "services": services,
       "radTransport": radTransport,
       "fmObjects": fmObjects,
       "radStkHub": radStkHub,
       "radPS": radPS,
       "radEthRptr": radEthRptr,
       "radMpls": radMpls,
       "radRouter": radRouter,
       "rtrBridge": rtrBridge,
       "radAtm": radAtm,
       "radPw": radPw,
       "radEMS": radEMS,
       "radAaw": radAaw,
       "radExperimental": radExperimental,
       "radSpecificDevices": radSpecificDevices,
       "radTextualConventions": radTextualConventions}
)
