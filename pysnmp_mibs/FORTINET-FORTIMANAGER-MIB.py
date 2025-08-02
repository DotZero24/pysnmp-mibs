_H='fmTrapsComplianceGroup'
_G='fmTrapHASwitch'
_F='sysName'
_E='SNMPv2-MIB'
_D='fnSysSerial'
_C='FORTINET-CORE-MIB'
_B='FORTINET-FORTIMANAGER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fnSysSerial,fortinet=mibBuilder.importSymbols(_C,_D,'fortinet')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fnFortiManagerMib=ModuleIdentity((1,3,6,1,4,1,12356,103))
if mibBuilder.loadTexts:fnFortiManagerMib.setRevisions(('2008-07-18 00:00','2008-06-26 00:00','2008-06-16 00:00','2008-06-10 00:00'))
_FmTraps_ObjectIdentity=ObjectIdentity
fmTraps=_FmTraps_ObjectIdentity((1,3,6,1,4,1,12356,103,0))
_FmTrapPrefix_ObjectIdentity=ObjectIdentity
fmTrapPrefix=_FmTrapPrefix_ObjectIdentity((1,3,6,1,4,1,12356,103,0,0))
_FmTrapObject_ObjectIdentity=ObjectIdentity
fmTrapObject=_FmTrapObject_ObjectIdentity((1,3,6,1,4,1,12356,103,0,1))
_FmModel_ObjectIdentity=ObjectIdentity
fmModel=_FmModel_ObjectIdentity((1,3,6,1,4,1,12356,103,1))
_Fmg100_ObjectIdentity=ObjectIdentity
fmg100=_Fmg100_ObjectIdentity((1,3,6,1,4,1,12356,103,1,1000))
_Fmg400_ObjectIdentity=ObjectIdentity
fmg400=_Fmg400_ObjectIdentity((1,3,6,1,4,1,12356,103,1,4000))
_Fmg400A_ObjectIdentity=ObjectIdentity
fmg400A=_Fmg400A_ObjectIdentity((1,3,6,1,4,1,12356,103,1,4001))
_Fmg2000XL_ObjectIdentity=ObjectIdentity
fmg2000XL=_Fmg2000XL_ObjectIdentity((1,3,6,1,4,1,12356,103,1,20000))
_Fmg3000_ObjectIdentity=ObjectIdentity
fmg3000=_Fmg3000_ObjectIdentity((1,3,6,1,4,1,12356,103,1,30000))
_Fmg3000B_ObjectIdentity=ObjectIdentity
fmg3000B=_Fmg3000B_ObjectIdentity((1,3,6,1,4,1,12356,103,1,30002))
_FmMIBConformance_ObjectIdentity=ObjectIdentity
fmMIBConformance=_FmMIBConformance_ObjectIdentity((1,3,6,1,4,1,12356,103,10))
fmTrapHASwitch=NotificationType((1,3,6,1,4,1,12356,103,0,0,401))
fmTrapHASwitch.setObjects(*((_C,_D),(_E,_F)))
if mibBuilder.loadTexts:fmTrapHASwitch.setStatus(_A)
fmTrapsComplianceGroup=NotificationGroup((1,3,6,1,4,1,12356,103,10,1))
fmTrapsComplianceGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:fmTrapsComplianceGroup.setStatus(_A)
fmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,103,10,100))
fmMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:fmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fnFortiManagerMib':fnFortiManagerMib,'fmTraps':fmTraps,'fmTrapPrefix':fmTrapPrefix,_G:fmTrapHASwitch,'fmTrapObject':fmTrapObject,'fmModel':fmModel,'fmg100':fmg100,'fmg400':fmg400,'fmg400A':fmg400A,'fmg2000XL':fmg2000XL,'fmg3000':fmg3000,'fmg3000B':fmg3000B,'fmMIBConformance':fmMIBConformance,_H:fmTrapsComplianceGroup,'fmMIBCompliance':fmMIBCompliance})