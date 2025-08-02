_E='pppoaConnectionCustomizationVer1'
_D='pppoaEnable'
_C='MxEnableState'
_B='MX-PPPOA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pppoaMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,350))
if mibBuilder.loadTexts:pppoaMIB.setRevisions(('2006-03-06 00:00','2005-04-12 00:00'))
_PppoaMIBObjects_ObjectIdentity=ObjectIdentity
pppoaMIBObjects=_PppoaMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,350,1))
class _PppoaEnable_Type(MxEnableState):defaultValue=0
_PppoaEnable_Type.__name__=_C
_PppoaEnable_Object=MibScalar
pppoaEnable=_PppoaEnable_Object((1,3,6,1,4,1,4935,15,350,1,50),_PppoaEnable_Type())
pppoaEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:pppoaEnable.setStatus(_A)
_PppoaConformance_ObjectIdentity=ObjectIdentity
pppoaConformance=_PppoaConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,350,5))
_PppoaCompliances_ObjectIdentity=ObjectIdentity
pppoaCompliances=_PppoaCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,350,5,1))
_PppoaGroups_ObjectIdentity=ObjectIdentity
pppoaGroups=_PppoaGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,350,5,5))
pppoaConnectionCustomizationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,350,5,5,10))
pppoaConnectionCustomizationVer1.setObjects((_B,_D))
if mibBuilder.loadTexts:pppoaConnectionCustomizationVer1.setStatus(_A)
pppoaComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,350,5,1,1))
pppoaComplVer1.setObjects((_B,_E))
if mibBuilder.loadTexts:pppoaComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pppoaMIB':pppoaMIB,'pppoaMIBObjects':pppoaMIBObjects,_D:pppoaEnable,'pppoaConformance':pppoaConformance,'pppoaCompliances':pppoaCompliances,'pppoaComplVer1':pppoaComplVer1,'pppoaGroups':pppoaGroups,_E:pppoaConnectionCustomizationVer1})