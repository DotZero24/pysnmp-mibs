_R='spaceIOGroup'
_Q='spaceUUID'
_P='spaceIONWrittenX'
_O='spaceIONReadX'
_N='spaceIOLA15'
_M='spaceIOLA5'
_L='spaceIOLA1'
_K='spaceIOLA'
_J='spaceIOWrites'
_I='spaceIOReads'
_H='spaceIONWritten'
_G='spaceIONRead'
_F='spaceIODevice'
_E='spaceIOIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-SPACEIO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
spaceIO=ModuleIdentity((1,3,6,1,4,1,6574,102))
if mibBuilder.loadTexts:spaceIO.setRevisions(('2013-09-11 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_SpaceIOTable_Object=MibTable
spaceIOTable=_SpaceIOTable_Object((1,3,6,1,4,1,6574,102,1))
if mibBuilder.loadTexts:spaceIOTable.setStatus(_A)
_SpaceIOEntry_Object=MibTableRow
spaceIOEntry=_SpaceIOEntry_Object((1,3,6,1,4,1,6574,102,1,1))
spaceIOEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:spaceIOEntry.setStatus(_A)
class _SpaceIOIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SpaceIOIndex_Type.__name__=_D
_SpaceIOIndex_Object=MibTableColumn
spaceIOIndex=_SpaceIOIndex_Object((1,3,6,1,4,1,6574,102,1,1,1),_SpaceIOIndex_Type())
spaceIOIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:spaceIOIndex.setStatus(_A)
_SpaceIODevice_Type=DisplayString
_SpaceIODevice_Object=MibTableColumn
spaceIODevice=_SpaceIODevice_Object((1,3,6,1,4,1,6574,102,1,1,2),_SpaceIODevice_Type())
spaceIODevice.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIODevice.setStatus(_A)
_SpaceIONRead_Type=Counter32
_SpaceIONRead_Object=MibTableColumn
spaceIONRead=_SpaceIONRead_Object((1,3,6,1,4,1,6574,102,1,1,3),_SpaceIONRead_Type())
spaceIONRead.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIONRead.setStatus(_A)
_SpaceIONWritten_Type=Counter32
_SpaceIONWritten_Object=MibTableColumn
spaceIONWritten=_SpaceIONWritten_Object((1,3,6,1,4,1,6574,102,1,1,4),_SpaceIONWritten_Type())
spaceIONWritten.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIONWritten.setStatus(_A)
_SpaceIOReads_Type=Counter32
_SpaceIOReads_Object=MibTableColumn
spaceIOReads=_SpaceIOReads_Object((1,3,6,1,4,1,6574,102,1,1,5),_SpaceIOReads_Type())
spaceIOReads.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIOReads.setStatus(_A)
_SpaceIOWrites_Type=Counter32
_SpaceIOWrites_Object=MibTableColumn
spaceIOWrites=_SpaceIOWrites_Object((1,3,6,1,4,1,6574,102,1,1,6),_SpaceIOWrites_Type())
spaceIOWrites.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIOWrites.setStatus(_A)
class _SpaceIOLA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SpaceIOLA_Type.__name__=_D
_SpaceIOLA_Object=MibTableColumn
spaceIOLA=_SpaceIOLA_Object((1,3,6,1,4,1,6574,102,1,1,8),_SpaceIOLA_Type())
spaceIOLA.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIOLA.setStatus(_A)
class _SpaceIOLA1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SpaceIOLA1_Type.__name__=_D
_SpaceIOLA1_Object=MibTableColumn
spaceIOLA1=_SpaceIOLA1_Object((1,3,6,1,4,1,6574,102,1,1,9),_SpaceIOLA1_Type())
spaceIOLA1.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIOLA1.setStatus(_A)
class _SpaceIOLA5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SpaceIOLA5_Type.__name__=_D
_SpaceIOLA5_Object=MibTableColumn
spaceIOLA5=_SpaceIOLA5_Object((1,3,6,1,4,1,6574,102,1,1,10),_SpaceIOLA5_Type())
spaceIOLA5.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIOLA5.setStatus(_A)
class _SpaceIOLA15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SpaceIOLA15_Type.__name__=_D
_SpaceIOLA15_Object=MibTableColumn
spaceIOLA15=_SpaceIOLA15_Object((1,3,6,1,4,1,6574,102,1,1,11),_SpaceIOLA15_Type())
spaceIOLA15.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIOLA15.setStatus(_A)
_SpaceIONReadX_Type=Counter64
_SpaceIONReadX_Object=MibTableColumn
spaceIONReadX=_SpaceIONReadX_Object((1,3,6,1,4,1,6574,102,1,1,12),_SpaceIONReadX_Type())
spaceIONReadX.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIONReadX.setStatus(_A)
_SpaceIONWrittenX_Type=Counter64
_SpaceIONWrittenX_Object=MibTableColumn
spaceIONWrittenX=_SpaceIONWrittenX_Object((1,3,6,1,4,1,6574,102,1,1,13),_SpaceIONWrittenX_Type())
spaceIONWrittenX.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceIONWrittenX.setStatus(_A)
_SpaceUUID_Type=DisplayString
_SpaceUUID_Object=MibTableColumn
spaceUUID=_SpaceUUID_Object((1,3,6,1,4,1,6574,102,1,1,14),_SpaceUUID_Type())
spaceUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:spaceUUID.setStatus(_A)
_SpaceIOConformance_ObjectIdentity=ObjectIdentity
spaceIOConformance=_SpaceIOConformance_ObjectIdentity((1,3,6,1,4,1,6574,102,2))
_SpaceIOCompliances_ObjectIdentity=ObjectIdentity
spaceIOCompliances=_SpaceIOCompliances_ObjectIdentity((1,3,6,1,4,1,6574,102,2,1))
_SpaceIOGroups_ObjectIdentity=ObjectIdentity
spaceIOGroups=_SpaceIOGroups_ObjectIdentity((1,3,6,1,4,1,6574,102,2,2))
spaceIOGroup=ObjectGroup((1,3,6,1,4,1,6574,102,2,2,1))
spaceIOGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:spaceIOGroup.setStatus(_A)
spaceIOCompliance=ModuleCompliance((1,3,6,1,4,1,6574,102,2,1,1))
spaceIOCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:spaceIOCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'spaceIO':spaceIO,'spaceIOTable':spaceIOTable,'spaceIOEntry':spaceIOEntry,_E:spaceIOIndex,_F:spaceIODevice,_G:spaceIONRead,_H:spaceIONWritten,_I:spaceIOReads,_J:spaceIOWrites,_K:spaceIOLA,_L:spaceIOLA1,_M:spaceIOLA5,_N:spaceIOLA15,_O:spaceIONReadX,_P:spaceIONWrittenX,_Q:spaceUUID,'spaceIOConformance':spaceIOConformance,'spaceIOCompliances':spaceIOCompliances,'spaceIOCompliance':spaceIOCompliance,'spaceIOGroups':spaceIOGroups,_R:spaceIOGroup})