_I='pppoeConnectionCustomizationVer1'
_H='pppoeServiceName'
_G='pppoeAcName'
_F='pppoeEnable'
_E='MxEnableState'
_D='read-write'
_C='OctetString'
_B='MX-PPPOE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pppoeMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,105))
if mibBuilder.loadTexts:pppoeMIB.setRevisions(('1903-07-09 00:00',))
_PppoeMIBObjects_ObjectIdentity=ObjectIdentity
pppoeMIBObjects=_PppoeMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,105,1))
class _PppoeEnable_Type(MxEnableState):defaultValue=0
_PppoeEnable_Type.__name__=_E
_PppoeEnable_Object=MibScalar
pppoeEnable=_PppoeEnable_Object((1,3,6,1,4,1,4935,15,105,1,5),_PppoeEnable_Type())
pppoeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoeEnable.setStatus(_A)
class _PppoeAcName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PppoeAcName_Type.__name__=_C
_PppoeAcName_Object=MibScalar
pppoeAcName=_PppoeAcName_Object((1,3,6,1,4,1,4935,15,105,1,10),_PppoeAcName_Type())
pppoeAcName.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoeAcName.setStatus(_A)
class _PppoeServiceName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PppoeServiceName_Type.__name__=_C
_PppoeServiceName_Object=MibScalar
pppoeServiceName=_PppoeServiceName_Object((1,3,6,1,4,1,4935,15,105,1,15),_PppoeServiceName_Type())
pppoeServiceName.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoeServiceName.setStatus(_A)
_PppoeConformance_ObjectIdentity=ObjectIdentity
pppoeConformance=_PppoeConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,105,5))
_PppoeCompliances_ObjectIdentity=ObjectIdentity
pppoeCompliances=_PppoeCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,105,5,1))
_PppoeGroups_ObjectIdentity=ObjectIdentity
pppoeGroups=_PppoeGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,105,5,5))
pppoeConnectionCustomizationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,105,5,5,10))
pppoeConnectionCustomizationVer1.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:pppoeConnectionCustomizationVer1.setStatus(_A)
pppoeComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,105,5,1,1))
pppoeComplVer1.setObjects((_B,_I))
if mibBuilder.loadTexts:pppoeComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pppoeMIB':pppoeMIB,'pppoeMIBObjects':pppoeMIBObjects,_F:pppoeEnable,_G:pppoeAcName,_H:pppoeServiceName,'pppoeConformance':pppoeConformance,'pppoeCompliances':pppoeCompliances,'pppoeComplVer1':pppoeComplVer1,'pppoeGroups':pppoeGroups,_I:pppoeConnectionCustomizationVer1})