if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbtwsRootMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1))
if mibBuilder.loadTexts:rbtwsRootMib.setRevisions(('2005-05-07 00:00',))
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,52,4))
_CtronTrapeze_ObjectIdentity=ObjectIdentity
ctronTrapeze=_CtronTrapeze_ObjectIdentity((1,3,6,1,4,1,52,4,15))
_RbtwsProducts_ObjectIdentity=ObjectIdentity
rbtwsProducts=_RbtwsProducts_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,1))
_RbtwsTemporary_ObjectIdentity=ObjectIdentity
rbtwsTemporary=_RbtwsTemporary_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,2))
_RbtwsRegistration_ObjectIdentity=ObjectIdentity
rbtwsRegistration=_RbtwsRegistration_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3))
_RbtwsMibs_ObjectIdentity=ObjectIdentity
rbtwsMibs=_RbtwsMibs_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4))
_RbtwsTraps_ObjectIdentity=ObjectIdentity
rbtwsTraps=_RbtwsTraps_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,5))
mibBuilder.exportSymbols('RBTWS-ROOT-MIB',**{'cabletron':cabletron,'mibs':mibs,'ctronTrapeze':ctronTrapeze,'rbtwsRootMib':rbtwsRootMib,'rbtwsProducts':rbtwsProducts,'rbtwsTemporary':rbtwsTemporary,'rbtwsRegistration':rbtwsRegistration,'rbtwsMibs':rbtwsMibs,'rbtwsTraps':rbtwsTraps})