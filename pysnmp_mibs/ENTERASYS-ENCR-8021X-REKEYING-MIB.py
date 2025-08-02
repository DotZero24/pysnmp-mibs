_K='etsysEncrDot1xRekeyingBaseGroup'
_J='etsysEncrDot1xRekeyAsymmetric'
_I='etsysEncrDot1xRekeyLength'
_H='etsysEncrDot1xRekeyEnabled'
_G='etsysEncrDot1xRekeyPeriod'
_F='dot1xPaePortNumber'
_E='IEEE8021-PAE-MIB'
_D='read-write'
_C='OctetString'
_B='ENTERASYS-ENCR-8021X-REKEYING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
dot1xPaePortNumber,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysEncr8021xRekeyingMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,20))
if mibBuilder.loadTexts:etsysEncr8021xRekeyingMIB.setRevisions(('2002-03-14 20:49',))
_EtsysEncrDot1xRekeyingObjects_ObjectIdentity=ObjectIdentity
etsysEncrDot1xRekeyingObjects=_EtsysEncrDot1xRekeyingObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,20,1))
_EtsysEncrDot1xRekeyBaseBranch_ObjectIdentity=ObjectIdentity
etsysEncrDot1xRekeyBaseBranch=_EtsysEncrDot1xRekeyBaseBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,20,1,1))
_EtsysEncrDot1xRekeyConfigTable_Object=MibTable
etsysEncrDot1xRekeyConfigTable=_EtsysEncrDot1xRekeyConfigTable_Object((1,3,6,1,4,1,5624,1,2,20,1,1,1))
if mibBuilder.loadTexts:etsysEncrDot1xRekeyConfigTable.setStatus(_A)
_EtsysEncrDot1xRekeyConfigEntry_Object=MibTableRow
etsysEncrDot1xRekeyConfigEntry=_EtsysEncrDot1xRekeyConfigEntry_Object((1,3,6,1,4,1,5624,1,2,20,1,1,1,1))
etsysEncrDot1xRekeyConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysEncrDot1xRekeyConfigEntry.setStatus(_A)
class _EtsysEncrDot1xRekeyEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xRekeyEnabled_Type.__name__=_C
_EtsysEncrDot1xRekeyEnabled_Object=MibTableColumn
etsysEncrDot1xRekeyEnabled=_EtsysEncrDot1xRekeyEnabled_Object((1,3,6,1,4,1,5624,1,2,20,1,1,1,1,1),_EtsysEncrDot1xRekeyEnabled_Type())
etsysEncrDot1xRekeyEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xRekeyEnabled.setStatus(_A)
class _EtsysEncrDot1xRekeyPeriod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xRekeyPeriod_Type.__name__=_C
_EtsysEncrDot1xRekeyPeriod_Object=MibTableColumn
etsysEncrDot1xRekeyPeriod=_EtsysEncrDot1xRekeyPeriod_Object((1,3,6,1,4,1,5624,1,2,20,1,1,1,1,2),_EtsysEncrDot1xRekeyPeriod_Type())
etsysEncrDot1xRekeyPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xRekeyPeriod.setStatus(_A)
class _EtsysEncrDot1xRekeyLength_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xRekeyLength_Type.__name__=_C
_EtsysEncrDot1xRekeyLength_Object=MibTableColumn
etsysEncrDot1xRekeyLength=_EtsysEncrDot1xRekeyLength_Object((1,3,6,1,4,1,5624,1,2,20,1,1,1,1,3),_EtsysEncrDot1xRekeyLength_Type())
etsysEncrDot1xRekeyLength.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xRekeyLength.setStatus(_A)
class _EtsysEncrDot1xRekeyAsymmetric_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysEncrDot1xRekeyAsymmetric_Type.__name__=_C
_EtsysEncrDot1xRekeyAsymmetric_Object=MibTableColumn
etsysEncrDot1xRekeyAsymmetric=_EtsysEncrDot1xRekeyAsymmetric_Object((1,3,6,1,4,1,5624,1,2,20,1,1,1,1,4),_EtsysEncrDot1xRekeyAsymmetric_Type())
etsysEncrDot1xRekeyAsymmetric.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEncrDot1xRekeyAsymmetric.setStatus(_A)
_EtsysEncrDot1xRekeyingConformance_ObjectIdentity=ObjectIdentity
etsysEncrDot1xRekeyingConformance=_EtsysEncrDot1xRekeyingConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,20,2))
_EtsysEncrDot1xRekeyingGroups_ObjectIdentity=ObjectIdentity
etsysEncrDot1xRekeyingGroups=_EtsysEncrDot1xRekeyingGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,20,2,1))
_EtsysEncrDot1xRekeyingCompliances_ObjectIdentity=ObjectIdentity
etsysEncrDot1xRekeyingCompliances=_EtsysEncrDot1xRekeyingCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,20,2,2))
etsysEncrDot1xRekeyingBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,20,2,1,1))
etsysEncrDot1xRekeyingBaseGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:etsysEncrDot1xRekeyingBaseGroup.setStatus(_A)
etsysEncrDot1xRekeyingCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,20,2,2,1))
etsysEncrDot1xRekeyingCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:etsysEncrDot1xRekeyingCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysEncr8021xRekeyingMIB':etsysEncr8021xRekeyingMIB,'etsysEncrDot1xRekeyingObjects':etsysEncrDot1xRekeyingObjects,'etsysEncrDot1xRekeyBaseBranch':etsysEncrDot1xRekeyBaseBranch,'etsysEncrDot1xRekeyConfigTable':etsysEncrDot1xRekeyConfigTable,'etsysEncrDot1xRekeyConfigEntry':etsysEncrDot1xRekeyConfigEntry,_H:etsysEncrDot1xRekeyEnabled,_G:etsysEncrDot1xRekeyPeriod,_I:etsysEncrDot1xRekeyLength,_J:etsysEncrDot1xRekeyAsymmetric,'etsysEncrDot1xRekeyingConformance':etsysEncrDot1xRekeyingConformance,'etsysEncrDot1xRekeyingGroups':etsysEncrDot1xRekeyingGroups,_K:etsysEncrDot1xRekeyingBaseGroup,'etsysEncrDot1xRekeyingCompliances':etsysEncrDot1xRekeyingCompliances,'etsysEncrDot1xRekeyingCompliance':etsysEncrDot1xRekeyingCompliance})