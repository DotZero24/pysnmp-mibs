_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,org=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','org')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
infinera=ModuleIdentity((1,3,6,1,4,1,21296))
if mibBuilder.loadTexts:infinera.setRevisions(('2008-09-05 17:00',))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Don_ObjectIdentity=ObjectIdentity
don=_Don_ObjectIdentity((1,3,6,1,4,1,21296,2))
if mibBuilder.loadTexts:don.setStatus(_A)
_Base_ObjectIdentity=ObjectIdentity
base=_Base_ObjectIdentity((1,3,6,1,4,1,21296,2,1))
if mibBuilder.loadTexts:base.setStatus(_A)
_Ne_ObjectIdentity=ObjectIdentity
ne=_Ne_ObjectIdentity((1,3,6,1,4,1,21296,2,2))
if mibBuilder.loadTexts:ne.setStatus(_A)
_Common_ObjectIdentity=ObjectIdentity
common=_Common_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1))
_InfnNE_ObjectIdentity=ObjectIdentity
infnNE=_InfnNE_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8))
_CommonEquipment_ObjectIdentity=ObjectIdentity
commonEquipment=_CommonEquipment_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9))
_CommonTerminationPoint_ObjectIdentity=ObjectIdentity
commonTerminationPoint=_CommonTerminationPoint_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10))
_CommonPerfMon_ObjectIdentity=ObjectIdentity
commonPerfMon=_CommonPerfMon_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11))
_Dtn_ObjectIdentity=ObjectIdentity
dtn=_Dtn_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2))
_Equipment_ObjectIdentity=ObjectIdentity
equipment=_Equipment_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1))
_TerminationPoint_ObjectIdentity=ObjectIdentity
terminationPoint=_TerminationPoint_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2))
_PerfMon_ObjectIdentity=ObjectIdentity
perfMon=_PerfMon_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3))
_Ola_ObjectIdentity=ObjectIdentity
ola=_Ola_ObjectIdentity((1,3,6,1,4,1,21296,2,2,3))
_Ems_ObjectIdentity=ObjectIdentity
ems=_Ems_ObjectIdentity((1,3,6,1,4,1,21296,2,3))
if mibBuilder.loadTexts:ems.setStatus(_A)
mibBuilder.exportSymbols('INFINERA-REG-MIB',**{'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'infinera':infinera,'don':don,'base':base,'ne':ne,'common':common,'infnNE':infnNE,'commonEquipment':commonEquipment,'commonTerminationPoint':commonTerminationPoint,'commonPerfMon':commonPerfMon,'dtn':dtn,'equipment':equipment,'terminationPoint':terminationPoint,'perfMon':perfMon,'ola':ola,'ems':ems})