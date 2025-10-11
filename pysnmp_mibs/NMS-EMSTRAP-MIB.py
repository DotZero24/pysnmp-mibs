# SNMP MIB module (NMS-EMSTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bdcom/NMS-EMSTRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:05:04 2025
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

(nmsWorkGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsWorkGroup")

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

eMSMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EMSTrapObject_ObjectIdentity = ObjectIdentity
eMSTrapObject = _EMSTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1)
)
_EMSTrap_ObjectIdentity = ObjectIdentity
eMSTrap = _EMSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1)
)
_EMSTrapInfo_ObjectIdentity = ObjectIdentity
eMSTrapInfo = _EMSTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3)
)
_EMSProcess_Type = Integer32
_EMSProcess_Object = MibScalar
eMSProcess = _EMSProcess_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 1),
    _EMSProcess_Type()
)
eMSProcess.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSProcess.setStatus("current")
_EMSProcessLimit_Type = Integer32
_EMSProcessLimit_Object = MibScalar
eMSProcessLimit = _EMSProcessLimit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 2),
    _EMSProcessLimit_Type()
)
eMSProcessLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSProcessLimit.setStatus("current")
if mibBuilder.loadTexts:
    eMSProcessLimit.setUnits("%")
_EMSCPURatio_Type = Integer32
_EMSCPURatio_Object = MibScalar
eMSCPURatio = _EMSCPURatio_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 3),
    _EMSCPURatio_Type()
)
eMSCPURatio.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSCPURatio.setStatus("current")
if mibBuilder.loadTexts:
    eMSCPURatio.setUnits("%")
_EMSCPURatioLimit_Type = Integer32
_EMSCPURatioLimit_Object = MibScalar
eMSCPURatioLimit = _EMSCPURatioLimit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 4),
    _EMSCPURatioLimit_Type()
)
eMSCPURatioLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSCPURatioLimit.setStatus("current")
if mibBuilder.loadTexts:
    eMSCPURatioLimit.setUnits("%")
_EMSMemorySize_Type = Integer32
_EMSMemorySize_Object = MibScalar
eMSMemorySize = _EMSMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 5),
    _EMSMemorySize_Type()
)
eMSMemorySize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    eMSMemorySize.setUnits("MB")
_EMSMemoryUsed_Type = Integer32
_EMSMemoryUsed_Object = MibScalar
eMSMemoryUsed = _EMSMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 6),
    _EMSMemoryUsed_Type()
)
eMSMemoryUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    eMSMemoryUsed.setUnits("MB")
_EMSMemoryRatioLimit_Type = Integer32
_EMSMemoryRatioLimit_Object = MibScalar
eMSMemoryRatioLimit = _EMSMemoryRatioLimit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 7),
    _EMSMemoryRatioLimit_Type()
)
eMSMemoryRatioLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSMemoryRatioLimit.setStatus("current")
if mibBuilder.loadTexts:
    eMSMemoryRatioLimit.setUnits("%")
_EMSDiskSize_Type = Integer32
_EMSDiskSize_Object = MibScalar
eMSDiskSize = _EMSDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 8),
    _EMSDiskSize_Type()
)
eMSDiskSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    eMSDiskSize.setUnits("MB")
_EMSDiskUsed_Type = Integer32
_EMSDiskUsed_Object = MibScalar
eMSDiskUsed = _EMSDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 9),
    _EMSDiskUsed_Type()
)
eMSDiskUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSDiskUsed.setStatus("current")
if mibBuilder.loadTexts:
    eMSDiskUsed.setUnits("MB")
_EMSDiskRatioLimit_Type = Integer32
_EMSDiskRatioLimit_Object = MibScalar
eMSDiskRatioLimit = _EMSDiskRatioLimit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 10),
    _EMSDiskRatioLimit_Type()
)
eMSDiskRatioLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSDiskRatioLimit.setStatus("current")
if mibBuilder.loadTexts:
    eMSDiskRatioLimit.setUnits("%")
_EMSDataSize_Type = Integer32
_EMSDataSize_Object = MibScalar
eMSDataSize = _EMSDataSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 11),
    _EMSDataSize_Type()
)
eMSDataSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSDataSize.setStatus("current")
if mibBuilder.loadTexts:
    eMSDataSize.setUnits("MB")
_EMSDataUsed_Type = Integer32
_EMSDataUsed_Object = MibScalar
eMSDataUsed = _EMSDataUsed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 12),
    _EMSDataUsed_Type()
)
eMSDataUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSDataUsed.setStatus("current")
if mibBuilder.loadTexts:
    eMSDataUsed.setUnits("MB")
_EMSDataRatioLimit_Type = Integer32
_EMSDataRatioLimit_Object = MibScalar
eMSDataRatioLimit = _EMSDataRatioLimit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 13),
    _EMSDataRatioLimit_Type()
)
eMSDataRatioLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSDataRatioLimit.setStatus("current")
if mibBuilder.loadTexts:
    eMSDataRatioLimit.setUnits("%")
_EMSLicense_Type = Integer32
_EMSLicense_Object = MibScalar
eMSLicense = _EMSLicense_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 14),
    _EMSLicense_Type()
)
eMSLicense.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSLicense.setStatus("current")
_EMSLicenseLimit_Type = Integer32
_EMSLicenseLimit_Object = MibScalar
eMSLicenseLimit = _EMSLicenseLimit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 3, 15),
    _EMSLicenseLimit_Type()
)
eMSLicenseLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eMSLicenseLimit.setStatus("current")

# Managed Objects groups


# Notification objects

eMSProcessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1, 1)
)
eMSProcessTrap.setObjects(
      *(("NMS-EMSTRAP-MIB", "eMSProcess"),
        ("NMS-EMSTRAP-MIB", "eMSProcessLimit"))
)
if mibBuilder.loadTexts:
    eMSProcessTrap.setStatus(
        "current"
    )

eMSCPUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1, 2)
)
eMSCPUTrap.setObjects(
      *(("NMS-EMSTRAP-MIB", "eMSCPURatio"),
        ("NMS-EMSTRAP-MIB", "eMSCPURatioLimit"))
)
if mibBuilder.loadTexts:
    eMSCPUTrap.setStatus(
        "current"
    )

eMSMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1, 3)
)
eMSMemoryTrap.setObjects(
      *(("NMS-EMSTRAP-MIB", "eMSMemorySize"),
        ("NMS-EMSTRAP-MIB", "eMSMemoryUsed"),
        ("NMS-EMSTRAP-MIB", "eMSMemoryRatioLimit"))
)
if mibBuilder.loadTexts:
    eMSMemoryTrap.setStatus(
        "current"
    )

eMSDiskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1, 4)
)
eMSDiskTrap.setObjects(
      *(("NMS-EMSTRAP-MIB", "eMSDiskSize"),
        ("NMS-EMSTRAP-MIB", "eMSDiskUsed"),
        ("NMS-EMSTRAP-MIB", "eMSDiskRatioLimit"))
)
if mibBuilder.loadTexts:
    eMSDiskTrap.setStatus(
        "current"
    )

eMSDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1, 5)
)
eMSDataTrap.setObjects(
      *(("NMS-EMSTRAP-MIB", "eMSDataSize"),
        ("NMS-EMSTRAP-MIB", "eMSDataUsed"),
        ("NMS-EMSTRAP-MIB", "eMSDataRatioLimit"))
)
if mibBuilder.loadTexts:
    eMSDataTrap.setStatus(
        "current"
    )

eMSLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 20, 1, 1, 1, 6)
)
eMSLicenseTrap.setObjects(
      *(("NMS-EMSTRAP-MIB", "eMSLicense"),
        ("NMS-EMSTRAP-MIB", "eMSLicenseLimit"))
)
if mibBuilder.loadTexts:
    eMSLicenseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EMSTRAP-MIB",
    **{"eMSMibModule": eMSMibModule,
       "eMSTrapObject": eMSTrapObject,
       "eMSTrap": eMSTrap,
       "eMSProcessTrap": eMSProcessTrap,
       "eMSCPUTrap": eMSCPUTrap,
       "eMSMemoryTrap": eMSMemoryTrap,
       "eMSDiskTrap": eMSDiskTrap,
       "eMSDataTrap": eMSDataTrap,
       "eMSLicenseTrap": eMSLicenseTrap,
       "eMSTrapInfo": eMSTrapInfo,
       "eMSProcess": eMSProcess,
       "eMSProcessLimit": eMSProcessLimit,
       "eMSCPURatio": eMSCPURatio,
       "eMSCPURatioLimit": eMSCPURatioLimit,
       "eMSMemorySize": eMSMemorySize,
       "eMSMemoryUsed": eMSMemoryUsed,
       "eMSMemoryRatioLimit": eMSMemoryRatioLimit,
       "eMSDiskSize": eMSDiskSize,
       "eMSDiskUsed": eMSDiskUsed,
       "eMSDiskRatioLimit": eMSDiskRatioLimit,
       "eMSDataSize": eMSDataSize,
       "eMSDataUsed": eMSDataUsed,
       "eMSDataRatioLimit": eMSDataRatioLimit,
       "eMSLicense": eMSLicense,
       "eMSLicenseLimit": eMSLicenseLimit}
)
