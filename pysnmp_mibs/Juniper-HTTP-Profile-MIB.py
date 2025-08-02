_H='juniHttpProfileGroup'
_G='juniHttpProfileRedirectUrl'
_F='juniHttpProfileSetMap'
_E='read-write'
_D='juniHttpProfileId'
_C='DisplayString'
_B='Juniper-HTTP-Profile-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniSetMap,=mibBuilder.importSymbols('Juniper-TC','JuniSetMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
juniHttpProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,79))
if mibBuilder.loadTexts:juniHttpProfileMIB.setRevisions(('2005-08-19 14:21',))
_JuniHttpProfileObjects_ObjectIdentity=ObjectIdentity
juniHttpProfileObjects=_JuniHttpProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,79,1))
_JuniHttpProfile_ObjectIdentity=ObjectIdentity
juniHttpProfile=_JuniHttpProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,79,1,1))
_JuniHttpProfileTable_Object=MibTable
juniHttpProfileTable=_JuniHttpProfileTable_Object((1,3,6,1,4,1,4874,2,2,79,1,1,1))
if mibBuilder.loadTexts:juniHttpProfileTable.setStatus(_A)
_JuniHttpProfileEntry_Object=MibTableRow
juniHttpProfileEntry=_JuniHttpProfileEntry_Object((1,3,6,1,4,1,4874,2,2,79,1,1,1,1))
juniHttpProfileEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:juniHttpProfileEntry.setStatus(_A)
_JuniHttpProfileId_Type=Unsigned32
_JuniHttpProfileId_Object=MibTableColumn
juniHttpProfileId=_JuniHttpProfileId_Object((1,3,6,1,4,1,4874,2,2,79,1,1,1,1,1),_JuniHttpProfileId_Type())
juniHttpProfileId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniHttpProfileId.setStatus(_A)
_JuniHttpProfileSetMap_Type=JuniSetMap
_JuniHttpProfileSetMap_Object=MibTableColumn
juniHttpProfileSetMap=_JuniHttpProfileSetMap_Object((1,3,6,1,4,1,4874,2,2,79,1,1,1,1,2),_JuniHttpProfileSetMap_Type())
juniHttpProfileSetMap.setMaxAccess(_E)
if mibBuilder.loadTexts:juniHttpProfileSetMap.setStatus(_A)
class _JuniHttpProfileRedirectUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniHttpProfileRedirectUrl_Type.__name__=_C
_JuniHttpProfileRedirectUrl_Object=MibTableColumn
juniHttpProfileRedirectUrl=_JuniHttpProfileRedirectUrl_Object((1,3,6,1,4,1,4874,2,2,79,1,1,1,1,3),_JuniHttpProfileRedirectUrl_Type())
juniHttpProfileRedirectUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniHttpProfileRedirectUrl.setStatus(_A)
_JuniHttpProfileConformance_ObjectIdentity=ObjectIdentity
juniHttpProfileConformance=_JuniHttpProfileConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,79,4))
_JuniHttpProfileCompliances_ObjectIdentity=ObjectIdentity
juniHttpProfileCompliances=_JuniHttpProfileCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,79,4,1))
_JuniHttpProfileGroups_ObjectIdentity=ObjectIdentity
juniHttpProfileGroups=_JuniHttpProfileGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,79,4,2))
juniHttpProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,79,4,2,1))
juniHttpProfileGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:juniHttpProfileGroup.setStatus(_A)
juniHttpProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,79,4,1,1))
juniHttpProfileCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:juniHttpProfileCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniHttpProfileMIB':juniHttpProfileMIB,'juniHttpProfileObjects':juniHttpProfileObjects,'juniHttpProfile':juniHttpProfile,'juniHttpProfileTable':juniHttpProfileTable,'juniHttpProfileEntry':juniHttpProfileEntry,_D:juniHttpProfileId,_F:juniHttpProfileSetMap,_G:juniHttpProfileRedirectUrl,'juniHttpProfileConformance':juniHttpProfileConformance,'juniHttpProfileCompliances':juniHttpProfileCompliances,'juniHttpProfileCompliance':juniHttpProfileCompliance,'juniHttpProfileGroups':juniHttpProfileGroups,_H:juniHttpProfileGroup})