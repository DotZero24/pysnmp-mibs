if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_mgmt,dlink_products=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-mgmt','dlink-products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dgs_3024SeriesProd_ObjectIdentity=ObjectIdentity
dgs_3024SeriesProd=_Dgs_3024SeriesProd_ObjectIdentity((1,3,6,1,4,1,171,10,68))
_Dgs_3024_ObjectIdentity=ObjectIdentity
dgs_3024=_Dgs_3024_ObjectIdentity((1,3,6,1,4,1,171,10,68,1))
_Dgs_3024SeriesProd_Mgmt_ObjectIdentity=ObjectIdentity
dgs_3024SeriesProd_Mgmt=_Dgs_3024SeriesProd_Mgmt_ObjectIdentity((1,3,6,1,4,1,171,11,68))
_Dgs_3024Mgmt_ObjectIdentity=ObjectIdentity
dgs_3024Mgmt=_Dgs_3024Mgmt_ObjectIdentity((1,3,6,1,4,1,171,11,68,1))
mibBuilder.exportSymbols('SWDGS3024PRIMGMT-MIB',**{'dgs-3024SeriesProd':dgs_3024SeriesProd,'dgs-3024':dgs_3024,'dgs-3024SeriesProd-Mgmt':dgs_3024SeriesProd_Mgmt,'dgs-3024Mgmt':dgs_3024Mgmt})