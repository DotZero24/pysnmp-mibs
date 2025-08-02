if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
casa,=mibBuilder.importSymbols('CASA-MIB','casa')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
casaIdMib=ModuleIdentity((1,3,6,1,4,1,20858,2))
if mibBuilder.loadTexts:casaIdMib.setRevisions(('1900-04-07 00:00',))
_Casa2100System_ObjectIdentity=ObjectIdentity
casa2100System=_Casa2100System_ObjectIdentity((1,3,6,1,4,1,20858,2,1))
_Casa2200System_ObjectIdentity=ObjectIdentity
casa2200System=_Casa2200System_ObjectIdentity((1,3,6,1,4,1,20858,2,20))
_Casa2300System_ObjectIdentity=ObjectIdentity
casa2300System=_Casa2300System_ObjectIdentity((1,3,6,1,4,1,20858,2,30))
_Casa2800System_ObjectIdentity=ObjectIdentity
casa2800System=_Casa2800System_ObjectIdentity((1,3,6,1,4,1,20858,2,40))
_Casa3000System_ObjectIdentity=ObjectIdentity
casa3000System=_Casa3000System_ObjectIdentity((1,3,6,1,4,1,20858,2,50))
_Casa6000System_ObjectIdentity=ObjectIdentity
casa6000System=_Casa6000System_ObjectIdentity((1,3,6,1,4,1,20858,2,100))
_Casa10000System_ObjectIdentity=ObjectIdentity
casa10000System=_Casa10000System_ObjectIdentity((1,3,6,1,4,1,20858,2,200))
mibBuilder.exportSymbols('CASA-ID-MIB',**{'casaIdMib':casaIdMib,'casa2100System':casa2100System,'casa2200System':casa2200System,'casa2300System':casa2300System,'casa2800System':casa2800System,'casa3000System':casa3000System,'casa6000System':casa6000System,'casa10000System':casa10000System})