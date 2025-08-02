if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
platform,=mibBuilder.importSymbols('F5-COMMON-SMI-MIB','platform')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
f5OsSystem=ModuleIdentity((1,3,6,1,4,1,12276,1,3))
if mibBuilder.loadTexts:f5OsSystem.setRevisions(('2022-04-07 00:00',))
_F5OsSystemModelOIDs_ObjectIdentity=ObjectIdentity
f5OsSystemModelOIDs=_F5OsSystemModelOIDs_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1))
_F5OsAppR5x00_ObjectIdentity=ObjectIdentity
f5OsAppR5x00=_F5OsAppR5x00_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1,1))
_F5OsAppR10x00_ObjectIdentity=ObjectIdentity
f5OsAppR10x00=_F5OsAppR10x00_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1,2))
_F5OsAppR2x00_ObjectIdentity=ObjectIdentity
f5OsAppR2x00=_F5OsAppR2x00_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1,3))
_F5OsAppR4x00_ObjectIdentity=ObjectIdentity
f5OsAppR4x00=_F5OsAppR4x00_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1,4))
_F5OsVelosCx410_ObjectIdentity=ObjectIdentity
f5OsVelosCx410=_F5OsVelosCx410_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1,5))
_F5OsVelosCx410Partition_ObjectIdentity=ObjectIdentity
f5OsVelosCx410Partition=_F5OsVelosCx410Partition_ObjectIdentity((1,3,6,1,4,1,12276,1,3,1,6))
mibBuilder.exportSymbols('F5-OS-SYSTEM-MIB',**{'f5OsSystem':f5OsSystem,'f5OsSystemModelOIDs':f5OsSystemModelOIDs,'f5OsAppR5x00':f5OsAppR5x00,'f5OsAppR10x00':f5OsAppR10x00,'f5OsAppR2x00':f5OsAppR2x00,'f5OsAppR4x00':f5OsAppR4x00,'f5OsVelosCx410':f5OsVelosCx410,'f5OsVelosCx410Partition':f5OsVelosCx410Partition})