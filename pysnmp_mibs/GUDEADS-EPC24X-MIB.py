_M='epc24Fuse3'
_L='epc24Fuse2'
_K='epc24Fuse1'
_J='epc24PortSwitchCount'
_I='epc24PortState'
_H='epc24PortName'
_G='epc24portNumber'
_F='epc24PortIndex'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='GUDEADS-EPC24X-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC24_ObjectIdentity=ObjectIdentity
gadsEPC24=_GadsEPC24_ObjectIdentity((1,3,6,1,4,1,28507,5))
_Epc24Objects_ObjectIdentity=ObjectIdentity
epc24Objects=_Epc24Objects_ObjectIdentity((1,3,6,1,4,1,28507,5,1))
_Epc24powerports_ObjectIdentity=ObjectIdentity
epc24powerports=_Epc24powerports_ObjectIdentity((1,3,6,1,4,1,28507,5,1,1))
class _Epc24portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Epc24portNumber_Type.__name__=_C
_Epc24portNumber_Object=MibScalar
epc24portNumber=_Epc24portNumber_Object((1,3,6,1,4,1,28507,5,1,1,1),_Epc24portNumber_Type())
epc24portNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:epc24portNumber.setStatus(_A)
_Epc24portTable_Object=MibTable
epc24portTable=_Epc24portTable_Object((1,3,6,1,4,1,28507,5,1,1,2))
if mibBuilder.loadTexts:epc24portTable.setStatus(_A)
_Epc24portEntry_Object=MibTableRow
epc24portEntry=_Epc24portEntry_Object((1,3,6,1,4,1,28507,5,1,1,2,1))
epc24portEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:epc24portEntry.setStatus(_A)
class _Epc24PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Epc24PortIndex_Type.__name__=_C
_Epc24PortIndex_Object=MibTableColumn
epc24PortIndex=_Epc24PortIndex_Object((1,3,6,1,4,1,28507,5,1,1,2,1,1),_Epc24PortIndex_Type())
epc24PortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:epc24PortIndex.setStatus(_A)
class _Epc24PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc24PortName_Type.__name__=_E
_Epc24PortName_Object=MibTableColumn
epc24PortName=_Epc24PortName_Object((1,3,6,1,4,1,28507,5,1,1,2,1,2),_Epc24PortName_Type())
epc24PortName.setMaxAccess(_D)
if mibBuilder.loadTexts:epc24PortName.setStatus(_A)
class _Epc24PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Epc24PortState_Type.__name__=_C
_Epc24PortState_Object=MibTableColumn
epc24PortState=_Epc24PortState_Object((1,3,6,1,4,1,28507,5,1,1,2,1,3),_Epc24PortState_Type())
epc24PortState.setMaxAccess('read-write')
if mibBuilder.loadTexts:epc24PortState.setStatus(_A)
_Epc24PortSwitchCount_Type=Counter32
_Epc24PortSwitchCount_Object=MibTableColumn
epc24PortSwitchCount=_Epc24PortSwitchCount_Object((1,3,6,1,4,1,28507,5,1,1,2,1,4),_Epc24PortSwitchCount_Type())
epc24PortSwitchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:epc24PortSwitchCount.setStatus(_A)
class _Epc24Fuse1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc24Fuse1_Type.__name__=_C
_Epc24Fuse1_Object=MibScalar
epc24Fuse1=_Epc24Fuse1_Object((1,3,6,1,4,1,28507,5,1,1,3),_Epc24Fuse1_Type())
epc24Fuse1.setMaxAccess(_D)
if mibBuilder.loadTexts:epc24Fuse1.setStatus(_A)
class _Epc24Fuse2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc24Fuse2_Type.__name__=_C
_Epc24Fuse2_Object=MibScalar
epc24Fuse2=_Epc24Fuse2_Object((1,3,6,1,4,1,28507,5,1,1,4),_Epc24Fuse2_Type())
epc24Fuse2.setMaxAccess(_D)
if mibBuilder.loadTexts:epc24Fuse2.setStatus(_A)
class _Epc24Fuse3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc24Fuse3_Type.__name__=_C
_Epc24Fuse3_Object=MibScalar
epc24Fuse3=_Epc24Fuse3_Object((1,3,6,1,4,1,28507,5,1,1,5),_Epc24Fuse3_Type())
epc24Fuse3.setMaxAccess(_D)
if mibBuilder.loadTexts:epc24Fuse3.setStatus(_A)
_Epc24Events_ObjectIdentity=ObjectIdentity
epc24Events=_Epc24Events_ObjectIdentity((1,3,6,1,4,1,28507,5,2))
_Epc24Conf_ObjectIdentity=ObjectIdentity
epc24Conf=_Epc24Conf_ObjectIdentity((1,3,6,1,4,1,28507,5,3))
_Epc24Groups_ObjectIdentity=ObjectIdentity
epc24Groups=_Epc24Groups_ObjectIdentity((1,3,6,1,4,1,28507,5,3,1))
_Epc24Compls_ObjectIdentity=ObjectIdentity
epc24Compls=_Epc24Compls_ObjectIdentity((1,3,6,1,4,1,28507,5,3,2))
epc24BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,5,3,1,1))
epc24BasicGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:epc24BasicGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gudeads':gudeads,'gadsEPC24':gadsEPC24,'epc24Objects':epc24Objects,'epc24powerports':epc24powerports,_G:epc24portNumber,'epc24portTable':epc24portTable,'epc24portEntry':epc24portEntry,_F:epc24PortIndex,_H:epc24PortName,_I:epc24PortState,_J:epc24PortSwitchCount,_K:epc24Fuse1,_L:epc24Fuse2,_M:epc24Fuse3,'epc24Events':epc24Events,'epc24Conf':epc24Conf,'epc24Groups':epc24Groups,'epc24BasicGroup':epc24BasicGroup,'epc24Compls':epc24Compls})