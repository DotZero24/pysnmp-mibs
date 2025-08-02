_L='cmrSubIfMIBGroup'
_K='rpmPortState'
_J='rpmPortSubNetMask'
_I='rpmPortIpAddress'
_H='rpmPortRowStatus'
_G='rpmPortInterface'
_F='rpmPortSubInterface'
_E='rpmPortSlotNum'
_D='Integer32'
_C='read-only'
_B='CISCO-MGX82XX-RPM-SUBIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rpmPort,=mibBuilder.importSymbols('BASIS-MIB','rpmPort')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxRpmSubIfMIB=ModuleIdentity((1,3,6,1,4,1,351,150,60))
if mibBuilder.loadTexts:ciscoMgx82xxRpmSubIfMIB.setRevisions(('2002-09-08 00:00',))
_RpmPortTable_Object=MibTable
rpmPortTable=_RpmPortTable_Object((1,3,6,1,4,1,351,110,5,2,9,1,1))
if mibBuilder.loadTexts:rpmPortTable.setStatus(_A)
_RpmPortEntry_Object=MibTableRow
rpmPortEntry=_RpmPortEntry_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1))
rpmPortEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:rpmPortEntry.setStatus(_A)
class _RpmPortSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RpmPortSlotNum_Type.__name__=_D
_RpmPortSlotNum_Object=MibTableColumn
rpmPortSlotNum=_RpmPortSlotNum_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,1),_RpmPortSlotNum_Type())
rpmPortSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortSlotNum.setStatus(_A)
class _RpmPortInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpmPortInterface_Type.__name__=_D
_RpmPortInterface_Object=MibTableColumn
rpmPortInterface=_RpmPortInterface_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,2),_RpmPortInterface_Type())
rpmPortInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortInterface.setStatus(_A)
class _RpmPortSubInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RpmPortSubInterface_Type.__name__=_D
_RpmPortSubInterface_Object=MibTableColumn
rpmPortSubInterface=_RpmPortSubInterface_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,3),_RpmPortSubInterface_Type())
rpmPortSubInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortSubInterface.setStatus(_A)
class _RpmPortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_RpmPortRowStatus_Type.__name__=_D
_RpmPortRowStatus_Object=MibTableColumn
rpmPortRowStatus=_RpmPortRowStatus_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,4),_RpmPortRowStatus_Type())
rpmPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortRowStatus.setStatus(_A)
_RpmPortIpAddress_Type=IpAddress
_RpmPortIpAddress_Object=MibTableColumn
rpmPortIpAddress=_RpmPortIpAddress_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,5),_RpmPortIpAddress_Type())
rpmPortIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortIpAddress.setStatus(_A)
_RpmPortSubNetMask_Type=IpAddress
_RpmPortSubNetMask_Object=MibTableColumn
rpmPortSubNetMask=_RpmPortSubNetMask_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,6),_RpmPortSubNetMask_Type())
rpmPortSubNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortSubNetMask.setStatus(_A)
class _RpmPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notConfigured',1),('active',2),('failed',3)))
_RpmPortState_Type.__name__=_D
_RpmPortState_Object=MibTableColumn
rpmPortState=_RpmPortState_Object((1,3,6,1,4,1,351,110,5,2,9,1,1,1,7),_RpmPortState_Type())
rpmPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmPortState.setStatus(_A)
_CmrSubIfMIBConformance_ObjectIdentity=ObjectIdentity
cmrSubIfMIBConformance=_CmrSubIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,60,2))
_CmrSubIfMIBCompliances_ObjectIdentity=ObjectIdentity
cmrSubIfMIBCompliances=_CmrSubIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,60,2,1))
_CmrSubIfMIBGroups_ObjectIdentity=ObjectIdentity
cmrSubIfMIBGroups=_CmrSubIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,60,2,2))
cmrSubIfMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,60,2,2,1))
cmrSubIfMIBGroup.setObjects(*((_B,_E),(_B,_G),(_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cmrSubIfMIBGroup.setStatus(_A)
cmrSubIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,60,2,1,1))
cmrSubIfMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:cmrSubIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rpmPortTable':rpmPortTable,'rpmPortEntry':rpmPortEntry,_E:rpmPortSlotNum,_G:rpmPortInterface,_F:rpmPortSubInterface,_H:rpmPortRowStatus,_I:rpmPortIpAddress,_J:rpmPortSubNetMask,_K:rpmPortState,'ciscoMgx82xxRpmSubIfMIB':ciscoMgx82xxRpmSubIfMIB,'cmrSubIfMIBConformance':cmrSubIfMIBConformance,'cmrSubIfMIBCompliances':cmrSubIfMIBCompliances,'cmrSubIfMIBCompliance':cmrSubIfMIBCompliance,'cmrSubIfMIBGroups':cmrSubIfMIBGroups,_L:cmrSubIfMIBGroup})