if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
btiMib=ModuleIdentity((1,3,6,1,4,1,18070,1,1))
if mibBuilder.loadTexts:btiMib.setRevisions(('2012-11-30 12:00','2012-03-09 12:00','2012-02-10 12:00','2011-09-26 12:00','2008-05-30 12:00','2007-08-27 12:00','2005-07-25 12:00','2004-09-23 12:00','2003-12-01 12:00'))
_BtiSystems_ObjectIdentity=ObjectIdentity
btiSystems=_BtiSystems_ObjectIdentity((1,3,6,1,4,1,18070))
_BtiModules_ObjectIdentity=ObjectIdentity
btiModules=_BtiModules_ObjectIdentity((1,3,6,1,4,1,18070,1))
_BtiProducts_ObjectIdentity=ObjectIdentity
btiProducts=_BtiProducts_ObjectIdentity((1,3,6,1,4,1,18070,2))
_Bti7000_ObjectIdentity=ObjectIdentity
bti7000=_Bti7000_ObjectIdentity((1,3,6,1,4,1,18070,2,2))
_Btiems_ObjectIdentity=ObjectIdentity
btiems=_Btiems_ObjectIdentity((1,3,6,1,4,1,18070,2,4))
_BtiPSM_ObjectIdentity=ObjectIdentity
btiPSM=_BtiPSM_ObjectIdentity((1,3,6,1,4,1,18070,2,6))
_WidecastCache_ObjectIdentity=ObjectIdentity
widecastCache=_WidecastCache_ObjectIdentity((1,3,6,1,4,1,18070,2,7))
_Bti800_ObjectIdentity=ObjectIdentity
bti800=_Bti800_ObjectIdentity((1,3,6,1,4,1,18070,2,8))
_Bti7800_ObjectIdentity=ObjectIdentity
bti7800=_Bti7800_ObjectIdentity((1,3,6,1,4,1,18070,2,9))
mibBuilder.exportSymbols('BTI-MIB',**{'btiSystems':btiSystems,'btiModules':btiModules,'btiMib':btiMib,'btiProducts':btiProducts,'bti7000':bti7000,'btiems':btiems,'btiPSM':btiPSM,'widecastCache':widecastCache,'bti800':bti800,'bti7800':bti7800})