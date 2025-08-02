if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_products,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_DXS_3600Series_ObjectIdentity=ObjectIdentity
dXS_3600Series=_DXS_3600Series_ObjectIdentity((1,3,6,1,4,1,171,10,127))
_DXS_3600_32S_ObjectIdentity=ObjectIdentity
dXS_3600_32S=_DXS_3600_32S_ObjectIdentity((1,3,6,1,4,1,171,10,127,1))
_DXS_3600_16S_ObjectIdentity=ObjectIdentity
dXS_3600_16S=_DXS_3600_16S_ObjectIdentity((1,3,6,1,4,1,171,10,127,2))
mibBuilder.exportSymbols('SW3600PRIMGMT-MIB',**{'dXS-3600Series':dXS_3600Series,'dXS-3600-32S':dXS_3600_32S,'dXS-3600-16S':dXS_3600_16S})