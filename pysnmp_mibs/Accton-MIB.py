if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Accton_ObjectIdentity=ObjectIdentity
accton=_Accton_ObjectIdentity((1,3,6,1,4,1,259))
_Edgecorenetworks_ObjectIdentity=ObjectIdentity
edgecorenetworks=_Edgecorenetworks_ObjectIdentity((1,3,6,1,4,1,259,10))
_EdgeCoreNetworksMgt_ObjectIdentity=ObjectIdentity
edgeCoreNetworksMgt=_EdgeCoreNetworksMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1))
_Ecs5510_48sMIB_ObjectIdentity=ObjectIdentity
ecs5510_48sMIB=_Ecs5510_48sMIB_ObjectIdentity((1,3,6,1,4,1,259,10,1,14))
_Rnd_ObjectIdentity=ObjectIdentity
rnd=_Rnd_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89))
mibBuilder.exportSymbols('Accton-MIB',**{'accton':accton,'edgecorenetworks':edgecorenetworks,'edgeCoreNetworksMgt':edgeCoreNetworksMgt,'ecs5510-48sMIB':ecs5510_48sMIB,'rnd':rnd})