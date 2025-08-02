_E='bootBehaviorGroupVer1'
_D='checkTcpIpStackForSuccessfulBoot'
_C='MxEnableState'
_B='MX-BOOT-BEHAVIOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bootBehaviorMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,70))
if mibBuilder.loadTexts:bootBehaviorMIB.setRevisions(('2004-08-12 00:00',))
_BootBehaviorMIBObjects_ObjectIdentity=ObjectIdentity
bootBehaviorMIBObjects=_BootBehaviorMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,70,1))
class _CheckTcpIpStackForSuccessfulBoot_Type(MxEnableState):defaultValue=1
_CheckTcpIpStackForSuccessfulBoot_Type.__name__=_C
_CheckTcpIpStackForSuccessfulBoot_Object=MibScalar
checkTcpIpStackForSuccessfulBoot=_CheckTcpIpStackForSuccessfulBoot_Object((1,3,6,1,4,1,4935,99,70,1,1),_CheckTcpIpStackForSuccessfulBoot_Type())
checkTcpIpStackForSuccessfulBoot.setMaxAccess('read-write')
if mibBuilder.loadTexts:checkTcpIpStackForSuccessfulBoot.setStatus(_A)
_BootBehaviorConformance_ObjectIdentity=ObjectIdentity
bootBehaviorConformance=_BootBehaviorConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,70,2))
_BootBehaviorCompliances_ObjectIdentity=ObjectIdentity
bootBehaviorCompliances=_BootBehaviorCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,70,2,1))
_BootBehaviorGroups_ObjectIdentity=ObjectIdentity
bootBehaviorGroups=_BootBehaviorGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,70,2,2))
bootBehaviorGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,70,2,2,10))
bootBehaviorGroupVer1.setObjects((_B,_D))
if mibBuilder.loadTexts:bootBehaviorGroupVer1.setStatus(_A)
bootBehaviorComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,70,2,1,10))
bootBehaviorComplVer1.setObjects((_B,_E))
if mibBuilder.loadTexts:bootBehaviorComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bootBehaviorMIB':bootBehaviorMIB,'bootBehaviorMIBObjects':bootBehaviorMIBObjects,_D:checkTcpIpStackForSuccessfulBoot,'bootBehaviorConformance':bootBehaviorConformance,'bootBehaviorCompliances':bootBehaviorCompliances,'bootBehaviorComplVer1':bootBehaviorComplVer1,'bootBehaviorGroups':bootBehaviorGroups,_E:bootBehaviorGroupVer1})