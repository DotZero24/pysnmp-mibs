# SNMP MIB module (HPOvSam-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPOvSam-MIB-V1
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:09 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpStorageAssistant_ObjectIdentity = ObjectIdentity
hpStorageAssistant = _HpStorageAssistant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 27)
)
_HpSanManager_ObjectIdentity = ObjectIdentity
hpSanManager = _HpSanManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3)
)
_HpSanManagerTraps_ObjectIdentity = ObjectIdentity
hpSanManagerTraps = _HpSanManagerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 0)
)
_HpSanManagerModules_ObjectIdentity = ObjectIdentity
hpSanManagerModules = _HpSanManagerModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1)
)
_HpSanManagerMibModule_ObjectIdentity = ObjectIdentity
hpSanManagerMibModule = _HpSanManagerMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1)
)
_MibModuleEventVars_ObjectIdentity = ObjectIdentity
mibModuleEventVars = _MibModuleEventVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1)
)


class _SeverityLevel_Type(Integer32):
    """Custom type severityLevel based on Integer32"""
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
        *(("informational", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_SeverityLevel_Type.__name__ = "Integer32"
_SeverityLevel_Object = MibScalar
severityLevel = _SeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 1),
    _SeverityLevel_Type()
)
severityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityLevel.setStatus("mandatory")
_Category_Type = DisplayString
_Category_Object = MibScalar
category = _Category_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 2),
    _Category_Type()
)
category.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    category.setStatus("mandatory")
_Id_Type = Integer32
_Id_Object = MibScalar
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 3),
    _Id_Type()
)
id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id.setStatus("mandatory")
_MsgString_Type = DisplayString
_MsgString_Object = MibScalar
msgString = _MsgString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 4),
    _MsgString_Type()
)
msgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgString.setStatus("mandatory")
_ContactName_Type = DisplayString
_ContactName_Object = MibScalar
contactName = _ContactName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 5),
    _ContactName_Type()
)
contactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactName.setStatus("mandatory")
_ContactEmail_Type = DisplayString
_ContactEmail_Object = MibScalar
contactEmail = _ContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 6),
    _ContactEmail_Type()
)
contactEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactEmail.setStatus("mandatory")
_ContactHomePhone_Type = DisplayString
_ContactHomePhone_Object = MibScalar
contactHomePhone = _ContactHomePhone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 7),
    _ContactHomePhone_Type()
)
contactHomePhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactHomePhone.setStatus("mandatory")
_ContactWorkPhone_Type = DisplayString
_ContactWorkPhone_Object = MibScalar
contactWorkPhone = _ContactWorkPhone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 8),
    _ContactWorkPhone_Type()
)
contactWorkPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactWorkPhone.setStatus("mandatory")
_ContactPager_Type = DisplayString
_ContactPager_Object = MibScalar
contactPager = _ContactPager_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 9),
    _ContactPager_Type()
)
contactPager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactPager.setStatus("mandatory")
_ContactFax_Type = DisplayString
_ContactFax_Object = MibScalar
contactFax = _ContactFax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 10),
    _ContactFax_Type()
)
contactFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactFax.setStatus("mandatory")
_SourceName_Type = DisplayString
_SourceName_Object = MibScalar
sourceName = _SourceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 11),
    _SourceName_Type()
)
sourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceName.setStatus("mandatory")
_UniqueId_Type = DisplayString
_UniqueId_Object = MibScalar
uniqueId = _UniqueId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 12),
    _UniqueId_Type()
)
uniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniqueId.setStatus("mandatory")
_VendorId_Type = DisplayString
_VendorId_Object = MibScalar
vendorId = _VendorId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 13),
    _VendorId_Type()
)
vendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorId.setStatus("mandatory")
_ProdId_Type = DisplayString
_ProdId_Object = MibScalar
prodId = _ProdId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 14),
    _ProdId_Type()
)
prodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodId.setStatus("mandatory")
_ProdRev_Type = DisplayString
_ProdRev_Object = MibScalar
prodRev = _ProdRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 15),
    _ProdRev_Type()
)
prodRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodRev.setStatus("mandatory")
_SerialNo_Type = DisplayString
_SerialNo_Object = MibScalar
serialNo = _SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 16),
    _SerialNo_Type()
)
serialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNo.setStatus("mandatory")
_StorageDmn_Type = DisplayString
_StorageDmn_Object = MibScalar
storageDmn = _StorageDmn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 1, 1, 1, 17),
    _StorageDmn_Type()
)
storageDmn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDmn.setStatus("mandatory")

# Managed Objects groups


# Notification objects

genericSanEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 0, 1)
)
genericSanEvent.setObjects(
      *(("HPOvSam-MIB-V1", "severityLevel"),
        ("HPOvSam-MIB-V1", "category"),
        ("HPOvSam-MIB-V1", "id"),
        ("HPOvSam-MIB-V1", "msgString"),
        ("HPOvSam-MIB-V1", "contactName"),
        ("HPOvSam-MIB-V1", "contactEmail"),
        ("HPOvSam-MIB-V1", "contactWorkPhone"),
        ("HPOvSam-MIB-V1", "contactHomePhone"),
        ("HPOvSam-MIB-V1", "contactPager"),
        ("HPOvSam-MIB-V1", "contactFax"))
)
if mibBuilder.loadTexts:
    genericSanEvent.setStatus(
        ""
    )

sanDeviceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 27, 3, 0, 2)
)
sanDeviceEvent.setObjects(
      *(("HPOvSam-MIB-V1", "severityLevel"),
        ("HPOvSam-MIB-V1", "category"),
        ("HPOvSam-MIB-V1", "id"),
        ("HPOvSam-MIB-V1", "msgString"),
        ("HPOvSam-MIB-V1", "contactName"),
        ("HPOvSam-MIB-V1", "contactEmail"),
        ("HPOvSam-MIB-V1", "contactWorkPhone"),
        ("HPOvSam-MIB-V1", "contactHomePhone"),
        ("HPOvSam-MIB-V1", "contactPager"),
        ("HPOvSam-MIB-V1", "contactFax"),
        ("HPOvSam-MIB-V1", "sourceName"),
        ("HPOvSam-MIB-V1", "uniqueId"),
        ("HPOvSam-MIB-V1", "vendorId"),
        ("HPOvSam-MIB-V1", "prodId"),
        ("HPOvSam-MIB-V1", "prodRev"),
        ("HPOvSam-MIB-V1", "serialNo"),
        ("HPOvSam-MIB-V1", "storageDmn"))
)
if mibBuilder.loadTexts:
    sanDeviceEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPOvSam-MIB-V1",
    **{"hp": hp,
       "nm": nm,
       "hpStorageAssistant": hpStorageAssistant,
       "hpSanManager": hpSanManager,
       "hpSanManagerTraps": hpSanManagerTraps,
       "genericSanEvent": genericSanEvent,
       "sanDeviceEvent": sanDeviceEvent,
       "hpSanManagerModules": hpSanManagerModules,
       "hpSanManagerMibModule": hpSanManagerMibModule,
       "mibModuleEventVars": mibModuleEventVars,
       "severityLevel": severityLevel,
       "category": category,
       "id": id,
       "msgString": msgString,
       "contactName": contactName,
       "contactEmail": contactEmail,
       "contactHomePhone": contactHomePhone,
       "contactWorkPhone": contactWorkPhone,
       "contactPager": contactPager,
       "contactFax": contactFax,
       "sourceName": sourceName,
       "uniqueId": uniqueId,
       "vendorId": vendorId,
       "prodId": prodId,
       "prodRev": prodRev,
       "serialNo": serialNo,
       "storageDmn": storageDmn}
)
