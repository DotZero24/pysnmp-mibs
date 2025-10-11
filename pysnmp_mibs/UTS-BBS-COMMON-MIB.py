# SNMP MIB module (UTS-BBS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/utstarcom/UTS-BBS-COMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:46 2025
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

(utBroadbandModules,
 utsBroadbandSwitch) = mibBuilder.importSymbols(
    "UTS-COMMON-MIB",
    "utBroadbandModules",
    "utsBroadbandSwitch")


# MODULE-IDENTITY

utBBSCommonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    utBBSCommonModule.setRevisions(
        ("2003-09-29 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BBSEntityInstance(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_UtBBSMIB_ObjectIdentity = ObjectIdentity
utBBSMIB = _UtBBSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 1)
)
_UtBBSChassis_ObjectIdentity = ObjectIdentity
utBBSChassis = _UtBBSChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 1, 1)
)
_UtBBSProducts_ObjectIdentity = ObjectIdentity
utBBSProducts = _UtBBSProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 1, 2)
)
_UtBBSTrapObjects_ObjectIdentity = ObjectIdentity
utBBSTrapObjects = _UtBBSTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 1, 3)
)
_UtBBSTrapEntityInstance_Type = BBSEntityInstance
_UtBBSTrapEntityInstance_Object = MibScalar
utBBSTrapEntityInstance = _UtBBSTrapEntityInstance_Object(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 1, 3, 1),
    _UtBBSTrapEntityInstance_Type()
)
utBBSTrapEntityInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    utBBSTrapEntityInstance.setStatus("current")
_UtsBBSProductSysId_ObjectIdentity = ObjectIdentity
utsBBSProductSysId = _UtsBBSProductSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    utsBBSProductSysId.setStatus("current")
_UtBBS1000_ObjectIdentity = ObjectIdentity
utBBS1000 = _UtBBS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 1)
)
if mibBuilder.loadTexts:
    utBBS1000.setStatus("current")
_UtBBS5000_ObjectIdentity = ObjectIdentity
utBBS5000 = _UtBBS5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 2)
)
if mibBuilder.loadTexts:
    utBBS5000.setStatus("current")
_UtBBS4000_ObjectIdentity = ObjectIdentity
utBBS4000 = _UtBBS4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 3)
)
if mibBuilder.loadTexts:
    utBBS4000.setStatus("current")
_UtBBS2000_ObjectIdentity = ObjectIdentity
utBBS2000 = _UtBBS2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 4)
)
if mibBuilder.loadTexts:
    utBBS2000.setStatus("current")
_UtBBS1000plus_ObjectIdentity = ObjectIdentity
utBBS1000plus = _UtBBS1000plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 5)
)
if mibBuilder.loadTexts:
    utBBS1000plus.setStatus("current")
_UtBBSEponOnuSysId_ObjectIdentity = ObjectIdentity
utBBSEponOnuSysId = _UtBBSEponOnuSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100)
)
if mibBuilder.loadTexts:
    utBBSEponOnuSysId.setStatus("current")
_UtBBSEponOnuSysId200A_ObjectIdentity = ObjectIdentity
utBBSEponOnuSysId200A = _UtBBSEponOnuSysId200A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100, 1)
)
if mibBuilder.loadTexts:
    utBBSEponOnuSysId200A.setStatus("current")
_UtBBSEponOnuSysId2024_ObjectIdentity = ObjectIdentity
utBBSEponOnuSysId2024 = _UtBBSEponOnuSysId2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100, 2)
)
if mibBuilder.loadTexts:
    utBBSEponOnuSysId2024.setStatus("current")
_UtBBSEponOnuSysId2004_ObjectIdentity = ObjectIdentity
utBBSEponOnuSysId2004 = _UtBBSEponOnuSysId2004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100, 6)
)
if mibBuilder.loadTexts:
    utBBSEponOnuSysId2004.setStatus("current")
_UtBBSGepon_ObjectIdentity = ObjectIdentity
utBBSGepon = _UtBBSGepon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 3)
)
if mibBuilder.loadTexts:
    utBBSGepon.setStatus("current")
_UtAccounting_ObjectIdentity = ObjectIdentity
utAccounting = _UtAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 3, 1)
)
if mibBuilder.loadTexts:
    utAccounting.setStatus("current")
_UtConfiguration_ObjectIdentity = ObjectIdentity
utConfiguration = _UtConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 3, 2)
)
if mibBuilder.loadTexts:
    utConfiguration.setStatus("current")
_UtFault_ObjectIdentity = ObjectIdentity
utFault = _UtFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 3, 3)
)
if mibBuilder.loadTexts:
    utFault.setStatus("current")
_UtPerformance_ObjectIdentity = ObjectIdentity
utPerformance = _UtPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 3, 4)
)
if mibBuilder.loadTexts:
    utPerformance.setStatus("current")
_UtSecurity_ObjectIdentity = ObjectIdentity
utSecurity = _UtSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 3, 5)
)
if mibBuilder.loadTexts:
    utSecurity.setStatus("current")
_UtBBSGeponOnu_ObjectIdentity = ObjectIdentity
utBBSGeponOnu = _UtBBSGeponOnu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu.setStatus("current")
_UtBBSGeponOnu200A_ObjectIdentity = ObjectIdentity
utBBSGeponOnu200A = _UtBBSGeponOnu200A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 1)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu200A.setStatus("current")
_UtBBSGeponOnu2024_ObjectIdentity = ObjectIdentity
utBBSGeponOnu2024 = _UtBBSGeponOnu2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 2)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu2024.setStatus("current")
_UtBBSGeponOnu2004_ObjectIdentity = ObjectIdentity
utBBSGeponOnu2004 = _UtBBSGeponOnu2004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 6)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu2004.setStatus("current")
_UtsGeponBBS_ObjectIdentity = ObjectIdentity
utsGeponBBS = _UtsGeponBBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200)
)
if mibBuilder.loadTexts:
    utsGeponBBS.setStatus("current")
_UtsGeponBBS1000_ObjectIdentity = ObjectIdentity
utsGeponBBS1000 = _UtsGeponBBS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 1)
)
if mibBuilder.loadTexts:
    utsGeponBBS1000.setStatus("current")
_UtsGeponBBS1000plus_ObjectIdentity = ObjectIdentity
utsGeponBBS1000plus = _UtsGeponBBS1000plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 2)
)
if mibBuilder.loadTexts:
    utsGeponBBS1000plus.setStatus("current")
_UtsGeponBBS4000_ObjectIdentity = ObjectIdentity
utsGeponBBS4000 = _UtsGeponBBS4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000.setStatus("current")
_UtsGeponBBS4000Accounting_ObjectIdentity = ObjectIdentity
utsGeponBBS4000Accounting = _UtsGeponBBS4000Accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 1)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000Accounting.setStatus("current")
_UtsGeponBBS4000Configuration_ObjectIdentity = ObjectIdentity
utsGeponBBS4000Configuration = _UtsGeponBBS4000Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 2)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000Configuration.setStatus("current")
_UtsGeponBBS4000Fault_ObjectIdentity = ObjectIdentity
utsGeponBBS4000Fault = _UtsGeponBBS4000Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 3)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000Fault.setStatus("current")
_UtsGeponBBS4000Performance_ObjectIdentity = ObjectIdentity
utsGeponBBS4000Performance = _UtsGeponBBS4000Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 4)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000Performance.setStatus("current")
_UtsGeponBBS4000Security_ObjectIdentity = ObjectIdentity
utsGeponBBS4000Security = _UtsGeponBBS4000Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000Security.setStatus("current")
_UtsGeponBBS4000V5TG_ObjectIdentity = ObjectIdentity
utsGeponBBS4000V5TG = _UtsGeponBBS4000V5TG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 6)
)
if mibBuilder.loadTexts:
    utsGeponBBS4000V5TG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UTS-BBS-COMMON-MIB",
    **{"BBSEntityInstance": BBSEntityInstance,
       "utBBSCommonModule": utBBSCommonModule,
       "utBBSMIB": utBBSMIB,
       "utBBSChassis": utBBSChassis,
       "utBBSProducts": utBBSProducts,
       "utBBSTrapObjects": utBBSTrapObjects,
       "utBBSTrapEntityInstance": utBBSTrapEntityInstance,
       "utsBBSProductSysId": utsBBSProductSysId,
       "utBBS1000": utBBS1000,
       "utBBS5000": utBBS5000,
       "utBBS4000": utBBS4000,
       "utBBS2000": utBBS2000,
       "utBBS1000plus": utBBS1000plus,
       "utBBSEponOnuSysId": utBBSEponOnuSysId,
       "utBBSEponOnuSysId200A": utBBSEponOnuSysId200A,
       "utBBSEponOnuSysId2024": utBBSEponOnuSysId2024,
       "utBBSEponOnuSysId2004": utBBSEponOnuSysId2004,
       "utBBSGepon": utBBSGepon,
       "utAccounting": utAccounting,
       "utConfiguration": utConfiguration,
       "utFault": utFault,
       "utPerformance": utPerformance,
       "utSecurity": utSecurity,
       "utBBSGeponOnu": utBBSGeponOnu,
       "utBBSGeponOnu200A": utBBSGeponOnu200A,
       "utBBSGeponOnu2024": utBBSGeponOnu2024,
       "utBBSGeponOnu2004": utBBSGeponOnu2004,
       "utsGeponBBS": utsGeponBBS,
       "utsGeponBBS1000": utsGeponBBS1000,
       "utsGeponBBS1000plus": utsGeponBBS1000plus,
       "utsGeponBBS4000": utsGeponBBS4000,
       "utsGeponBBS4000Accounting": utsGeponBBS4000Accounting,
       "utsGeponBBS4000Configuration": utsGeponBBS4000Configuration,
       "utsGeponBBS4000Fault": utsGeponBBS4000Fault,
       "utsGeponBBS4000Performance": utsGeponBBS4000Performance,
       "utsGeponBBS4000Security": utsGeponBBS4000Security,
       "utsGeponBBS4000V5TG": utsGeponBBS4000V5TG}
)
