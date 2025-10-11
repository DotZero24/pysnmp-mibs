# SNMP MIB module (MX-H323-DEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-H323-DEBUG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:31 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

h323DebugMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35)
)
if mibBuilder.loadTexts:
    h323DebugMIB.setRevisions(
        ("2004-10-14 00:00",
         "2003-04-09 00:00",
         "2003-01-07 00:00",
         "2002-12-19 00:00",
         "2002-11-13 00:00",
         "2002-10-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323DebugMIBObjects_ObjectIdentity = ObjectIdentity
h323DebugMIBObjects = _H323DebugMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1)
)
_H323DebugH323StackTrace_ObjectIdentity = ObjectIdentity
h323DebugH323StackTrace = _H323DebugH323StackTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5)
)


class _H323DebugH323StackTraceLevel_Type(Integer32):
    """Custom type h323DebugH323StackTraceLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level-0", 0),
          ("level-1", 1),
          ("level-2", 2),
          ("level-3", 3))
    )


_H323DebugH323StackTraceLevel_Type.__name__ = "Integer32"
_H323DebugH323StackTraceLevel_Object = MibScalar
h323DebugH323StackTraceLevel = _H323DebugH323StackTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 5),
    _H323DebugH323StackTraceLevel_Type()
)
h323DebugH323StackTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceLevel.setStatus("current")
_H323DebugH323StackTraceModules_ObjectIdentity = ObjectIdentity
h323DebugH323StackTraceModules = _H323DebugH323StackTraceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10)
)


class _H323DebugH323StackTraceModulesAnnexE_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesAnnexE based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesAnnexE_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesAnnexE_Object = MibScalar
h323DebugH323StackTraceModulesAnnexE = _H323DebugH323StackTraceModulesAnnexE_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 5),
    _H323DebugH323StackTraceModulesAnnexE_Type()
)
h323DebugH323StackTraceModulesAnnexE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesAnnexE.setStatus("current")


class _H323DebugH323StackTraceModulesCa_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesCa based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesCa_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesCa_Object = MibScalar
h323DebugH323StackTraceModulesCa = _H323DebugH323StackTraceModulesCa_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 10),
    _H323DebugH323StackTraceModulesCa_Type()
)
h323DebugH323StackTraceModulesCa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesCa.setStatus("current")


class _H323DebugH323StackTraceModulesCaerr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesCaerr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesCaerr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesCaerr_Object = MibScalar
h323DebugH323StackTraceModulesCaerr = _H323DebugH323StackTraceModulesCaerr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 15),
    _H323DebugH323StackTraceModulesCaerr_Type()
)
h323DebugH323StackTraceModulesCaerr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesCaerr.setStatus("current")


class _H323DebugH323StackTraceModulesChannels_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesChannels based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesChannels_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesChannels_Object = MibScalar
h323DebugH323StackTraceModulesChannels = _H323DebugH323StackTraceModulesChannels_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 20),
    _H323DebugH323StackTraceModulesChannels_Type()
)
h323DebugH323StackTraceModulesChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesChannels.setStatus("current")


class _H323DebugH323StackTraceModulesCm_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesCm based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesCm_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesCm_Object = MibScalar
h323DebugH323StackTraceModulesCm = _H323DebugH323StackTraceModulesCm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 25),
    _H323DebugH323StackTraceModulesCm_Type()
)
h323DebugH323StackTraceModulesCm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesCm.setStatus("current")


class _H323DebugH323StackTraceModulesCmapi_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesCmapi based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesCmapi_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesCmapi_Object = MibScalar
h323DebugH323StackTraceModulesCmapi = _H323DebugH323StackTraceModulesCmapi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 30),
    _H323DebugH323StackTraceModulesCmapi_Type()
)
h323DebugH323StackTraceModulesCmapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesCmapi.setStatus("current")


class _H323DebugH323StackTraceModulesCmapicb_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesCmapicb based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesCmapicb_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesCmapicb_Object = MibScalar
h323DebugH323StackTraceModulesCmapicb = _H323DebugH323StackTraceModulesCmapicb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 35),
    _H323DebugH323StackTraceModulesCmapicb_Type()
)
h323DebugH323StackTraceModulesCmapicb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesCmapicb.setStatus("current")


class _H323DebugH323StackTraceModulesCmerr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesCmerr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesCmerr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesCmerr_Object = MibScalar
h323DebugH323StackTraceModulesCmerr = _H323DebugH323StackTraceModulesCmerr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 40),
    _H323DebugH323StackTraceModulesCmerr_Type()
)
h323DebugH323StackTraceModulesCmerr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesCmerr.setStatus("current")


class _H323DebugH323StackTraceModulesDebug_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesDebug based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesDebug_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesDebug_Object = MibScalar
h323DebugH323StackTraceModulesDebug = _H323DebugH323StackTraceModulesDebug_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 45),
    _H323DebugH323StackTraceModulesDebug_Type()
)
h323DebugH323StackTraceModulesDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesDebug.setStatus("current")


class _H323DebugH323StackTraceModulesEfrm_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesEfrm based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesEfrm_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesEfrm_Object = MibScalar
h323DebugH323StackTraceModulesEfrm = _H323DebugH323StackTraceModulesEfrm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 50),
    _H323DebugH323StackTraceModulesEfrm_Type()
)
h323DebugH323StackTraceModulesEfrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesEfrm.setStatus("current")


class _H323DebugH323StackTraceModulesEtimer_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesEtimer based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesEtimer_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesEtimer_Object = MibScalar
h323DebugH323StackTraceModulesEtimer = _H323DebugH323StackTraceModulesEtimer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 55),
    _H323DebugH323StackTraceModulesEtimer_Type()
)
h323DebugH323StackTraceModulesEtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesEtimer.setStatus("current")


class _H323DebugH323StackTraceModulesEtimerheap_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesEtimerheap based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesEtimerheap_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesEtimerheap_Object = MibScalar
h323DebugH323StackTraceModulesEtimerheap = _H323DebugH323StackTraceModulesEtimerheap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 60),
    _H323DebugH323StackTraceModulesEtimerheap_Type()
)
h323DebugH323StackTraceModulesEtimerheap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesEtimerheap.setStatus("current")


class _H323DebugH323StackTraceModulesH450apdu_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesH450apdu based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesH450apdu_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesH450apdu_Object = MibScalar
h323DebugH323StackTraceModulesH450apdu = _H323DebugH323StackTraceModulesH450apdu_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 65),
    _H323DebugH323StackTraceModulesH450apdu_Type()
)
h323DebugH323StackTraceModulesH450apdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesH450apdu.setStatus("current")


class _H323DebugH323StackTraceModulesLi_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesLi based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesLi_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesLi_Object = MibScalar
h323DebugH323StackTraceModulesLi = _H323DebugH323StackTraceModulesLi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 70),
    _H323DebugH323StackTraceModulesLi_Type()
)
h323DebugH323StackTraceModulesLi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesLi.setStatus("current")


class _H323DebugH323StackTraceModulesLiinfo_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesLiinfo based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesLiinfo_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesLiinfo_Object = MibScalar
h323DebugH323StackTraceModulesLiinfo = _H323DebugH323StackTraceModulesLiinfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 75),
    _H323DebugH323StackTraceModulesLiinfo_Type()
)
h323DebugH323StackTraceModulesLiinfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesLiinfo.setStatus("current")


class _H323DebugH323StackTraceModulesMei_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesMei based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesMei_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesMei_Object = MibScalar
h323DebugH323StackTraceModulesMei = _H323DebugH323StackTraceModulesMei_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 80),
    _H323DebugH323StackTraceModulesMei_Type()
)
h323DebugH323StackTraceModulesMei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesMei.setStatus("current")


class _H323DebugH323StackTraceModulesNamechan_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesNamechan based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesNamechan_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesNamechan_Object = MibScalar
h323DebugH323StackTraceModulesNamechan = _H323DebugH323StackTraceModulesNamechan_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 85),
    _H323DebugH323StackTraceModulesNamechan_Type()
)
h323DebugH323StackTraceModulesNamechan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesNamechan.setStatus("current")


class _H323DebugH323StackTraceModulesPer_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPer based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPer_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPer_Object = MibScalar
h323DebugH323StackTraceModulesPer = _H323DebugH323StackTraceModulesPer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 90),
    _H323DebugH323StackTraceModulesPer_Type()
)
h323DebugH323StackTraceModulesPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPer.setStatus("current")


class _H323DebugH323StackTraceModulesPererr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPererr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPererr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPererr_Object = MibScalar
h323DebugH323StackTraceModulesPererr = _H323DebugH323StackTraceModulesPererr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 95),
    _H323DebugH323StackTraceModulesPererr_Type()
)
h323DebugH323StackTraceModulesPererr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPererr.setStatus("current")


class _H323DebugH323StackTraceModulesPdlapi_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlapi based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlapi_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlapi_Object = MibScalar
h323DebugH323StackTraceModulesPdlapi = _H323DebugH323StackTraceModulesPdlapi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 100),
    _H323DebugH323StackTraceModulesPdlapi_Type()
)
h323DebugH323StackTraceModulesPdlapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlapi.setStatus("current")


class _H323DebugH323StackTraceModulesPdlchan_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlchan based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlchan_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlchan_Object = MibScalar
h323DebugH323StackTraceModulesPdlchan = _H323DebugH323StackTraceModulesPdlchan_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 105),
    _H323DebugH323StackTraceModulesPdlchan_Type()
)
h323DebugH323StackTraceModulesPdlchan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlchan.setStatus("current")


class _H323DebugH323StackTraceModulesPdlcomm_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlcomm based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlcomm_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlcomm_Object = MibScalar
h323DebugH323StackTraceModulesPdlcomm = _H323DebugH323StackTraceModulesPdlcomm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 110),
    _H323DebugH323StackTraceModulesPdlcomm_Type()
)
h323DebugH323StackTraceModulesPdlcomm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlcomm.setStatus("current")


class _H323DebugH323StackTraceModulesPdlconf_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlconf based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlconf_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlconf_Object = MibScalar
h323DebugH323StackTraceModulesPdlconf = _H323DebugH323StackTraceModulesPdlconf_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 115),
    _H323DebugH323StackTraceModulesPdlconf_Type()
)
h323DebugH323StackTraceModulesPdlconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlconf.setStatus("current")


class _H323DebugH323StackTraceModulesPdlencode_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlencode based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlencode_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlencode_Object = MibScalar
h323DebugH323StackTraceModulesPdlencode = _H323DebugH323StackTraceModulesPdlencode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 120),
    _H323DebugH323StackTraceModulesPdlencode_Type()
)
h323DebugH323StackTraceModulesPdlencode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlencode.setStatus("current")


class _H323DebugH323StackTraceModulesPdlerror_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlerror based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlerror_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlerror_Object = MibScalar
h323DebugH323StackTraceModulesPdlerror = _H323DebugH323StackTraceModulesPdlerror_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 125),
    _H323DebugH323StackTraceModulesPdlerror_Type()
)
h323DebugH323StackTraceModulesPdlerror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlerror.setStatus("current")


class _H323DebugH323StackTraceModulesPdlfnerr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlfnerr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlfnerr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlfnerr_Object = MibScalar
h323DebugH323StackTraceModulesPdlfnerr = _H323DebugH323StackTraceModulesPdlfnerr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 130),
    _H323DebugH323StackTraceModulesPdlfnerr_Type()
)
h323DebugH323StackTraceModulesPdlfnerr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlfnerr.setStatus("current")


class _H323DebugH323StackTraceModulesPdllist_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdllist based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdllist_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdllist_Object = MibScalar
h323DebugH323StackTraceModulesPdllist = _H323DebugH323StackTraceModulesPdllist_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 135),
    _H323DebugH323StackTraceModulesPdllist_Type()
)
h323DebugH323StackTraceModulesPdllist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdllist.setStatus("current")


class _H323DebugH323StackTraceModulesPdlmisc_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlmisc based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlmisc_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlmisc_Object = MibScalar
h323DebugH323StackTraceModulesPdlmisc = _H323DebugH323StackTraceModulesPdlmisc_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 140),
    _H323DebugH323StackTraceModulesPdlmisc_Type()
)
h323DebugH323StackTraceModulesPdlmisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlmisc.setStatus("current")


class _H323DebugH323StackTraceModulesPdlmtask_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlmtask based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlmtask_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlmtask_Object = MibScalar
h323DebugH323StackTraceModulesPdlmtask = _H323DebugH323StackTraceModulesPdlmtask_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 145),
    _H323DebugH323StackTraceModulesPdlmtask_Type()
)
h323DebugH323StackTraceModulesPdlmtask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlmtask.setStatus("current")


class _H323DebugH323StackTraceModulesPdlprint_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlprint based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlprint_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlprint_Object = MibScalar
h323DebugH323StackTraceModulesPdlprint = _H323DebugH323StackTraceModulesPdlprint_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 150),
    _H323DebugH323StackTraceModulesPdlprint_Type()
)
h323DebugH323StackTraceModulesPdlprint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlprint.setStatus("current")


class _H323DebugH323StackTraceModulesPdlprnerr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlprnerr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlprnerr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlprnerr_Object = MibScalar
h323DebugH323StackTraceModulesPdlprnerr = _H323DebugH323StackTraceModulesPdlprnerr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 155),
    _H323DebugH323StackTraceModulesPdlprnerr_Type()
)
h323DebugH323StackTraceModulesPdlprnerr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlprnerr.setStatus("current")


class _H323DebugH323StackTraceModulesPdlprnwrn_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlprnwrn based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlprnwrn_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlprnwrn_Object = MibScalar
h323DebugH323StackTraceModulesPdlprnwrn = _H323DebugH323StackTraceModulesPdlprnwrn_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 160),
    _H323DebugH323StackTraceModulesPdlprnwrn_Type()
)
h323DebugH323StackTraceModulesPdlprnwrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlprnwrn.setStatus("current")


class _H323DebugH323StackTraceModulesPdlsm_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlsm based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlsm_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlsm_Object = MibScalar
h323DebugH323StackTraceModulesPdlsm = _H323DebugH323StackTraceModulesPdlsm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 165),
    _H323DebugH323StackTraceModulesPdlsm_Type()
)
h323DebugH323StackTraceModulesPdlsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlsm.setStatus("current")


class _H323DebugH323StackTraceModulesPdlsrc_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdlsrc based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdlsrc_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdlsrc_Object = MibScalar
h323DebugH323StackTraceModulesPdlsrc = _H323DebugH323StackTraceModulesPdlsrc_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 170),
    _H323DebugH323StackTraceModulesPdlsrc_Type()
)
h323DebugH323StackTraceModulesPdlsrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdlsrc.setStatus("current")


class _H323DebugH323StackTraceModulesPdltimer_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPdltimer based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPdltimer_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPdltimer_Object = MibScalar
h323DebugH323StackTraceModulesPdltimer = _H323DebugH323StackTraceModulesPdltimer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 175),
    _H323DebugH323StackTraceModulesPdltimer_Type()
)
h323DebugH323StackTraceModulesPdltimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPdltimer.setStatus("current")


class _H323DebugH323StackTraceModulesPi_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesPi based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesPi_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesPi_Object = MibScalar
h323DebugH323StackTraceModulesPi = _H323DebugH323StackTraceModulesPi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 180),
    _H323DebugH323StackTraceModulesPi_Type()
)
h323DebugH323StackTraceModulesPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesPi.setStatus("current")


class _H323DebugH323StackTraceModulesQ931_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesQ931 based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesQ931_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesQ931_Object = MibScalar
h323DebugH323StackTraceModulesQ931 = _H323DebugH323StackTraceModulesQ931_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 185),
    _H323DebugH323StackTraceModulesQ931_Type()
)
h323DebugH323StackTraceModulesQ931.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesQ931.setStatus("current")


class _H323DebugH323StackTraceModulesQ931err_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesQ931err based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesQ931err_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesQ931err_Object = MibScalar
h323DebugH323StackTraceModulesQ931err = _H323DebugH323StackTraceModulesQ931err_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 190),
    _H323DebugH323StackTraceModulesQ931err_Type()
)
h323DebugH323StackTraceModulesQ931err.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesQ931err.setStatus("current")


class _H323DebugH323StackTraceModulesRa_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesRa based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesRa_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesRa_Object = MibScalar
h323DebugH323StackTraceModulesRa = _H323DebugH323StackTraceModulesRa_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 195),
    _H323DebugH323StackTraceModulesRa_Type()
)
h323DebugH323StackTraceModulesRa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesRa.setStatus("current")


class _H323DebugH323StackTraceModulesRasctrl_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesRasctrl based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesRasctrl_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesRasctrl_Object = MibScalar
h323DebugH323StackTraceModulesRasctrl = _H323DebugH323StackTraceModulesRasctrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 200),
    _H323DebugH323StackTraceModulesRasctrl_Type()
)
h323DebugH323StackTraceModulesRasctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesRasctrl.setStatus("current")


class _H323DebugH323StackTraceModulesRasindb_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesRasindb based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesRasindb_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesRasindb_Object = MibScalar
h323DebugH323StackTraceModulesRasindb = _H323DebugH323StackTraceModulesRasindb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 205),
    _H323DebugH323StackTraceModulesRasindb_Type()
)
h323DebugH323StackTraceModulesRasindb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesRasindb.setStatus("current")


class _H323DebugH323StackTraceModulesSeli_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSeli based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSeli_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSeli_Object = MibScalar
h323DebugH323StackTraceModulesSeli = _H323DebugH323StackTraceModulesSeli_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 210),
    _H323DebugH323StackTraceModulesSeli_Type()
)
h323DebugH323StackTraceModulesSeli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSeli.setStatus("current")


class _H323DebugH323StackTraceModulesSsapi_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSsapi based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSsapi_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSsapi_Object = MibScalar
h323DebugH323StackTraceModulesSsapi = _H323DebugH323StackTraceModulesSsapi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 215),
    _H323DebugH323StackTraceModulesSsapi_Type()
)
h323DebugH323StackTraceModulesSsapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSsapi.setStatus("current")


class _H323DebugH323StackTraceModulesSsapicb_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSsapicb based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSsapicb_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSsapicb_Object = MibScalar
h323DebugH323StackTraceModulesSsapicb = _H323DebugH323StackTraceModulesSsapicb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 220),
    _H323DebugH323StackTraceModulesSsapicb_Type()
)
h323DebugH323StackTraceModulesSsapicb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSsapicb.setStatus("current")


class _H323DebugH323StackTraceModulesSschan_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSschan based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSschan_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSschan_Object = MibScalar
h323DebugH323StackTraceModulesSschan = _H323DebugH323StackTraceModulesSschan_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 225),
    _H323DebugH323StackTraceModulesSschan_Type()
)
h323DebugH323StackTraceModulesSschan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSschan.setStatus("current")


class _H323DebugH323StackTraceModulesSseapi_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSseapi based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSseapi_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSseapi_Object = MibScalar
h323DebugH323StackTraceModulesSseapi = _H323DebugH323StackTraceModulesSseapi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 230),
    _H323DebugH323StackTraceModulesSseapi_Type()
)
h323DebugH323StackTraceModulesSseapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSseapi.setStatus("current")


class _H323DebugH323StackTraceModulesSseapicb_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSseapicb based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSseapicb_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSseapicb_Object = MibScalar
h323DebugH323StackTraceModulesSseapicb = _H323DebugH323StackTraceModulesSseapicb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 235),
    _H323DebugH323StackTraceModulesSseapicb_Type()
)
h323DebugH323StackTraceModulesSseapicb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSseapicb.setStatus("current")


class _H323DebugH323StackTraceModulesSsechan_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSsechan based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSsechan_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSsechan_Object = MibScalar
h323DebugH323StackTraceModulesSsechan = _H323DebugH323StackTraceModulesSsechan_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 240),
    _H323DebugH323StackTraceModulesSsechan_Type()
)
h323DebugH323StackTraceModulesSsechan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSsechan.setStatus("current")


class _H323DebugH323StackTraceModulesSseerr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSseerr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSseerr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSseerr_Object = MibScalar
h323DebugH323StackTraceModulesSseerr = _H323DebugH323StackTraceModulesSseerr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 245),
    _H323DebugH323StackTraceModulesSseerr_Type()
)
h323DebugH323StackTraceModulesSseerr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSseerr.setStatus("current")


class _H323DebugH323StackTraceModulesSserr_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesSserr based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesSserr_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesSserr_Object = MibScalar
h323DebugH323StackTraceModulesSserr = _H323DebugH323StackTraceModulesSserr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 250),
    _H323DebugH323StackTraceModulesSserr_Type()
)
h323DebugH323StackTraceModulesSserr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesSserr.setStatus("current")


class _H323DebugH323StackTraceModulesTimer_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesTimer based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesTimer_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesTimer_Object = MibScalar
h323DebugH323StackTraceModulesTimer = _H323DebugH323StackTraceModulesTimer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 255),
    _H323DebugH323StackTraceModulesTimer_Type()
)
h323DebugH323StackTraceModulesTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesTimer.setStatus("current")


class _H323DebugH323StackTraceModulesTpktchan_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesTpktchan based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesTpktchan_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesTpktchan_Object = MibScalar
h323DebugH323StackTraceModulesTpktchan = _H323DebugH323StackTraceModulesTpktchan_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 260),
    _H323DebugH323StackTraceModulesTpktchan_Type()
)
h323DebugH323StackTraceModulesTpktchan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesTpktchan.setStatus("current")


class _H323DebugH323StackTraceModulesTransport_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesTransport based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesTransport_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesTransport_Object = MibScalar
h323DebugH323StackTraceModulesTransport = _H323DebugH323StackTraceModulesTransport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 265),
    _H323DebugH323StackTraceModulesTransport_Type()
)
h323DebugH323StackTraceModulesTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesTransport.setStatus("current")


class _H323DebugH323StackTraceModulesTunnctrl_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesTunnctrl based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesTunnctrl_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesTunnctrl_Object = MibScalar
h323DebugH323StackTraceModulesTunnctrl = _H323DebugH323StackTraceModulesTunnctrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 270),
    _H323DebugH323StackTraceModulesTunnctrl_Type()
)
h323DebugH323StackTraceModulesTunnctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesTunnctrl.setStatus("current")


class _H323DebugH323StackTraceModulesUdpchan_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesUdpchan based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesUdpchan_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesUdpchan_Object = MibScalar
h323DebugH323StackTraceModulesUdpchan = _H323DebugH323StackTraceModulesUdpchan_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 275),
    _H323DebugH323StackTraceModulesUdpchan_Type()
)
h323DebugH323StackTraceModulesUdpchan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesUdpchan.setStatus("current")


class _H323DebugH323StackTraceModulesUnreg_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesUnreg based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesUnreg_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesUnreg_Object = MibScalar
h323DebugH323StackTraceModulesUnreg = _H323DebugH323StackTraceModulesUnreg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 280),
    _H323DebugH323StackTraceModulesUnreg_Type()
)
h323DebugH323StackTraceModulesUnreg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesUnreg.setStatus("current")


class _H323DebugH323StackTraceModulesVt_Type(MxEnableState):
    """Custom type h323DebugH323StackTraceModulesVt based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTraceModulesVt_Type.__name__ = "MxEnableState"
_H323DebugH323StackTraceModulesVt_Object = MibScalar
h323DebugH323StackTraceModulesVt = _H323DebugH323StackTraceModulesVt_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 5, 10, 285),
    _H323DebugH323StackTraceModulesVt_Type()
)
h323DebugH323StackTraceModulesVt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTraceModulesVt.setStatus("current")
_H323DebugSupplementaryTrace_ObjectIdentity = ObjectIdentity
h323DebugSupplementaryTrace = _H323DebugSupplementaryTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 10)
)


class _H323DebugSuppTraceEngineProvision_Type(MxEnableState):
    """Custom type h323DebugSuppTraceEngineProvision based on MxEnableState"""
    defaultValue = 0


_H323DebugSuppTraceEngineProvision_Type.__name__ = "MxEnableState"
_H323DebugSuppTraceEngineProvision_Object = MibScalar
h323DebugSuppTraceEngineProvision = _H323DebugSuppTraceEngineProvision_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 10, 5),
    _H323DebugSuppTraceEngineProvision_Type()
)
h323DebugSuppTraceEngineProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugSuppTraceEngineProvision.setStatus("current")


class _H323DebugSuppTraceMediaProvision_Type(MxEnableState):
    """Custom type h323DebugSuppTraceMediaProvision based on MxEnableState"""
    defaultValue = 0


_H323DebugSuppTraceMediaProvision_Type.__name__ = "MxEnableState"
_H323DebugSuppTraceMediaProvision_Object = MibScalar
h323DebugSuppTraceMediaProvision = _H323DebugSuppTraceMediaProvision_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 10, 15),
    _H323DebugSuppTraceMediaProvision_Type()
)
h323DebugSuppTraceMediaProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugSuppTraceMediaProvision.setStatus("current")


class _H323DebugSuppTraceDebugProvision_Type(MxEnableState):
    """Custom type h323DebugSuppTraceDebugProvision based on MxEnableState"""
    defaultValue = 0


_H323DebugSuppTraceDebugProvision_Type.__name__ = "MxEnableState"
_H323DebugSuppTraceDebugProvision_Object = MibScalar
h323DebugSuppTraceDebugProvision = _H323DebugSuppTraceDebugProvision_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 10, 20),
    _H323DebugSuppTraceDebugProvision_Type()
)
h323DebugSuppTraceDebugProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugSuppTraceDebugProvision.setStatus("current")


class _H323DebugSuppTraceGkReg_Type(MxEnableState):
    """Custom type h323DebugSuppTraceGkReg based on MxEnableState"""
    defaultValue = 0


_H323DebugSuppTraceGkReg_Type.__name__ = "MxEnableState"
_H323DebugSuppTraceGkReg_Object = MibScalar
h323DebugSuppTraceGkReg = _H323DebugSuppTraceGkReg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 10, 25),
    _H323DebugSuppTraceGkReg_Type()
)
h323DebugSuppTraceGkReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugSuppTraceGkReg.setStatus("current")
_H323DebugH323StackTrace2_ObjectIdentity = ObjectIdentity
h323DebugH323StackTrace2 = _H323DebugH323StackTrace2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15)
)


class _H323DebugH323StackTrace2Enable_Type(MxEnableState):
    """Custom type h323DebugH323StackTrace2Enable based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTrace2Enable_Type.__name__ = "MxEnableState"
_H323DebugH323StackTrace2Enable_Object = MibScalar
h323DebugH323StackTrace2Enable = _H323DebugH323StackTrace2Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 5),
    _H323DebugH323StackTrace2Enable_Type()
)
h323DebugH323StackTrace2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2Enable.setStatus("current")


class _H323DebugH323StackTrace2ContentEnable_Type(MxEnableState):
    """Custom type h323DebugH323StackTrace2ContentEnable based on MxEnableState"""
    defaultValue = 0


_H323DebugH323StackTrace2ContentEnable_Type.__name__ = "MxEnableState"
_H323DebugH323StackTrace2ContentEnable_Object = MibScalar
h323DebugH323StackTrace2ContentEnable = _H323DebugH323StackTrace2ContentEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 10),
    _H323DebugH323StackTrace2ContentEnable_Type()
)
h323DebugH323StackTrace2ContentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2ContentEnable.setStatus("current")


class _H323DebugH323StackTrace2GeneralLevel_Type(Integer32):
    """Custom type h323DebugH323StackTrace2GeneralLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("exception", 1),
          ("error", 2),
          ("warning", 3))
    )


_H323DebugH323StackTrace2GeneralLevel_Type.__name__ = "Integer32"
_H323DebugH323StackTrace2GeneralLevel_Object = MibScalar
h323DebugH323StackTrace2GeneralLevel = _H323DebugH323StackTrace2GeneralLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 15),
    _H323DebugH323StackTrace2GeneralLevel_Type()
)
h323DebugH323StackTrace2GeneralLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2GeneralLevel.setStatus("current")
_H323DebugH323StackTrace2ModuleTable_Object = MibTable
h323DebugH323StackTrace2ModuleTable = _H323DebugH323StackTrace2ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 20)
)
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2ModuleTable.setStatus("current")
_H323DebugH323StackTrace2ModuleEntry_Object = MibTableRow
h323DebugH323StackTrace2ModuleEntry = _H323DebugH323StackTrace2ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 20, 1)
)
h323DebugH323StackTrace2ModuleEntry.setIndexNames(
    (0, "MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2ModuleIndex"),
)
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2ModuleEntry.setStatus("current")
_H323DebugH323StackTrace2ModuleIndex_Type = Unsigned32
_H323DebugH323StackTrace2ModuleIndex_Object = MibTableColumn
h323DebugH323StackTrace2ModuleIndex = _H323DebugH323StackTrace2ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 20, 1, 5),
    _H323DebugH323StackTrace2ModuleIndex_Type()
)
h323DebugH323StackTrace2ModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2ModuleIndex.setStatus("current")


class _H323DebugH323StackTrace2Module_Type(Integer32):
    """Custom type h323DebugH323StackTrace2Module based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              99)
        )
    )
    namedValues = NamedValues(
        *(("annexe", 0),
          ("appl", 1),
          ("ares", 2),
          ("cat", 3),
          ("ci", 4),
          ("cm", 5),
          ("cmapi", 6),
          ("cmapicb", 7),
          ("cmerr", 8),
          ("config", 9),
          ("ema", 10),
          ("faststart", 11),
          ("h245", 12),
          ("host", 13),
          ("lock", 14),
          ("memory", 15),
          ("mti", 16),
          ("mutex", 17),
          ("per", 18),
          ("pererr", 19),
          ("port", 20),
          ("q931", 21),
          ("q931err", 22),
          ("queue", 23),
          ("ra", 24),
          ("ras", 25),
          ("sec", 26),
          ("select", 27),
          ("sema4", 28),
          ("socket", 29),
          ("ssapi", 30),
          ("ssapicb", 31),
          ("sschan", 32),
          ("sseapi", 33),
          ("sseapicb", 34),
          ("sseerr", 35),
          ("sserr", 36),
          ("sups", 37),
          ("tcp", 38),
          ("thread", 39),
          ("timepool", 40),
          ("timestamp", 41),
          ("tls", 42),
          ("tm", 43),
          ("tpktchan", 44),
          ("tpktwire", 45),
          ("transport", 46),
          ("udpchan", 47),
          ("udpwire", 48),
          ("unreg", 49),
          ("vt", 50),
          ("watchdog", 51),
          ("moduleDisabled", 99))
    )


_H323DebugH323StackTrace2Module_Type.__name__ = "Integer32"
_H323DebugH323StackTrace2Module_Object = MibTableColumn
h323DebugH323StackTrace2Module = _H323DebugH323StackTrace2Module_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 20, 1, 10),
    _H323DebugH323StackTrace2Module_Type()
)
h323DebugH323StackTrace2Module.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2Module.setStatus("current")


class _H323DebugH323StackTrace2Level_Type(Integer32):
    """Custom type h323DebugH323StackTrace2Level based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("exception", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5),
          ("function", 6))
    )


_H323DebugH323StackTrace2Level_Type.__name__ = "Integer32"
_H323DebugH323StackTrace2Level_Object = MibTableColumn
h323DebugH323StackTrace2Level = _H323DebugH323StackTrace2Level_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 1, 15, 20, 1, 15),
    _H323DebugH323StackTrace2Level_Type()
)
h323DebugH323StackTrace2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2Level.setStatus("current")
_H323DebugConformance_ObjectIdentity = ObjectIdentity
h323DebugConformance = _H323DebugConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2)
)
_H323DebugCompliances_ObjectIdentity = ObjectIdentity
h323DebugCompliances = _H323DebugCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2, 1)
)
_H323DebugGroups_ObjectIdentity = ObjectIdentity
h323DebugGroups = _H323DebugGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2, 2)
)

# Managed Objects groups

h323DebugH323StackTraceGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2, 2, 5)
)
h323DebugH323StackTraceGroupVer1.setObjects(
      *(("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceLevel"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesAnnexE"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesCa"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesCaerr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesChannels"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesCm"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesCmapi"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesCmapicb"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesCmerr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesDebug"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesEfrm"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesEtimer"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesEtimerheap"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesH450apdu"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesLi"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesLiinfo"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesMei"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesNamechan"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPer"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPererr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlapi"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlchan"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlcomm"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlconf"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlencode"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlerror"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlfnerr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdllist"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlmisc"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlmtask"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlprint"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlprnerr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlprnwrn"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlsm"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdlsrc"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPdltimer"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesPi"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesQ931"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesQ931err"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesRa"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesRasctrl"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesRasindb"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSeli"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSsapi"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSsapicb"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSschan"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSseapi"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSseapicb"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSsechan"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSseerr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesSserr"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesTimer"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesTpktchan"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesTransport"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesTunnctrl"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesUdpchan"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesUnreg"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceModulesVt"))
)
if mibBuilder.loadTexts:
    h323DebugH323StackTraceGroupVer1.setStatus("current")

h323DebugH323StackTrace2GroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2, 2, 10)
)
h323DebugH323StackTrace2GroupVer1.setObjects(
      *(("MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2Enable"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2ContentEnable"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2GeneralLevel"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2Module"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2Level"))
)
if mibBuilder.loadTexts:
    h323DebugH323StackTrace2GroupVer1.setStatus("current")

h323DebugH323SupplementaryTraceGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2, 2, 15)
)
h323DebugH323SupplementaryTraceGroupVer1.setObjects(
      *(("MX-H323-DEBUG-MIB", "h323DebugSuppTraceEngineProvision"),
        ("MX-H323-DEBUG-MIB", "h323DebugSuppTraceMediaProvision"),
        ("MX-H323-DEBUG-MIB", "h323DebugSuppTraceDebugProvision"),
        ("MX-H323-DEBUG-MIB", "h323DebugSuppTraceGkReg"))
)
if mibBuilder.loadTexts:
    h323DebugH323SupplementaryTraceGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h323DebugBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 35, 2, 1, 5)
)
h323DebugBasicComplVer1.setObjects(
      *(("MX-H323-DEBUG-MIB", "h323DebugH323StackTraceGroupVer1"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323StackTrace2GroupVer1"),
        ("MX-H323-DEBUG-MIB", "h323DebugH323SupplementaryTraceGroupVer1"))
)
if mibBuilder.loadTexts:
    h323DebugBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-H323-DEBUG-MIB",
    **{"h323DebugMIB": h323DebugMIB,
       "h323DebugMIBObjects": h323DebugMIBObjects,
       "h323DebugH323StackTrace": h323DebugH323StackTrace,
       "h323DebugH323StackTraceLevel": h323DebugH323StackTraceLevel,
       "h323DebugH323StackTraceModules": h323DebugH323StackTraceModules,
       "h323DebugH323StackTraceModulesAnnexE": h323DebugH323StackTraceModulesAnnexE,
       "h323DebugH323StackTraceModulesCa": h323DebugH323StackTraceModulesCa,
       "h323DebugH323StackTraceModulesCaerr": h323DebugH323StackTraceModulesCaerr,
       "h323DebugH323StackTraceModulesChannels": h323DebugH323StackTraceModulesChannels,
       "h323DebugH323StackTraceModulesCm": h323DebugH323StackTraceModulesCm,
       "h323DebugH323StackTraceModulesCmapi": h323DebugH323StackTraceModulesCmapi,
       "h323DebugH323StackTraceModulesCmapicb": h323DebugH323StackTraceModulesCmapicb,
       "h323DebugH323StackTraceModulesCmerr": h323DebugH323StackTraceModulesCmerr,
       "h323DebugH323StackTraceModulesDebug": h323DebugH323StackTraceModulesDebug,
       "h323DebugH323StackTraceModulesEfrm": h323DebugH323StackTraceModulesEfrm,
       "h323DebugH323StackTraceModulesEtimer": h323DebugH323StackTraceModulesEtimer,
       "h323DebugH323StackTraceModulesEtimerheap": h323DebugH323StackTraceModulesEtimerheap,
       "h323DebugH323StackTraceModulesH450apdu": h323DebugH323StackTraceModulesH450apdu,
       "h323DebugH323StackTraceModulesLi": h323DebugH323StackTraceModulesLi,
       "h323DebugH323StackTraceModulesLiinfo": h323DebugH323StackTraceModulesLiinfo,
       "h323DebugH323StackTraceModulesMei": h323DebugH323StackTraceModulesMei,
       "h323DebugH323StackTraceModulesNamechan": h323DebugH323StackTraceModulesNamechan,
       "h323DebugH323StackTraceModulesPer": h323DebugH323StackTraceModulesPer,
       "h323DebugH323StackTraceModulesPererr": h323DebugH323StackTraceModulesPererr,
       "h323DebugH323StackTraceModulesPdlapi": h323DebugH323StackTraceModulesPdlapi,
       "h323DebugH323StackTraceModulesPdlchan": h323DebugH323StackTraceModulesPdlchan,
       "h323DebugH323StackTraceModulesPdlcomm": h323DebugH323StackTraceModulesPdlcomm,
       "h323DebugH323StackTraceModulesPdlconf": h323DebugH323StackTraceModulesPdlconf,
       "h323DebugH323StackTraceModulesPdlencode": h323DebugH323StackTraceModulesPdlencode,
       "h323DebugH323StackTraceModulesPdlerror": h323DebugH323StackTraceModulesPdlerror,
       "h323DebugH323StackTraceModulesPdlfnerr": h323DebugH323StackTraceModulesPdlfnerr,
       "h323DebugH323StackTraceModulesPdllist": h323DebugH323StackTraceModulesPdllist,
       "h323DebugH323StackTraceModulesPdlmisc": h323DebugH323StackTraceModulesPdlmisc,
       "h323DebugH323StackTraceModulesPdlmtask": h323DebugH323StackTraceModulesPdlmtask,
       "h323DebugH323StackTraceModulesPdlprint": h323DebugH323StackTraceModulesPdlprint,
       "h323DebugH323StackTraceModulesPdlprnerr": h323DebugH323StackTraceModulesPdlprnerr,
       "h323DebugH323StackTraceModulesPdlprnwrn": h323DebugH323StackTraceModulesPdlprnwrn,
       "h323DebugH323StackTraceModulesPdlsm": h323DebugH323StackTraceModulesPdlsm,
       "h323DebugH323StackTraceModulesPdlsrc": h323DebugH323StackTraceModulesPdlsrc,
       "h323DebugH323StackTraceModulesPdltimer": h323DebugH323StackTraceModulesPdltimer,
       "h323DebugH323StackTraceModulesPi": h323DebugH323StackTraceModulesPi,
       "h323DebugH323StackTraceModulesQ931": h323DebugH323StackTraceModulesQ931,
       "h323DebugH323StackTraceModulesQ931err": h323DebugH323StackTraceModulesQ931err,
       "h323DebugH323StackTraceModulesRa": h323DebugH323StackTraceModulesRa,
       "h323DebugH323StackTraceModulesRasctrl": h323DebugH323StackTraceModulesRasctrl,
       "h323DebugH323StackTraceModulesRasindb": h323DebugH323StackTraceModulesRasindb,
       "h323DebugH323StackTraceModulesSeli": h323DebugH323StackTraceModulesSeli,
       "h323DebugH323StackTraceModulesSsapi": h323DebugH323StackTraceModulesSsapi,
       "h323DebugH323StackTraceModulesSsapicb": h323DebugH323StackTraceModulesSsapicb,
       "h323DebugH323StackTraceModulesSschan": h323DebugH323StackTraceModulesSschan,
       "h323DebugH323StackTraceModulesSseapi": h323DebugH323StackTraceModulesSseapi,
       "h323DebugH323StackTraceModulesSseapicb": h323DebugH323StackTraceModulesSseapicb,
       "h323DebugH323StackTraceModulesSsechan": h323DebugH323StackTraceModulesSsechan,
       "h323DebugH323StackTraceModulesSseerr": h323DebugH323StackTraceModulesSseerr,
       "h323DebugH323StackTraceModulesSserr": h323DebugH323StackTraceModulesSserr,
       "h323DebugH323StackTraceModulesTimer": h323DebugH323StackTraceModulesTimer,
       "h323DebugH323StackTraceModulesTpktchan": h323DebugH323StackTraceModulesTpktchan,
       "h323DebugH323StackTraceModulesTransport": h323DebugH323StackTraceModulesTransport,
       "h323DebugH323StackTraceModulesTunnctrl": h323DebugH323StackTraceModulesTunnctrl,
       "h323DebugH323StackTraceModulesUdpchan": h323DebugH323StackTraceModulesUdpchan,
       "h323DebugH323StackTraceModulesUnreg": h323DebugH323StackTraceModulesUnreg,
       "h323DebugH323StackTraceModulesVt": h323DebugH323StackTraceModulesVt,
       "h323DebugSupplementaryTrace": h323DebugSupplementaryTrace,
       "h323DebugSuppTraceEngineProvision": h323DebugSuppTraceEngineProvision,
       "h323DebugSuppTraceMediaProvision": h323DebugSuppTraceMediaProvision,
       "h323DebugSuppTraceDebugProvision": h323DebugSuppTraceDebugProvision,
       "h323DebugSuppTraceGkReg": h323DebugSuppTraceGkReg,
       "h323DebugH323StackTrace2": h323DebugH323StackTrace2,
       "h323DebugH323StackTrace2Enable": h323DebugH323StackTrace2Enable,
       "h323DebugH323StackTrace2ContentEnable": h323DebugH323StackTrace2ContentEnable,
       "h323DebugH323StackTrace2GeneralLevel": h323DebugH323StackTrace2GeneralLevel,
       "h323DebugH323StackTrace2ModuleTable": h323DebugH323StackTrace2ModuleTable,
       "h323DebugH323StackTrace2ModuleEntry": h323DebugH323StackTrace2ModuleEntry,
       "h323DebugH323StackTrace2ModuleIndex": h323DebugH323StackTrace2ModuleIndex,
       "h323DebugH323StackTrace2Module": h323DebugH323StackTrace2Module,
       "h323DebugH323StackTrace2Level": h323DebugH323StackTrace2Level,
       "h323DebugConformance": h323DebugConformance,
       "h323DebugCompliances": h323DebugCompliances,
       "h323DebugBasicComplVer1": h323DebugBasicComplVer1,
       "h323DebugGroups": h323DebugGroups,
       "h323DebugH323StackTraceGroupVer1": h323DebugH323StackTraceGroupVer1,
       "h323DebugH323StackTrace2GroupVer1": h323DebugH323StackTrace2GroupVer1,
       "h323DebugH323SupplementaryTraceGroupVer1": h323DebugH323SupplementaryTraceGroupVer1}
)
