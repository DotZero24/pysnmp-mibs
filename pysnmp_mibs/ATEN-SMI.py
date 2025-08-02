if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Aten_ObjectIdentity=ObjectIdentity
aten=_Aten_ObjectIdentity((1,3,6,1,4,1,21317))
_AtenProducts_ObjectIdentity=ObjectIdentity
atenProducts=_AtenProducts_ObjectIdentity((1,3,6,1,4,1,21317,1))
_OtherEnterprises_ObjectIdentity=ObjectIdentity
otherEnterprises=_OtherEnterprises_ObjectIdentity((1,3,6,1,4,1,21317,2))
_AtenExperiment_ObjectIdentity=ObjectIdentity
atenExperiment=_AtenExperiment_ObjectIdentity((1,3,6,1,4,1,21317,3))
mibBuilder.exportSymbols('ATEN-SMI',**{'aten':aten,'atenProducts':atenProducts,'otherEnterprises':otherEnterprises,'atenExperiment':atenExperiment})