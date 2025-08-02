if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntwsRootMib=ModuleIdentity((1,3,6,1,4,1,45,6,1))
if mibBuilder.loadTexts:ntwsRootMib.setRevisions(('2007-08-15 00:04','2006-03-31 00:03','2005-04-21 00:00'))
_NtwsProducts_ObjectIdentity=ObjectIdentity
ntwsProducts=_NtwsProducts_ObjectIdentity((1,3,6,1,4,1,45,6,1,1))
_NtwsTemporary_ObjectIdentity=ObjectIdentity
ntwsTemporary=_NtwsTemporary_ObjectIdentity((1,3,6,1,4,1,45,6,1,2))
_NtwsRegistration_ObjectIdentity=ObjectIdentity
ntwsRegistration=_NtwsRegistration_ObjectIdentity((1,3,6,1,4,1,45,6,1,3))
_NtwsMibs_ObjectIdentity=ObjectIdentity
ntwsMibs=_NtwsMibs_ObjectIdentity((1,3,6,1,4,1,45,6,1,4))
_NtwsTraps_ObjectIdentity=ObjectIdentity
ntwsTraps=_NtwsTraps_ObjectIdentity((1,3,6,1,4,1,45,6,1,5))
mibBuilder.exportSymbols('NTWS-ROOT-MIB',**{'ntwsRootMib':ntwsRootMib,'ntwsProducts':ntwsProducts,'ntwsTemporary':ntwsTemporary,'ntwsRegistration':ntwsRegistration,'ntwsMibs':ntwsMibs,'ntwsTraps':ntwsTraps})