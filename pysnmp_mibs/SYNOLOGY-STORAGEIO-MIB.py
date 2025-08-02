_R='storageIOGroup'
_Q='storageIODeviceSerial'
_P='storageIONWrittenX'
_O='storageIONReadX'
_N='storageIOLA15'
_M='storageIOLA5'
_L='storageIOLA1'
_K='storageIOLA'
_J='storageIOWrites'
_I='storageIOReads'
_H='storageIONWritten'
_G='storageIONRead'
_F='storageIODevice'
_E='storageIOIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-STORAGEIO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
storageIO=ModuleIdentity((1,3,6,1,4,1,6574,101))
if mibBuilder.loadTexts:storageIO.setRevisions(('2013-09-11 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_StorageIOTable_Object=MibTable
storageIOTable=_StorageIOTable_Object((1,3,6,1,4,1,6574,101,1))
if mibBuilder.loadTexts:storageIOTable.setStatus(_A)
_StorageIOEntry_Object=MibTableRow
storageIOEntry=_StorageIOEntry_Object((1,3,6,1,4,1,6574,101,1,1))
storageIOEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:storageIOEntry.setStatus(_A)
class _StorageIOIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StorageIOIndex_Type.__name__=_D
_StorageIOIndex_Object=MibTableColumn
storageIOIndex=_StorageIOIndex_Object((1,3,6,1,4,1,6574,101,1,1,1),_StorageIOIndex_Type())
storageIOIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:storageIOIndex.setStatus(_A)
_StorageIODevice_Type=DisplayString
_StorageIODevice_Object=MibTableColumn
storageIODevice=_StorageIODevice_Object((1,3,6,1,4,1,6574,101,1,1,2),_StorageIODevice_Type())
storageIODevice.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIODevice.setStatus(_A)
_StorageIONRead_Type=Counter32
_StorageIONRead_Object=MibTableColumn
storageIONRead=_StorageIONRead_Object((1,3,6,1,4,1,6574,101,1,1,3),_StorageIONRead_Type())
storageIONRead.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIONRead.setStatus(_A)
_StorageIONWritten_Type=Counter32
_StorageIONWritten_Object=MibTableColumn
storageIONWritten=_StorageIONWritten_Object((1,3,6,1,4,1,6574,101,1,1,4),_StorageIONWritten_Type())
storageIONWritten.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIONWritten.setStatus(_A)
_StorageIOReads_Type=Counter32
_StorageIOReads_Object=MibTableColumn
storageIOReads=_StorageIOReads_Object((1,3,6,1,4,1,6574,101,1,1,5),_StorageIOReads_Type())
storageIOReads.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIOReads.setStatus(_A)
_StorageIOWrites_Type=Counter32
_StorageIOWrites_Object=MibTableColumn
storageIOWrites=_StorageIOWrites_Object((1,3,6,1,4,1,6574,101,1,1,6),_StorageIOWrites_Type())
storageIOWrites.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIOWrites.setStatus(_A)
class _StorageIOLA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_StorageIOLA_Type.__name__=_D
_StorageIOLA_Object=MibTableColumn
storageIOLA=_StorageIOLA_Object((1,3,6,1,4,1,6574,101,1,1,8),_StorageIOLA_Type())
storageIOLA.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIOLA.setStatus(_A)
class _StorageIOLA1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_StorageIOLA1_Type.__name__=_D
_StorageIOLA1_Object=MibTableColumn
storageIOLA1=_StorageIOLA1_Object((1,3,6,1,4,1,6574,101,1,1,9),_StorageIOLA1_Type())
storageIOLA1.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIOLA1.setStatus(_A)
class _StorageIOLA5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_StorageIOLA5_Type.__name__=_D
_StorageIOLA5_Object=MibTableColumn
storageIOLA5=_StorageIOLA5_Object((1,3,6,1,4,1,6574,101,1,1,10),_StorageIOLA5_Type())
storageIOLA5.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIOLA5.setStatus(_A)
class _StorageIOLA15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_StorageIOLA15_Type.__name__=_D
_StorageIOLA15_Object=MibTableColumn
storageIOLA15=_StorageIOLA15_Object((1,3,6,1,4,1,6574,101,1,1,11),_StorageIOLA15_Type())
storageIOLA15.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIOLA15.setStatus(_A)
_StorageIONReadX_Type=Counter64
_StorageIONReadX_Object=MibTableColumn
storageIONReadX=_StorageIONReadX_Object((1,3,6,1,4,1,6574,101,1,1,12),_StorageIONReadX_Type())
storageIONReadX.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIONReadX.setStatus(_A)
_StorageIONWrittenX_Type=Counter64
_StorageIONWrittenX_Object=MibTableColumn
storageIONWrittenX=_StorageIONWrittenX_Object((1,3,6,1,4,1,6574,101,1,1,13),_StorageIONWrittenX_Type())
storageIONWrittenX.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIONWrittenX.setStatus(_A)
_StorageIODeviceSerial_Type=DisplayString
_StorageIODeviceSerial_Object=MibTableColumn
storageIODeviceSerial=_StorageIODeviceSerial_Object((1,3,6,1,4,1,6574,101,1,1,14),_StorageIODeviceSerial_Type())
storageIODeviceSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:storageIODeviceSerial.setStatus(_A)
_StorageIOConformance_ObjectIdentity=ObjectIdentity
storageIOConformance=_StorageIOConformance_ObjectIdentity((1,3,6,1,4,1,6574,101,2))
_StorageIOCompliances_ObjectIdentity=ObjectIdentity
storageIOCompliances=_StorageIOCompliances_ObjectIdentity((1,3,6,1,4,1,6574,101,2,1))
_StorageIOGroups_ObjectIdentity=ObjectIdentity
storageIOGroups=_StorageIOGroups_ObjectIdentity((1,3,6,1,4,1,6574,101,2,2))
storageIOGroup=ObjectGroup((1,3,6,1,4,1,6574,101,2,2,1))
storageIOGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:storageIOGroup.setStatus(_A)
storageIOCompliance=ModuleCompliance((1,3,6,1,4,1,6574,101,2,1,1))
storageIOCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:storageIOCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'storageIO':storageIO,'storageIOTable':storageIOTable,'storageIOEntry':storageIOEntry,_E:storageIOIndex,_F:storageIODevice,_G:storageIONRead,_H:storageIONWritten,_I:storageIOReads,_J:storageIOWrites,_K:storageIOLA,_L:storageIOLA1,_M:storageIOLA5,_N:storageIOLA15,_O:storageIONReadX,_P:storageIONWrittenX,_Q:storageIODeviceSerial,'storageIOConformance':storageIOConformance,'storageIOCompliances':storageIOCompliances,'storageIOCompliance':storageIOCompliance,'storageIOGroups':storageIOGroups,_R:storageIOGroup})